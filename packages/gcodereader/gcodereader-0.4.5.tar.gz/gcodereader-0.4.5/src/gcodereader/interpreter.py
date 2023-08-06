import matplotlib.pyplot as plt
import numpy as np
import rich.progress as rp

plt.rcParams["figure.figsize"] = (30, 30)
from gcodereader.support import log


class Interpreter(object):
    def __init__(self, dx_values=[1, 1, 1]):
        self.dx_values = np.array(dx_values)

    def _find_nearest_neighbor_init_(self, X):
        return {"x": sorted(X["x"]), "y": sorted(X["y"]), "z": sorted(X["z"])}

    def _find_nearest_neighbor_(self, points, point):
        pass

    def get_direction(self, pointA, pointB):
        return np.array([pointA[0] - pointB[0], pointA[1] - pointB[1], pointA[2] - pointB[2]])

    def calculate_angle(self, direction):
        # Calculate the z angle
        z_angle = np.degrees(np.arctan2(direction[1], direction[0]))

        # Return the angles in a list
        return [0, 0, z_angle]

    def active_grid(self, baseGrid, rawData, dt=1e-8):
        return_data = {
            "points": [],
            "angles": [],
            "vol": [],
            "block_id": [],
            "time": [],
        }
        path_grid = self._create_path_grid_(rawData, dt)
        "erstellen der Pfadpunkte -> check"
        "Pfadpunkte in grid mit rein"
        " für Pfadpunkte die nachbarn mit radius bestimmen"
        "diesen Punkten Zeiten zuordnen"
        "durch 4 weil Mittelwert und Radius -> halbe Spurbreite"
        return_data = self.bruteNN(path_grid, baseGrid)
        # nn = NearestNeighbors(radius=(self.dx_values[1] + self.dx_values[2]) / 4)
        # dat = nn.fit(path_grid)
        return return_data

    def bruteNN(self, points, refGrid):
        dx_values = self.dx_values

        with rp.Progress() as progress:
            task = progress.add_task("[green]Searching nearest Neighbor", total=len(points["points"]))

            refGrid_time = np.array(refGrid["time"])
            refGrid_angles = np.array(refGrid["angles"])
            refGrid_points = np.array(refGrid["points"])

            grid_x, grid_y, grid_z = np.meshgrid(refGrid["pointx"], refGrid["pointy"], refGrid["pointz"])
            grid_x = grid_x.ravel()
            grid_y = grid_y.ravel()
            grid_z = grid_z.ravel()

            # Extract the x, y, and z coordinates into separate arrays
            points_x, points_y, points_z = points["points"].T

            plt.plot(grid_x, grid_y, "x")
            plt.plot(points_x, points_y, "o")
            # plt.savefig("path.png")

            # Calculate the ranges using broadcasting
            x_min, x_max = points_x - dx_values[0], points_x + dx_values[0]
            y_min, y_max = points_y - dx_values[1], points_y + dx_values[1]
            z_min, z_max = points_z - dx_values[2], points_z + dx_values[2]

            for idp, point in enumerate(points["points"]):
                indices = np.where(
                    (grid_z >= z_min[idp])
                    & (grid_z <= z_max[idp])
                    & (grid_y >= y_min[idp])
                    & (grid_y <= y_max[idp])
                    & (grid_x >= x_min[idp])
                    & (grid_x <= x_max[idp])
                )
                if len(indices) == 0:
                    continue

                time_mask = refGrid_time == 0
                # create new boolean array of same size as original boolean array
                indices_mask = np.zeros_like(time_mask, dtype=bool)

                # set values at indices in indices array to True
                indices_mask[indices] = True

                mask = np.logical_and(indices_mask, time_mask)

                refGrid_time[mask] = points["time"][idp]
                refGrid_angles[mask] = points["angles"][idp].copy()
                refGrid_points[mask] = np.column_stack((grid_x[mask], grid_y[mask], grid_z[mask]))

                progress.update(task, advance=1)

            progress.update(task, description="[green]Nearest Neighbor found")

        refGrid["time"] = refGrid_time
        refGrid["angles"] = refGrid_angles
        refGrid["points"] = refGrid_points

        nearNeighbors = self.filter_grid(refGrid)
        plt.plot(nearNeighbors["points"][:, 0], nearNeighbors["points"][:, 1], "x")
        plt.savefig("path.png")
        return nearNeighbors

    def filter_grid(self, refGrid):
        nearNeighbors = {
            "points": [],
            "angles": [],
            "time": [],
        }
        for idt, time in enumerate(refGrid["time"]):
            if time != 0:
                nearNeighbors["points"].append(refGrid["points"][idt])
                nearNeighbors["time"].append(time)
                nearNeighbors["angles"].append(refGrid["angles"][idt])
        nearNeighbors["points"] = np.array(nearNeighbors["points"])
        nearNeighbors["time"] = np.array(nearNeighbors["time"])
        nearNeighbors["angles"] = np.array(nearNeighbors["angles"])
        return nearNeighbors

    def _create_path_grid_(self, rawData, dt):
        grid = []
        gridTime = []
        gridAngle = []
        globaltime = 0
        time_needed = 0
        min_time_needed = 100
        started = False
        with rp.Progress() as progress:
            task = progress.add_task("[green]Create Path Grid", total=len(rawData["points"][:, 1]) - 1)
            for i in range(0, len(rawData["points"][:, 1]) - 1):
                if rawData["feedrate"][i] == 0:
                    progress.update(task, advance=1)
                    continue
                direction = self.get_direction(
                    rawData["points"][i + 1, :],
                    rawData["points"][i, :],
                )
                active = rawData["active"][i]
                if not started and active:
                    started = True
                if started:
                    norm = np.linalg.norm(direction)
                    direction /= norm
                    time_needed = norm / rawData["feedrate"][i]
                    if time_needed < min_time_needed:
                        min_time_needed = time_needed
                    vel = norm / time_needed
                    localtime = 0
                    if rawData["new_layer"][i + 1]:
                        globaltime += time_needed
                        if active:
                            grid.append(rawData["points"][i, :] + time_needed * direction * vel)
                            gridTime.append(globaltime)
                            gridAngle.append(self.calculate_angle(direction))
                    else:
                        while localtime < time_needed:
                            if localtime + dt > time_needed:
                                globaltime += time_needed - localtime
                                localtime = time_needed
                            else:
                                localtime += dt
                                globaltime += dt
                            if active:
                                grid.append(rawData["points"][i, :] + localtime * direction * vel)
                                gridTime.append(globaltime)
                                gridAngle.append(self.calculate_angle(direction))
                progress.update(task, advance=1)
            progress.update(task, description="[green]Path Grid created")

        if min_time_needed < dt:
            log.warning("min_time_needed < dt: " + str(min_time_needed) + " < " + str(dt))
        else:
            log.info("min_time_needed: " + str(min_time_needed))

        return {
            "points": np.array(grid),
            "time": gridTime,
            "angles": np.array(gridAngle),
        }
