from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

def scrape_billionaire_data():
    """
    Scrapes billionaire data from the Bloomberg Billionaires website.

    Returns:
        pandas.DataFrame: A DataFrame containing billionaire names and net worth.
    """

    url = "https://www.bloomberg.com/billionaires/"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the relevant HTML elements (adjust this based on the website's structure)
    # Example: Assuming the net worth is within a specific tag/class
    billionaire_data = []
    for item in soup.find_all("div", class_="some-class-for-billionaire-data"): 
        name = item.find("span", class_="name").text.strip()
        net_worth_str = item.find("span", class_="net-worth").text.strip()
        net_worth = float(net_worth_str.replace("$", "").replace("B", "000000000")) 
        billionaire_data.append({"Name": name, "Net Worth": net_worth})

    return pd.DataFrame(billionaire_data)

def plot_billionaire_net_worth(df):
    """
    Creates a balloon plot of billionaire net worth.

    Args:
        df (pandas.DataFrame): DataFrame containing billionaire names and net worth.
    """

    plt.figure(figsize=(10, 6))
    import pdb; pdb.set_trace() 
    plt.scatter(df["Name"], [1] * len(df), s=df["Net Worth"] / 1e9, alpha=0.5)  # Normalize size
    plt.xlabel("Billionaire")
    plt.ylabel("")  # No y-axis label needed for this plot
    plt.title("Billionaire Net Worth (Bubble Size Represents Net Worth in Billions)")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
    plt.show()

if __name__ == "__main__":
    billionaire_df = scrape_billionaire_data()
    plot_billionaire_net_worth(billionaire_df)