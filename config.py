import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

# LINK OFICIAL GG ROLETA 24H
LINK_CADASTRO = "https://abrir.link/jPgNp"

TEXTO_CADASTRO = f"""
🔗 <b>Registre-se clicando aqui:</b>
(<a href="{LINK_CADASTRO}">https://abrir.link/jPgNp</a>)

⚠️ Jogue com Responsabilidade. Somente para Maiores de 18 Anos.
"""