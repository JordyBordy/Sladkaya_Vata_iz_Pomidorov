# Название бота @JordyBordyTestbot  / Bot Name @JordyBordyTestbot

import telebot
import random
import sys
from random import randint
import pickle
from threading import Timer
import time

from secret import token

from keyboards import Keyboards

from lists import phrases_for_greeting_list, how_are_you_list, goodbye_phrases_list, minerals_list

from setings import CHANCES, NUMBER_OF_CHANCE

from Miner_Igor import Player

try:

    keyboards = Keyboards()

    #Таймер
    def timer():
        global time2
        for i in Users:
            if not(i == '0'):
                if Users[i].stamina < Users[i].stamina_max:
                    Users[i].stamina += 1
                    if Users[i].stamina == Users[i].stamina_max:
                        bot.send_message(int(i), 'Твоя выносливость полностью востановилась', reply_markup = keyboards.main)
                Users[i].income()
                
        file = open('Users.data', 'wb')
        pickle.dump(Users, file)
        file.close()
        time2 = int(time.time())          
        time1 = Timer(60 * 1, timer) 
        time1.start()

    #Загрузка "бд"
    file = open('Users.data', 'rb')
    Users = pickle.load(file)
    file.close()

    time1 = Timer(60 * 1, timer)
    time1.start()
    time2 = int(time.time())

    bot = telebot.TeleBot(token)

    for i in Users:
        if not(i == '0'):
            if not(hasattr(Users[i], 'percent')):
                username = Users[i].username
                balance = Users[i].balance
                pickaxe = Users[i].pickaxe
                stamina = Users[i].stamina
                helmet = Users[i].helmet
                vest = Users[i].vest
                pants = Users[i].pants
                boots = Users[i].boots
                bank_account = Users[i].bank_account
                stamina_max = Users[i].stamina_max
                Users[i] = Player(username)
                Users[i].balance = balance
                Users[i].stamina = stamina
                Users[i].pickaxe = pickaxe
                Users[i].helmet = helmet
                Users[i].vest = vest
                Users[i].pants = pants
                Users[i].boots = boots
                Users[i].bank_account = bank_account
                bot.send_message(int(i), 'Пока тебя не было, были добавлены новые функции.', reply_markup = keyboards.main)

    for i in Users:
        Users[i].recount_stamina_max()

    #Функция запуска команды старт
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Я готов работать', reply_markup = keyboards.main)
        if str(message.chat.id) in Users:
            Users[str(message.chat.id)].current_keyboard ='main'
        else:
            Users[str(message.chat.id)] = Player(message.chat.username)
            print(Users[str(message.chat.id)].username)

    #Обработка команд 
    @bot.message_handler(content_types = ['text'])
    def send_text(message):
        if not(str(message.chat.id) in Users):
            bot.send_message(message.chat.id, 'Напишите "/start"')
        elif message.text.lower() == 'привет':
            bot.send_message(message.chat.id, random.choice(phrases_for_greeting_list))  
        elif message.text.lower() == 'как дела?':
            bot.send_message(message.chat.id, random.choice(how_are_you_list))
        elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, random.choice(goodbye_phrases_list))
        elif message.text == 'Игры 🎮':
            bot.send_message(message.chat.id, 'Давай поиграем', reply_markup = keyboards.game)
            Users[str(message.chat.id)].current_keyboard = 'game' 
        elif message.text == 'Случайное число 🎲':
            bot.send_message(message.chat.id, random.randint(0, 1000))
        elif message.text == 'Шахтер Игорь':
            bot.send_message(message.chat.id, 'Давай поиграем', reply_markup = keyboards.miner_menu)
            Users[str(message.chat.id)].current_keyboard = 'miner_menu'
        elif message.text == 'Копать ⛏':
            res = Users[str(message.chat.id)].mine(NUMBER_OF_CHANCE)
            if res == 0:
                current_time = int(time.time())
                bot.send_message(message.chat.id, f'Вы устали, отдохните.\nЭнергия востановится через {60 - int((current_time - time2))} секунд.')
            elif res == 'creeper':
                creeper_Igor = open('C:\JordyBordy\Всякая херня\Игорь Крипер.png', 'rb')   
                bot.send_photo(message.chat.id, creeper_Igor, caption = f'Вы встретили крипера Игоря!\nВаша выносливость:{Users[str(message.chat.id)].stamina}/{Users[str(message.chat.id)].stamina_max}.')
                creeper_Igor.close()
            else:
                bot.send_message(message.chat.id, res + f'\nВаша выносливость:{Users[str(message.chat.id)].stamina}/{Users[str(message.chat.id)].stamina_max}.')
            file = open('Users.data', 'wb')
            pickle.dump(Users, file)
            file.close()

        #Вывод описания кирок                        
        elif message.text == 'Каменная кирка':
            stone_pickaxe = open('C:\Питон\Bot\Photos\pickaxes\stone_pickaxe.png', 'rb')
            bot.send_photo(message.chat.id, stone_pickaxe, 'Стоимость: 1000$\nУвеличивает шанс выпадения редких руд на 2%', reply_markup = keyboards.buy_stone_pickaxe)
            stone_pickaxe.close()
        elif message.text == 'Железная кирка':
            iron_pickaxe = open('C:\Питон\Bot\Photos\pickaxes\iron_pickaxe.png', 'rb')
            bot.send_photo(message.chat.id, iron_pickaxe, 'Стоимость: 2500$\nУвеличивает шанс выпадения редких руд на 5%', reply_markup = keyboards.buy_iron_pickaxe)
            iron_pickaxe.close()
        elif message.text == 'Золотая кирка':
            golden_pickaxe = open('C:\Питон\Bot\Photos\pickaxes\golden_pickaxe.png', 'rb')
            bot.send_photo(message.chat.id, golden_pickaxe, 'Стоимость: 5000$\nУвеличивает шанс выпадения редких руд на 10%', reply_markup = keyboards.buy_golden_pickaxe)
            golden_pickaxe.close()   
        elif message.text == 'Алмазная кирка':
            diamond_pickaxe = open('C:\Питон\Bot\Photos\pickaxes\diamond_pickaxe.png', 'rb')
            bot.send_photo(message.chat.id, diamond_pickaxe, 'Стоимость: 10000$\nУвеличивает шанс выпадения редких руд на 20%', reply_markup = keyboards.buy_diamond_pickaxe)
            diamond_pickaxe.close()
        elif message.text == 'Хлеб 🥖':
            bread = open('C:\Питон\Bot\Photos/foods/bread.png', 'rb')
            bot.send_photo(message.chat.id, bread, 'Стоимость: 80$\nДобавляет 5 очков выносливости', reply_markup = keyboards.buy_bread)
            bread.close()
        elif message.text == 'Борщ 🍲':
            borscht = open('C:\Питон\Bot\Photos/foods/borscht.png', 'rb')
            bot.send_photo(message.chat.id, borscht, 'Стоимость: 160$\nДобавляет 10 очков выносливости', reply_markup = keyboards.buy_borscht)
            borscht.close()
        elif message.text == 'Кортофель с мясом 🥔🍖':
            potato_with_cutlets = open('C:\Питон\Bot\Photos/foods\potato with cutlets.png', 'rb')
            bot.send_photo(message.chat.id, potato_with_cutlets, 'Стоимость: 320$\nДобавляет 20 очков выносливости', reply_markup = keyboards.buy_potato_with_cutlets)
            potato_with_cutlets.close()

        #1 Одежда для шахтера
        #1.1 Каска    
        elif message.text == 'Старая каска':
            old_helmet = open('C:\Питон\Bot\Photos\miner\helmets\old_helmet.png', 'rb')
            bot.send_photo(message.chat.id, old_helmet, 'Стоимость: 500$,\nДобавляет 5 очков к максимальной выносливости', reply_markup = keyboards.buy_old_helmet)
            old_helmet.close()
        elif message.text == 'Обычная каска':
            common_helmet = open('\Питон\Bot\Photos\miner\helmets\common_helmet.png', 'rb')
            bot.send_photo(message.chat.id, common_helmet, 'Стоимость: 1000$,\nДобавляет 10 очков к максимальной выносливости', reply_markup = keyboards.buy_common_helmet)
            common_helmet.close()
        elif message.text == 'Каска с фонарём':
            helmet_with_lamp = open('\Питон\Bot\Photos\miner\helmets\helmet_with_lamp.png', 'rb')
            bot.send_photo(message.chat.id, helmet_with_lamp, 'Стоимость: 2000$,\nДобавляет 15 очков к максимальной выносливости', reply_markup = keyboards.buy_helmet_with_lamp)
            helmet_with_lamp.close()
        elif message.text == 'Современная каска':
            modern_helmet = open('\Питон\Bot\Photos\miner\helmets\modern_helmet.png', 'rb')
            bot.send_photo(message.chat.id, modern_helmet, 'Стоимость: 4000$,\nДобавляет 20 очков к максимальной выносливости', reply_markup = keyboards.buy_modern_helmet)
            modern_helmet.close()

        #1.2 Жилетка    
        elif message.text == 'Рваная жилетка':
            ragged_vest = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, ragged_vest, 'Стоимость: 500$,\nДобавляет 5 очков к максимальной выносливости', reply_markup = keyboards.buy_ragged_vest)
        elif message.text == 'Обычная жилетка':
            common_vest = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, common_vest, 'Стоимость: 1000$,\nДобавляет 10 очков к максимальной выносливости', reply_markup = keyboards.buy_common_vest)
        elif message.text == 'Непромокаемая жилетка':
            waterproof_vest = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, waterproof_vest, 'Стоимость: 2000$,\nДобавляет 15 очков к максимальной выносливости', reply_markup = keyboards.buy_waterproof_vest)
        elif message.text == 'Непромокаемая тёплая жилетка':
            waterproof_warm_vest = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, waterproof_warm_vest, 'Стоимость: 4000$,\nДобавляет 20 очков к максимальной выносливости', reply_markup = keyboards.buy_waterproof_warm_vest)
        
        #1.3 Штаны 
        elif message.text == 'Летние шорты':
            summer_shorts = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, summer_shorts, 'Стоимость: 500$,\nДобавляет 5 очков к максимальной выносливости', reply_markup = keyboards.buy_summer_shorts)
        elif message.text == 'Легкие штаны':
            lightweight_pants = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, lightweight_pants, 'Стоимость: 1000$,\nДобавляет 10 очков к максимальной выносливости', reply_markup = keyboards.buy_lightweight_pants)
        elif message.text == 'Непромокаемые штаны':
            waterproof_pants = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, waterproof_pants, 'Стоимость: 2000$,\nДобавляет 15 очков к максимальной выносливости', reply_markup = keyboards.buy_waterproof_pants)
        elif message.text == 'Непромокаемые тёплые штаны':
            waterproof_warm_pants = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, waterproof_warm_pants, 'Стоимость: 4000$,\nДобавляет 20 очков к максимальной выносливости', reply_markup = keyboards.buy_waterproof_warm_pants)
        
        #1.4 Ботинки 
        elif message.text == 'Тапочки':
            slippers = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, slippers, 'Стоимость: 500$,\nДобавляет 5 очков к максимальной выносливости', reply_markup = keyboards.buy_slippers)
        elif message.text == 'Старые кроссовки':
            sneakers = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, sneakers, 'Стоимость: 1000$,\nДобавляет 10 очков к максимальной выносливости', reply_markup = keyboards.buy_sneakers)
        elif message.text == 'Дешевые ботинки':
            cheap_shoes = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, cheap_shoes, 'Стоимость: 2000$,\nДобавляет 15 очков к максимальной выносливости', reply_markup = keyboards.buy_cheap_shoes)
        elif message.text == 'Дорогие ботинки':
            expensive_shoes = open('C:\JordyBordy\Всякая херня\Игорь хэд.png', 'rb')
            bot.send_photo(message.chat.id, expensive_shoes, 'Стоимость: 4000$,\nДобавляет 20 очков к максимальной выносливости', reply_markup = keyboards.buy_expensive_shoes)                        
        
        #Вывод описания вкладов в банке
        elif message.text == 'Открыть вклад':
            сontribution = open('C:\Питон\Bot\Photos/bank\money3.png', 'rb')
            bot.send_photo(message.chat.id, сontribution, 'Сумма открытия вклада=1000$\nДоход +0,1% в миннуту от суммы вклада', reply_markup = keyboards.contribution)
            сontribution.close() 
        elif message.text == 'Ваш вклад':
            if Users[str(message.chat.id)].bank_account == 0:
                bot.send_message(message.chat.id, 'У вас ещё не открыт вклад. Перейдите во вкладку "Открыть вклад".')
            else:
                contribution_2 = open('C:\Питон\Bot\Photos/bank\money3.png', 'rb')
                bot.send_photo(message.chat.id, contribution_2, f'Доход +0,1% в миннуту от суммы вклада\nМинимальная сумма вклада=1000$\nДенег на счете: {Users[str(message.chat.id)].bank_account}$' , reply_markup = keyboards.contribution_menu)
                contribution_2.close()           

        elif message.text == 'Баланс 💰':
            bot.send_message(message.chat.id, f'{Users[str(message.chat.id)].balance}$')
        elif message.text == 'Магазин 🛒':
            bot.send_message(message.chat.id, 'Заходи-покупай!', reply_markup = keyboards.shop_menu)
            Users[str(message.chat.id)].current_keyboard = 'shop_menu'

        #Банк    
        elif message.text == 'Банк 🏦':
            bot.send_message(message.chat.id, 'Давай заставим твои деньги работать!', reply_markup = keyboards.bank)
            Users[str(message.chat.id)].current_keyboard = 'bank'
        elif message.text == 'Внести деньги':
            bot.send_message(message.chat.id, 'Внеси деньги', reply_markup = keyboards.make_money)
            Users[str(message.chat.id)].current_keyboard = 'make_money'
        elif message.text == 'Вывести деньги':
            bot.send_message(message.chat.id, 'Выведи деньги', reply_markup = keyboards.withdraw_money)
            Users[str(message.chat.id)].current_keyboard = 'withdraw_money'
        elif message.text == 'Состояние счета':
            bot.send_message(message.chat.id, f'У вас на счете: {Users[str(message.chat.id)].bank_account} $')
        
        #Транспорт
        elif message.text == 'Транспорт 🚃':
            bot.send_message(message.chat.id, 'Давай улучшим твой транспорт', reply_markup = keyboards.transport)
            Users[str(message.chat.id)].current_keyboard = 'transport'
        elif message.text == 'Вагонетка первого уровня':
            trolley_lvl1 = open('C:\Питон\Bot\Photos/transport/trolley_lvl1.png', 'rb')
            bot.send_photo(message.chat.id, trolley_lvl1, 'Стоимость: 1000$\nУвеличивает кол-во выпадаемых ресурсов на 25%', reply_markup = keyboards.trolley_lvl1)
            trolley_lvl1.close()
        elif message.text == 'Вагонетка второго уровня':
            trolley_lvl2 = open('C:\Питон\Bot\Photos/transport/trolley_lvl2.png', 'rb')
            bot.send_photo(message.chat.id, trolley_lvl2, 'Стоимость: 2500$\nУвеличивает кол-во выпадаемых ресурсов на 50%', reply_markup = keyboards.trolley_lvl2)
            trolley_lvl2.close()
        elif message.text == 'Вагонетка третьего уровня':
            trolley_lvl3 = open('C:\Питон\Bot\Photos/transport/trolley_lvl3.png', 'rb')
            bot.send_photo(message.chat.id, trolley_lvl3, 'Стоимость: 5000$\nУвеличивает кол-во выпадаемых ресурсов на 75%', reply_markup = keyboards.trolley_lvl3)
            trolley_lvl3.close()
        elif message.text == 'Вагонетка четвёртого уровня':
            trolley_lvl4 = open('C:\Питон\Bot\Photos/transport/trolley_lvl4.jpg', 'rb')
            bot.send_photo(message.chat.id, trolley_lvl4, 'Стоимость: 10000$\nУвеличивает кол-во выпадаемых ресурсов на 100%', reply_markup = keyboards.trolley_lvl4)                
            trolley_lvl4.close()


        #Ввод и вывод денег со счета    
        elif message.text == '1000$':
            if Users[str(message.chat.id)].current_keyboard == 'make_money':
                if Users[str(message.chat.id)].balance >= 1000:
                   Users[str(message.chat.id)].balance -= 1000
                   Users[str(message.chat.id)].bank_account += 1000
                   bot.send_message(message.chat.id, 'Вы внесли 1000$ в свой вклад')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')

            elif Users[str(message.chat.id)].current_keyboard == 'withdraw_money':
                if Users[str(message.chat.id)].bank_account >= 1000:
                   Users[str(message.chat.id)].bank_account -= 1000
                   Users[str(message.chat.id)].balance += 1000
                   bot.send_message(message.chat.id, 'Вы вывели 1000$ со своего вклада')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')
        elif message.text == '5000$':
            if Users[str(message.chat.id)].current_keyboard == 'make_money':
                if Users[str(message.chat.id)].balance >= 5000:
                   Users[str(message.chat.id)].balance -= 5000
                   Users[str(message.chat.id)].bank_account += 5000
                   bot.send_message(message.chat.id, 'Вы внесли 5000$ в свой вклад')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')

            elif Users[str(message.chat.id)].current_keyboard == 'withdraw_money':
                if Users[str(message.chat.id)].bank_account >= 5000:
                   Users[str(message.chat.id)].bank_account -= 5000
                   Users[str(message.chat.id)].balance += 5000
                   bot.send_message(message.chat.id, 'Вы вывели 50000$ со своего вклада')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')
        elif message.text == '10000$':
            if Users[str(message.chat.id)].current_keyboard == 'make_money':
                if Users[str(message.chat.id)].balance >= 10000:
                   Users[str(message.chat.id)].balance -= 10000
                   Users[str(message.chat.id)].bank_account += 10000
                   bot.send_message(message.chat.id, 'Вы внесли 10000$ в свой вклад')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')

            elif Users[str(message.chat.id)].current_keyboard == 'withdraw_money':
                if Users[str(message.chat.id)].bank_account >= 10000:
                   Users[str(message.chat.id)].bank_account -= 10000
                   Users[str(message.chat.id)].balance += 10000
                   bot.send_message(message.chat.id, 'Вы вывели 10000$ со своего вклада')
                else:
                   bot.send_message(message.chat.id, 'У вас не достаточно средств')                                 


            
        elif message.text == 'Еда 🍗':
            bot.send_message(message.chat.id, 'Давай съедим что-нибудь', reply_markup = keyboards.food_shop_menu)
            Users[str(message.chat.id)].current_keyboard = 'food_shop_menu'        
        elif message.text == 'Инфо ℹ':
            info = Users[str(message.chat.id)].info()
            if info[0] == 'wood':
                wooden_pickaxe = open('Photos\pickaxes\wooden_pickaxe.png', 'rb')
                bot.send_photo(message.chat.id, wooden_pickaxe, caption = info[1])
                wooden_pickaxe.close()
            elif info[0] == 'stone':
                stone_pickaxe = open('Photos\pickaxes\stone_pickaxe.png', 'rb')
                bot.send_photo(message.chat.id, stone_pickaxe, caption = info[1])
                stone_pickaxe.close()
            elif info[0] == 'iron':
                iron_pickaxe = open('Photos\pickaxes\iron_pickaxe.png', 'rb')
                bot.send_photo(message.chat.id, iron_pickaxe, caption = info[1])
                iron_pickaxe.close() 
            elif info[0] == 'gold':
                golden_pickaxe = open('Photos\pickaxes\golden_pickaxe.png', 'rb')
                bot.send_photo(message.chat.id, golden_pickaxe, caption = info[1])
                golden_pickaxe.close()
            elif info[0] == 'diamond':
                diamond_pickaxe = open('Photos\pickaxes\diamond_pickaxe.png', 'rb')
                bot.send_photo(message.chat.id, diamond_pickaxe, caption = info[1])
                diamond_pickaxe.close()               
        elif message.text == 'Улучшения ⬆':
            bot.send_message(message.chat.id, 'Давай что-нибудь улучшим', reply_markup = keyboards.upgrade)
            Users[str(message.chat.id)].current_keyboard = 'upgrade'        
        elif message.text == 'Кирка':
             bot.send_message(message.chat.id, 'Давай улучшим твою кирку', reply_markup = keyboards.pickaxes)
             Users[str(message.chat.id)].current_keyboard = 'pickaxes'
        #Вывод клавиатур "Шахтер"     
        elif message.text == 'Шахтер':
             bot.send_message(message.chat.id, 'Давай улучшим твоего шахтера', reply_markup = keyboards.upgrade_miner)
             Users[str(message.chat.id)].current_keyboard = 'upgrade_miner'
        elif message.text == 'Каска':
            bot.send_message(message.chat.id, 'Давай купим тебе каску', reply_markup = keyboards.helmet)
            Users[str(message.chat.id)].current_keyboard = 'helmet' 
        elif message.text == 'Жилет':
            bot.send_message(message.chat.id, 'Давай купим тебе жилет', reply_markup = keyboards.vest)
            Users[str(message.chat.id)].current_keyboard = 'vest'
        elif message.text == 'Штаны':
            bot.send_message(message.chat.id, 'Давай купим тебе штаны', reply_markup = keyboards.pants)
            Users[str(message.chat.id)].current_keyboard = 'pants'
        elif message.text == 'Ботинки':
            bot.send_message(message.chat.id, 'Давай купим тебе ботинки', reply_markup = keyboards.boots)
            Users[str(message.chat.id)].current_keyboard = 'boots' 

        #Обработка функций "Назад"                
        elif message.text == 'Назад 🔙':
            if Users[str(message.chat.id)].current_keyboard == 'game':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.main)
                Users[str(message.chat.id)].current_keyboard ='main'
            elif Users[str(message.chat.id)].current_keyboard == 'miner_menu':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.game)
                Users[str(message.chat.id)].current_keyboard = 'game'
            elif Users[str(message.chat.id)].current_keyboard == 'upgrade':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.miner_menu)
                Users[str(message.chat.id)].current_keyboard = 'miner_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'pickaxes':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.upgrade)
                Users[str(message.chat.id)].current_keyboard = 'upgrade'
            elif Users[str(message.chat.id)].current_keyboard == 'upgrade_miner':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.upgrade)
                Users[str(message.chat.id)].current_keyboard = 'upgrade'
            elif Users[str(message.chat.id)].current_keyboard == 'shop_menu':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.miner_menu)
                Users[str(message.chat.id)].current_keyboard = 'miner_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'food_shop_menu':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.shop_menu)
                Users[str(message.chat.id)].current_keyboard = 'shop_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'helmet' or Users[str(message.chat.id)].current_keyboard == 'vest' or Users[str(message.chat.id)].current_keyboard == 'pants' or Users[str(message.chat.id)].current_keyboard == 'boots':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.upgrade_miner)
                Users[str(message.chat.id)].current_keyboard = 'upgrade_miner'
            elif Users[str(message.chat.id)].current_keyboard == 'bank':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.miner_menu)
                Users[str(message.chat.id)].current_keyboard = 'miner_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'contribution_menu':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.bank)
                Users[str(message.chat.id)].current_keyboard = 'bank'
            elif Users[str(message.chat.id)].current_keyboard == 'make_money':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.contribution_menu)
                Users[str(message.chat.id)].current_keyboard = 'contribution_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'withdraw_money':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.contribution_menu)
                Users[str(message.chat.id)].current_keyboard = 'contribution_menu'
            elif Users[str(message.chat.id)].current_keyboard == 'transport':
                bot.send_message(message.chat.id, 'Назад 🔙', reply_markup = keyboards.upgrade)
                Users[str(message.chat.id)].current_keyboard = 'upgrade'                                  
        elif message.text == 'soon':
            bot.send_message(message.chat.id, 'В разработке')
        else:
            bot.send_message(message.chat.id, 'Я не знаю, что вам ответить')

    #Функция обработки инлайн клавиатур
    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):

        bot.answer_callback_query(callback_query_id=call.id)
        answer = ''
        if call.data == 'stone':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                answer = 'Вы приобрели каменную кирку'
                Users[str(call.message.chat.id)].change_pickaxe('stone')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'iron':
            if Users[str(call.message.chat.id)].balance >= 2500:
                Users[str(call.message.chat.id)].balance -= 2500
                answer = 'Вы приобрели железную кирку'
                Users[str(call.message.chat.id)].change_pickaxe('iron')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'gold':
            if Users[str(call.message.chat.id)].balance >= 5000:
                Users[str(call.message.chat.id)].balance -= 5000
                answer = 'Вы приобрели золотую кирку'
                Users[str(call.message.chat.id)].change_pickaxe('gold')
            else:
                answer = 'У вас не хватает денег' 
        elif call.data == 'diamond':
            if Users[str(call.message.chat.id)].balance >= 10000:
                Users[str(call.message.chat.id)].balance -= 10000
                answer = 'Вы приобрели алмазную кирку'
                Users[str(call.message.chat.id)].change_pickaxe('diamond')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'bread':
            if Users[str(call.message.chat.id)].balance >= 80:
                Users[str(call.message.chat.id)].balance -= 80
                answer = 'Вы приобрели Хлеб 🥖'
                Users[str(call.message.chat.id)].stamina += 5
            else:
                answer = 'У вас не хватает денег'                       
        elif call.data == 'borscht':
            if Users[str(call.message.chat.id)].balance >= 160:
                Users[str(call.message.chat.id)].balance -= 160
                answer = 'Вы приобрели Борщ 🍲'
                Users[str(call.message.chat.id)].stamina += 10
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'potato_w_c':
            if Users[str(call.message.chat.id)].balance >= 320:
                Users[str(call.message.chat.id)].balance -= 320
                answer = 'Вы приобрели Кортофель с мясом 🥔🍖'
                Users[str(call.message.chat.id)].stamina += 20
            else:
                answer = 'У вас не хватает денег'

        # Улучшения шахтера (одежда)
        elif call.data == 'old_h':
            if Users[str(call.message.chat.id)].balance >= 500:
                Users[str(call.message.chat.id)].balance -= 500
                answer = 'Вы приобрели Старая каска'
                Users[str(call.message.chat.id)].change_helmet('old_helmet')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'common_h':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                answer = 'Вы приобрели Обычная каска'
                Users[str(call.message.chat.id)].change_helmet('common_helmet')
            else:
                answer = 'У вас не хватает денег' 
        elif call.data == 'with_lamp_h':
            if Users[str(call.message.chat.id)].balance >= 2000:
                Users[str(call.message.chat.id)].balance -= 2000
                answer = 'Вы приобрели Каска с фонарём'
                Users[str(call.message.chat.id)].change_helmet('helmet_with_lamp')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'modern_h':
            if Users[str(call.message.chat.id)].balance >= 4000:
                Users[str(call.message.chat.id)].balance -= 4000
                answer = 'Вы приобрели Современная каска'
                Users[str(call.message.chat.id)].change_helmet('modern_helmet')
            else:
                answer = 'У вас не хватает денег'
        
        elif call.data == 'ragged_v':
            if Users[str(call.message.chat.id)].balance >= 500:
                Users[str(call.message.chat.id)].balance -= 500
                answer = 'Вы приобрели Рваная жилетка'
                Users[str(call.message.chat.id)].change_vest('ragged_vest')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'common_v':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                answer = 'Вы приобрели Обычная жилетка'
                Users[str(call.message.chat.id)].change_vest('common_vest')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'waterproof_v':
            if Users[str(call.message.chat.id)].balance >= 2000:
                Users[str(call.message.chat.id)].balance -= 2000
                answer = 'Вы приобрели Непромокаемая жилетка'
                Users[str(call.message.chat.id)].change_vest('waterproof_vest')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'waterproof_warm_v':
            if Users[str(call.message.chat.id)].balance >= 4000:
                Users[str(call.message.chat.id)].balance -= 4000
                answer = 'Вы приобрели Непромокаемая тёплая жилетка'
                Users[str(call.message.chat.id)].change_vest('waterproof_warm_vest')
            else:
                answer = 'У вас не хватает денег'

        elif call.data == 'summer_s':
            if Users[str(call.message.chat.id)].balance >= 500:
                Users[str(call.message.chat.id)].balance -= 500
                answer = 'Вы приобрели Летние шорты'
                Users[str(call.message.chat.id)].change_pants('summer_shorts')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'lightweight_p':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                answer = 'Вы приобрели Легкие штаны'
                Users[str(call.message.chat.id)].change_pants('lightweight_pants')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'waterproof_p':
            if Users[str(call.message.chat.id)].balance >= 2000:
                Users[str(call.message.chat.id)].balance -= 2000
                answer = 'Вы приобрели Непромокаемые штаны'
                Users[str(call.message.chat.id)].change_pants('waterproof_pants')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'waterproof_warm_p':
            if Users[str(call.message.chat.id)].balance >= 4000:
                Users[str(call.message.chat.id)].balance -= 4000
                answer = 'Вы приобрели Непромокаемые тёплые штаны'
                Users[str(call.message.chat.id)].change_pants('waterproof_warm_pants')
            else:
                answer = 'У вас не хватает денег'
                
        elif call.data == 'slippers':
            if Users[str(call.message.chat.id)].balance >= 500:
                Users[str(call.message.chat.id)].balance -= 500
                answer = 'Вы приобрели Тапочки'
                Users[str(call.message.chat.id)].change_boots('slippers')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'sneakers':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                answer = 'Вы приобрели Старые кроссовки'
                Users[str(call.message.chat.id)].change_boots('sneakers')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'cheap_s':
            if Users[str(call.message.chat.id)].balance >= 2000:
                Users[str(call.message.chat.id)].balance -= 2000
                answer = 'Вы приобрели Дешевые ботинки'
                Users[str(call.message.chat.id)].change_boots('cheap_shoes')
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'expensive_s':
            if Users[str(call.message.chat.id)].balance >= 4000:
                Users[str(call.message.chat.id)].balance -= 4000
                answer = 'Вы приобрели Дорогие ботинки'
                Users[str(call.message.chat.id)].change_boots('expensive_shoes')
            else:
                answer = 'У вас не хватает денег'
        
        #Банк
        elif call.data == 'contribution':
            if not(Users[str(call.message.chat.id)].bank_account == 0):
                answer = 'Вклад уже открыт. Чтобы узнать информацию о нём перейдите во вкладку "Ваш вклад"'
            elif Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000
                Users[str(call.message.chat.id)].bank_account += 1000 
                answer = 'Ваш счет открыт'
            else:
                answer = 'У вас не хватает денег'

        #Транспорт
        elif call.data == 'trolley_lvl1':
            if Users[str(call.message.chat.id)].balance >= 1000:
                Users[str(call.message.chat.id)].balance -= 1000 
                answer = 'Вы приобрели вагонетку первого уровня'
                Users[str(call.message.chat.id)].percent = 1.25
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'trolley_lvl2':
            if Users[str(call.message.chat.id)].balance >= 2500:
                Users[str(call.message.chat.id)].balance -= 2500 
                answer = 'Вы приобрели вагонетку второго уровня'
                Users[str(call.message.chat.id)].percent = 1.5
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'trolley_lvl3':
            if Users[str(call.message.chat.id)].balance >= 5000:
                Users[str(call.message.chat.id)].balance -= 5000 
                answer = 'Вы приобрели вагонетку третьего уровня'
                Users[str(call.message.chat.id)].percent = 1.75
            else:
                answer = 'У вас не хватает денег'
        elif call.data == 'trolley_lvl4':
            if Users[str(call.message.chat.id)].balance >= 10000:
                Users[str(call.message.chat.id)].balance -= 10000 
                answer = 'Вы приобрели вагонетку четвёртого уровня'
                Users[str(call.message.chat.id)].percent = 2
            else:
                answer = 'У вас не хватает денег'                        



        bot.send_message(call.message.chat.id, answer) 
                
    bot.infinity_polling(True)     
    time1.cancel()
    exit()

except:
    time1.cancel()
    exit()