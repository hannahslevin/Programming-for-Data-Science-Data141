import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def extract(df, characteristics, by_value = False):
	copy_df = df
    for key,value in characteristics.items():
        if key in copy_df:
            if by_value == False:
                index = value
                copy_df=copy_df[copy_df[key].isin(index)]
                return copy_df
            if by_value == True:
                index = get_valid_index(copy_df[key],value)
                copy_df = copy_df[copy_df[key].isin(index)]
                return copy_df

def get_valid_index(ser,cutoff):
    v = ser.value_counts()
    return list(v[v>=cutoff].index)

def compare_bar(df, plot_cat, hue_cat, log = False, rotation = 0, dim = [8,8], legend_loc = 'best'):
    plt.figure(figsize = dim)
    plt.xticks(rotation = rotation)
    if log == True:
        plt.yscale('log')
    bar = sns.countplot(df[plot_cat], hue = df[hue_cat])
    plt.legend(loc = legend_loc, title = hue_cat)
    return bar

def compare_heat(df, cat_1, cat_2, norm = False, dim = [10,10]):
	heat_table = (pd.crosstab(df[cat_1], df[cat_2], normalize = norm)
	plt.figure(figsize = dim)
	heat_map = sns.heatmap(heat_table)
    return heat

