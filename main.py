from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.pipline.stage_02_data_validation import DataValidationTrainingPipeline

""" responsible for running the data ingestion stage of the pipeline, which is responsible for
 preparing the data for training the model."""

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
