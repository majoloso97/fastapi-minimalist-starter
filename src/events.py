import logging
from typing import Callable
from fastapi import FastAPI


def start_handler(app: FastAPI) -> Callable:
    '''Things to do while starting the API server'''
    async def start_app() -> None:
        logging.info('Starting API!')

    return start_app
