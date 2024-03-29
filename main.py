import telebot
from telebot import types

TOKEN = 'Введите ваш токен'  # Замените на ваш токен
ADMIN_CHAT_ID = id чата  # ID чата администратора

bot = telebot.TeleBot(TOKEN)

user_data = {}
call_requests = {}  # Словарь для хранения статусов вызовов

