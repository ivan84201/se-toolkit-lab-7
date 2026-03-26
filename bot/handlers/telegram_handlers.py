from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.test_handlers.test_handlers import handle_command
from LLM_backend.router import route_intent

def build_keyboard():
    keyboard = [
        [InlineKeyboardButton("List labs", callback_data="/items")],
        [InlineKeyboardButton("Top learners", callback_data="/get_top_learners")],
        [InlineKeyboardButton("Trigger sync", callback_data="/trigger_sync")],
    ]
    return InlineKeyboardMarkup(keyboard)

async def button_callback(update, context):
    query = update.callback_query
    command = query.data
    response = handle_command(command)
    await query.answer()
    await query.edit_message_text(text=response, reply_markup=build_keyboard())

async def message_handler(update, context):
    text = update.message.text
    if text.startswith("/"):
        response = handle_command(text)
    else:
        response = route_intent(text)
    await update.message.reply_text(text=response, reply_markup=build_keyboard())