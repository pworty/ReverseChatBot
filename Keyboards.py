from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# Keyboards
menu_keyboard = [['/createchat', '/presets'],
                 ['/settings']]

createchat_keyboard = [['Time', 'Battery', 'Background'],
                       ['Name', 'Last online', 'Profile pic'],
                       ['Add message', 'Remove message'],
                       ['Generate']]

keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['', '0', '']]

time_keyboard = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9'],
                 [':', '0', ':']]

last_seen_keyboard = [[InlineKeyboardButton('Online')],
                      [InlineKeyboardButton('Last seen recently')],
                      [InlineKeyboardButton('Last seen M minutes ago')],
                      [InlineKeyboardButton('Last seen H hours ago')],
                      [InlineKeyboardButton('Last seen yesterday at hh:mm')],
                      [InlineKeyboardButton('Last seen dd.mm.yy')],
                      [InlineKeyboardButton('Last seen a long time ago')]]

# Keyboard markups
menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=False)
createchat_markup = ReplyKeyboardMarkup(createchat_keyboard, one_time_keyboard=True)
keypad_markup = ReplyKeyboardMarkup(keypad, one_time_keyboard=False)
time_markup = ReplyKeyboardMarkup(time_keyboard, one_time_keyboard=False)
last_seen_markup = InlineKeyboardMarkup.from_button(
    InlineKeyboardButton('Last seen a long time ago'))
