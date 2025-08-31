from src.ATS_RESUME.config.configuration import ConfigurationManager
from src.ATS_RESUME.components.model_trainer import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    def initiate_model_training_pipeline(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.initiate_model_trainer()
