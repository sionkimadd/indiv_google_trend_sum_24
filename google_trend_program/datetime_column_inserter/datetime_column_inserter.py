import pandas as pd

class CSVDatetimeInserter:
    def __init__(self, source_path, target_path):
        """
        Initialize with source_path, and effect_path.
        """
        self.source_path = source_path
        self.target_path = target_path
        self.source_data = pd.read_csv(source_path)
        self.target_data = pd.read_csv(target_path)

    def insert_column(self, source_col, target_col, upadate_file):
        """
        Inserrt datetime column from the source CSV into the target CSV next to a compound column.
        """
        # Insert + 1 column after target_col
        insert_position = self.target_data.columns.get_loc(target_col) + 1
        
        # Insert source colum in target data
        self.target_data.insert(insert_position, source_col, self.source_data[source_col])
        
        # Save updated DataFrame to CSV file
        self.target_data.to_csv(upadate_file, index=False)
