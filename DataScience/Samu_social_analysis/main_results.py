import install_pkg
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_corr_matrix(df):
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filepath = os.path.join(current_dir,filename)
    df = pd.read_excel(filepath)
    # Compute the correlation matrix
    corr_matrix = df.corr()

    # Set diagonal and upper-triangular elements to NaN
    corr_matrix_below_diagonal = np.tril(corr_matrix, k=0)  # "k=-1" means below diagonal
    corr_matrix_below_diagonal[corr_matrix_below_diagonal == 0] = np.nan

    # Create a heatmap using Seaborn
    sns.set(style='ticks',font_scale=1)
    sns.heatmap(corr_matrix_below_diagonal, cmap='coolwarm', annot=True, fmt='.2f',
                xticklabels=corr_matrix.columns.values,
                yticklabels=corr_matrix.columns.values)

    # Rotate the x-axis tick labels by 45 degrees
    plt.xticks(rotation=45, ha='right')
    # Add title
    plt.title('')

    # Save plot
    savedir = os.path.join(current_dir,'correlation_matrix.jpeg')
    plt.savefig(savedir,dpi=300, bbox_inches='tight')

def plot_scatter(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filepath = os.path.join(current_dir,filename)
    df = pd.read_excel(filepath)
    
    # Create a scatterplot matrix using Seaborn
    sns.set(style='ticks',font_scale=1.5)
    g = sns.PairGrid(df, diag_sharey=False,hue="Posição")
    g.map_lower(sns.scatterplot, size =df['Total minutos'])
    g.map_diag(sns.kdeplot)

    # Rotate tick labels
    for ax in g.axes.flat:
        ax.xaxis.label.set_rotation(45)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha('right')
        ax.xaxis.label.set_ha('center')

    g.add_legend(title="", adjust_subtitles=True)

    # # Save plot
    savedir = os.path.join(current_dir,'correlation_scatter.jpeg')
    plt.savefig(savedir, dpi=300, bbox_inches='tight')

filename = 'Dados.xlsx'
plot_corr_matrix(filename)

plot_scatter(filename)