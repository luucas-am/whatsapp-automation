import time
import re

import pandas as pd

from fastapi import APIRouter
from urllib import parse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.constants import NAVEGADOR

messages_router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@messages_router.post("/send", status_code=200, responses={200: {"description": "Mensagens enviadas com sucesso!"}})
def send_messages():
    contatos_df = pd.read_excel("contatos.xlsx")

    for i, mensagem in enumerate(contatos_df["Mensagem"]):
        numero = contatos_df.loc[i, "Número"]
        numero_formatado = re.sub(r"[\D]", "", numero)
        texto = parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={numero_formatado}&text={texto}"
        NAVEGADOR.get(link)

        # busca elemento com id side para verificar se pagina está carregcada
        while len(NAVEGADOR.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)
        NAVEGADOR.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
        time.sleep(10)