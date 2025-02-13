import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Country_template_dataset:
    def __init__(self, name):
        self.name = name

    def generate_trend(base, frequency, noise_level, years):
        trend = base + 0.4 * np.sin(frequency * np.pi * (years - 1920))
        noise = noise_level * np.random.randn(len(years))
        trend = trend / np.sum(trend) * 10
        return trend + noise

    # make dataframe for Political views (left, right, center, libertarian, etc.) in percentage over time for last 100 years in europe
    def generate_template_dataset(self, years, frequency, noise_level):
        views_df = pd.DataFrame({"Year": years})
        
            
        views_df["Germany"] = self.generate_trend(0.5, frequency, noise_level, years)
        views_df["France"] = self.generate_trend(0.5, frequency, noise_level, years)
        views_df["Italy"] = self.generate_trend(0.5, frequency, noise_level, years)
        views_df["Spain"] = self.generate_trend(0.5, frequency, noise_level, years)
        views_df["United Kingdom"] = self.generate_trend(0.5, frequency, noise_level, years)
        
        return views_df


    def plot_line(df, x, y, size, color, title):
        plt.figure(figsize=(10, 6))
        plt.scatter(df[x], df[y], s=df[size] * 1000, c=df[color], alpha=0.5, cmap='viridis')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)
        plt.colorbar()
    
    def create_figure(self, save=False):    
        base = 0.5
        frequency = 0.1
        noise_level = 0.05
        years = np.arange(1920, 2021, 1)
        
        # Generate template dataset
        views_df = self.generate_template_dataset(years, frequency, noise_level)
        
        # Plot the dataset
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(views_df["Year"], views_df["Germany"], label="Germany")
        ax.plot(views_df["Year"], views_df["France"], label="France")
        ax.plot(views_df["Year"], views_df["Italy"], label="Italy")
        ax.plot(views_df["Year"], views_df["Spain"], label="Spain")
        ax.plot(views_df["Year"], views_df["United Kingdom"], label="United Kingdom")
        ax.legend()
        ax.set_xlabel("Year")
        ax.set_ylabel("Political Views")
        ax.set_title("Political Views in Europe over time")
        
        # print the settings on a text box on the plot
        plt.text(0.5, 0.5, "Base: 0.5\nFrequency: 0.1\nNoise Level: 0.05", transform=ax.transAxes)
        
        plt.show()
        
        # Save the dataset
        if save:
            views_df.to_csv("political_views.csv", index=False)




if __name__ == "__main__":
    
    # Create a template dataset (fix)
    # template = Country_template_dataset("Europe")
    # template.create_figure(save=True)
    
    
    def plot_from_csv(filepath):
        df = pd.read_csv(filepath)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(df["Year"], df["Germany"], label="Germany")
    
    
    current_path = os.path.dirname(__file__)
    print('Current path:', current_path)
    
    filepath = os.path.join(current_path, "parties_long_MPDataset_MPDS2024a.csv")
    df = pd.read_csv(filepath)
    # print(df.head())
    
    # sort party data per left-right axis
    df = df.sort_values("party")