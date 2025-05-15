from datetime import datetime

def register_user(data: dict[int, dict[str, str]], user_id: int) -> None:
    """
    Убеждаемся, что для данного user_id есть запись в словаре data.
    Если отсутствует - создаём пустой словарь для этого пользователя.
    """
    if user_id not in data:
        data[user_id] = {}

def get_today_birthdays(user_data: dict[str, str]) -> list[str]:
    """Вернуть список имен друзей, у которых день рождения сегодня (по дню и месяцу)."""
    today = datetime.now().strftime("%d.%m")  # Текущая дата в формате ДД.MM
    # Отбираем имена, дата которых совпадает с сегодняшним днем и месяцем