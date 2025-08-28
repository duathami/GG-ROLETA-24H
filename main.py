import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN', '8316806934:AAHWD94_BKRo25x7Ong5jE4-AaQDN8eC4JM')

def start(update: Update, context: CallbackContext):
    keyboard = [['🎰 Sinal GG', '📊 Estatísticas'], ['🔍 Análise GG', 'ℹ️ Info GG']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    update.message.reply_text(
        '👋 Bem-vindo ao GG ROLETA 24H!\n\n'
        '💎 Sinais Premium 24/7\n'
        '✅ Use os botões abaixo:',
        reply_markup=reply_markup
    )

def sinal_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        '🔔 GG ROLETA - SINAL CONFIRMADO!\n\n'
        '🎮 Jogo: Roleta Brasileira\n'
        '🎯 ENTRADA: 🔴 Vermelho\n'
        '💰 RETORNO: 5x\n\n'
        '🔗 https://abrir.link/jPgNp\n\n'
        '⚠️ Jogue com Responsabilidade.'
    )

def estatisticas_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        '📊 GG ROLETA - ESTATÍSTICAS\n\n'
        '✅ Vitórias: 184\n'
        '❌ Derrotas: 9\n'
        '🎯 Taxa: 95.3%\n\n'
        '🔗 https://abrir.link/jPgNp'
    )

def analise_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        '🔍 GG ROLETA - ANÁLISE\n\n'
        '📈 Mercado favorável\n'
        '🎯 Recomendação: Entradas\n\n'
        '🔗 https://abrir.link/jPgNp'
    )

def info_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        'ℹ️ GG ROLETA 24H - OFICIAL\n\n'
        '🏆 Vantagens:\n'
        '• Sinais 24/7\n'
        '• 95.3% de acerto\n\n'
        '🔗 https://abrir.link/jPgNp\n\n'
        '⚠️ Jogue com Responsabilidade.'
    )

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == '🎰 Sinal GG':
        sinal_command(update, context)
    elif text == '📊 Estatísticas':
        estatisticas_command(update, context)
    elif text == '🔍 Análise GG':
        analise_command(update, context)
    elif text == 'ℹ️ Info GG':
        info_command(update, context)

def main():
    try:
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("sinal", sinal_command))
        dp.add_handler(CommandHandler("estatisticas", estatisticas_command))
        dp.add_handler(CommandHandler("analise", analise_command))
        dp.add_handler(CommandHandler("info", info_command))
        dp.add_handler(CommandHandler("gg", sinal_command))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        
        print("💎 GG Roleta 24H - ONLINE!")
        print("🔗 https://abrir.link/jPgNp")
        print("🤖 Aguardando comandos...")
        
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"Erro: {e}")

if __name__ == '__main__':
    main()
