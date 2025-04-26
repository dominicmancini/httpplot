# httpplot
----------------

A lightweight, interactive plotting backend and web viewer for matplotlib — inspired by R's `httpgd`. Plots are displayed in real-time in your browser with a scrollable history of previous plots. Great for live development, exploration, and REPL workflows.

<!-- TODO: put a screenshot here -->

## Features

- Real-time plot updates in the browser
- Clickable plot history (thumbnail sidebar)
- Clean, minimal UI using Flask and vanilla JS
- Save and copy plot images from browser

### Future plans
- Rich display of dataframes and tabular data
- Integration as a custom `matplotlib` backend for easy use ( `matplotlib.use("module://httpsplot.backend")`)

## Quick start
```bash
git clone https://github.com/dominicgmancini/httpplot.git
cd httpplot
pip install .
```

## Usage
```python
from httpplot import start_server

# start server and automatically open browser
start_server()

# Create plots to display
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])

# display plot
plt.show() 
```

## About

`plotting_backend` was written by `Dominic Mancini <dominicgmancini@gmail.com>`.
A data science student passionate about building tools for analytics, workflows, and visualizations. 

`plotting_backend` is released under the [MIT License](https://github.com/domancini/plotting_backend/blob/main/LICENSE)

### Authors
