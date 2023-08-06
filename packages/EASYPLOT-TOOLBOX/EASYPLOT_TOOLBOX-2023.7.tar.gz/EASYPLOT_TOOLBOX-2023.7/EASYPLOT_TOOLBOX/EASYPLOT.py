import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.lines import Line2D

def CONVERT_SI_TO_INCHES(WIDTH, HEIGHT):
    """ 
    This function convert figure dimensions from meters to inches.
    
    Input:
    WIDTH    |  Figure width in SI units       |         |  Float
    HEIGHT   |  Figure height in SI units      |         |  Float
    
    Output:
    WIDTH    |  Figure width in INCHES units   |         |  Float
    HEIGHT   |  Figure height in INCHES units  |         |  Float
    """
    
    # Converting dimensions
    WIDTH /= 0.0254
    HEIGHT /= 0.0254
    
    return WIDTH, HEIGHT

def SAVE_GRAPHIC(NAME, EXT, DPI):
    """ 
    This function saves graphics according to the selected extension.

    Input: 
    NAME  | Path + name figure               |         |  String
          |   NAME = 'svg'                   |         |  
          |   NAME = 'png'                   |         |
          |   NAME = 'eps'                   |         | 
          |   NAME = 'pdf'                   |         |
    EXT   | File extension                   |         |  String
    DPI   | The resolution in dots per inch  |         |  Integer
    
    Output:
    N/A
    """
    
    plt.savefig(NAME + '.' + EXT, dpi = DPI, bbox_inches = 'tight', transparent = True)

def HISTOGRAM_CHART(**kwargs):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-1.html
    """

    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    CHART_COLOR = PLOT_SETUP['CHART COLOR']
    BINS = int(PLOT_SETUP['BINS'])
    # KDE = PLOT_SETUP['KDE']
    DPI = PLOT_SETUP['DPI']
    EXT = PLOT_SETUP['EXTENSION']
    
    # Dataset and others information
    DATA = DATASET['DATASET']
    COLUMN = DATASET['COLUMN']
 
    # Plot
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    sns.set(style = 'ticks')
    FIG, (AX_BOX, AX_HIST) = plt.subplots(2, figsize = (W, H), sharex = True, gridspec_kw = {'height_ratios': (.15, .85)})
    sns.boxplot(data = DATA, x = COLUMN, ax = AX_BOX, color = CHART_COLOR)
    sns.histplot(data = DATA, x = COLUMN, ax = AX_HIST, color = CHART_COLOR, bins = BINS)
    AX_BOX.set(yticks = [])
    AX_BOX.set(xlabel = '')
    FONT = {'fontname': 'DejaVu Sans',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX_HIST.set_xlabel(xlabel = X_AXIS_LABEL, fontdict = FONT)
    AX_HIST.set_ylabel(ylabel = Y_AXIS_LABEL, fontdict = FONT)
    AX_HIST.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX_HIST.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    plt.grid()
    sns.despine(ax = AX_HIST)
    sns.despine(ax = AX_BOX, left = True)
    
    # Save figure
    SAVE_GRAPHIC(NAME, EXT, DPI)

def LINE_CHART(**kwargs):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-2.html
    """
    
    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    MARKER = PLOT_SETUP['MARKER']
    MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
    LINE_WIDTH = PLOT_SETUP['LINE WIDTH']
    LINE_STYLE = PLOT_SETUP['LINE STYLE']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    COLORS = PLOT_SETUP['CHART COLOR']
    GRID = PLOT_SETUP['ON GRID?']
    YLOGSCALE = PLOT_SETUP['Y LOG']
    XLOGSCALE = PLOT_SETUP['X LOG']
    LOC = PLOT_SETUP['LOC LEGEND']
    SIZE_LEGEND = PLOT_SETUP['SIZE LEGEND']
    
    # Dataset and others information
    X = DATASET['X']
    DATA_Y = DATASET['Y']
    LEGEND = DATASET['LEGEND']
    
    
    # Plot
    W, H = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H), sharex = True)
    for K, Y in enumerate(DATA_Y):
        AX.plot(X, Y, marker = MARKER,  linestyle = LINE_STYLE[K], linewidth = LINE_WIDTH, markersize = MARKER_SIZE, label = LEGEND[K], color = COLORS[K])
    if YLOGSCALE:
        AX.semilogy()
    if XLOGSCALE:
        AX.semilogx()
    font = {'fontname': 'DejaVu Sans',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
    AX.set_xlabel(X_AXIS_LABEL, fontdict = font)   
    AX.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    if GRID == True:
        AX.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
    plt.legend(loc = LOC, prop = {'size': SIZE_LEGEND})
    
    # Save figure
    SAVE_GRAPHIC(NAME, EXT, DPI)

def SCATTER_CHART(**kwargs):    
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-3.html
    """

    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
    CMAP = PLOT_SETUP['CMAP COLOR']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']  
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    GRID = PLOT_SETUP['ON GRID?']
    YLOGSCALE = PLOT_SETUP['Y LOG']
    XLOGSCALE = PLOT_SETUP['X LOG']
    DPI = PLOT_SETUP['DPI']
    EXT = PLOT_SETUP['EXTENSION']

    # Data
    X = DATASET['X']
    Y = DATASET['Y']
    Z = DATASET['SCALE COLOR']
    
    # Plot
    W, H = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H), sharex = True)
    im = AX.scatter(X, Y, c = Z, marker = 'o', s = MARKER_SIZE , cmap = CMAP)
    colorbar = plt.colorbar(im)
    if YLOGSCALE:
        AX.semilogy()
    if XLOGSCALE:
        AX.semilogx()
    FONT = {'fontname': 'DejaVu Sans',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX.set_ylabel(Y_AXIS_LABEL, fontdict = FONT)
    AX.set_xlabel(X_AXIS_LABEL, fontdict = FONT)   
    AX.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR, labelrotation = 0, direction = 'out', which = 'both', length = 10)
    AX.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    if GRID == True:
        AX.grid(color = 'grey', linestyle = '-', linewidth = 1, alpha = 0.20)
    SAVE_GRAPHIC(NAME, EXT, DPI)

def BAR_CHART(**kwargs):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-4.html
    """

    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    BAR_WIDTH = PLOT_SETUP['BAR WIDTH']
    OPACITY = PLOT_SETUP['OPACITY']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    COLORS = PLOT_SETUP['COLORS']
    GRID = PLOT_SETUP['ON GRID?']    
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    
    # Data
    X = DATASET['X']
    Y = DATASET['Y']
    LEGEND = DATASET['LEGEND']
   
    # Plot
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H))
    #error_config = {'ecolor': '0.3'}
    # Create the bar chart for each category
    for I, CATEGORY in enumerate(LEGEND):
        X_VALUES = [CAT + I * BAR_WIDTH for CAT in X]
        AX.bar(X_VALUES, Y[I], BAR_WIDTH, alpha = OPACITY, color = COLORS[I], label = CATEGORY) #, error_kw = error_config)
    FONT = {'fontname': 'DejaVu Sans',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX.set_ylabel(Y_AXIS_LABEL, fontdict = FONT)
    AX.set_xlabel(X_AXIS_LABEL, fontdict = FONT)
    AX.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    AX.set_xticks([CAT + (len(LEGEND) - 1) * BAR_WIDTH / 2 for CAT in X])
    AX.set_xticklabels(X)
    AX.legend()

    if GRID == True:
        AX.grid(color = 'grey', linestyle = '-', linewidth = 1, alpha = 0.20, axis = 'y')
    plt.tight_layout()
    SAVE_GRAPHIC(NAME, EXT, DPI)

def PIZZA_CHART(**kwargs):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-5.html
    """

    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    TEXT_COLOR = PLOT_SETUP['TEXT COLOR']
    TEXT_FONT_SIZE = PLOT_SETUP['TEXT FONT SIZE']
    COLORS = PLOT_SETUP['COLORS']
    LEGEND_SIZE = PLOT_SETUP['SIZE LEGEND']
    UNIT = PLOT_SETUP['UNIT']
    DPI = PLOT_SETUP['DPI']
    EXT = PLOT_SETUP['EXTENSION']

    
    # Dataset
    ELEMENTS = DATASET['ELEMENTS']
    DATA = DATASET['DATA']
    
    
    # Plot
    W, H = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H), subplot_kw = dict(aspect='equal'))
    def func(pct, allvals,unit):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d} {})".format(pct, absolute, unit)
    WEDGES, texts, autotexts = AX.pie(DATA, autopct = lambda pct: func(pct, DATA,UNIT), textprops = dict(color = TEXT_COLOR), colors = COLORS)
    AX.legend(WEDGES,ELEMENTS, loc = 'center left', bbox_to_anchor=(1, 0.5), fontsize=LEGEND_SIZE)
    plt.setp(autotexts,  size = TEXT_FONT_SIZE, weight='bold')
    SAVE_GRAPHIC(NAME, EXT, DPI)

def RADAR_CHART(**kwargs):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-6.html
    """

    # Setup
    DATASET = kwargs.get('DATASET')
    PLOT_SETUP = kwargs.get('PLOT_SETUP')
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    RADAR_DIV_SIZE = PLOT_SETUP['TEXT SIZE']
    RADAR_DIV_COLOR = PLOT_SETUP['DIV COLOR']
    RADAR_COLOR = PLOT_SETUP['RADAR COLOR']
    OPACITY = PLOT_SETUP['OPACITY']
    POLAR_COLOR = PLOT_SETUP['BACKGROUND']
    SIZE_LEGEND = PLOT_SETUP['LEGEND SIZE']
    DPI = PLOT_SETUP['DPI']
    EXT = PLOT_SETUP['EXTENSION']
    
    # Dataset
    DATA = DATASET['COMPLETE DATA']
    RADAR_DIV = DATASET['DIVS']
    RADAR_LABEL = DATASET['DIV LABELS']

    # Plot
    W, H = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H), subplot_kw = {'projection': 'polar'})
    CATEGORIES = list(DATA)[1:]
    N = len(CATEGORIES)
    print(N)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    AX.set_theta_offset(np.pi / 2)
    AX.set_theta_direction(-1)  
    plt.xticks(angles[:-1], CATEGORIES, size = RADAR_DIV_SIZE)  
    AX.set_rlabel_position(180 / N)
    angless = np.linspace(0, 2 * np.pi, N, endpoint = False).tolist()
    for label, anglee in zip(AX.get_xticklabels(), angless):
        if anglee in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < anglee < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
    plt.yticks(RADAR_DIV, RADAR_LABEL, color = RADAR_DIV_COLOR, size = RADAR_DIV_SIZE)
    max_value = max(list(DATA.max())[1:])
    plt.ylim(0, max_value)
    for I in range(len(list(DATA['group']))):
        GROUP = list(DATA['group'])
        values=DATA.loc[I].drop('group').values.flatten().tolist()
        values += values[:1]
        AX.plot(angles, values, linewidth = 2, linestyle = '--', label = GROUP[I], c = RADAR_COLOR[I])
        AX.fill(angles, values, RADAR_COLOR[I], alpha = OPACITY)
    AX.set_facecolor(POLAR_COLOR)
    plt.legend(loc = 'upper right', bbox_to_anchor = (0.1, 0.1), prop = {'size': SIZE_LEGEND})

    SAVE_GRAPHIC(NAME, EXT, DPI)

"""
def TREEMAP_CHART(**kwargs):
    
    libraries
    #!pip install squarify
    import matplotlib.pyplot as plt
    import squarify    # pip install squarify (algorithm for treemap)
    import pandas as pd

    # Create a data frame with fake data
    df = pd.DataFrame({'nb_people':[8,3,4,2], 'group':["group A", "group B", "group C", "group D"] })

    # plot it
    colors = ["red", "black", "green","violet"]
    squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.2, color=colors)
    plt.axis('off')
    plt.show()
"""