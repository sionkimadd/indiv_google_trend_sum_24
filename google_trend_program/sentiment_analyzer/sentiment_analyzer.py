import csv
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysis:
    
    def __init__(self, output_txt, output_four_scores_csv):
        """
        Initialize with output_txt, and output_four_scores_csv.
        """
        self.output_txt = output_txt
        self.output_four_scores_csv = output_four_scores_csv
        self.stop_word = '   '
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self):
        """
        Analyze the title of articles.
        Save the sentiment scores (neg, neu, pos, compound) to a CSV file.
        """
        # Open sentiment CSV file for writing
        with open(self.output_four_scores_csv, mode='w', newline='', encoding='utf-8') as out_file:
            
            # Create a CSV writer object
            csv_writer = csv.writer(out_file)
            
            # Write the header row
            csv_writer.writerow(['neg', 'neu', 'pos', 'compound'])

            # Open and read the output_txt file
            with open(self.output_txt, 'r', encoding='utf-8') as in_file:
                
                # Skip the first line due to headers
                next(in_file)  
                
                # Skip the second line due to seperator
                next(in_file)

                # Iterate over per line 
                for line in in_file:
                    
                    if self.stop_word in line:
                        
                        # Extract the title part before the stop word (three spaces)
                        per_line = line[:line.index(self.stop_word)]

                        # Analyze sentiment of title
                        sentiment_scores = self.sia.polarity_scores(per_line)

                        # Write sentiment scores to sentiment CSV file
                        csv_writer.writerow([
                            sentiment_scores['neg'],
                            sentiment_scores['neu'],
                            sentiment_scores['pos'],
                            sentiment_scores['compound']
                        ])