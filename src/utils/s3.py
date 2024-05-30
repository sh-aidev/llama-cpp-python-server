import boto3
import os
from src.utils.logger import logger


def download_from_s3(
        model_name: str = "mistral-7b-openorca.Q6_K.gguf",
        bucket_name: str = "machanirobotics-models", 
        src_file_path: str = "llm/gguf"
        ) -> str:
    """
    Downloads a file from an S3 bucket to the local machine. The file is saved in the .cache/llm/gguf directory.

    Args:
        bucket_name (str): The name of the S3 bucket where the file is stored.
        src_file_path (str): The path to the file in the S3 bucket.
    """
    
    cache_path = ".cache/llm/gguf"
    os.makedirs(cache_path, exist_ok=True) # create the .cache directory if it does not exist
    logger.debug(f"Created directory {cache_path}")

    output_path = os.path.join(cache_path, model_name) # create the output path
    logger.debug(f"Output path: {output_path}")

    if os.path.exists(output_path): # check if the file already exists
        logger.info(f"File {output_path} already exists")
        return output_path
    try:
        s3 = boto3.client('s3') # create an S3 client
        logger.debug("Created an S3 client")
    except:
        logger.error("Failed to create an S3 client")
        return

    src_file = os.path.join(src_file_path, model_name) # create the source file path
    try:
        s3.head_object(Bucket=bucket_name, Key=src_file) # check if the file exists in S3
        logger.debug(f"File {src_file} exists in S3 bucket {bucket_name}")
    except:
        logger.error(f"File {src_file_path} does not exist in S3 bucket {bucket_name}")
        return
    
    s3.download_file(bucket_name, src_file, output_path)    # download the file from S3
    logger.info(f"Downloaded file from S3 bucket {bucket_name} to {output_path}")
    
    return output_path
