import numpy as np

import matplotlib.pyplot as plt

def plot_function(func, x_range):
    x = generate_x_values(x_range)
    y = compute_y_values(func, x)
    
    setup_plot()
    plot_data(x, y, func)
    finalize_plot(func)

def generate_x_values(x_range):
    return np.linspace(x_range[0], x_range[1], 400)

def compute_y_values(func, x):
    return func(x)

def setup_plot():
    plt.figure(figsize=(8, 6))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.yscale('log')

def plot_data(x, y, func):
    plt.plot(x, y, label=f'{func.__name__}(x)')

def finalize_plot(func):
    plt.title(f'Plot of {func.__name__}(x)')
    plt.legend()
    plt.show()

# Example usage:
if __name__ == "__main__":
    def G(t):
        return 1 / (1 - t)
    plot_function(G, (0, 1))