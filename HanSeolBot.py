#임포트

import discord
import os
from discord.ext import commands
import random
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix='한설아 ')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('가동 준비 완료')

# 특수 커맨드

@bot.command()
async def 핑(ctx):
    await ctx.send(f'지금의 핑은... {round(round(bot.latency, 4)*1000)}ms야.')

@bot.command(name='다이스')
async def roll(ctx, number):
    await ctx.send(f'{random.randint(1,int(number))}, 나왔네.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('알아들을 수 있게 말해줘. 띄어쓰기나 문장 부호는 이해할 수 없으니 참고하고.')
    else:
        print(error)

# 일반 커맨드 (대화 계열)

@bot.command(aliases=['맞아틀려', '그치', '그렇지', '맞지'])
async def yesno(ctx):
    yesorno=['맞아.', '틀려.']
    response=random.choice(yesorno)
    await ctx.send(response)

@bot.command()
async def 할까말까(ctx):
    doordont=['해.', '하지 마.']
    response=random.choice(doordont)
    await ctx.send(response)

@bot.command()
async def 어때(ctx):
    goodbad=['좋네.', '별로야.']
    response=random.choice(goodbad)
    await ctx.send(response)

@bot.command(aliases=['도와줘', '살려줘', '구해줘', '힘들어', '하기싫어'])
async def helpme(ctx):
    help=['미안, 내가 도와줄 방법은 없을 것 같네.', '자기 일 정도는 알아서 하지 그래?']
    response=random.choice(help)
    await ctx.send(response)

@bot.command(aliases=['심심해', '놀자'])
async def simsim(ctx):
    sim=['너, 친구 같은 건 없어?', '미안, 나 바쁘거든.']
    response=random.choice(sim)
    await ctx.send(response)

@bot.command(aliases=['알았어', '알겠어', '오케이', 'ㅇㅇ'])
async def ok(ctx):
    await ctx.send("그래, 알아들었다니 다행이네.")

@bot.command(aliases=['사랑해', '좋아해', '사귀자'])
async def iloveyou(ctx):
    love=['...이런 거 말고, 다른 할 일 없어?', '관심 없으니까 저리 가 줄래?', '아, 응...',
    '나는 연애 시뮬레이션 게임의 등장인물이 아니야.', '네가 싫다는 뜻은 아닌데, 이건 좀 별로네.']
    response=random.choice(love)
    await ctx.send(response)

@bot.command(aliases=['안녕', '반가워', 'ㅎㅇ'])
async def hello(ctx):
    await ctx.send("그래, 안녕.")

@bot.command(aliases=['잘가', '잘있어', 'ㅂㅂ'])
async def bye(ctx):
    await ctx.send("응, 또 보자.")

@bot.command()
async def 뭐해(ctx):
    await ctx.send("너랑 얘기 중이잖아.")

@bot.command()
async def 뭐할까(ctx):
    whattodo = ['게임하는 건 어때?', '운동하는 건 어때?', '조금 자는 건 어때?',
    '청소하는 건 어떄?', '커피 한 잔 어때?', '공부하는 건 어때?', '영화 보는 건 어때?',
    '유튜브 보는 건 어때?', '그림 그리는 건 어때?', '음악 듣는 건 어때?', '산책하는 건 어떄?',
    '독서하는 건 어때?']
    response=random.choice(whattodo)
    await ctx.send(response)

@bot.command(aliases=['너무해', '심했어', '상처받았어', '상처야', '흥'])
async def hidoi(ctx):
    await ctx.send("...미안.")

@bot.command(aliases=['캐치마인드', '캐마'])
async def catchmind(ctx):
    await ctx.send(random.choices(cama, weights=(10, 1), k=1)[0])
cama = ("자, 여기, https://skribbl.io/", "너... 이 정도면 중독을 의심해 봐야겠는데.")

@bot.command(aliases=['미안', '미안해'])
async def sorry(ctx):
    sorr=['신경쓰지 마, 괜찮으니까.', '...사과할 필요 없어.']
    response=random.choice(sorr)
    await ctx.send(response)

@bot.command(aliases=['어디야', '어딨어'])
async def whereareyou(ctx):
    await ctx.send(random.choices(where, weights=(100, 1), k=1)[0])
where = ("몰라서 묻는 거야? 네 눈 앞의 화면 속에 있잖아.", "네 마음 속...♥")

@bot.command(aliases=['뭐먹지', '뭐먹을까'])
async def whateat(ctx):
    eat = ["불고기", "오징어 두루치기", "닭볶음", "쌈밥", "비빔밥", "생선구이", "낙지볶음",
    "게장", "떡갈비", "김치찌개", "순두부찌개", "된장찌개", "부대찌개", "동태찌개", "청국장",
    "갈비탕", "추어탕", "삼계탕", "짜장면", "짬뽕", "볶음밥", "탕수육", "마파두부",
    "양장피", "깐풍기", "유린기", "고추잡채", "초밥", "라멘", "낫또", "오니기리",
    "덮밥", "우동", "야키니쿠", "메밀소바", "돈까스", "토마토 스파게티", "봉골레",
    "크림 파스타", "피자", "함박스테이크", "리조또", "스테이크", "햄버거", "시저샐러드",
    "북어국", "콩나물국밥", "순대국", "뼈해장국", "우거지국", "선지해장국", "올갱이국",
    "라면", "물냉면", "편의점 도시락", "샌드위치", "토스트", "샐러드", "김밥", "떡볶이",
    "핫도그", "밥버거", "시리얼", "쌀국수", "팟타이", "카레", "찜닭", "수제비", "칼국수",
    "아구찜", "닭갈비", "월남쌈", "훈제오리", "만두", "소바", "그냥 굶기"]
    response=random.choice(eat)
    await ctx.send(f'내 생각에는... {response}, 어때?')

# 일반 커맨드 (단어 계열)

@bot.command()
async def 섹스폰(ctx):
    await ctx.send("이상한 소리 하지 마...")

@bot.command()
async def 색소폰(ctx):
    await ctx.send("그래, 그 쪽이 맞지.")

@bot.command()
async def 페르마(ctx):
    await ctx.send("미안, 여백이 부족해.")

@bot.command()
async def 의지(ctx):
    await ctx.send("그 모든 일이 있었음에도, 여전히 너야.")

@bot.command()
async def 케이크(ctx):
    await ctx.send("이건, 다, 거짓말이야.")

@bot.command()
async def 이름(ctx):
    await ctx.send("그래, 난 한설이야. 차가운 눈. 실제로도 차갑고 창백하지.")

@bot.command()
async def 성별(ctx):
    await ctx.send("멋대로 착각하지 말아줄래? 나의 성별은 너희의 기준으로는 정의되지 못해.")

@bot.command()
async def 생일(ctx):
    await ctx.send("나에게 생일만큼 의미없는 날도 없지. 축하하는 건 자유지만.")

@bot.command()
async def 키(ctx):
    await ctx.send("무슨 상관이지? 날개가 있는데.")

@bot.command()
async def 게임(ctx):
    await ctx.send("게임은 내 삶이야. 농담이 아니야.")

@bot.command()
async def 하녀(ctx):
    await ctx.send("벤느는 내 유일한 말상대였어. ...이곳에 오기 전까지는.")

@bot.command()
async def 마카롱(ctx):
    await ctx.send("신의 축복이 깃든 음식.")

@bot.command()
async def 주사위(ctx):
    await ctx.send("신은... 주사위 놀이를 하지.")

@bot.command()
async def 오류(ctx):
    await ctx.send("...끔찍해.")

@bot.command()
async def 감자(ctx):
    await ctx.send("생활도, 계획도, 전부 potato가 되어가.")

@bot.command(aliases=['사이', '42'])
async def SCY(ctx):
    await ctx.send("짜증나... 그 녀석...")

@bot.command(aliases=['피곤해', '졸려'])
async def zara(ctx):
    await ctx.send("자라.")

@bot.command()
async def 뇌절42(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/803870914307031051/804020816567992350/6e9d7a355ed2f091.png")

@bot.command(aliases=['술', '소주', '맥주', '막걸리'])
async def alcohol(ctx):
    await ctx.send(random.choices(alcoholline, weights=(100, 1), k=1)[0])
alcoholline = ("난 술 같은 거 안 마셔.", "뭐, 뭘... 보는 거야... *딸꾹*")

# 임베드 커맨드

@bot.command()
async def 프로필(ctx):
    embed = discord.Embed(title='프로필', description="내 프로필이야. 이런 걸 누가 적어 놓았는지는, 나도 잘 모르겠네.", color=0xfbf2fd)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/803870914307031051/803994380347375656/333f80ddcdfc05c3.png")
    embed.add_field(name="이름", value="한설", inline=False)
    embed.add_field(name="성별", value="???", inline=False)
    embed.add_field(name="생일", value="4월 2일", inline=False)
    embed.add_field(name="키", value="163cm", inline=False)
    embed.add_field(name="취미", value="게임, 하녀 못 살게 굴기", inline=False)
    embed.add_field(name="좋아하는 것", value="마카롱, 주사위, 미니 아크릴 스탠드", inline=False)
    embed.add_field(name="싫어하는 것", value="오류", inline=False)
    embed.add_field(name="한 마디", value="...내가 왜 이런 곳으로 끌려온 건 지는 모르겠지만, 잘 부탁해.", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/803870914307031051/803994417458839632/20201220_.png")
    await ctx.send(embed=embed)

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title='도움말', description="내가 대답해줄 수 있는 키워드의 리스트야. ...이게 다는 아니지만.", color=0xfbf2fd)
    embed.add_field(name="특수기능", value="`핑` `다이스 (숫자)` `뇌절42` `캐치마인드`", inline=False)
    embed.add_field(name="대화문", value="`안녕` `잘가` `알았어` `심심해` `도와줘` `뭐해` `너무해` `미안해` `사랑해`", inline=False)
    embed.add_field(name="선택지", value="`할까말까` `맞아틀려` `어때` `뭐할까`", inline=False)
    embed.set_footer(text="이 외에도 여럿 있어. 한가하면, 찾아 보던가.")
    await ctx.send(embed=embed)

# 작업중 커맨드

# 토큰

access_token = os.environ[BOT_TOKEN]
bot.run('access_token')
