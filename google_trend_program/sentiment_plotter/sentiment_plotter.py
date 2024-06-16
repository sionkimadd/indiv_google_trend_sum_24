import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

class SentimentPlotter:

    def __init__(self, output_sentiment_csv):
        """
        Initialize with output_sentiment_csv.
        """
        self.sentiment_data = pd.read_csv(output_sentiment_csv)
        self.sentiment_data['datetime'] = pd.to_datetime(self.sentiment_data['datetime'])
        self.filter_sentiment_data()

    def filter_sentiment_data(self):
        """ Filter compound 0 for remove neutral article. """
        
        # Filter data to exclude rows that is compound 0
        self.filtered_data = self.sentiment_data[self.sentiment_data['compound'] != 0]

    def plot_sentiment(self):
        """ Plotter CSV to scatter. """
        # Create a new figure with a specified size
        plt.figure(figsize=(1.618 * 8, 8))

        # Plot a scatter plot of datetime and compound
        plt.scatter(self.filtered_data['datetime'], self.filtered_data['compound'], alpha=0.5)
        
        # Convert datetime to ordinal value
        # Store datetime value in x
        x_numeric = self.filtered_data['datetime'].map(pd.Timestamp.toordinal)
        
        # Store compound value in y
        y = self.filtered_data['compound']

        # 2nd degree polynomial (ax^2 + bx + c = y)
        z = np.polyfit(x_numeric, y, 2)

        # Create a polynomial object
        p = np.poly1d(z)

        # Plot a polynomial with a blue solid line        
        plt.plot(self.filtered_data['datetime'], p(x_numeric), "b-")

        # Set title
        plt.title('Archive of Trend', fontsize=14)

        # Set x-axis (empty)
        plt.xlabel('')

        # Set y-axis
        plt.ylabel('Range of Compound Score', fontsize=11)
        
        # Set y-axis limits
        plt.ylim(-1, 1)

        # Draw a red horizontal solid line at y=0
        plt.axhline(0, color='red', linewidth=1, linestyle='-')
        
        # Enable grid
        plt.grid(True)

        # Rotate x-axis
        # Set font size
        plt.xticks(rotation=90, fontsize=7)
        
        # Display plot
        plt.show()