import time

from selenium.webdriver.common.by import By
from fastapi.concurrency import asynccontextmanager

from src.constants import NAVEGADOR

@asynccontextmanager
async def create_connection():
    try:
        # É necessário logar em uma conta ao passar por esse processo
        NAVEGADOR.get("https://web.whatsapp.com/")

        # busca elemento com id side para verificar se login já foi efetuado
        while len(NAVEGADOR.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)
        yield
    except Exception as e:
        raise e