from . import vue2


def setup(server, **kwargs):
    if server.client_type != "vue2":
        raise ValueError("trame-video only support vue2")

    server.enable_module(vue2)
