import pandas as pd

class ConverterCSVtoTXT:
    
    def __init__(self, output_csv, output_txt, encoding = 'utf-8'):
        """
        Initialize with output_csv, output_txt, and encoding.
        """
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.encoding = encoding
    
    def read_csv(self):
        """
        Read a CSV file.
        Calculate maxinum width of content in each column.
        """
        # Read data from CSV file as DataFrame
        self.data = pd.read_csv(self.output_csv, encoding=self.encoding)

        # Calculate max width for each column
        self.max_widths = [max(self.data[col].astype(str).apply(len).max(), len(col)) for col in self.data.columns]

    def write_txt(self): 
        """
        Write data in TXT file.
        Each column is left-justified based on its maximum width + 3.

        Steps:
        - Open the TXT file.
        - Write the headers.
        - Insert a _ seperator.
        - Write each row of data.
        - Ensure the alignment.
        """
        # Open TXT file for writing
        with open(self.output_txt, 'w', encoding=self.encoding) as txtfile:
            
            # Create header by left-justifying each column name to the maximum width plus 3 spaces
            formatted_header = "".join(col.ljust(width + 3) for col, width in zip(self.data.columns, self.max_widths))
            
            # Write formatted header to TXT file
            txtfile.write(formatted_header + '\n')

            # Write a separator line under header
            txtfile.write('_' * len(formatted_header) + '\n')
            
            for row in self.data.itertuples(index=False):
                
                # Format each row by left-justifying each item to the maximum width plus 3 spaces
                formatted_row = "".join(str(item).ljust(width + 3) for item, width in zip(row, self.max_widths))
                
                # Write formatted row to TXT file
                txtfile.write(formatted_row + '\n')
