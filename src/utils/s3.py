import boto3
import os
from src.utils.logger import logger
from src.utils.configs import LLMConfig

def download_from_s3(
        cfg: LLMConfig,
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

    if cfg.llm_config.llm.multimodal:
        model_name = cfg.llm_config.llm.name + "-" + cfg.llm_config.llm.quantization + ".gguf"
        clip_model_name = cfg.llm_config.llm.name + "-mmproj-f16.gguf"

    output_path = os.path.join(cache_path, cfg.llm_config.llm.name) if not cfg.llm_config.llm.multimodal else os.path.join(cache_path, model_name) # create the output file path
    if cfg.llm_config.llm.multimodal:
        clip_output_path = os.path.join(cache_path, clip_model_name)
    logger.debug(f"Output path: {output_path}")

    if os.path.exists(output_path): # check if the file already exists
        logger.info(f"File {output_path} already exists")
        return (output_path, clip_output_path) if cfg.llm_config.llm.multimodal else output_path
    try:
        s3 = boto3.client('s3') # create an S3 client
        logger.debug("Created an S3 client")
    except:
        logger.error("Failed to create an S3 client")
        return

    src_file = os.path.join(cfg.llm_config.s3.root_path, cfg.llm_config.llm.name) if not cfg.llm_config.llm.multimodal else os.path.join(cfg.llm_config.s3.root_path, model_name) # create the source file path
    if cfg.llm_config.llm.multimodal:
        clip_src_file = os.path.join(cfg.llm_config.s3.root_path, clip_model_name)
    try:
        s3.head_object(Bucket=cfg.llm_config.s3.bucket, Key=src_file) # check if the file exists in the S3 bucket
        logger.debug(f"File {src_file} exists in S3 bucket {cfg.llm_config.s3.bucket}")
    except:
        logger.error(f"File {src_file} does not exist in S3 bucket {cfg.llm_config.s3.bucket}")
        return
    
    s3.download_file(cfg.llm_config.s3.bucket, src_file, output_path) # download the file from the S3 bucket
    if cfg.llm_config.llm.multimodal:
        s3.download_file(cfg.llm_config.s3.bucket, clip_src_file, clip_output_path)
    logger.info(f"Downloaded file from S3 bucket {cfg.llm_config.s3.bucket} to {output_path}")
    
    return (output_path, clip_output_path) if cfg.llm_config.llm.multimodal else output_path
