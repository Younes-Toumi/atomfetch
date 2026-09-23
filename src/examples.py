"""Some orbit examples"""

from orbit import Orbit
import math

DEFAULT = [
    Orbit(
            radius = 25.0,
            inclination = math.radians(75),
            rotation = math.radians(25),
            speed = 1.8,
            color = "#00FFFF",
            n_electrons = 16,
            n_path_points = 24,
            n_shades = 24,
        ),

    Orbit(
        radius = 25.0,
        inclination = math.radians(75),
        rotation = math.radians(-25),
        speed = 1.8,
        color = "#FFAE00FF",
        n_electrons = 16,
        n_path_points = 24,
        n_shades = 24,
    ) 
]

# DEFAULT = [
#     Orbit(
#             radius = 20.0,
#             inclination = math.radians(70),
#             rotation = math.radians(25),
#             speed = 2,
#             color = "#00FFFF",
#             n_electrons = 12,
#             n_path_points = 12,
#             n_shades = 24,
#         ),

#     Orbit(
#         radius = 27.0,
#         inclination = math.radians(70),
#         rotation = math.radians(-25),
#         speed = 0.3,
#         color = "#FFAE00FF",
#         n_electrons = 20,
#         n_path_points = 12,
#         n_shades = 24,
#     ),

#     Orbit(
#         radius = 8.0,
#         inclination = math.radians(80),
#         rotation = math.radians(0),
#         speed = 5,
#         color = "#992D2DFF",
#         n_electrons = 6,
#         n_path_points = 12,
#         n_shades = 24,
#     ) 

# ]

# DEFAULT = [
#     Orbit(
#             radius = 18.0,
#             inclination = math.radians(60),
#             rotation = math.radians(0),
#             speed = 4,
#             color = "#00FFFF",
#             n_electrons = 3,
#             n_path_points = 12,
#             n_shades = 24,
#         ),

#     Orbit(
#         radius = 12.0,
#         inclination = math.radians(60),
#         rotation = math.radians(0),
#         speed = 2,
#         color = "#FFAE00FF",
#         n_electrons = 3,
#         n_path_points = 12,
#         n_shades = 24,
#     ),

#     Orbit(
#         radius = 6.0,
#         inclination = math.radians(60),
#         rotation = math.radians(0),
#         speed = 5,
#         color = "#992D2DFF",
#         n_electrons = 3,
#         n_path_points = 12,
#         n_shades = 24,
#     ) 

# ]


# DEFAULT = [
#     Orbit(
#             radius = 16.0,
#             inclination = math.radians(70),
#             rotation = math.radians(45),
#             speed = 1.6,
#             color = "#00FFFF",
#             n_electrons = 12,
#             n_path_points = 24,
#             n_shades = 24,
#         ),

#     Orbit(
#         radius = 16.0,
#         inclination = math.radians(70),
#         rotation = math.radians(-45),
#             speed = 1.6,
#         color = "#00FFFF",
#         n_electrons = 12,
#         n_path_points = 24,
#         n_shades = 24,
#     ),

#     Orbit(
#         radius = 17.0,
#         inclination = math.radians(75),
#         rotation = math.radians(0),
#         speed = 1.6,
#         color = "#00FFFF",
#         n_electrons = 12,
#         n_path_points = 24,
#         n_shades = 24,
#     ),
# ]