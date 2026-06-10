import httpx
import logging

logger = logging.getLogger("DiscordSwarmBot")

# URL вебхука вашего канала Discord (заберите из настроек канала в Discord)
DISCORD_WEBHOOK_URL = "https://discord.com"

async def send_payment_notification(payment_id: str, amount: float, uid: str):
    """
    Отправляет мгновенное форматированное уведомление в Discord-канал 
    о прохождении платежа в экосистеме.
    """
    if not DISCORD_WEBHOOK_URL or "YOUR_WEBHOOK" in DISCORD_WEBHOOK_URL:
        logger.warning("Discord Webhook URL не настроен. Пропуск отправки.")
        return

    # Формируем красивую карточку (Embed) для канала
    payload = {
        "username": "Единый Квантовый Оркестратор",
        "avatar_url": "https://imgur.com",  # Можете заменить на свой логотип
        "embeds": [
            {
                "title": "🟢 Успешная транзакция Pi Network",
                "color": 3066993,  # Зеленый цвет полосы
                "fields": [
                    {"name": "ID Пользователя (UID)", "value": f"`{uid}`", "inline": True},
                    {"name": "Сумма платежа", "value": f"**{amount} PI**", "inline": True},
                    {"name": "Идентификатор транзакции", "value": f"`{payment_id}`", "inline": False}
                ],
                "footer": {
                    "text": "Fractal Lego Builder | Мониторинг систем"
                }
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5.0)
            if response.status_code == 204:
                logger.info(f"Уведомление о платеже {payment_id} успешно отправлено в Discord.")
            else:
                logger.error(f"Сбой отправки в Discord: {response.status_code} - {response.text}")
        except httpx.RequestError as exc:
            logger.error(f"Сетевая ошибка при отправке вебхука в Discord: {exc}")
