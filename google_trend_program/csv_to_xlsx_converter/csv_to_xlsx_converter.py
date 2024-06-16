import pandas as pd

class ConverterCSVtoXLSX:
    
    def __init__(self, output_csv, output_xlxs):
        """
        Initialize with input_csv, and output_xlxs.
        """
        self.output_csv = output_csv
        self.output_xlxs = output_xlxs

    def read_csv(self):
        """ 
        Read the CSV file.
        Store the data in DataFrame. 
        """
        # Read data from CSV file as DataFrame
        self.data = pd.read_csv(self.output_csv)

    def write_excel(self):
        """ 
        Write the data from the DataFrame to Excel.
        """
        # Save data to Excel file without index
        self.data.to_excel(self.output_xlxs, index = False, engine='openpyxl')