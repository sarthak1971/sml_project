import sys
import os

# Add the project root to path
sys.path.insert(0, os.getcwd())

from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        print("Starting data ingestion...")
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        print(f"\n✓ Data ingestion completed successfully!")
        print(f"Train data saved to: {train_path}")
        print(f"Test data saved to: {test_path}")
    except Exception as e:
        print(f"Error during data ingestion: {e}")
        sys.exit(1)
