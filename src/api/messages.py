import re
import time
import pytz

import pandas as pd

from datetime import datetime

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
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M")
    contatos_df = pd.read_excel("contatos.xlsx")

    for i, mensagem in enumerate(contatos_df["Mensagem"]):
        if current_time not in contatos_df.loc[i, "Horário"].split(","):
            continue

        numero = contatos_df.loc[i, "Número"]
        numero_formatado = re.sub(r"[\D]", "", str(numero))

        nome = contatos_df.loc[i, "Nome"]
        if nome:
            texto = parse.quote(f"{nome}, {mensagem}")
        elif nome == "nan":
            texto = parse.quote(mensagem)

        link = f"https://web.whatsapp.com/send?phone=55{numero_formatado}&text={texto}"
        NAVEGADOR.get(link)

        # busca elemento com id side para verificar se pagina está carregcada
        while len(NAVEGADOR.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(10)
        NAVEGADOR.find_element(By.CSS_SELECTOR, "Button[aria-label='Enviar']").click()
        time.sleep(10)