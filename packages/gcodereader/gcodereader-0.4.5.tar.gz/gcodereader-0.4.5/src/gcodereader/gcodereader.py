import os

# import matplotlib.pyplot as plt
import numpy as np

from gcodereader.interpreter import Interpreter
from gcodereader.meshWriter import Mesh_writer
from gcodereader.reader import Reader
from gcodereader.support import Support, log
from gcodereader.writer import Writer

# import meshio


def run(**kwargs):
    log.info("Start reading GCode")
    fileName = kwargs["filename"]
    reader = Reader()
    data = reader.readPrusaFile(fileName)
    writer = Writer()
    eventFiledata = writer.createEventSeriesFileData(data)
    writer.exportEventSeriesFileData(fileName, eventFiledata)
    log.info("Finished")


def read(filename="L-Angle2D", input_path="Input", output_path="Output", dx=1, dt=0.02, scale=0.001):
    log.info("Start reading GCode")

    # output_path = os.path.join(output_path, filename)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    su = Support()

    filepath = os.path.join(input_path, filename + ".gcode")
    content = su.read_file(filepath)
    gc = Reader(scale=scale)
    width = gc.get_base_information(content, key="width")
    # width=0.3
    if dx < width:
        log.warning("dx: " + str(dx) + ", width: " + str(width))

    filter = {
        "Stop": ["stop printing object", "WIPE_START"],
        "Start": [
            "TYPE:Perimeter",
            "TYPE:External perimeter",
            "TYPE:Solid infill",
            "TYPE:Internal infill",
            "TYPE:Top solid infill",
            "TYPE:Gap fill",
        ],
    }

    rawData = gc.read_structure_path(content, filter)

    mask = rawData["active"]
    filtered_points = rawData["points"][mask]

    layers = np.unique(filtered_points[:, 2]).round(decimals=10)
    if len(layers) > 1:
        layer_diff = np.diff(layers).round(decimals=10)

        if not np.all(layer_diff == layer_diff[0]):
            log.warning("Layer thickness is different: " + str(layer_diff))

        height = np.min(np.abs(layer_diff))

        dx_value = [dx * scale, width * scale, height / 2]

    else:
        dx_value = [dx * scale, width * scale, 1]

    baseGrid = su.baseShape(
        [min(filtered_points[:, 0]) - dx_value[0], max(filtered_points[:, 0]) + dx_value[0]],
        [min(filtered_points[:, 1]) - dx_value[1], max(filtered_points[:, 1]) + dx_value[1]],
        layers,
        dx_value[0],
    )

    # dt = 0.02

    volume = dx_value[0] * dx_value[1] * dx_value[2]
    gc.dx_values = dx_value
    interpreter = Interpreter(dx_value)
    mesh_data = interpreter.active_grid(baseGrid, rawData, dt)

    x_peri_np = mesh_data["points"][:, 0]
    y_peri_np = mesh_data["points"][:, 1]
    z_peri_np = mesh_data["points"][:, 2]
    angle_x_np = mesh_data["angles"][:, 0]
    angle_y_np = mesh_data["angles"][:, 1]
    angle_z_np = mesh_data["angles"][:, 2]
    time_np = mesh_data["time"]

    log.info("Min: " + str(min(x_peri_np)) + " " + str(min(y_peri_np)) + " " + str(min(z_peri_np)))
    log.info("Max: " + str(max(x_peri_np)) + " " + str(max(y_peri_np)) + " " + str(max(z_peri_np)))
    log.info("Print time: " + str(max(time_np)) + " seconds")

    k = np.full_like(x_peri_np, 1)
    vol_np = np.full_like(x_peri_np, volume)

    model = np.transpose(
        np.vstack(
            [
                x_peri_np.ravel(),
                y_peri_np.ravel(),
                z_peri_np.ravel(),
                k.ravel(),
                vol_np.ravel(),
                time_np.ravel(),
                angle_x_np.ravel(),
                angle_y_np.ravel(),
                angle_z_np.ravel(),
            ]
        )
    )

    me = Mesh_writer()
    me.write_mesh(model, output_path, filename)

    file_paths = [os.path.join(output_path, f"ns_{filename}_{i}.txt") for i in range(1, 6)]
    file_handles = [open(file_path, "w") for file_path in file_paths]

    my_strings = ["", "", "", "", ""]

    for idx, z in enumerate(z_peri_np, 1):
        if z < height * 1.5:
            my_strings[0] += str(idx) + " \n"
        else:
            my_strings[1] += str(idx) + " \n"

    for idx, x in enumerate(x_peri_np, 1):
        if x > max(x_peri_np) - 3.5 * dx_value[0]:
            my_strings[4] += str(idx) + " \n"
        elif x < min(x_peri_np) + 3.5 * dx_value[0]:
            my_strings[3] += str(idx) + " \n"
        else:
            my_strings[2] += str(idx) + " \n"

    for handle, string in zip(file_handles, my_strings):
        handle.write(string)
        handle.close()

    print()

    # plt.plot(x_peri_np, y_peri_np, "x")
    # plt.savefig(os.path.join(output_path, "path.png"))
    # won't use cells, so define vertex cell (1 point per cell)
    # cells = [("vertex", np.array([[i,] for i in range(len(x_peri_np))]))]

    # mesh = meshio.Mesh(
    #     [x_peri_np,y_peri_np,z_peri_np],
    #     cells
    # )
    # mesh.write(
    #     os.path.join(output_path, filename + ".e"),  # str, os.PathLike, or buffer/open file
    #     # file_format="vtk",  # optional if first argument is a path; inferred from extension
    # )
    log.info("Finished")
