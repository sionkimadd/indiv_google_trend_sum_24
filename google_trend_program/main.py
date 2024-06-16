from google_news_fetcher.google_news_fetcher import GoogleNewsFetcher
from csv_to_xlsx_converter.csv_to_xlsx_converter import ConverterCSVtoXLSX
from csv_to_txt_converter.csv_to_txt_converter import ConverterCSVtoTXT

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

    else:
        print("Date range must be from 1 to 20.")
        
else:
    print("Seach word length must be from 1 to 20.")  