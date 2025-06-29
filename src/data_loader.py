# import libraries
import os
import numpy as np
import pandas as pd

class DataLoader:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.data = None

    def load_data(self, filename: str) -> pd.DataFrame:
        """Load data from a CSV file."""
        file_path = os.path.join(self.data_dir, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {filename} not found in {self.data_dir}")
        self.data = pd.read_csv(file_path)
        return self.data