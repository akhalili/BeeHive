__author__ = 'Amirhossein'

from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color

class TrackBar(Widget):

    __num_markers = 10

    def __init__(self):
        super(TrackBar, self).__init__()

        with self.canvas:

            # some consts for rational draw
            center_x = self.width / 2
            height_factor = self.height / self.__num_markers

            # draw markers
            for marker_idx in range(self.__num_markers):

                # Add the marker
                Color(1, 1, 0)
                marker_diameter = abs(marker_idx - self.__num_markers / 2) * height_factor / 4 + 3
                Ellipse(pos=(center_x - marker_diameter / 2, marker_idx*height_factor),
                        size=(marker_diameter, marker_diameter)
                        )
