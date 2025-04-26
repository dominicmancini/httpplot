"""httpplot - Utilities for interactive matplotlib plotting."""

from .server import start_server, stop_server
from .plotter import hook_matplotlib
from .example_plots import plot_bar, plot_line, plot_scatter
from .loader import load_resource_text
import matplotlib
matplotlib.use("Agg")

# hook into plt.show() to capture plots
hook_matplotlib()
