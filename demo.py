from customer_personality.exception.exception_handler import AppException
from customer_personality.logger import log
from customer_personality.components.data_ingestion import DataIngestion
from customer_personality.components.data_validation import DataValidation
from customer_personality.components.data_transformation import DataTransformation
from customer_personality.components.model_training import ModelTrainer
from customer_personality.pipeline.training_pipeline import TrainingPipeline
#obj = DataIngestion()
#obj.initiate_data_ingestion()
#print("Data Ingestion Completed!")


obj = DataValidation()
obj.initiate_data_validation()
print("Data Ingestion Completed!")

obj = DataTransformation()
obj.initiate_data_transformation()
print("Data Validation Completed!")


obj = ModelTrainer()
obj.initiate_model_trainer()
print("Model Training Completed!")

obj = TrainingPipeline()
obj.start_training_pipeline()
print(" Training Completed!")