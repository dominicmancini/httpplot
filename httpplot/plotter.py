# plotter.py

import matplotlib.pyplot as plt
from .server import save_current_plot

_original_show = plt.show

def custom_show(*args, **kwargs):
    save_current_plot()
    # Suppress GUI show by not calling _original_show()
    # Uncomment the next line if you *do* want to also show the GUI window:
    # return _original_show(*args, **kwargs)

def hook_matplotlib():
    plt.show = custom_show
