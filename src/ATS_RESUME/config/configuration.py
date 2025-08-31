from src.ATS_RESUME.constants import *
from src.ATS_RESUME.utils.common import read_yaml ,create_directories
from src.ATS_RESUME.entity import DataIngestionConfig , DataTransformationConfig ,ModelTrainerConfig
class ConfigurationManager:
    def __init__(self , config_path = CONFIG_FILE_PATH , param_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(param_path)
        
        create_directories([self.config.artifact_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig :
        
        config = self.config.data_ingestion
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir ,
            data_source = config.data_source
            
            
            
            
        )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        config = self.config.data_transformation
        
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir ,
            train_path = config.train_path ,
            test_path = config.test_path ,
            transformed_train_path = config.transformed_train_path ,
            transformed_test_path = config.transformed_test_path , 
            model_name= config.model_name , 
            tokenizer_name=config.tokenizer_name

            
        )
        
        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            transformed_train_path=config.transformed_train_path,
            transformed_test_path=config.transformed_test_path,
            trained_model_artifact_path=config.trained_model_artifact_path,  # FIXED
            output_dir=params.output_dir,
            eval_strategy=params.eval_strategy,
            save_strategy=params.save_strategy,
            learning_rate=params.learning_rate,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size=params.per_device_eval_batch_size,
            num_train_epochs=params.num_train_epochs,
            weight_decay=params.weight_decay,
            logging_dir="./logs",
            logging_steps=params.logging_steps,
            save_total_limit=params.save_total_limit,
            load_best_model_at_end=params.load_best_model_at_end,
            metric_for_best_model=params.metric_for_best_model,
            greater_is_better=params.greater_is_better,
            warmup_ratio=params.warmup_ratio,
            lr_scheduler_type=params.lr_scheduler_type,
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            fp16=params.fp16,
            seed=params.seed,
            model_name = config.model_name,
            model_pusher = config.model_pusher,
            artifact_root = config.artifact_root,
        )
        return model_trainer_config
