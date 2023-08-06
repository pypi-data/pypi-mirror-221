from trame_client.widgets.core import AbstractElement
from .. import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


# ---------------------------------------------------------
# Core
# ---------------------------------------------------------


class Container(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreContainer", children, **kwargs)


class ImageSource(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreImageSource", children, **kwargs)


class Layers(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreLayers", children, **kwargs)


class LayersBasicTrack(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreLayersBasicTrack", children, **kwargs)


class LayersOpenface(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreLayersOpenface", children, **kwargs)


class LayersSourceNotReady(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreLayersSourceNotReady", children, **kwargs)


class Track(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreTrack", children, **kwargs)


class TrackStore(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreTrackStore", children, **kwargs)


class WebSocketTrackstore(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreWebSocketTrackstore", children, **kwargs)


class AppController(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtkCoreAppController", children, **kwargs)
        # self._attr_names += [
        #     "attribute_name",
        #     ("py_attr_name", "js_attr_name"),
        # ]
        # self._event_names += [
        #     "click",
        #     "change",
        # ]


# ---------------------------------------------------------
# Components
# ---------------------------------------------------------


class ControlBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentControlBar", children, **kwargs)


class Controls(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentControls", children, **kwargs)


class SvgStackCursorBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackCursorBar", children, **kwargs)


class SvgStackEventBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackEventBar", children, **kwargs)


class SvgStackPathBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackPathBar", children, **kwargs)


class SvgStackProgressBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackProgressBar", children, **kwargs)


class SvgStackRangeSlider(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackRangeSlider", children, **kwargs)


class SvgStackRangeSliderVertical(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackRangeSliderVertical", children, **kwargs)


class SvgStackStackContainer(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackStackContainer", children, **kwargs)


class SvgStackTickBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackTickBar", children, **kwargs)


class TimeSlider(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTimeSlider", children, **kwargs)


class TimeStamp(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTimeStamp", children, **kwargs)


class TrackTable(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTrackTable", children, **kwargs)


class Video(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentVideo", children, **kwargs)
