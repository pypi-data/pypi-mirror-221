import os

import numpy as np

from gcodereader.support import log


class Mesh_writer(object):
    def __init__(self):
        pass

    def mesh_file_writer(self, filename, string, mesh_array, mesh_format):
        """doc"""

        log.info("Write mesh file")
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(string)
            np.savetxt(file, mesh_array, fmt=mesh_format, delimiter=" ")

    def write_mesh(self, model, output_path, filename):
        """doc"""
        string = "# x y z block_id volume time angle_x angle_y angle_z\n"
        self.mesh_file_writer(
            os.path.join(output_path, filename) + ".txt",
            string,
            model,
            "%.18e %.18e %.18e %d %.18e %.18e %.18e %.18e %.18e",
        )
