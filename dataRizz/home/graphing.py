import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def makeGraph(x_name, x_data, y_name, y_data, title='', x_descriptor='', y_descriptor='', color="#888888", highlight_color='#FF0000',highlight=None):
    results = pd.DataFrame({x_name: x_data, y_name: y_data})
    results = results.sort_values(by=[y_name], ascending=True)
    graph = plt.bar(results[x_name], results[y_name], color=color)
    
    if highlight != None:
        graph.patches[highlight].set_color(highlight_color)

    plt.xlabel(x_descriptor)
    plt.ylabel(y_descriptor)
    plt.title(title)
    
    plt.bar_label(plt.gca().containers[0], fmt='%.2f%%', padding=3, fontsize=6)
    plt.show()