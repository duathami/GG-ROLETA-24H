import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, Filters
from sinais_gg import gg_bot

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token direto para hospedagem
TOKEN = os.getenv('TELEGRAM_TOKEN', '8316806934:AAHWD94_BKRo25x7Ong5jE4-AaQDN8eC4JM')

# Teclado estilo GG Roleta
teclado_gg = ReplyKeyboardMarkup(
    [['🎰 Sinal GG', '📊 Estatísticas'], ['🔍 Análise GG', 'ℹ️ Info GG']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"👋 <b>Bem-vindo ao GG ROLETA 24H!</b>\n\n"
        "💎 <b>Sinais Premium 24/7</b>\n"
        "✅ <b>Taxa de Acerto: 95.3%</b>\n"
        "🔥 <b>Sequência: 35 Vitórias</b>\n\n"
        "🎯 <b>Use os botões abaixo:</b>",
        reply_markup=teclado_gg
    )

async def sinal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sinal = gg_bot.gerar_sinal_gg()
    await update.message.reply_text(sinal, parse_mode='HTML')

async def analise_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    analise = gg_bot.gerar_analise_gg()
    await update.message.reply_text(analise, parse_mode='HTML')

async def estatisticas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = gg_bot.gerar_estatisticas_gg()
    await update.message.reply_text(stats, parse_mode='HTML')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
ℹ️ <b>GG ROLETA 24H - OFICIAL</b>

🏆 <b>Vantagens:</b>
• Sinais 24/7
• 95.3% de acerto
• Suporte especializado

🔗 <b>Cadastre-se:</b>
https://abrir.link/jPgNp

⚠️ Jogue com Responsabilidade. 18+
"""
    await update.message.reply_html(info_text)

def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == '🎰 Sinal GG':
        return sinal_command(update, context)
    elif text == '📊 Estatísticas':
        return estatisticas_command(update, context)
    elif text == '🔍 Análise GG':
        return analise_command(update, context)
    elif text == 'ℹ️ Info GG':
        return info_command(update, context)

def main():
    try:
        # Usando Updater para versão 13.15
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # Handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("sinal", sinal_command))
        dispatcher.add_handler(CommandHandler("analise", analise_command))
        dispatcher.add_handler(CommandHandler("estatisticas", estatisticas_command))
        dispatcher.add_handler(CommandHandler("info", info_command))
        dispatcher.add_handler(CommandHandler("gg", sinal_command))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        
        print("💎 GG Roleta 24H - ONLINE!")
        print("🌐 Bot hospedado na nuvem")
        print("🔗 https://abrir.link/jPgNp")
        print("🤖 Aguardando comandos...")
        
        # Iniciar bot
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"Erro: {e}")

if __name__ == "__main__":
    main()
