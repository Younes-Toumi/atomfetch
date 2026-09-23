"""Orbit geometry: projects a tilted, rotated circle onto the 2D canvas."""

import math
from dataclasses import dataclass

from colors import make_shades
from config import Y_SCALE


@dataclass
class Orbit:
    """
    one electron shell: a circle of given radius, tilted and rotated in 3D,
    then projected onto the flat canvas. `path` is the static ring of dots;
    `electrons(t)` gives the moving electrons on that ring at time t.
    """
        
    radius: float       # [canvas units] orbit radius before projection/scaling 
    inclination: float  # [rad] tilt of the orbital plane, about the x-axis
    rotation: float     # [rad] spin of the tilted plane, about the viewing axis
    speed: float        # [rad/s] electron angular speed
    color: str          # [hex] HEX color code for the elctron 
    n_electrons: int    # [ - ] number of electrons per orbit
    n_path_points: int  # [ - ] dots drawn along the static ring
    n_shades: int       # [ - ] depth-shading steps, far (dim) to near (bright)

    def __post_init__(self):
        self.shades = make_shades(self.color, self.n_shades)

        # depth range of the orbit, used to normalize z into a shade index
        self._depth_range = self.radius * math.sin(self.inclination)

        # the orbital path is static, so it is computed once
        self.path = [
            self._point(2 * math.pi * k / self.n_path_points)
            for k in range(self.n_path_points)
        ]

    def _point(self, angle):
        """project a point at `angle` on the untilted circle into canvas-offset
        (x, y) plus a depth shade, by tilting the circle's plane and then
        rotating it about the viewing axis.
        """

        # point on the flat circle, before any tilt.
        flat_x = self.radius * math.cos(angle)
        flat_y = self.radius * math.sin(angle)

        # tilt the circle's plane by `inclination`: this is what turns a flat
        # ring into an ellipse-like path and gives it depth (z)
        tilted_y = flat_y * math.cos(self.inclination)
        depth_z = flat_y * math.sin(self.inclination)

        # spin the tilted plane by `rotation` about the axis facing the viewer.
        screen_x = flat_x * math.cos(self.rotation) - tilted_y * math.sin(self.rotation)
        screen_y = flat_x * math.sin(self.rotation) + tilted_y * math.cos(self.rotation)

        return screen_x, screen_y * Y_SCALE, self._shade(depth_z)

    def _shade(self, depth_z):
        """map a depth value in [-depth_range, +depth_range] to a shade
        (far from viewer = dim, near = bright)."""

        if self._depth_range == 0:
            return self.shades[-1]

        fraction = (depth_z + self._depth_range) / (2 * self._depth_range)


        # convert the normalized depth [0, 1] into an index
        # into the shades list: 0 = dimmest, last = brightest.
        index = min(
            len(self.shades) - 1,
            int(fraction * len(self.shades))
        )
        
        return self.shades[index]
    
    def electrons(self, t):
        """yield (x, y, shade) canvas offsets for every electron on this orbit at time t."""

        for k in range(self.n_electrons):
            angle = 2 * math.pi * k / self.n_electrons + t * self.speed
            yield self._point(angle)
