#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="lilacflower88",
    password="tahminochka88",
    like_per_day=1000,
    comments_per_day=0,
    tag_list=[ 'starbucks', 'starbuckslife', 'coffeelike', 'marriott', 'cafemumu', 'юникредитбанк', 'росевробанк',
    'swissotel', 'уралсиб', 'корпаратив', 'keramamarazzi', 'праймкафе', 'torrogrill','втб', 'нлмк', 'цветымосква',
    'доставкацветовмосква', 'цветысдоставкоймосква', 'цветылюбимой', 'sendflowersmoscow','цветы', 'букет',
    'букетсдоставкой', 'доставкацветов', 'доставкабукетов', 'цветывкоробке','доставка', 'букетлюбимой',
    'цветыкруглрсуточно','moscowflowers', 'доставкацветов','цветыкруглосуточно', 'подарок', 'оформление',
    'мода', 'топлес', 'футбол', 'чм2018', 'рэп', 'lilacflowers', 'lilacflowersmoscow','авто', 'love', 'selfie',
    'photooftheday', 'followme', 'smile', 'follow4follow', 'fashion', 'like4like', 'instagood', 'amazing',
    'friends', 'happy', 'beautiful', 'я', 'любовь', 'россия', 'москва', 'лайки', 'природа', 'девушки', 'улыбка',
    'жизньпрекрасна', 'друзья', 'селфи', 'ночь', 'модели', 'супер', 'красота', 'дружба', 'party', 'hot', 'fitness', 
    'lol', 'style', 'funny', 'girls', 'pretty', 'my', 'cool', 'life', 'облака', 'успех', 'инстамамс', 'инстамама',
    'инстадети', 'город', 'нравится', 'фотография', 'любовьморковь', 'счастье', 'вид', 'model', 'awesome', 'home',
    'beauty', 'harrystyles', 'makeup', 'да', 'классно', 'праздник', 'доброеутро', 'деньги', 'сила', 'настроение',
    'отдыхаем', 'хорошо', 'конкурс', 'утро', 'сон', 'дорога', 'гуляем', 'солнце', 'любимые', 'любимая', 'отзывы',
    'люди', 'напишите', 'коментариев', 'парни', 'music', 'funtime', 'goodtimes', 'cute', 'celebrations', 'fun',
    'веселимся', 'отдыхатьнеработать', 'отмечаем', 'гуляем', 'отдыхаемхорошо', 'отрыв', 'гуляемдоутра', 'праздники',
    'веселаякомпания', 'гуляйпокамолодой', 'веселобыло', 'отметили', 'веселье', 'отрываемся', 'веселушки', 'радость',
    'веселуха', 'свадьба', 'женихиневеста', 'деньрождения', 'мойдень', 'travel', 'trip', 'tourism', 'vacation',
    'visiting', 'travels', 'tourist', 'отпускэтохорошо', 'улетаю', 'каникулы', 'заграница', 'вокругсвета', 'турист',
    'путешествие', 'круиз', 'путешествуй', 'отдых', 'food', 'foodlove', 'foodphotography', 'yum', 'foodlover',
    'вкуснотища', 'кофетайм', 'горячийчай', 'look', 'outfit', 'модавмоскве', 'стильнаяодежда', 'модаиталии',
    'стильномодно', 'gym', 'healthy', 'спорт', 'тренировка', 'здоровье', 'фитнесмотивация', 'фитнес', 'officemate',
    'office', 'workflow', 'businessman', 'workout', 'универ', 'вышка', 'работаработа', 'банк', 'биткоин',
 ],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=1000,
    follow_time=1 * 60,
    unfollow_per_day=500,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["Лучшие цветы Москвы по низким ценам",],
                  ["Доставка цветов по Москве и МО"],
                  ["Скидка 10% при заказе через W/A"],
                  ["+79968888022 м.Повелецкая"],
                  [".", "!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
    ],
    unfollow_whitelist=[])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
