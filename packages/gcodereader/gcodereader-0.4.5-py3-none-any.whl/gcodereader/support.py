import logging

import numpy as np
import rich.progress
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])
logging.getLogger("matplotlib").setLevel(logging.ERROR)

log = logging.getLogger("rich")


class Support(object):
    def __init__(self):
        pass

    def read_file(self, filename):
        with rich.progress.open(filename) as f:
            content = f.readlines()
        return content

    def baseShape(self, x, y, zgrid, dx):
        shape = {
            "pointx": 0,
            "pointy": 0,
            "pointz": 0,
            "points": [],
            "time": [],
            "angles": [],
        }
        if x[0] == x[1]:
            xgrid = [x[0]]
        else:
            xgrid = np.arange(x[0], x[1], dx)
        if y[0] == y[1]:
            ygrid = [y[0]]
        else:
            ygrid = np.arange(y[0], y[1], dx)
        # if z[0] == z[1]:
        #     zgrid = [z[0]]
        # else:
        #     zgrid = np.arange(z[0], z[1], dx)
        shape["pointx"] = xgrid
        shape["pointy"] = ygrid
        shape["pointz"] = zgrid

        for z in zgrid:
            for y in ygrid:
                for x in xgrid:
                    shape["time"].append(0.0)
                    shape["angles"].append([0.0, 0.0, 0.0])
                    shape["points"].append([0.0, 0.0, 0.0])

        return shape
