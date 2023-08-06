from trame_client.widgets.core import AbstractElement
from .. import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class ControlBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentControlBar", children, **kwargs)
        self._attr_names += ["background"]


class Controls(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentControls", children, **kwargs)
        self._attr_names += [
            ("show_timestamp", "showTimestamp"),
        ]


class SvgStackCursorBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackCursorBar", children, **kwargs)
        self._attr_names += [
            "timelines",
            "height",
            "width",
            "xbuffer",
        ]


class SvgStackEventBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackEventBar", children, **kwargs)
        self._attr_names += [
            "events",
            "title",
            "color",
            "height",
            "width",
            "xbuffer",
        ]


class SvgStackPathBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackPathBar", children, **kwargs)
        self._attr_names += [
            "width",
            "height",
            "signals",
            "color",
            ("stroke_width", "strokeWidth"),
            "opacity",
            "xbuffer",
            "domain",
            ("show_domain", "showDomain"),
            ("show_threshold", "showThreshold"),
        ]


class SvgStackProgressBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackProgressBar", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            "width",
            "xbuffer",
            "progress",
        ]


class SvgStackRangeSlider(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackRangeSlider", children, **kwargs)
        self._attr_names += [
            "height",
            "width",
            "xbuffer",
            "down",
            "scale",
            "seconds",
        ]


class SvgStackRangeSliderVertical(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackRangeSliderVertical", children, **kwargs)
        self._attr_names += [
            "height",
            "right",
            "domain",
            "value",
            "scale",
        ]


class SvgStackStackContainer(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackStackContainer", children, **kwargs)
        self._attr_names += [
            "xbuffer",
            "ybuffer",
            "height",
            ("stack_heights", "stackHeights"),
        ]


class SvgStackTickBar(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentSvgStackTickBar", children, **kwargs)
        self._attr_names += [
            "height",
            "width",
            "down",
            "density",
            ("no_range_slider", "noRangeSlider"),
            "seconds",
            "xbuffer",
        ]


class TimeSlider(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTimeSlider", children, **kwargs)
        self._attr_names += [("step_size", "stepsize")]


class TimeStamp(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTimeStamp", children, **kwargs)


class TrackTable(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentTrackTable", children, **kwargs)


class Video(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("vtComponentVideo", children, **kwargs)
