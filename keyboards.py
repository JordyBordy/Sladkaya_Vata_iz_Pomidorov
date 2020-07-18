import telebot

class Keyboards():

    def __init__(self):

        #Клавиатуры общие
        self.main = telebot.types.ReplyKeyboardMarkup(True)
        self.main.row('Привет', 'Как дела?', 'Пока', 'Игры 🎮')

        self.game = telebot.types.ReplyKeyboardMarkup(True)
        self.game.row('Случайное число 🎲', 'Шахтер Игорь', 'soon')
        self.game.row('Назад 🔙')

        #Клавиатуры для Шахтера
        self.miner_menu = telebot.types.ReplyKeyboardMarkup(True)
        self.miner_menu.row('Копать ⛏', 'Улучшения ⬆', 'Баланс 💰')
        self.miner_menu.row('Магазин 🛒', 'Банк 🏦')
        self.miner_menu.row('Инфо ℹ', 'Достижения 🎖')
        self.miner_menu.row('Назад 🔙')

        self.shop_menu = telebot.types.ReplyKeyboardMarkup(True)
        self.shop_menu.row('Еда 🍗', 'Строительные материалы 🧱')
        self.shop_menu.row('Назад 🔙')

        self.bank = telebot.types.ReplyKeyboardMarkup(True)
        self.bank.row('Открыть вклад')
        self.bank.row('Ваш вклад')
        self.bank.row('Назад 🔙')

        self.contribution_menu = telebot.types.ReplyKeyboardMarkup(True)
        self.contribution_menu.row('Внести деньги')
        self.contribution_menu.row('Вывести деньги')
        self.contribution_menu.row('Состояние счета')
        self.contribution_menu.row('Назад 🔙')

        self.make_money = telebot.types.ReplyKeyboardMarkup(True)
        self.make_money.row('1000$', '5000$', '10000$')
        self.make_money.row('Назад 🔙')

        self.withdraw_money = telebot.types.ReplyKeyboardMarkup(True)
        self.withdraw_money.row('1000$', '5000$', '10000$')
        self.withdraw_money.row('Назад 🔙')


        self.food_shop_menu = telebot.types.ReplyKeyboardMarkup(True)
        self.food_shop_menu.row('Хлеб 🥖', 'Борщ 🍲', 'Кортофель с мясом 🥔🍖')
        self.food_shop_menu.row('Назад 🔙') 

        self.upgrade = telebot.types.ReplyKeyboardMarkup(True)
        self.upgrade.row('Шахтер', 'Кирка', 'Транспорт 🚃')
        self.upgrade.row('Назад 🔙')

        #Клавиатуры для кнопки "Кирка"
        self.pickaxes = telebot.types.ReplyKeyboardMarkup(True)
        self.pickaxes.row('Каменная кирка')
        self.pickaxes.row('Железная кирка')
        self.pickaxes.row('Золотая кирка')
        self.pickaxes.row('Алмазная кирка')
        self.pickaxes.row('Назад 🔙')

        #Клавиатуры для кнопки "Шахтер"

        self.upgrade_miner = telebot.types.ReplyKeyboardMarkup(True)
        self.upgrade_miner.row('Каска')
        self.upgrade_miner.row('Жилет')
        self.upgrade_miner.row('Штаны')
        self.upgrade_miner.row('Ботинки')
        self.upgrade_miner.row('Назад 🔙')

        self.helmet = telebot.types.ReplyKeyboardMarkup(True)
        self.helmet.row('Старая каска')
        self.helmet.row('Обычная каска')
        self.helmet.row('Каска с фонарём')
        self.helmet.row('Современная каска')
        self.helmet.row('Назад 🔙')

        self.vest = telebot.types.ReplyKeyboardMarkup(True)
        self.vest.row('Рваная жилетка')
        self.vest.row('Обычная жилетка')
        self.vest.row('Непромокаемая жилетка')
        self.vest.row('Непромокаемая тёплая жилетка')
        self.vest.row('Назад 🔙')

        self.pants = telebot.types.ReplyKeyboardMarkup(True)
        self.pants.row('Летние шорты')
        self.pants.row('Легкие штаны')
        self.pants.row('Непромокаемые штаны')
        self.pants.row('Непромокаемые тёплые штаны')
        self.pants.row('Назад 🔙')

        self.boots = telebot.types.ReplyKeyboardMarkup(True)
        self.boots.row('Тапочки')
        self.boots.row('Старые кроссовки')
        self.boots.row('Дешевые ботинки')
        self.boots.row('Дорогие ботинки')
        self.boots.row('Назад 🔙')

        #Клавиатуры для кнопки "Транспорт"
        self.transport = telebot.types.ReplyKeyboardMarkup(True)
        self.transport.row('Вагонетка первого уровня')
        self.transport.row('Вагонетка второго уровня')
        self.transport.row('Вагонетка третьего уровня')
        self.transport.row('Вагонетка четвёртого уровня')
        self.transport.row('Назад 🔙')


        #Инлайн клавиатуры

        #Инлайн клавиатуры для шахтера

        #1 Кирки
        self.buy_stone_pickaxe = telebot.types.InlineKeyboardMarkup(True)
        self.buy_stone_pickaxe.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'stone'))

        self.buy_iron_pickaxe = telebot.types.InlineKeyboardMarkup(True)
        self.buy_iron_pickaxe.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'iron'))

        self.buy_golden_pickaxe = telebot.types.InlineKeyboardMarkup(True)
        self.buy_golden_pickaxe.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'gold'))

        self.buy_diamond_pickaxe = telebot.types.InlineKeyboardMarkup(True)
        self.buy_diamond_pickaxe.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'diamond'))

        #2 Еда
        self.buy_bread = telebot.types.InlineKeyboardMarkup(True)
        self.buy_bread.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'bread'))

        self.buy_borscht = telebot.types.InlineKeyboardMarkup(True)
        self.buy_borscht.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'borscht'))

        self.buy_potato_with_cutlets = telebot.types.InlineKeyboardMarkup(True)
        self.buy_potato_with_cutlets.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'potato_w_c'))

        #3 Шахтер

        #3.1  Каски для шахтера
        self.buy_old_helmet = telebot.types.InlineKeyboardMarkup(True)
        self.buy_old_helmet.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'old_h'))

        self.buy_common_helmet = telebot.types.InlineKeyboardMarkup(True)
        self.buy_common_helmet.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'common_h'))

        self.buy_helmet_with_lamp = telebot.types.InlineKeyboardMarkup(True)
        self.buy_helmet_with_lamp.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'with_lamp_h'))

        self.buy_modern_helmet = telebot.types.InlineKeyboardMarkup(True)
        self.buy_modern_helmet.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'modern_h'))

        #3.2 Желетки для шахтера
        self.buy_ragged_vest = telebot.types.InlineKeyboardMarkup(True)
        self.buy_ragged_vest.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'ragged_v'))

        self.buy_common_vest = telebot.types.InlineKeyboardMarkup(True)
        self.buy_common_vest.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'common_v'))

        self.buy_waterproof_vest = telebot.types.InlineKeyboardMarkup(True)
        self.buy_waterproof_vest.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'waterproof_v'))

        self.buy_waterproof_warm_vest = telebot.types.InlineKeyboardMarkup(True)
        self.buy_waterproof_warm_vest.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'waterproof_warm_v'))

        #3.3 Штаны для шахтера
        self.buy_summer_shorts = telebot.types.InlineKeyboardMarkup(True)
        self.buy_summer_shorts.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'summer_s'))

        self.buy_lightweight_pants = telebot.types.InlineKeyboardMarkup(True)
        self.buy_lightweight_pants.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'lightweight_p'))

        self.buy_waterproof_pants = telebot.types.InlineKeyboardMarkup(True)
        self.buy_waterproof_pants.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'waterproof_p'))
        
        self.buy_waterproof_warm_pants = telebot.types.InlineKeyboardMarkup(True)
        self.buy_waterproof_warm_pants.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'waterproof_warm_p'))

        #3.4 Ботинки для шахтера
        self.buy_slippers = telebot.types.InlineKeyboardMarkup(True)
        self.buy_slippers.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'slippers'))

        self.buy_sneakers = telebot.types.InlineKeyboardMarkup(True)
        self.buy_sneakers.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'sneakers'))

        self.buy_cheap_shoes = telebot.types.InlineKeyboardMarkup(True)
        self.buy_cheap_shoes.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'cheap_s'))

        self.buy_expensive_shoes = telebot.types.InlineKeyboardMarkup(True)
        self.buy_expensive_shoes.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'expensive_s'))

        #Инлайн клавиатуры для банка
        self.contribution = telebot.types.InlineKeyboardMarkup(True)
        self.contribution.add(telebot.types.InlineKeyboardButton(text = 'Открыть вклад', callback_data = 'contribution'))

        #Транспорт
        self.trolley_lvl1 = telebot.types.InlineKeyboardMarkup(True)
        self.trolley_lvl1.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'trolley_lvl1'))

        self.trolley_lvl2 = telebot.types.InlineKeyboardMarkup(True)
        self.trolley_lvl2.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'trolley_lvl2'))

        self.trolley_lvl3 = telebot.types.InlineKeyboardMarkup(True)
        self.trolley_lvl3.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'trolley_lvl3'))

        self.trolley_lvl4 = telebot.types.InlineKeyboardMarkup(True)
        self.trolley_lvl4.add(telebot.types.InlineKeyboardButton(text = 'Купить', callback_data = 'trolley_lvl4'))