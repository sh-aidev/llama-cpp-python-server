from pydantic import BaseModel

class LoggerModel(BaseModel):
    environment: str


class ServerModel(BaseModel):
    host: str
    port: int


class LLMModel(BaseModel):
    name: str
    n_ctx: int
    n_threads: int

class S3Model(BaseModel):
    bucket: str
    root_path: str

class EmbedModel(BaseModel):
    name: str

class LlamaCppModel(BaseModel):
    logger: LoggerModel
    server: ServerModel
    llm: LLMModel
    s3: S3Model
    embed: EmbedModel
