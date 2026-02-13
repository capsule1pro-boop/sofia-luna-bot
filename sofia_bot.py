import telebot

# Pon tu token aquí (el que te dio BotFather)
TOKEN = "7988446868:AAE0UAKYwOnLGERCcnXHMdMgNWNoOlhXPPM" 

bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "¡Hola papi! 😏 Bienvenido al mundo de Sofia Luna 🔥\nSoy tu bot personal para paquetes, customs y acceso VIP.\n\nUsa estos comandos:\n/paquetes - Ver precios\n/comprar - Cómo pagar\n/vip - Acceso VIP\n/custom - Pedir algo personalizado\n/help - Ayuda")

# Comando /paquetes
@bot.message_handler(commands=['paquetes'])
def paquetes(message):
    bot.reply_to(message, """
Paquetes disponibles:
1. Tease Starter: 5 fotos + 1 video corto (15 seg) - $150 MXN
2. Full Spicy: 10 fotos + 2 videos largos (30-60 seg) - $300 MXN
3. Mega Bundle: 20 fotos + 4 videos + 1 custom corto - $500 MXN
Customs personalizados: $400–$800 MXN (según duración y explícito)

Para comprar escribe /comprar 😈
""")

# Comando /comprar
@bot.message_handler(commands=['comprar'])
def comprar(message):
    bot.reply_to(message, """
Para comprar:
1. Elige paquete (ej. Full Spicy $300)
2. Paga por:
   - SPEI / Transferencia: [tu cuenta bancaria o Mercado Pago aquí]
   - Stripe: [tu link Stripe Checkout aquí]
3. Envía comprobante aquí mismo (foto o captura)
Te doy acceso VIP inmediato o te mando el paquete por DM 💦

¿Cuál quieres? 😏
""")

# Comando /vip
@bot.message_handler(commands=['vip'])
def vip(message):
    bot.reply_to(message, "Verificando pago... Si ya pagaste, envía comprobante y te invito al canal VIP @SofiaLunaVIP 🔥\nSi no has pagado, usa /comprar primero.")

# Comando /custom
@bot.message_handler(commands=['custom'])
def custom(message):
    bot.reply_to(message, "¡Customs son mi especialidad! 😈\nDime qué quieres: escena (ducha, cama, playa, etc.), duración, nivel spicy, ropa o sin ropa...\nTe cotizo en 1 minuto 💦")

# Comando /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Comandos disponibles:\n/start - Bienvenida\n/paquetes - Lista de paquetes\n/comprar - Cómo pagar\n/vip - Acceso VIP\n/custom - Pedir personalizado\n/help - Este mensaje")

# Maneja cualquier mensaje que no sea comando (para que responda algo)
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "¡Hola! Usa /paquetes para ver opciones o /custom para algo personalizado 😏 Si necesitas ayuda escribe /help")

print("Bot iniciado...")


bot.polling()

