"""A simple example demonstrating the httpplot library."""

# %%
from httpplot import start_server, plot_bar, plot_line, plot_scatter

# %%
start_server()
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# %% 
fig, ax = plot_scatter()
plt.show()

# %%
fig, ax = plot_bar()
plt.show()


# %%
fig, ax = plot_line()
plt.show()

