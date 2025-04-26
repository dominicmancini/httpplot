# example_plots.py

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.random.randn(100)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 60]

# 1. Line Plot (Sine and Cosine)
def plot_line():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, label='Sine Wave')
    ax.plot(x, y2, label='Cosine Wave', linestyle='--')
    ax.set_title('Sine and Cosine Waves')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    return fig, ax

# 2. Scatter Plot (Random Data)
def plot_scatter():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y3, color='r', alpha=0.5, label='Random Data')
    ax.set_title('Scatter Plot of Random Data')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    return fig, ax

# 3. Bar Chart
def plot_bar():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(categories, values, color=['b', 'g', 'r', 'c'])
    ax.set_title('Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    return fig, ax

