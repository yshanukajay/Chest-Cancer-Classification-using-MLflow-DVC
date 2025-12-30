import os
from chestCNN import logger
from chestCNN.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from chestCNN.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chestCNN.pipeline.stage03_model_trainer import ModelTrainingPipeline
from chestCNN.pipeline.stage04_model_evaluation import EvaluationPipeline

# Set MLflow tracking environment variables
os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/YohanJay23/Chest-Cancer-Classification-using-MLflow-DVC.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "YohanJay23"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "12aa8bae310f0795c7c23dcd43e1bb74fec38ea1"

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

    
STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
            