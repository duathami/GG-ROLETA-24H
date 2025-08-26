import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
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
        
        # Handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("sinal", sinal_command))
        application.add_handler(CommandHandler("analise", analise_command))
        application.add_handler(CommandHandler("estatisticas", estatisticas_command))
        application.add_handler(CommandHandler("info", info_command))
        application.add_handler(CommandHandler("gg", sinal_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("💎 GG Roleta 24H - ONLINE!")
        print("🌐 Bot hospedado na nuvem")
        print("🔗 https://abrir.link/jPgNp")
        print("🤖 Aguardando comandos...")
        
        # Configuração para hospedagem
        port = int(os.environ.get('PORT', 5000))
        application.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=f"https://seu-app.render.com/{TOKEN}"
        )
        
    except Exception as e:
        logger.error(f"Erro: {e}")
        # Fallback para polling
        application.run_polling()

if __name__ == "__main__":
    main()