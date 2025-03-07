# 🤖 Telegram Bot for Merchandise Store

## 🔹 Project Description
This project is a Telegram bot for selling corporate merchandise. It allows customers to browse products, place orders, and receive assistance from an AI-powered assistant.

## 🛠️ Technologies
- **Rebus** – Product catalog management
- **OpenAI API** – AI assistant request processing
- **Telegram Bot API** – Interaction with customers
- **Python + python-telegram-bot** – Bot development

## ⚙️ Bot Features
- Product catalog browsing
- Product details and availability clarification
- Order placement assistance
- Answers to questions about payment, delivery, and returns
- Manager notifications about orders

## 🔄 Running the Bot 24/7
### VPS (Server) – Recommended Option
- Uses a cloud server (VPS)
- Install Python, run with `nohup python bot.py &`
- Autostart via `systemd`

### Railway.app / Render.com / Google Cloud Run
- **Railway**: `railway init` → `railway up`
- **Render**: Upload code, start Python service
- **Google Cloud Run**: Deploy using a container

### Local Server / Raspberry Pi
- Running on a home device: `nohup python bot.py &` (device must stay powered on)

### Docker Container
- **Build Image**: `docker build -t bot .`
- **Run**: `docker run -d bot`

  # 🤖 Telegram-бот для интернет-магазина мерча

## 🔹 Описание проекта
Этот проект — Telegram-бот для продажи корпоративного мерча.  
Он позволяет клиентам просматривать товары, оформлять заказы и получать консультацию от ИИ-ассистента.

## 🛠️ Технологии
- **Rebus** — управление каталогом товаров
- **OpenAI API** — обработка запросов к ИИ-ассистенту
- **Telegram Bot API** — взаимодействие с клиентами
- **Python + python-telegram-bot** — разработка бота

## ⚙️ Функционал бота
 Просмотр каталога товаров  
 Уточнение характеристик и доступности  
 Помощь в оформлении заказов  
 Ответы на вопросы об оплате, доставке и возврате  
 Уведомления менеджеров о заказах  

 ##  Варианты запуска бота 24/7
VPS (Сервер) — рекомендуемый вариант

Используется облачный сервер (VPS)
Установка Python, запуск через nohup python bot.py &
Автозапуск через systemd
Railway.app / Render.com / Google Cloud Run

Railway: railway init → railway up
Render: загрузка кода, запуск Python-сервиса
Google Cloud Run: запуск через контейнер
Локальный сервер / Raspberry Pi

Запуск на домашнем устройстве
nohup python bot.py & (нужно оставить устройство включенным)
Docker-контейнер

Сборка образа: docker build -t bot .
Запуск: docker run -d bot
