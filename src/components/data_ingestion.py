import pandas as pd
import os
from src.logger import logging
from src.custom_exception import CustomException
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self, source_data_path: str = None):
        logging.info("Data ingestion process has started.")
        try:
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            if source_data_path:
                source_path = source_data_path
                if not os.path.exists(source_path):
                    raise FileNotFoundError(
                        f"Source data file not found at {source_path}."
                    )
            else:
                source_path = self.ingestion_config.raw_data_path
                if not os.path.exists(source_path):
                    raise FileNotFoundError(
                        f"Raw data file not found at {source_path}."
                    )

            df = pd.read_csv(source_path)
            logging.info("Dataset read successfully from %s.", source_path)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved successfully to %s.", self.ingestion_config.raw_data_path)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info(
                "Train and test data saved successfully to %s and %s.",
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            raise CustomException(e, sys.exc_info())

