
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from datasets import load_from_disk
from sentence_transformers import SentenceTransformer, InputExample, losses, models, evaluation
from torch.utils.data import DataLoader
import pandas as pd
from datasets import load_dataset
import pickle
import os
from src.ATS_RESUME.entity import ModelTrainerConfig
from src.ATS_RESUME.constants import *
from src.ATS_RESUME.utils.common import read_yaml ,create_directories
from src.ATS_RESUME.cloud.s3_syncer import s3_sync
from src.ATS_RESUME.config.configuration import ConfigurationManager
from datetime import datetime
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.root = read_yaml(CONFIG_FILE_PATH)
        self.config = config
        self.s3_syncer = s3_sync()
        

    def sync_artifact_dir_to_s3(self):

        TRAINING_BUCKET_NAME = 'resumeats1'
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifacts/{datetime.now().timestamp()}"
            
            self.s3_syncer.sync_folder_to_s3(folder = self.config.artifact_root  , aws_bucket_url=aws_bucket_url)
        
        except Exception as e:
            raise (e)
    
    
    def sync_saved_model_dir_from_s3(self):

        TRAINING_BUCKET_NAME = 'resumeats1'
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/model5/{datetime.now().timestamp()}"
            
            self.s3_syncer.sync_folder_to_s3(folder = self.config.model_pusher , aws_bucket_url=aws_bucket_url)
        
        except Exception as e:
            raise e
            
    
    
    
    def initiate_model_trainer(self):
        
        
    #     train_file = os.path.join(self.config.transformed_train_path, "train.pkl")
    #     test_file = os.path.join(self.config.transformed_test_path, "test.pkl")
        
    #     with open(train_file, "rb") as f:
    #       train_data = pickle.load(f)

    #     with open(test_file, "rb") as f:
    #        val_data = pickle.load(f)

        
        
    #     train_dataloader = DataLoader(train_data, shuffle=True, batch_size=16)
    #     test_dataloader = DataLoader(val_data, shuffle=False, batch_size=16)


    #     model = SentenceTransformer(self.config.model_name)


    #     train_loss = losses.CosineSimilarityLoss(model)

    #     evaluator = evaluation.EmbeddingSimilarityEvaluator.from_input_examples(val_data, name="val")


    #     model.fit(
    # train_objectives=[(train_dataloader, train_loss)],
    # evaluator=evaluator,
    # epochs=6,
    # warmup_steps=100,
    # evaluation_steps=500,
    # output_path= self.config.trained_model_artifact_path
    # )
        
        
    #     model.save_pretrained(self.config.model_pusher)
        
        self.sync_artifact_dir_to_s3()
        self.sync_saved_model_dir_from_s3()
        
# if __name__ == "__main__":
    
#     model_trainer = ModelTrainer()
#     model_trainer.sync_artifact_dir_to_s3()
#     model_trainer.sync_saved_model_dir_from_s3()
        
    

        
