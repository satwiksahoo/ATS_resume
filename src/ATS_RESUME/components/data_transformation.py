import re
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer , pipeline

from datasets import Dataset
import numpy as np

from sentence_transformers import SentenceTransformer, InputExample, losses, models, evaluation
from torch.utils.data import DataLoader
import pandas as pd
from datasets import load_dataset
import pickle
from src.ATS_RESUME.entity import DataTransformationConfig
import os
class DataTransformation:
    def __init__(self , config : DataTransformationConfig):
        self.config = config
        
    def preprocess_text(self , text):
        tokens = []
        text = re.sub(r'\r\n|\n', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'<.*?>', ' ', text)
        text = text.strip().lower()
        return text
    
    # def data_transformation_(self):
    #     df_train  = pd.read_csv('./artifacts/data_ingestion/train.csv')
    #     df_test  = pd.read_csv('./artifacts/data_ingestion/test.csv')
        
    #     df_train['label_encoding'] = df_train['label'].map({'No Fit' : 0  , 'Potential Fit' : 1 , 'Good Fit' : 2  } )
    #     df_test['label_encoding'] = df_test['label'].map({'No Fit' : 0  , 'Potential Fit' : 1 , 'Good Fit' : 2  } )
        
    #     df_train['resume_text'] = df_train['resume_text'].apply(self.preprocess_text)
    #     df_test['resume_text'] = df_test['resume_text'].apply(self.preprocess_text)
        
        
    #     df_train['job_description_text'] = df_train['job_description_text'].apply(self.preprocess_text)
    #     df_test['job_description_text'] = df_test['job_description_text'].apply(self.preprocess_text)
        
    #     num_labels = 3  # No Fit, Potential Fit, Good Fit
    #     model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased",  num_labels=num_labels)
    #     tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        
    #     df_train['tokens'] = df_train.apply(lambda row: tokenizer(row['resume_text'] , row['job_description_text'] , padding = 'max_length' , 
    #                                                               truncation = True  , max_length = 256)  ,axis = 1)
    #     df_test['tokens'] = df_test.apply(lambda row: tokenizer(row['resume_text'] , row['job_description_text'] , padding = 'max_length' , 
    #                                                               truncation = True  , max_length = 256)  ,axis = 1)
        
    #     tokens_df = pd.DataFrame(df_train['tokens'].tolist())
        
    #     df_train_expanded = pd.concat([tokens_df , df_train['label_encoding'] ] ,axis =1 )
    #     df_test_expanded = pd.concat([pd.DataFrame(df_test['tokens'].tolist()) , df_test['label_encoding'] ] ,axis =1 )
        
    #     df_train_expanded.rename(columns={"label_encoding": "labels"}, inplace=True)
    #     df_test_expanded.rename(columns={"label_encoding": "labels"}, inplace=True)
        
        
    #     train_dataset = Dataset.from_pandas(df_train_expanded , preserve_index=False)
    #     test_dataset = Dataset.from_pandas(df_test_expanded , preserve_index=False)
        
    #     os.makedirs(os.path.dirname(self.config.transformed_train_path), exist_ok=True)
    #     os.makedirs(os.path.dirname(self.config.transformed_test_path), exist_ok=True)
        
    #     train_dataset.save_to_disk(self.config.transformed_train_path)
    #     test_dataset.save_to_disk(self.config.transformed_test_path)
    
    
    def data_transformation(self):
        
        
        df_train  = pd.read_csv('./artifacts/data_ingestion/train.csv')
        df_test  = pd.read_csv('./artifacts/data_ingestion/test.csv')
        label2score = {
           "No Fit": 0.0,
    "Potential Fit": 0.5,
    "Good Fit": 1.0
}       
        
        train_examples = [
             InputExample(
        texts=[row.resume_text, row.job_description_text],
        label=label2score[row.label])
             for _, row in df_train.iterrows()
]



        test_examples = [
    InputExample(
        texts=[row.resume_text, row.job_description_text],
        label=label2score[row.label]
    )
    for _, row in df_test.iterrows()
]


        train_data = train_examples
        val_data = test_examples
        
        os.makedirs(os.path.dirname(self.config.transformed_train_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.config.transformed_test_path), exist_ok=True)
        
        train_file = os.path.join(self.config.transformed_train_path, "train.pkl")
        test_file = os.path.join(self.config.transformed_test_path, "test.pkl")
        
        # train_data.save_to_disk(self.config.transformed_train_path)
        # val_data.save_to_disk(self.config.transformed_test_path)
        
        with open(train_file, "wb") as f:
         pickle.dump(train_data, f)

        with open(test_file, "wb") as f:
         pickle.dump(val_data, f)

        
    
        
    
        
        
        
        
        


        
        
        
        