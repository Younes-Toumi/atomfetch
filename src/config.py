"""Visual and animation settings."""

# Canvas
WIDTH = 60
HEIGHT = 20

# Animation
FRAME_DELAY = 0.01  # seconds between frames

# Layout
GAP = 2             # spaces between the atom and system information
Y_SCALE = 0.5       # vertical scale to compensate for terminal cell shape

# Electron
ELECTRON = ["(-)"]

# Nucleus
NUCLEUS_STEP = 0.2  # seconds between nucleus animation frames
NUCLEUS_COLOR = "\033[38;2;128;215;128m"

NUCLEUS_FRAMES = [
    [
        "/+++\\",
        "\\###/",
    ],
    [
        "/#++\\",
        "\\##+/",
    ],
    [
        "/##+\\",
        "\\#++/",
    ],
    [
        "/###\\",
        "\\+++/",
    ],
    [
        "/+##\\",
        "\\++#/",
    ],
    [
        "/++#\\",
        "\\+##/",
    ],
]


# NUCLEUS_FRAMES = [
#     [
#         "/++\\",
#         "\\##/",
#     ],
#     [
#         "/#+\\",
#         "\\#+/",
#     ],
#     [
#         "/##\\",
#         "\\++/",
#     ],

#     [
#         "/+#\\",
#         "\\+#/",
#     ],
# ]

# NUCLEUS_FRAMES = [
#     [      
#     " /\\_/\\",
#     "( o.o )",
#     " > ^ <",
#     ],

#     [      
#     " /\\_/\\",
#     "( ~.~ )",
#     " > ^ <",
#     ],

#     [      
#     " /\\_/\\",
#     "( o.o )",
#     " > ^ <",
#     ],

#     [      
#     " /\\_/\\",
#     "( ~.~ )",
#     " > ^ <",
#     ],


# ]