import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
from google_news_fetcher.google_news_fetcher import GoogleNewsFetcher
from csv_to_xlsx_converter.csv_to_xlsx_converter import ConverterCSVtoXLSX
from csv_to_txt_converter.csv_to_txt_converter import ConverterCSVtoTXT
from sentiment_analyzer.sentiment_analyzer import SentimentAnalysis
from datetime_column_inserter.datetime_column_inserter import CSVDatetimeInserter
from sentiment_plotter.sentiment_plotter import SentimentPlotter

# List of storage space
output_csv = None
# output_xlsx =
output_txt = None
output_sentiment_csv = None
# new_file =
# List of generated files
generated_file = []  

def file_list_box(new_file):
    """ Append and insert file on list and listbox. """
    # Conduct code if new_file not in generated file
    if new_file and new_file not in generated_file:

        # Append new file on list
        generated_file.append(new_file)

        # Insert new file on listbox (Tkinter)
        listbox_widget.insert(tk.END, new_file)

def fetch_google_news():
    """ Fetch Google news. """
    global output_csv

    # Store search word from enter field
    search_word = entry_search.get()

    # Store day range from enter field
    days_back = int(entry_days.get())

    # Name CSV based on search word
    output_csv = f"{search_word}_articles.csv"

    # Fetch articles about the ? from the last ? days
    news_fetcher = GoogleNewsFetcher(search_word, days_back, output_csv)
    news_fetcher.setup_period()
    news_fetcher.fetch_news()
    news_fetcher.save_as_csv()

    # Append on list
    # Insert on listbox (Tkinter)
    file_list_box(output_csv)
    messagebox.showinfo("Success", "Google news fetched and saved as CSV!")
    
    # Delete existing file
    entry_file.delete(0, tk.END)
    
    # Insert new file
    entry_file.insert(0, output_csv)

def convert_csv_to_txt():
    """ Convert CSV to TXT. """
    global output_txt 

    # Bring CSV file name
    output_csv = entry_file.get()

    if output_csv:

        # Rename from _articles.csv to _articles.txt
        output_txt = output_csv.replace('_articles.csv', '_articles.txt')  
        
        # Convert from CSV to TXT
        converter = ConverterCSVtoTXT(output_csv, output_txt, encoding='utf-8')
        converter.read_csv()
        converter.write_txt()

        # Append on list
        # Insert on listbox (Tkinter)
        file_list_box(output_txt)
        messagebox.showinfo("Success", f"File converted and saved as {output_txt}!")

def convert_csv_to_xlsx():
    """ Convert CSV to Excel. """
    # Bring CSV file name
    output_csv = entry_file.get()

    if output_csv:

        # Rename from _articles.csv to _articles.xlsx
        output_xlsx = output_csv.replace('_articles.csv', '_articles.xlsx')
        
        # Convert from CSV to Excel
        converter = ConverterCSVtoXLSX(output_csv, output_xlsx)
        converter.read_csv()
        converter.write_excel()

        # Append on list
        # Insert on listbox (Tkinter)
        file_list_box(output_xlsx)
        messagebox.showinfo("Success", f"File converted and saved as {output_xlsx}!")

def analyze_sentiment_nltk():
    """ Analyze sentiment by NLTK. """
    global output_txt
    global output_sentiment_csv

    if output_txt:

        # Rename from _articles.txt to _articles_sentiment.csv
        output_sentiment_csv = output_txt.replace('.txt', '_sentiment.csv')
        
        # Analyze title of txt by nltk
        # Save four scores to CSV
        sa = SentimentAnalysis(output_txt, output_sentiment_csv)
        sa.analyze_sentiment()
        messagebox.showinfo("Success", f"Sentiment analysis completed in {output_sentiment_csv}!")

def insert_datetime():
    """ Insert datetime in sentiment CSV. """
    global output_csv
    global output_sentiment_csv 

    if output_csv:
        
        # Insert datetime colum at four score CSV
        insert = CSVDatetimeInserter(output_csv, output_sentiment_csv)
        insert.insert_column('datetime', 'compound', output_sentiment_csv)

        # Append on list
        # Insert on listbox (Tkinter)
        file_list_box(output_sentiment_csv)
        messagebox.showinfo("Success", f"Datetime inserted and saved as {output_sentiment_csv}!")

def plotter_sentiment_nltk():
    """ Plot title by sentiment. """
    global output_sentiment_csv

    if output_sentiment_csv:

        # Plotter four score CSV
        plotter = SentimentPlotter(output_sentiment_csv)
        plotter.plot_sentiment()

def conduct_all():
    """ Conduct all methods. """
    convert_csv_to_txt()
    convert_csv_to_xlsx()
    analyze_sentiment_nltk()
    insert_datetime()
    plotter_sentiment_nltk()

def download_file():

    global listbox_widget

    # Bring selected file on listbox
    selected_file = listbox_widget.get(tk.ANCHOR)

    if selected_file:

        # Select destination for saving
        destination = filedialog.asksaveasfilename(initialfile = selected_file)
        
        if destination:
            
            # Copy file on destination
            shutil.copy(selected_file, destination)
            messagebox.showinfo("Success", f"File saved to {destination}")

# Create root window (Tkinter)
root = tk.Tk()

# Naming root window
root.title("Google News Fetcher and Plotter")

# Sizing root window
# Locating root window
root.geometry("500x500+500+200")

# Create label
tk.Label(root, text = "Search Word:").pack()
# Create search field
entry_search = tk.Entry(root)
# Display on root window
entry_search.pack()

# Create label
tk.Label(root, text = "Days Back:").pack()
# Create search field
entry_days = tk.Entry(root)
# Display on root window
entry_days.pack()

# Create a button to fecth_news method
fetch_button = tk.Button(root, text = "Fetch News", command = fetch_google_news)
fetch_button.pack(pady=5)

# Create label
tk.Label(root, text = "File for Conversion (CSV):").pack()
# Creat field to output_csv
entry_file = tk.Entry(root)
# Display on root window
entry_file.pack()

# Create a button to conduct_all_button
conduct_all_button = tk.Button(root, text = "All", command = conduct_all)
conduct_all_button.pack(pady=5)

# Create a listbox
listbox_widget = tk.Listbox(root, width=50, height=10)
listbox_widget.pack(pady=10)

# Create a button to download_file
download_button = tk.Button(root, text = "Download File", command = download_file)
download_button.pack(pady=5)

root.mainloop()