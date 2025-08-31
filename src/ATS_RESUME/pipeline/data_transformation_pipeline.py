from src.ATS_RESUME.config.configuration import ConfigurationManager
from src.ATS_RESUME.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
       pass
    
    def initiate_Data_transformation_pipeline(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.data_transformation()        
    

    # def initiate_data_ingestion_pipeline(self):
        
    #     config = ConfigurationManager()
    #     data_ingestion_config = config.get_data_ingestion_config()
    #     data_ingestion = DataIngestion(config = data_ingestion_config)
    #     data_ingestion.download_data()
