import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
import matplotlib.patches as mpatches
from matplotlib.patches import Arc
import math
pd.options.mode.chained_assignment = None

def draw_wenxiang(sequence, colors = ["gray", "yellow", "blue", "red"], labels = False, labelcolor = "black", legend = False):
    "draw wenxiang"
    min_num = 2
    max_num = 18
    num_colors = 4
    circle_radius = 0.04
    num_resid = len(sequence)
    residues = {"A":0, "R":2, "N":1, "D":3, "C":1,
                  "Q":1, "E":3, "G":0, "H":2, "I":0,
                  "L":0, "K":2, "M":0, "F":0, "P":0,
                  "S":1, "T":1, "W":0, "Y":0, "V":0}
    if num_resid not in range(min_num, max_num + 1):
        return "ERROR: sequence must have between 2 and 18 (inclusive) characters."
    if len(colors) != 4:
        return "ERROR: parameter `colors` has missing or too many colors."
    for i in range(len(colors)):
        if colors[i] not in pltcol.cnames:
            return "ERROR: parameter `colors` has invalid colors." 
            
    between_distance = 0.042
    start_radius = 0.0625
    CENTER_Y = 0.5
    CENTER_X = 0.52
    df_spiral = pd.DataFrame(data={'end_angle': [90, 270] * 5, 'start_angle': [270, 90] * 5, 
        'center_y': [CENTER_Y, CENTER_Y + between_distance] * 5, 'center_x': [CENTER_X]* 10, 'radius': start_radius}) 
    df_spiral['start_angle'][9] = 190
    for i in range(10):
        df_spiral['radius'][i] = start_radius + i* between_distance
        
    df_resid = pd.DataFrame(data ={'y': np.array([0.5625, 0.4891, 0.4438, 
        0.5943, 0.6122, 0.3878, 0.4478, 0.7191, 0.54, 0.2695, 
        0.5893, 0.7955, 0.3428, 0.2689, 0.8151, 0.6993, 0.1255, 
        0.4655]), 'x': np.array([0.52, 0.5816, 0.4843, 0.4295, 0.6142, 
        0.6142, 0.3568, 0.4555, 0.747, 0.52, 0.2516, 0.6276, 
        0.7924, 0.2908, 0.2908, 0.8651, 0.6563, 0.0862]), 'color': 'blue', 'type': -5})
    df_resid = df_resid.iloc[range(num_resid)]
    resid_spiral = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10])    
    df_spiral = df_spiral.iloc[range(resid_spiral[num_resid-1])]
    df_spiral['start_angle'][len(df_spiral)-1] = (df_spiral['end_angle'][len(df_spiral)-1] - (num_resid-1) * 100 + 180 * (resid_spiral[num_resid-1]-1))% 360        
    for i in range(num_resid):
        if sequence[i] not in residues:
            return "ERROR: " + sequence[i] + " is not a valid one-letter code for an amino acid."
        df_resid['color'][i] = colors[residues[sequence[i]]]
    #    df_resid['lettername'][i] = sequence[i]
        df_resid['type'][i] = residues[sequence[i]]
    
    fig, ax = plt.subplots()
    for i in range(resid_spiral[num_resid-1]):
        ax.add_patch(Arc((df_spiral['center_x'][i], df_spiral['center_y'][i]), 2*df_spiral['radius'][i], 2*df_spiral['radius'][i], theta1 = df_spiral['start_angle'][i], theta2 = df_spiral['end_angle'][i]))     

    for i in range(num_resid):
        circle = plt.Circle((df_resid['x'][i], df_resid['y'][i]), circle_radius, clip_on = False, zorder = 10, facecolor=df_resid['color'][i], edgecolor = 'black')
        ax.add_artist(circle)
        if labels:
            ax.annotate(sequence[i], xy=(df_resid['x'][i], df_resid['y'][i]), zorder = 15, fontsize=10, ha="center", va = "center", color = labelcolor)
    
    if legend:
        restypes = set(df_resid['type'])
        handleid = []
        nonpolar = mpatches.Patch(color = colors[0], label = 'hydrophobic')
        polar = mpatches.Patch(color = colors[1], label = 'polar')
        basic = mpatches.Patch(color = colors[2], label = 'basic')
        acidic = mpatches.Patch(color = colors[3], label = 'acidic')
        if 0 in restypes:
            handleid = [nonpolar]
            
        if 1 in restypes:
            if bool(handleid):
                handleid.append(polar)
            else:
                handleid = [polar]
                
        if 2 in restypes:
            if bool(handleid):
                handleid.append(basic)
            else:
                handleid = [basic]
        
        if 3 in restypes:
            if bool(handleid):
                handleid.append(acidic)
            else:
                handleid = [acidic]
                
        plt.legend(handles = handleid, loc='center left', bbox_to_anchor=(1.04, 0.5))
        
    plt.axis('off') 
    ax.set_aspect('equal')
    return fig, ax
    