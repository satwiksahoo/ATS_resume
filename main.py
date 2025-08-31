from src.ATS_RESUME.custom_logging import logger
from src.ATS_RESUME.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.ATS_RESUME.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.ATS_RESUME.pipeline.model_trainer_pipeline import ModelTrainingPipeline

STAGE_NAME = 'DATA INGESTION'

try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion_pipeline()
    logger.info(f'stage {STAGE_NAME} completed')

except Exception as e:
    logger.exception(e)
    

STAGE_NAME = 'DATA TRANSFORMATION'

try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_Data_transformation_pipeline()
    logger.info(f'stage {STAGE_NAME} completed')

except Exception as e:
    logger.exception(e)


STAGE_NAME = 'Model Trainer'

try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.initiate_model_training_pipeline()
    logger.info(f'stage {STAGE_NAME} completed')

except Exception as e:
    logger.exception(e)