import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token
TOKEN = os.getenv('TELEGRAM_TOKEN', '8316806934:AAHWD94_BKRo25x7Ong5jE4-AaQDN8eC4JM')

# Teclado
teclado_gg = ReplyKeyboardMarkup(
    [['🎰 Sinal GG', '📊 Estatísticas'], ['🔍 Análise GG', 'ℹ️ Info GG']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bem-vindo ao GG ROLETA 24H!\n\n"
        "💎 Sinais Premium 24/7\n"
        "✅ Use os botões abaixo:",
        reply_markup=teclado_gg
    )

async def sinal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔔 GG ROLETA - SINAL CONFIRMADO!\n\n"
        "🎮 Jogo: Roleta Brasileira\n"
        "🎯 ENTRADA: 🔴 Vermelho\n"
        "💰 RETORNO: 5x\n\n"
        "🔗 https://abrir.link/jPgNp\n\n"
        "⚠️ Jogue com Responsabilidade."
    )

async def estatisticas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 GG ROLETA - ESTATÍSTICAS\n\n"
        "✅ Vitórias: 184\n"
        "❌ Derrotas: 9\n"
        "🎯 Taxa: 95.3%\n\n"
        "🔗 https://abrir.link/jPgNp"
    )

async def analise_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 GG ROLETA - ANÁLISE\n\n"
        "📈 Mercado favorável\n"
        "🎯 Recomendação: Entradas\n\n"
        "🔗 https://abrir.link/jPgNp"
    )

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ GG ROLETA 24H - OFICIAL\n\n"
        "🏆 Vantagens:\n"
        "• Sinais 24/7\n"
        "• 95.3% de acerto\n\n"
        "🔗 https://abrir.link/jPgNp\n\n"
        "⚠️ Jogue com Responsabilidade."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == '🎰 Sinal GG':
        await sinal_command(update, context)
    elif text == '📊 Estatísticas':
        await estatisticas_command(update, context)
    elif text == '🔍 Análise GG':
        await analise_command(update, context)
    elif text == 'ℹ️ Info GG':
        await info_command(update, context)

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("sinal", sinal_command))
        application.add_handler(CommandHandler("estatisticas", estatisticas_command))
        application.add_handler(CommandHandler("analise", analise_command))
        application.add_handler(CommandHandler("info", info_command))
        application.add_handler(CommandHandler("gg", sinal_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("💎 GG Roleta 24H - ONLINE!")
        application.run_polling()
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
