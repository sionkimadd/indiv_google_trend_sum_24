from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import main_web as mweb
import os

# Create Flask app
app = Flask(__name__)

# Create empty list to store generated files
generated_file = []

# Route for main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for All button for POST data to server
@app.route('/conduct_all', methods = ['POST'])
def conduct_all():
    
    # Get JSON data 
    data = request.get_json()
    # Extract search_word data from JSON
    search_word = data.get('search_word')
    # Extract days_back data from JSON and convert to int
    days_back = int(data.get('days_back'))
    
    ##################################main_web#######################################
    output_csv = mweb.fetch_google_news(search_word, days_back)
    output_txt = mweb.convert_csv_to_txt(output_csv)
    output_xlsx = mweb.convert_csv_to_xlsx(output_csv)
    output_sentiment_csv = mweb.analyze_sentiment_nltk(output_txt)
    output_sentiment_csv = mweb.insert_datetime(output_csv, output_sentiment_csv)
    output_merged_data_csv = mweb.merge_data(output_csv, output_sentiment_csv)
    mweb.plotter_sentiment_nltk(search_word, output_sentiment_csv) 
    #################################################################################
    
    # Store genreated files on generated_files list
    generated_files = [
        output_csv, output_txt, output_xlsx, output_sentiment_csv, output_merged_data_csv
    ]
    
    # Return JSON with a list of generated files and graph URL
    return jsonify({
        'generated_files': generated_files,
        'plot_url': url_for('static', filename = f'sentiment_plot_{search_word}.png')
    })

# Route for file download for GET data from server
@app.route('/download/<filename>', methods = ['GET'])
def download_file(filename):
    directory = os.getcwd()
    return send_from_directory(directory, filename, as_attachment=True)

# Start Flask app in debug mode
# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
