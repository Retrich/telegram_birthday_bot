from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_friends_keyboard(names: list[str], action: str):
   builder = InlineKeyboardBuilder()
   for name in names:
