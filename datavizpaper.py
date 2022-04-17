import matplotlib
import math

def initialize_config(text_width_pt, scale=0.3):
    golden_ratio = (math.sqrt(5.0) - 1.0) / 2.0
    text_width_in = text_width_pt / 72.0
    matplotlib.rcParams.update({
        'text.usetex' : True,
        'font.family' : 'serif',
        'font.serif' : [],
        'font.sans-serif' : [],
        'font.monospace' : [],
        'figure.figsize' : [scale * (text_width_in), scale * (text_width_in * golden_ratio)],
        'figure.dpi' : 500,
        'figure.edgecolor' : 'black',
        'axes.edgecolor' : 'black',
        'axes.linewidth' : 0.8,
        'xtick.minor.visible' : True,
        'xtick.top' : True,
        'xtick.direction' : 'in',
        'ytick.minor.visible' : True,
        'ytick.right' : True,
        'ytick.direction' : 'in',
        'figure.autolayout' : True,
        'legend.fancybox' : False,
    })