import os
from datetime import datetime, timedelta
import pandas as pd
from GoogleNews import GoogleNews

class GoogleNewsFetcher:
    def __init__(self, search_word, days_back, output_csv):
        """
        Initialize with search_word, days_back, and output_csv.
        """
        self.search_word = search_word
        self.days_back = days_back
        self.output_csv = output_csv
        self.setup_period()

    def setup_period(self):
        """
        Set up date range.
        """
        # Save current date in "YYYY-MM-DD" format
        today = datetime.now().date()

        # Subtract days_back from today in "YYYY-MM-DD" format
        start_date = today - timedelta(days = self.days_back)

        # Convert end date format from "YYYY-MM-DD" to "MM/DD/YYYY"
        self.end_date_str = today.strftime("%m/%d/%Y")

        # Convert start date format from "YYYY-MM-DD" to "MM/DD/YYYY"    
        self.start_date_str  = start_date.strftime("%m/%d/%Y")

    def fetch_news(self):
        """
        Fetch news from Google News.
        """
        # Set up date range for GoogleNews 
        g_news = GoogleNews(start = self.start_date_str , end = self.end_date_str)
        
        # Fetch news by search_word
        g_news.get_news(self.search_word)
        
        # Save fetched news as a list
        self.fetched_list = g_news.result()

    def save_as_csv(self):
        """ 
        Save and sort fetched news data as a CSV file.
        """
        # Convert fetched news from list to pandas DataFrame
        news_data = pd.DataFrame(self.fetched_list)

        # Select columns as title, datetime, link
        selected_news_data = ["title", "datetime", "link"]
        news_data = news_data[selected_news_data]

        # Convert "datetime" column from string to datetime object
        # Convert error to Not a Time(Nat)
        news_data["datetime"] = pd.to_datetime(news_data["datetime"], errors = "coerce")
        
        # Check presence or absence of output_csv
        if os.path.exists(self.output_csv):

            # Read existing date from CSV file as a
            existing_news_data = pd.read_csv(self.output_csv)

            # Convert "datetime" column from string to datetime object
            # Convert error to Not a Time (Nat)
            existing_news_data["datetime"] = pd.to_datetime(existing_news_data["datetime"], errors = "coerce")

            # Concatenate existing data with new news data
            # Ignore index
            combined_news_data = pd.concat([existing_news_data, news_data], ignore_index = True)
            
            # Drop duplicate row based on "title" column
            # Keep last 
            combined_news_data = combined_news_data.drop_duplicates(subset = ["title"], keep = "last")
            
            # Drop rows with NaT
            combined_news_data = combined_news_data.dropna(subset = ["datetime"])
            
            # Sort combined data by "datetime" column
            combined_news_data = combined_news_data.sort_values("datetime")
        
        else:
            
            # Drop rows with NaT
            news_data = news_data.dropna(subset=["datetime"])

            # Sort combined data by "datetime" column
            combined_news_data = news_data.sort_values("datetime")

        # Save sorted data to CSV file without index
        combined_news_data.to_csv(self.output_csv, index = False)