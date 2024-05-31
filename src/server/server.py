import time
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
from threading import Thread
from typing import AsyncGenerator, Optional, Annotated, Union, List
import uvicorn
import asyncio
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware

from src.utils.configs import LLMConfig
from src.utils.logger import logger
from src.core.llm_core import LlamaCpp
from src.core.llm_openai import LLMOpenAI, EmbedOpenAI
from src.core.llm_multimodal import LlamaCppMultimodal
from src.core.llm_embed import LLMEmbed
from src.utils.openai_protocol import (ChatCompletionRequest, ChatCompletionResponse, random_uuid, EmbeddingRequest, CreateEmbeddingResponse)

def get_router(cfg: LLMConfig) -> APIRouter:
    v1Router = APIRouter()
    @v1Router.post("/v1/chat/completions")
    async def create_chat_completion(
        request: ChatCompletionRequest
        ) -> StreamingResponse:
        """
        Create a chat completion response for the given request. This is a streaming endpoint that will send the response in chunks.

        Args:
            request (Request): Request object

        Returns:
            StreamingResponse: Streaming response object
        """

        cfg.llm_config.llm.name = request.model
        cfg.llm_config.llm.multimodal = True if "llava" in request.model else False
        if "gpt" in request.model:
            openai_llm = LLMOpenAI(cfg)
            logger.debug(f"Request Messages: {request.messages}")

            generation_kwargs = dict(
                model_name = request.model, messages = request.messages, max_tokens = request.max_tokens
            )
            response = await asyncio.to_thread(openai_llm.predict, **generation_kwargs)
        else:

            llm = LlamaCppMultimodal(cfg) if cfg.llm_config.llm.multimodal else LlamaCpp(cfg)

            generation_kwargs = dict(
                messages = request.messages, 
                grammar_txt = request.grammar, 
                max_tokens = request.max_tokens
            )

            response = await asyncio.to_thread(llm.predict, **generation_kwargs)

        return response


    @v1Router.post("/v1/embeddings")
    async def get_embeddings(request: EmbeddingRequest) -> CreateEmbeddingResponse:
        """
        Get embeddings for the given text

        Args:
            request (EmbeddingRequest): Request object

        Returns:
            CreateEmbeddingResponse: Embedding response object
        """
        cfg.llm_config.embed.name = request.model
        if "ada-002" in request.model:
            embed = EmbedOpenAI()
            embeddings = await asyncio.to_thread(embed.encode, request.text, request.model)
        else:
            embed = LLMEmbed(cfg)
            embeddings = await asyncio.to_thread(embed.encode, request.text)
        
        logger.debug(f"Embedding Response: {embeddings}")
        return embeddings

    @v1Router.get("/health")
    def health():
        return {"message": "ok"}
    
    return v1Router

class APIServer:
    def __init__(self, config: LLMConfig) -> None:
        """
        Initialize the API server with the given configuration

        Args:
            config (Config): Configuration object
        """
        logger.debug("Initializing API server")
        self.port = config.llm_config.server.port       # Port to run the server on
        self.host = config.llm_config.server.host       # Host to run the server on

        self.app = FastAPI()
        logger.debug("FastAPI app initialized")
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins = ["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            
        )
        logger.debug("CORS middleware enabled")

        router = get_router(config)
        logger.debug("Router initialized")

        self.app.include_router(router)
        logger.debug("Router included in the app")
    
    def serve(self):
        logger.debug(f"Server running on {self.host}:{self.port}")
        uvicorn.run(self.app, port=self.port, host=self.host)