from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__trame_video": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = [
    ("__trame_video/trame-fabric.js", {"serial": "videothing"}),
    ("__trame_video/trame-panzoom.js", {"serial": "videothing"}),
    ("__trame_video/trame-videothing.js", {"serial": "videothing"}),
    ("__trame_video/trame-install.js", {"serial": "videothing"}),
    ("__trame_video/trame-videothing-comp.js", {"serial": "videothing"}),
]

styles = ["__trame_video/trame-videothing-comp.css"]

vue_use = ["trameVideothing"]
