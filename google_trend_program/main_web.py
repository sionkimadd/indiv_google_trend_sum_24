from google_news_fetcher.google_news_fetcher import GoogleNewsFetcher
from csv_to_xlsx_converter.csv_to_xlsx_converter import ConverterCSVtoXLSX
from csv_to_txt_converter.csv_to_txt_converter import ConverterCSVtoTXT
from sentiment_analyzer.sentiment_analyzer import SentimentAnalysis
from datetime_column_inserter.datetime_column_inserter import CSVDatetimeInserter
from sentiment_plotter_png.sentiment_plotter_png import SentimentPlotter
from data_merger.data_merger import Merger

generated_file = []  

def fetch_google_news(search_word, days_back):
    output_csv = f"{search_word}_articles.csv"
    news_fetcher = GoogleNewsFetcher(search_word, days_back, output_csv)
    news_fetcher.setup_period()
    news_fetcher.fetch_news()
    news_fetcher.save_as_csv()
    generated_file.append(output_csv)
    return output_csv

def convert_csv_to_txt(output_csv):
    output_txt = output_csv.replace('_articles.csv', '_articles.txt')  
    converter = ConverterCSVtoTXT(output_csv, output_txt, encoding='utf-8')
    converter.read_csv()
    converter.write_txt()
    generated_file.append(output_txt)
    return output_txt

def convert_csv_to_xlsx(output_csv):
    output_xlsx = output_csv.replace('_articles.csv', '_articles.xlsx')
    converter = ConverterCSVtoXLSX(output_csv, output_xlsx)
    converter.read_csv()
    converter.write_excel()
    generated_file.append(output_xlsx)
    return output_xlsx

def analyze_sentiment_nltk(output_txt):
    output_sentiment_csv = output_txt.replace('.txt', '_sentiment.csv')
    sa = SentimentAnalysis(output_txt, output_sentiment_csv)
    sa.analyze_sentiment()
    return output_sentiment_csv

def insert_datetime(output_csv, output_sentiment_csv):
    insert = CSVDatetimeInserter(output_csv, output_sentiment_csv)
    insert.insert_column('datetime', 'compound', output_sentiment_csv)
    return output_sentiment_csv

def plotter_sentiment_nltk(search_word, output_sentiment_csv):
    plotter = SentimentPlotter(output_sentiment_csv)
    plotter.plot_sentiment(search_word)

def merge_data(output_csv, output_sentiment_csv):
    output_merged_data_csv = output_csv.replace('.csv', '_title_compound_datetime.csv')
    merger = Merger(output_csv, output_sentiment_csv, output_merged_data_csv)
    merger.merge_title_compound_datetime()
    generated_file.append(output_merged_data_csv)
    return output_merged_data_csv
