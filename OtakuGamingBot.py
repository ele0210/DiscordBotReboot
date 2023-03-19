import discord
from discord.ext import tasks
import datetime
import random
import asyncio

import umamusume
import tenor
# import redisForBot
import quizfromjson
import youtubeapi

TOKEN = os.environ['DISCORD_TOKEN']

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
intents.members = True
intents.typing = False
client = discord.Client(intents=intents)

# redis
# redis_conn = redisForBot.connect()

channel_current = None
message_count = {}
member_list = []
wolf_list = []
sus = []
answer_global = ''
otsupi = 0
youtube_flag = 0
game_start = ''
task_debugcount = 0
# umatask_count = 0
# msgtask_count = 0
count_ready = 0

think_time = 60

# # 起動時に動作する処理
@client.event
async def on_ready():
    global count_ready
    print('ready')
    count_ready += 1
    if count_ready >= 2:
        print('already started')
    else:
        await client.change_presence(activity=discord.Game(name="虚無", type=1))
        print('ready first time')

@client.event
async def on_disconnect():
    # if channel_current != None:
    #     global otsupi
    #     otsupi += 1
    #     if random.randint(0, 50) == 0 and channel_current is not None:
    #         await channel_current.send('じゃあの x' + str(otsupi))
    #         otsupi = 0

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    print('message')
    # サーバー登録
    global channel_current
    global message_count
    global youtube_flag
    channel_current = message.channel
    # メンバー登録
    global member_list
    if len(member_list) == 0:
        for member in channel_current.members:
            if member.bot == False:
                member_list.append(member)
                print(member)
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        # if message.content.startswith('今日はやるか？'):
        #     one = "<:one:729023009536344229>"
        #     two = "<:two:729023009536344229>"
        #     three = "<:three:729023009536344229>"
        #     await message.add_reaction(one)
        #     await message.add_reaction(two)
        #     await message.add_reaction(three)
        return
    # メッセージ数カウント
    author = message.author.nick
    if author in message_count:
        message_count[author] += 1
    else:
        message_count[author] = 1
    # ウマ娘画像送信
    if message.content == '/uma':
        await message.channel.send(umamusume.get_link(random.randint(0, 36)))
    # シャットダウンコマンド
    elif message.content == '/shutdown_bot':
        await client.logout()
    # ガチャ
    elif '/gacha' in message.content:
        await play_gacha(message.author)
    # デバッグ用
    elif message.content == '/task_debugcount':
        await message.channel.send(str(task_debugcount) + '時間まで稼働')
    # デバッグ用
    elif message.content == '/count_ready':
        await message.channel.send(str(count_ready))
    # デバッグ用
    elif message.content == '/member_list':
        for member in member_list:
            await message.channel.send(member.nick + '\n')
    # 人狼（未完成）
    # elif message.content == '/word_wolf':
    #         await word_wolf(message.author)
    # 人狼（未完成）
    # elif '/wolf' in message.content:
    #     global sus
    #     if len(wolf_list) > 0:
    #         for num in range(0, len(wolf_list)):
    #             if str(num) in message.content:
    #                 sus[num] += 1
    # メッセージDBランダム出力
    # elif message.content == '/icopy':
    #     copied_mem = member_list[random.randint(0, len(member_list)-1)]
    #     ran_mess = redis_conn.srandmember(copied_mem.name)
    #     if ran_mess != 'nil':
    #         await message.channel.guild.me.edit(nick=copied_mem.nick)
    #         await message.channel.send(ran_mess)
    # クイズ
    elif message.content == '/quiz':
        await play_quiz()
    # クイズ
    elif message.content.startswith('/a '):
        await answer_quiz(message.content[3:])
    # メッセージDB登録
    # elif random.randint(0, 3) == 0:
    #     result = redis_conn.sadd(message.author.name, message.content)
    # Youtubeから動画を検索して貼る
    elif youtube_flag == 1:
        if len(message.content) > 4 and message.content[0] != ':':
            youtube_search_result = youtubeapi.search_youtubevideo(message.content)
            await message.channel.send(youtube_search_result)
            youtube_flag = 0
    # 草でGIF
    # elif '草' in message.content and random.randint(0, 9) == 0:
    #     await message.channel.send(tenor.get_trending_gif())
    # ごく低確率で過去のメッセージ発信
    # elif random.randint(0, 49) == 0:
    #     copied_mem = member_list[random.randint(0, len(member_list)-1)]
    #     ran_mess = redis_conn.srandmember(copied_mem.name)
    #     if ran_mess != 'nil':
    #         await message.channel.guild.me.edit(nick=copied_mem.nick)
    #         await message.channel.send(ran_mess)

# ボイスチャンネルに誰か一人入ったら通知する(または寝落ちを笑う)
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel and len(after.channel.members) == 1 and channel_current is not None:
            msg = '@everyone ' + member.nick + 'がボイチャ入ったぞはよしろ'
            await channel_current.send(msg)
    if after.afk:
        if len(after.channel.members) == 1 and channel_current is not None:
            msg = member.nick + '寝落ちてて草'
            await channel_current.send(msg)

# 集約タスク
@tasks.loop(hours=1)
async def task_onehour():
    print('task started')
    if channel_current is not None:
        # メンバー更新
        global member_list
        member_list.clear()
        for member in channel_current.members:
            if member.bot == False:
                member_list.append(member)
                print(member)
    global task_debugcount
    task_debugcount += 1
    now_hour = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%H')
    now_weekday = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%A')
    print('get time' + now_hour)
    if channel_current is not None:
        if now_hour == '08' and now_weekday != 'Saturday' and now_weekday != 'Sunday':
            if random.randint(0, 2) == 0:
                await channel_current.send('今日のウマ')
                await channel_current.send(umamusume.get_link(random.randint(0, 36)))
            else:
                limit = len(member_list) - 1
                await channel_current.send('今日のガチャ')
                await play_gacha(member_list[random.randint(0, limit)])
        elif now_hour == '10':
            global youtube_flag
            youtube_flag = 1
        # elif now_hour == '14':
        #     if random.randint(0, 1) == 0:
        #         one = ":one:"
        #         two = ":two:"
        #         three = ":three:"
        #         msg_question = await channel_current.send('今日はやるか？\n\n' + one + '15~16時くらいから\n' + two + '20~21時くらいから\n' + three + 'むり')
        #         await asyncio.sleep(2)
        #         await msg_question.add_reaction(one)
        #         await msg_question.add_reaction(two)
        #         await msg_question.add_reaction(three)
            else:
                await channel_current.send('今日のクイズ')
                await play_quiz()
        elif now_hour == '18' and now_weekday != 'Saturday' and now_weekday != 'Sunday':
            await channel_current.send('おつぴ')
        elif now_hour == '19':
            global message_count
            msg = '今日のつぶやきカウント\n'
            for author in message_count:
                msg += '  ' + author + ' : ' + str(message_count[author]) + '回\n'
                message_count[author] = 0
            await channel_current.send(msg)

# # 今日のウマタスク
# @tasks.loop(hours=1)
# async def send_umamusume():
#     now = datetime.now(datetime.timezone(datetime.timedelta(hours=9)).strftime('%H')
#     if now == '08':
#         await channel_current.send('今日のウマ')
#         await channel_current.send(umamusume.get_link(random.randint(0, 36)))
#
# # メッセージ数カウントタスク
# @tasks.loop(hours=1)
# async def send_msgcount():
#     now = datetime.now(datetime.timezone(datetime.timedelta(hours=9)).strftime('%H')
#     if now == '19':
#         global message_count
#         msg = '今日のつぶやきカウント\n'
#         for author in message_count:
#             msg += '  ' + author.nick + ' : ' + str(message_count[author]) + '回\n'
#             message_count[author] = 0
#         await channel_current.send(msg)

async def play_gacha(author):
    gacha = random.randint(0, 99)
    limit = len(member_list) - 1
    if gacha <= 0:
        # ケイスケホンダ
        await channel_current.send('https://tenor.com/Y2IF.gif')
    elif gacha <= 1:
        # ひろゆき
        await channel_current.send('https://tenor.com/bAPIp.gif')
    elif gacha <= 3:
        # 船降りろ
        await channel_current.send(member_list[random.randint(0, limit)].nick + '、お前もう船降りろ')
    elif gacha <= 5:
        # ホモ
        await channel_current.send(member_list[random.randint(0, limit)].nick + 'はホモ')
    elif gacha <= 8:
        # 給食
        await channel_current.send(member_list[random.randint(0, limit)].nick + 'は給食した。' + str(random.randint(1, 36)) + 'ヶ月休み')
    elif gacha <= 11:
        # 給料
        await channel_current.send(member_list[random.randint(0, limit)].nick + 'の来月の給料が' + str(random.randint(1, 300000)) + '円になった')
    elif gacha <= 15:
        # 仕事しろ
        await channel_current.send(author.nick + '仕事しろ')
    elif gacha <= 17:
        # 寝るな
        await channel_current.send(member_list[random.randint(0, limit)].nick + '寝るな（寝ろ）')
    elif gacha <= 19:
        # オタク
        await channel_current.send(member_list[random.randint(0, limit)].nick + '「' + author.nick + 'はオタク」')
    elif gacha <= 21:
        # 草
        await channel_current.send(member_list[random.randint(0, limit)].nick + '「草」')
    elif gacha <= 23:
        # どけ
        await channel_current.send(member_list[random.randint(0, limit)].nick + '「どけ！！！　俺はお兄ちゃんだぞ！！！」')
    elif gacha <= 26:
        # 席ねえ
        str = member_list[random.randint(0, limit)].nick + 'の席ねぇから！'
        await channel_current.edit(name=str)
        await channel_current.send('何かが変化した…')
    elif gacha <= 27:
        # ハッテン場
        str = 'ハッテン場'
        await channel_current.edit(name=str)
        await channel_current.send('何かが変化した…')
    elif gacha <= 28:
        # Twitter
        str = 'Twitter'
        await channel_current.edit(name=str)
        await channel_current.send('何かが変化した…')
    elif gacha <= 29:
        # R&D
        str = 'R＆Dセンター'
        await channel_current.edit(name=str)
        await channel_current.send('何かが変化した…')
    elif gacha <= 30:
        # 家
        str = member_list[random.randint(0, limit)].nick + 'の家'
        await channel_current.edit(name=str)
        await channel_current.send('何かが変化した…')
    elif gacha <= 33:
        # cat
        await channel_current.send(tenor.get_search_gif('cat'))
    elif gacha <= 35:
        # doge
        await channel_current.send(tenor.get_search_gif('doge'))
    elif gacha <= 37:
        # nerd
        await channel_current.send(tenor.get_search_gif('nerd'))
        await channel_current.send('↑お前')
    elif gacha <= 39:
        # space cat
        await channel_current.send(tenor.get_search_gif('space cat'))
        await channel_current.send('（何言ってんだこいつ…）')
    elif gacha <= 43:
        # umamusume
        await channel_current.send(tenor.get_search_gif('umamusume'))
        await channel_current.send('かわいい')
    elif gacha <= 47:
        # overtime work
        await channel_current.send(tenor.get_search_gif('overtime work'))
        await channel_current.send('↑お前')
    elif gacha <= 49:
        # fatty
        await channel_current.send(tenor.get_search_gif('fatty'))
        await channel_current.send('↑お前')
    elif gacha <= 52:
        # ボットplay1
        botname = 'あつまれ ' + member_list[random.randint(0, limit)].nick + 'の森'
        await client.change_presence(activity=discord.Game(name=botname, type=1))
        await channel_current.send('何かが変化した…')
    elif gacha <= 53:
        # ボットplay2
        botname = 'アスペックス ' + member_list[random.randint(0, limit)].nick
        await client.change_presence(activity=discord.Game(name=botname, type=1))
        await channel_current.send('何かが変化した…')
    elif gacha <= 54:
        # ボットplay3
        botname = member_list[random.randint(0, limit)].nick + ' プリティダービー'
        await client.change_presence(activity=discord.Game(name=botname, type=1))
        await channel_current.send('何かが変化した…')
    elif gacha <= 55:
        # ボットplay4
        botname = 'ポケットモンスター ' + member_list[random.randint(0, limit)].nick
        await client.change_presence(activity=discord.Game(name=botname, type=1))
        await channel_current.send('何かが変化した…')
    elif gacha <= 56:
        # ボットplay5
        botname = member_list[random.randint(0, limit)].nick + 'ハザード8'
        await client.change_presence(activity=discord.Game(name=botname, type=1))
        await channel_current.send('何かが変化した…')
    elif gacha <= 57:
        # ボット名1
        botname = member_list[random.randint(0, limit)].nick
        await channel_current.guild.me.edit(nick=botname)
        await channel_current.send('何かが変化した…')
    elif gacha <= 58:
        # ボット名1
        botname = member_list[random.randint(0, limit)].nick + '（本物）'
        await channel_current.guild.me.edit(nick=botname)
        await channel_current.send('何かが変化した…')
    elif gacha <= 59:
        # ボット名1
        botname = member_list[random.randint(0, limit)].nick + 'パッパ'
        await channel_current.guild.me.edit(nick=botname)
        await channel_current.send('何かが変化した…')
    elif gacha <= 60:
        # ボット名1
        botname = member_list[random.randint(0, limit)].nick + 'の上司'
        await channel_current.guild.me.edit(nick=botname)
        await channel_current.send('何かが変化した…')
    elif gacha <= 61:
        # ボット名1
        botname = member_list[random.randint(0, limit)].nick + '（偽物）'
        await channel_current.guild.me.edit(nick=botname)
        await channel_current.send('何かが変化した…')
    elif gacha <= 64:
        # ラーメン
        await channel_current.send('https://ramendb.supleks.jp/ippai')
    elif gacha <= 66:
        # Twitterトレンド
        await channel_current.send('https://twittrend.jp/trend/prev/24/')
    elif gacha <= 68:
        # fast.com
        await channel_current.send('https://fast.com/ja/')
    elif gacha <= 70:
        # 診断メーカー
        await channel_current.send('https://shindanmaker.com/list')
    elif gacha <= 72:
        # reddit
        await channel_current.send('https://www.reddit.com/r/Hololive/')
    elif gacha <= 74:
        # 2021最新
        await channel_current.send('https://www.amazon.co.jp/s?k=2021%E6%9C%80%E6%96%B0&rh=n%3A3210981&dc&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&qid=1622905453&rnid=2321267051&ref=sr_nr_n_1')
    elif gacha <= 76:
        # Steam
        await channel_current.send('https://store.steampowered.com/search/?filter=topsellers&os=win')
    elif gacha <= 80:
        # wiki
        await channel_current.send('http://ja.wikipedia.org/wiki/Special:Randompage')
    elif gacha <= 82:
        # googlemapfail
        await channel_current.send('https://twitter.com/googlemapsfaiI')
    elif gacha <= 84:
        # ひろゆき
        await channel_current.send('https://www.youtube.com/channel/UC0yQ2h4gQXmVUFWZSqlMVOA')
    elif gacha <= 86:
        # もこう
        await channel_current.send('https://www.youtube.com/user/mokoustream/featured')
    elif gacha <= 88:
        # ヨシダヨシオ
        await channel_current.send('https://www.youtube.com/channel/UC9WJo5ZJVXMZiA5XV2jLx5Q')
    elif gacha <= 94:
        # ウマステータス
        await channel_current.send(author.nick + 'のステータス\n   スピード : ' + str(random.randint(0, 1200)) + '\n   スタミナ : ' + str(random.randint(0, 1200)) + '\n   パワー　 : ' + str(random.randint(0, 1200)) + '\n   根性　　 : ' + str(random.randint(0, 1200)) + '\n   賢さ　　 : ' + str(random.randint(0, 1200)))
    elif gacha <= 96:
        # 育成
        await channel_current.send(author.nick + 'が今日育成するウマ\n' + umamusume.get_link(random.randint(0, 36)))
    elif gacha <= 98:
        # 説
        await channel_current.send('野獣先輩' + member_list[random.randint(0, limit)].nick + '説')
    elif gacha == 99:
        # あたり
        await channel_current.send('https://tenor.com/84o9.gif')
        await asyncio.sleep(5)
        if random.randint(0, 1) == 0:
            await channel_current.send(tenor.get_search_gif('congratulations'))
            await asyncio.sleep(1)
            await channel_current.send(tenor.get_search_gif('winning'))
            await asyncio.sleep(1)
            await channel_current.send(tenor.get_search_gif('great'))
            await asyncio.sleep(1)
            await channel_current.send(tenor.get_search_gif('perfect'))
            await asyncio.sleep(1)
            await channel_current.send(tenor.get_search_gif('yes'))
            botname = author.nick + 'の勝ち'
            await channel_current.guild.me.edit(nick=botname)
            await client.change_presence(activity=discord.Game(name=botname, type=1))
            await channel_current.edit(name=botname)
        else:
            await channel_current.send(tenor.get_search_gif('you lose'))
            botname = author.nick + 'の負け'
            await channel_current.guild.me.edit(nick=botname)
            await client.change_presence(activity=discord.Game(name=botname, type=1))
            await channel_current.edit(name=botname)

async def play_quiz():
    global answer_global
    quiz = random.randint(0, 99)
    if quiz <= -1:
        # セリフあて
        # quiz_mem = member_list[random.randint(0, len(member_list)-1)]
        # ran_mess = redis_conn.srandmember(quiz_mem.name)
        # if ran_mess != 'nil':
        #     await channel_current.send('誰のセリフでしょう？\n\n' + ran_mess)
        #     answer_global = quiz_mem.nick
    else:
        # クイズFromデータセット
        quiz_picked = quizfromjson.get_quiz()
        if 'other1' not in quiz_picked:
            await channel_current.send(quiz_picked['text'])
            answer_global = quiz_picked['answer']
        else:
            ansNum = random.randint(0, 3)
            qtext = ''
            j = 1
            for i in range(4):
                if i == ansNum:
                    t = str(i + 1) + '. ' + quiz_picked['answer'] + '\n'
                    qtext += t
                else:
                    t = str(i + 1) + '. ' + quiz_picked['other' + str(j)] + '\n'
                    qtext += t
                    j += 1
            await channel_current.send(quiz_picked['text'] + '\n\n' + qtext)
            answer_global = quiz_picked['answer']

async def answer_quiz(answer_player):
    if answer_global in answer_player:
        await channel_current.send('やるやん正解だぞ')
    else:
        await channel_current.send('違うぞボケ\n正解は' + answer_global + 'だぞ')

async def word_wolf(author):
    global game_start
    global wolf_list
    global sus
    if game_start == 'waiting':
        await channel_current.send(author.nick + 'の参加を受け付けました')
        wolf_list.append(author)
        return
    elif game_start != 'started':
        game_start = 'waiting'
        await channel_current.send('ゲームを開始します\n参加者は60秒以内に/word_wolfで参加してください\n')
        await asyncio.sleep(60)
        game_start = 'started'
        await channel_current.send('募集を締め切りました\n[メンバー]\n')
        if len(wolf_list) <= 2:
            await channel_current.send('終わり！閉廷！！！')
            game_start = ''
            wolf_list.clear()
            return
        wolfnum = random.randint(0, len(wolf_list)-1)
        for num in range(0, len(wolf_list)):
            await channel_current.send(str(num) + ' : ' + wolf_list[num].nick)
            sus.append(0)
            if num == wolfnum:
                await wolf_list[num].send('あなたは人狼です')
            else:
                await wolf_list[num].send('あなたは市民です')
        await channel_current.send('\n制限時間は' + str(think_time) + '秒です\n/wolf [番号]で投票してください')
        await asyncio.sleep(think_time)
        sus_top = sus.index(max(sus))
        sus.clear()
        await channel_current.send(wolf_list[sus_top].nick + 'が処刑されました\n[メンバー]\n')
        del wolf_list[sus_top]
        if sus == wolfnum:
            await channel_current.send('市民の勝ちです')
        elif len(wolf_list) <= 3:
            await channel_current.send('人狼の勝ちです')
        else:
            await channel_current.send('引き分け！終わり！閉廷！！！')
        game_start = ''
        wolf_list.clear()
        return

# taskの起動
task_onehour.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
