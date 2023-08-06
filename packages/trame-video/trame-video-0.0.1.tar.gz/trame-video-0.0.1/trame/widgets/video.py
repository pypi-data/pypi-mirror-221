from trame_video.widgets.video import *


def initialize(server):
    from trame_video import module

    server.enable_module(module)
