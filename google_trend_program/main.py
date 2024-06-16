from google_news_fetcher.google_news_fetcher import GoogleNewsFetcher
from csv_to_xlsx_converter.csv_to_xlsx_converter import ConverterCSVtoXLSX
from csv_to_txt_converter.csv_to_txt_converter import ConverterCSVtoTXT
from sentiment_analyzer.sentiment_analyzer import SentimentAnalysis
from datetime_column_inserter.datetime_column_inserter import CSVDatetimeInserter
from sentiment_plotter.sentiment_plotter import SentimentPlotter

# Seach word from 1 to 20
search_word = input("Search word: ")
if 1 <= len(search_word) <= 20:

    # Date range from 1 to 20
    days_back = int(input("Enter a number of range: "))
    if 1 <= days_back <= 20:

        # List of files for naming
        output_csv = (f"{search_word}_articles.csv")
        output_xlsx = (f"{search_word}_articles.xlsx")
        output_txt = (f"{search_word}_articles.txt")
        output_sentiment_csv = (f"{search_word}_articles_sentiment.csv")

        # Fetch articles about the ? from the last ? days
        news_fetcher = GoogleNewsFetcher(search_word, days_back, output_csv)
        news_fetcher.setup_period()
        news_fetcher.fetch_news()
        news_fetcher.save_as_csv()

        # Convert from CSV to Excel
        converter = ConverterCSVtoXLSX(output_csv, output_xlsx)
        converter.read_csv()
        converter.write_excel()

        # Convert from CSV to TXT
        converter = ConverterCSVtoTXT(output_csv, output_txt, encoding='utf-8')
        converter.read_csv()
        converter.write_txt()

        # Analyze title of txt by nltk
        # Save four scores to CSV
        sa = SentimentAnalysis(output_txt, output_sentiment_csv)
        sa.analyze_sentiment()

        # Insert datetime colum at four score CSV
        insert = CSVDatetimeInserter(output_csv, output_sentiment_csv)
        insert.insert_column('datetime', 'compound', output_sentiment_csv)

        # Plotter four score CSV
        plotter = SentimentPlotter(output_sentiment_csv)
        plotter.plot_sentiment()

    else:
        print("Date range must be from 1 to 20.")
        
else:
    print("Seach word length must be from 1 to 20.")  