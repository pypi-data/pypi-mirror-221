import math
import re

import numpy as np
import rich.progress as rp

from gcodereader.support import log


class Reader(object):
    def __init__(self, scale=1):
        self.scale = scale
        self.dx_values = [1, 1, 1]
        self.globalSpeed = 0.0
        self.globalZdir = 0.0
        self.globalBeatWidth = 0.3

    def readPrusaFile(self, fileName):
        layerList = []

        # set up regular expressions
        # use https://regexper.com to visualise these if required
        # d+ : match one or more digits between 0 and 9
        # .  wildcard,
        # * quantifier represents zero or more.
        # () group the match
        #         rx_dict = {
        #             'xdir':  re.compile(r" X([-+]?\d+\.?\d*)",re.I),
        #             'ydir':  re.compile(r" Y([-+]?\d+\.?\d*)",re.I),
        #             'zdir':  re.compile(r" Z([-+]?\d+\.?\d*)",re.I),
        #             'fspeed':re.compile(r" F([-+]?\d+\.?\d*)",re.I),
        #         }
        try:
            with rp.open(fileName, "r") as inpfile:
                line = inpfile.readline()
                while line:
                    # Test if line starts withe "Layer"
                    line = line.strip()
                    # if line.startswith(';BEFORE_LAYER_CHANGE'):
                    #    self.globalBeatWidth=line.strip().split(':')[1]
                    #    line = inpfile.readline()
                    # if line.startswith(';LAYER_COUNT'):
                    #    line = inpfile.readline()
                    # if line.startswith(';Layer') or line.startswith(';LAYER'):
                    if line.startswith(";AFTER_LAYER_CHANGE"):
                        line = self.readLayer(line, inpfile, layerList)
                    if line.startswith(";LAYER_CHANGE"):
                        line = self.readLayerChange(line, inpfile, layerList)
                    else:
                        line = inpfile.readline()

            inpfile.close()

        except FileNotFoundError:
            message = "Sorry the file " + fileName + " could not be found."
            log.error(message)

        return layerList

    def readLayerChange(self, line, inpfile, layerList):
        dataList = []
        layerNumber = len(layerList) + 1
        layerName = "Layer_" + str(layerNumber)
        layerThickness = False
        while True:
            onOrOff = 0
            line = inpfile.readline()  # next line
            if not layerThickness:  # first line after ";AFTER_LAYER_CHANGE" ;Z:0.35
                layerThickness = line.strip().split(";")[1].split(":")[1]  # Get layer thickness ;0.3
                self.globalZdir = float(layerThickness)
                layerThickness = True
                line = inpfile.readline()  # next line
            if line.startswith(";LAYER_CHANGE"):
                dataList.append((x, y, z, speed, 0))  # add further layer with zero extrusion
                # stop loop
                layerList.append((layerName, dataList))
                line = inpfile.readline()
                break
            if line.startswith("; Filament-specific end gcode"):
                layerList.append((layerName, dataList))
                line = inpfile.readline()
                break
            if not line.startswith("G"):
                continue
            line = line.strip()
            data = line.split()
            # if len(data) <=3:
            #    continue
            x = self.readCoordX(line)
            y = self.readCoordY(line)
            z = self.globalZdir
            # Get deposition rate
            speed = self.readSpeed(line)
            if speed is not None:
                self.globalSpeed = speed
            else:
                speed = self.globalSpeed

            extrusion = self.readExtrusion(line)
            if (extrusion is not None) and (extrusion > 0.0):
                onOrOff = 1
            # if x and y and extrusion and speed:
            if x and y:
                dataList.append((x, y, z, speed, onOrOff))
                log.info(line)
            else:
                continue

        return line

    def readLayer(self, line, inpfile, layerList):
        dataList = []
        layerNumber = len(layerList) + 1
        layerName = "Layer_" + str(layerNumber)
        layerThickness = False
        while True:
            onOrOff = 0
            line = inpfile.readline()  # next line
            if not layerThickness:  # first line after ";AFTER_LAYER_CHANGE"
                layerThickness = line.strip().split(";")[1]  # Get layer thickness ;0.3
                self.globalZdir = float(layerThickness)
                layerThickness = True
                line = inpfile.readline()  # next line
            if line.startswith(";BEFORE_LAYER_CHANGE"):
                dataList.append((x, y, z, speed, 0))  # add further layer with zero extrusion
                # stop loop
                layerList.append((layerName, dataList))
                line = inpfile.readline()
                break
            if line.startswith("; Filament-specific end gcode"):
                line = inpfile.readline()
                break
            if not line.startswith("G"):
                continue
            line = line.strip()
            data = line.split()
            # Read x, y and z coordinate
            x = self.readCoordX(line)
            y = self.readCoordY(line)
            z = self.globalZdir
            # test speed
            speed = self.readSpeed(line)
            if speed is not None:
                self.globalSpeed = speed
            else:
                speed = self.globalSpeed

            extrusion = self.readExtrusion(line)
            if (extrusion is not None) and (extrusion > 0.0):
                onOrOff = 1
            # if x and y and extrusion and speed:
            if x and y:
                dataList.append((x, y, z, speed, onOrOff))
                log.info(line)
            else:
                continue

        return line

    def readCoordX(self, string):
        reX = re.compile(r"X([-+]?\d+\.?\d*)", re.I)
        match = reX.search(string)
        if match:
            val = match.group(1)
            fval = float(val)
            return fval
        else:
            return None

    def readCoordY(self, string):
        reX = re.compile(r"Y([-+]?\d+\.?\d*)", re.I)
        match = reX.search(string)
        if match:
            val = match.group(1)
            fval = float(val)
            return fval
        else:
            return None

    def readCoordZ(self, string):
        reX = re.compile(r"Z([-+]?\d+\.?\d*)", re.I)
        match = reX.search(string)
        if match:
            val = match.group(1)
            fval = float(val)
            return fval
        else:
            return None

    def readSpeed(self, string):
        reX = re.compile(r"F([-+]?\d+\.?\d*)", re.I)
        match = reX.search(string)
        if match:
            val = match.group(1)
            fval = float(val)
            return fval
        else:
            return None

    def readExtrusion(self, string):
        reX = re.compile(r"E([-+]?\d+\.?\d*)", re.I)
        match = reX.search(string)
        if match:
            val = match.group(1)
            fval = float(val)
            return fval
        else:
            return None

    def get_base_information(self, content=[], key=""):
        for line in content:
            if key in line:
                temp = re.split(" |=|m|\n", line)
                for t in temp:
                    try:
                        return float(t)
                    except ValueError:
                        pass
        return 0

    def read_structure_path(self, content, filter={"Start": [], "Stop": []}):
        data = {"points": [], "active": [], "ext1": [], "feedrate": [], "new_layer": []}
        point = [0, 0, 0]
        fr = 0
        e1 = 0
        if len(filter["Start"]) == 0:
            gofurther = True
        else:
            gofurther = False
        new_layer = False
        with rp.Progress() as progress:
            task = progress.add_task("[green]Analyzing GCode", total=len(content))
            for line in content:
                part = line.split(" ")
                # Get z if possible:
                if len(part) > 1:
                    if "Z" in part[1]:
                        point[2] = float(part[1][1:]) * self.scale
                        new_layer = True

                for start in filter["Start"]:
                    if start in line:
                        gofurther = True
                for stop in filter["Stop"]:
                    if stop in line:
                        gofurther = False
                # if gofurther:
                parts = re.split(r" |;", line)
                done = False

                if parts[0] in ["G1", "G0"]:
                    pointDef = False

                    for part in parts[1:]:
                        if "\t" in part or len(part) == 0:
                            break
                        # tmp=float(part[1:])

                        if part[0] == "X":
                            point[0] = float(part[1:]) * self.scale
                        elif part[0] == "Y":
                            point[1] = float(part[1:]) * self.scale
                            pointDef = True
                        elif part[0] == "E":
                            e1 = float(part[1:])

                        if "\n" in part and pointDef:
                            done = True
                            data["points"].append(point.copy())
                            data["active"].append(gofurther)
                            data["ext1"].append(e1)
                            data["feedrate"].append(fr)
                            data["new_layer"].append(new_layer)
                            if new_layer:
                                new_layer = False

                        if part[0] == "F":
                            fr = float(part[1:]) * self.scale / 60  # mm/min in m/s

                        if done:
                            break
                progress.update(task, advance=1)
            progress.update(task, description="[green]GCode analyzed")
        data["points"] = np.array(data["points"])
        data["active"] = np.array(data["active"])
        # plt.plot(data["points"][:, 0], data["points"][:, 1])
        # plt.plot(np.extract(data["active"],data["points"][:, 0]), np.extract(data["active"],data["points"][:, 1]))
        # plt.savefig("path.png")
        return data

    def _get_linear_function_(self, data, start, end):
        direction = np.array([data["x"][start], data["y"][start], data["z"][start]]) - np.array(
            [data["x"][end], data["y"][end], data["z"][end]]
        )
        norm = np.linalg.norm(direction)
        return direction / norm, norm

    def _get_discretized_rectangle_(self, dx_values):
        yrange = self.__get_vals__(dx_values[0], dx_values[1])
        zrange = self.__get_vals__(dx_values[0], dx_values[2])
        return yrange, zrange

    def __get_vals__(self, discA, discB):
        numY = int(discB / discA)
        if numY == 1:
            val_range = np.array([0.0])
        else:
            val_range = np.linspace(-discB / 2, discB / 2, num=4, endpoint=True)
        return val_range

    def create_peridynamic_mesh(self, data, twoD=False):
        return_data = {
            "x": [],
            "y": [],
            "z": [],
            "angle_x": [],
            "angle_y": [],
            "angle_z": [],
            "vol": [],
            "block_id": [],
            "time": [],
        }

        dx_value = self.dx_values
        if twoD:
            dx_value[2] = dx_value[0]
        # check the discance between two linear functions
        yrange, zrange = self._get_discretized_rectangle_(self.dx_values)
        # if volume is split in multiple points, it has to be reduced
        # it is assumed that the discretization is more or less constant in the first place

        for i in range(1, len(data["x"])):
            beforeDirection, beforeDistance = self._get_linear_function_(data, i - 1, i)
            try:
                afterDirection, afterDistance = self._get_linear_function_(data, i, i + 1)
            except IndexError:  # for the last point, because it has no distance and is than set to dx
                afterDistance = dx_value[0]

            if beforeDistance != 0.0:
                time_needed = beforeDistance / data["feedrate"][i]

                if beforeDistance > dx_value[0]:
                    x_range = []
                    y_range = []
                    z_range = []

                    # cells which can be vary in number of points
                    # here
                    numCells = int(beforeDistance / dx_value[0])
                    dx = numCells * dx_value[0]
                    volume = dx * dx_value[1] * dx_value[2] / (len(yrange) * len(zrange))

                    x_range, y_range, z_range = self.__create_cells__(
                        np.array([data["x"][i - 1], data["y"][i - 1], data["z"][i - 1]]),
                        np.array([data["x"][i], data["y"][i], data["z"][i]]),
                        yrange,
                        zrange,
                        beforeDirection,
                        numCells,
                    )
                    time_range = self._get_time_(
                        return_data["time"],
                        time_needed,
                        numCells,
                        len(yrange) * len(zrange),
                    )

                    x_angle, y_angle, z_angle = self._get_angle_(
                        beforeDirection,
                        numCells,
                        len(yrange) * len(zrange),
                    )
                    return_data["x"].extend(x_range)
                    return_data["y"].extend(y_range)
                    return_data["z"].extend(z_range)
                    return_data["angle_x"].extend(x_angle)
                    return_data["angle_y"].extend(y_angle)
                    return_data["angle_z"].extend(z_angle)

                    return_data["time"].extend(time_range)

                    return_data["vol"].extend(np.full_like(x_range, volume))

                return_data["x"].append(data["x"][i])
                return_data["y"].append(data["y"][i])
                return_data["z"].append(data["z"][i])

                return_data["angle_x"].append(0.0)
                return_data["angle_y"].append(0.0)
                return_data["angle_z"].append(0.0)

                return_data["time"].append(return_data["time"][-1] + time_needed)

                if beforeDistance > dx_value[0] or afterDistance > dx_value[0]:
                    beforeDistance = math.sqrt(
                        math.pow(data["x"][i] - return_data["x"][-1], 2)
                        + math.pow(data["y"][i] - return_data["y"][-1], 2)
                        + math.pow(data["z"][i] - return_data["z"][-1], 2)
                    )
                    return_data["vol"].append(volume)

                else:
                    return_data["vol"].append(volume * ((beforeDistance + afterDistance) / (2 * dx_value[0])))

        return return_data

    def _get_angle_(self, direction, numCells, num):
        x_angle = np.array([])
        y_angle = np.array([])
        z_angle = np.array([])

        for i in range(0, num):
            x_angle = np.append(
                x_angle,
                np.full(
                    numCells,
                    np.degrees(
                        np.arcsin(
                            direction[2] / np.sqrt(direction[2] * direction[2] + direction[1] + direction[1]),
                        )
                    ),
                ),
            )
            y_angle = np.append(
                x_angle,
                np.full(
                    numCells,
                    np.degrees(
                        np.arcsin(
                            direction[0] / np.sqrt(direction[2] * direction[2] + direction[0] * direction[0]),
                        )
                    ),
                ),
            )
            z_angle = np.append(
                x_angle,
                np.full(
                    numCells,
                    np.degrees(
                        np.arcsin(
                            direction[1] / np.sqrt(direction[0] * direction[0] + direction[1] * direction[1]),
                        )
                    ),
                ),
            )
        return x_angle, y_angle, z_angle

    def _get_time_(self, time, time_needed, numCells, num):
        time_range = np.array([])
        for i in range(0, num):
            if len(time) != 0:
                time_range = np.append(
                    time_range,
                    np.linspace(
                        time[-1],
                        time[-1] + time_needed,
                        num=numCells,
                        endpoint=False,
                    ),
                )
            else:
                time_range = time_range = np.append(
                    time_range,
                    np.linspace(1e-9, time_needed, num=numCells, endpoint=False),
                )
        return time_range

    def __create_cells__(self, xStart, xEnd, yrange, zrange, direction, num_cells):
        # so muesste es sein
        # get direction
        # get surface
        # discrete
        x_range = np.array([])
        y_range = np.array([])
        z_range = np.array([])
        for i in range(0, len(yrange)):
            for j in range(0, len(zrange)):
                surfPos = np.array([0, yrange[i], zrange[j]])
                projPos = self._project_(surfPos, direction)
                x_range = np.append(
                    x_range,
                    np.linspace(
                        xStart[0] + projPos[0],
                        xEnd[0] + projPos[0],
                        num=num_cells,
                        endpoint=False,
                    ),
                )
                y_range = np.append(
                    y_range,
                    np.linspace(
                        xStart[1] + projPos[1],
                        xEnd[1] + projPos[1],
                        num=num_cells,
                        endpoint=False,
                    ),
                )
                z_range = np.append(
                    z_range,
                    np.linspace(
                        xStart[2] + projPos[2],
                        xEnd[2] + projPos[2],
                        num=num_cells,
                        endpoint=False,
                    ),
                )

        return x_range, y_range, z_range

    def _project_(self, point, normal):
        normN = np.linalg.norm(normal)

        alpha = np.arccos(normal[0] / normN) * 180 / np.pi
        beta = np.arccos(normal[1] / normN) * 180 / np.pi - 90
        gamma = np.arccos(normal[2] / normN) * 180 / np.pi - 90

        R = self.Rypr(alpha, beta, gamma)

        return np.array(np.matmul(R, point))[0]

    def Rypr(self, y, p, r):
        """
        Rotationsmatrix für y=yaw, p=pitch, r=roll in degrees
        """
        # from Degree to Radians
        y = y * np.pi / 180.0
        p = p * np.pi / 180.0
        r = r * np.pi / 180.0

        Rr = np.matrix([[1.0, 0.0, 0.0], [0.0, np.cos(r), -np.sin(r)], [0.0, np.sin(r), np.cos(r)]])
        Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)], [0.0, 1.0, 0.0], [-np.sin(p), 0.0, np.cos(p)]])
        Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0], [np.sin(y), np.cos(y), 0.0], [0.0, 0.0, 1.0]])
        R = np.matmul(Rr, Ry)
        return R

    def _find_nearest_neighbor_init_(self, X):
        return {"x": sorted(X["x"]), "y": sorted(X["y"]), "z": sorted(X["z"])}

    def _find_nearest_neighbor_(self, points, point):
        pass

    def get_direction(self, pointA, pointB):
        return np.array([pointA[0] - pointB[0], pointA[1] - pointB[1], pointA[2] - pointB[2]])

    def calculate_angle(self, direction):
        x_angle = np.degrees(
            np.arcsin(
                direction[2] / np.sqrt(direction[2] * direction[2] + direction[1] * direction[1]),
            )
        )
        y_angle = np.degrees(
            np.arcsin(
                direction[0] / np.sqrt(direction[2] * direction[2] + direction[0] * direction[0]),
            )
        )
        z_angle = np.degrees(
            np.arcsin(
                direction[1] / np.sqrt(direction[0] * direction[0] + direction[1] * direction[1]),
            )
        )

        return x_angle, y_angle, z_angle

    def active_grid(self, baseGrid, rawData, dt=1e-8):
        return_data = {
            "points": [],
            "angles": [],
            "vol": [],
            "block_id": [],
            "time": [],
        }
        path_grid = self._create_path_grid_(rawData, dt)
        "erstellen der Pfadpunkte"
        "Pfadpunkte in grid mit rein"
        " für Pfadpunkte die nachbarn mit radius bestimmen"
        "diesen Punkten Zeiten zuordnen"
        "durch 4 weil Mittelwert und Radius -> halbe Spurbreite"
        # nn = NearestNeighbors(radius=(self.dx_values[1] + self.dx_values[2]) / 4)
        # dat = nn.fit(path_grid)
        return return_data

    def bruteNN(self, point, refGrid):
        nearNeighbors = {
            "points": [],
            "angles": [],
            "time": [],
        }
        for x in refGrid["x"]:  # -> array x,y,z
            if not x - self.dx_values[1] <= point[0] <= x - self.dx_values[1]:
                break
            for y in refGrid["y"]:
                if not y - self.dx_values[1] <= point[1] <= y - self.dx_values[1]:
                    break
                for z in refGrid["z"]:
                    if not z - self.dx_values[1] <= point[2] <= z - self.dx_values[1]:
                        break
                    nearNeigbors["angle_x"].append()
        return nearNeighbors
