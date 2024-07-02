import pandas as pd

class Merger:
    def __init__(self, output_csv, output_sentiment_csv, output_merged_data_csv):
        """
        Initialize with output_csv, output_sentiment_csv, output_merged_data_csv.
        """
        self.output_csv = output_csv
        self.output_sentiment_csv = output_sentiment_csv
        self.output_merged_data_csv = output_merged_data_csv

    def merge_title_compound_datetime(self):
        """
        Merge title compound and datetime.
        """
        articles_df = pd.read_csv(self.output_csv)
        sentiment_df = pd.read_csv(self.output_sentiment_csv)

        # Extract 'title' column from articles_df and 'compound' and 'datetime' column from sentiment_df
        extracted_df = pd.DataFrame({
            'title': articles_df['title'],
            'compound': sentiment_df['compound'],
            'datetime': sentiment_df['datetime'] 
        })

        # Save the extracted columns to a new CSV file
        extracted_df.to_csv(self.output_merged_data_csv, index=False)
