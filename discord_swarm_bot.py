name: Refactor SwarmBot integration

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build_and_run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Network Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install httpx

      - name: Run SwarmBot Core Process
        env:
          XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: |
          echo "🚀 Квантовый оркестратор активирован. Запуск ядра..."
          python discord_swarm_bot.py
