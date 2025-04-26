# httpsplot/backend.py

# NOTE: May need to import this module in __init__.py

import matplotlib.backends.backend_agg as backend_agg
from matplotlib.backend_bases import FigureManagerBase, ShowBase
from matplotlib.figure import Figure
from .server import save_current_plot, start_server  # use your server logic

class FigureCanvasHttpPlot(backend_agg.FigureCanvasAgg):
    def draw(self):
        super().draw()
        save_current_plot()

class FigureManagerHttpPlot(FigureManagerBase):
    pass



def new_figure_manager(num, *args, **kwargs):
    # NOTE: OLD code these 2 lines
    # canvas = FigureCanvasHttpPlot(backend_agg.Figure(*args, **kwargs))
    # return FigureManagerHttpPlot(canvas, num)
    figure = Figure(*args, **kwargs)
    canvas = FigureCanvasHttpPlot(figure)
    return FigureManagerHttpPlot(canvas, num)



def show(*args, **kwargs):
    start_server()
    # Do nothing else; auto refresh is already handled by the web viewer

# Required backend name
backend_version = '1.0'
