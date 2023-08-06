import os

import numpy as np
import rich.progress


class Writer(object):
    def createEventSeriesFileData(self, data):
        """ """
        eventSeries = []
        totalTime = 0.0
        # get startingp point
        x0, y0, z0, v0, e0 = data[0][1][0]
        eventSeries.append((totalTime, x0, y0, z0, e0))
        for i in range(0, len(data)):
            for j in range(0, len(data[i][1]) - 1):
                x1, y1, z1, v1, e1 = data[i][1][j + 1]
                dist = self.getDistance(x0, y0, x1, y1)
                dt = dist / v1 * 60.0  # distance in mm, speed in mm/min
                totalTime += dt
                eventSeries.append((totalTime, x1, y1, z1, e1))
                x0, y0 = x1, y1

        return eventSeries

    def exportEventSeriesFileData(self, fileName, eventFile):
        """
        Exports the eventFile as text-file
        """
        beatwidth = "0.3"
        onOrOff = 0  # 0 or 1
        offset = 0.0
        path, name = os.path.split(fileName)
        nameroot = name.split(".")[0]
        newName = nameroot + "_EventSeries.inp"
        outFile = "Output"
        newFile = os.path.join(os.path.dirname(path), outFile, newName)
        eventList = iter(eventFile)
        currentLine = next(eventList)
        with open(newFile, "w") as f:
            while True:
                try:
                    nextLine = next(eventList)
                    if nextLine[4] == 0:
                        onOrOff = 0
                    else:
                        onOrOff = 1
                    f.write(
                        "{0:.2f},{1},{2},{3:.2f},{4}\n".format(
                            currentLine[0], currentLine[1], currentLine[2], currentLine[3] + offset, onOrOff
                        )
                    )
                    currentLine = nextLine
                except StopIteration:
                    break
            # for line in eventFile:

        f.close()

    def getDistance(self, x0, y0, x1, y1):
        """
        calculate the distance between 2 points
        """
        # print(x0,y0,x1,y1)
        return np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
