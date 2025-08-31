from datasets import load_dataset
from src.ATS_RESUME.custom_logging import logger
from src.ATS_RESUME.entity import DataIngestionConfig
import os


class DataIngestion:
    def __init__(self , config: DataIngestionConfig):
        self.config = config
        
    def download_data(self):
        
        ds = load_dataset(self.config.data_source)
        
        os.makedirs(self.config.root_dir , exist_ok= True)
        
        train_path = os.path.join(self.config.root_dir , 'train.csv')
        test_path = os.path.join(self.config.root_dir , 'test.csv')
        ds["train"].to_csv(train_path, index=False)
        ds["test"].to_csv(test_path, index=False)
        
