import discord, asyncio, os, json, re, random

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
token=os.getenv('DISCORD_TOKEN')
client=discord.Client(fetch_offline_members=True)

@client.event
async def on_ready():
    time = datetime.now().strftime("[%D %H:%M:%S]")
    print('|'+ time +'|-[hexadecimalbot] patBot online.')

def sendRandomError(message):
    return message.channel.send(["ono i don't know what to do!","owo what is happening?","u-u that's not right...","unu i'm not happy with the look of this... ","q.q why is this so hard?","owo ... i don't know what to do... don't look at me like that!"][random.randint(0,5)])

def checkPats(message,user=0):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    if(user==0):
        print('|'+ time +'| >{0.author} just checked his pat points.'.format(message))
        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}
            if(json_members.get(str(message.author.id), 0) != 1):
                return message.channel.send("{0.author.mention}, you have {1} pat points!".format(message, json_members.get(str(message.author.id), 0)))
            else:
                return message.channel.send("{0.author.mention}, you have {1} pat point!".format(message, json_members.get(str(message.author.id), 0)))
    else:
        #print(user)
        print("|"+ time +"| >{0.author} just checked {1}'s pat points.".format(message, user))
        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}
            if(json_members.get(str(message.author.id), 0) != 1):
                return message.channel.send("{0.mention} has {1} pat points!".format(user, json_members.get(str(user.id), 0)))
            else:
                return message.channel.send("{0.mention} has {1} pat point!".format(user, json_members.get(str(user.id), 0)))

def pat(message,idString):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    try:
        patee = message.channel.guild.get_member(int(idString))
    except:
        patee = None

    with open("users.json") as json_file:
        try:
            json_members = json.load(json_file)
        except ValueError:
            json_members = {}

    json_members[idString] = json_members.get(idString, 0) + 1

    with open("users.json", "w") as  outfile:
        json.dump(json_members, outfile)

    if patee != None:
        print('|'+ time +'| >{0.author} just patted {1}.'.format(message, patee))
        return message.channel.send('[+1pp] {0.author.mention} pats {1.mention}! (≧ω≦)ԅ( ˘⌣˘)'.format(message, patee))
    else:
        print('|'+ time +'| >{0.author} patted themselves.'.format(message))
        return message.channel.send('[+1pp] {0.author.mention} patted themselves... (￢_￢;) (つд｀)'.format(message))

def slap(message, idString):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    try:
        patee = message.channel.guild.get_member(int(idString))
    except:
        return sendRandomError(message)
    with open("users.json") as json_file:
        try:
            json_members = json.load(json_file)
        except ValueError:
            json_members = {}

    json_members[idString] = json_members.get(idString, 0) - 1

    with open("users.json", "w") as  outfile:
        json.dump(json_members, outfile)


    if patee != None:
        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just slapped themselves.'.format(message))
            return message.channel.send('[-1 pp] {0.author.mention} just slapped themselves... (つ✖╭╮✖)   	╮(￣ω￣;)╭'.format(message, patee))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just slapped {1}.'.format(message, patee))
            return message.channel.send('[-1 pp] {0.author.mention} slaps {1.mention}! ᕦ(ò_óˇ)ᕤ    Σ(°་།°)'.format(message, patee))
    else:
        return sendRandomError(message)

def kick(message, idString):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    try:
        patee = message.channel.guild.get_member(int(idString))
    except:
        return sendRandomError(message)
    with open("users.json") as json_file:
        try:
            json_members = json.load(json_file)
        except ValueError:
            json_members = {}

    json_members[idString] = json_members.get(idString, 0) - 3

    with open("users.json", "w") as  outfile:
        json.dump(json_members, outfile)


    if patee != None:
        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just kicked themselves.'.format(message))
            return message.channel.send('[-1 pp] {0.author.mention} just kicked themselves... _:(´ཀ`」 ∠):_     ლ(ಠ_ಠლ) '.format(message, patee))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just kicked {1}. Ouch'.format(message, patee))
            return message.channel.send('[-3 pp] {0.author.mention} kicks {1.mention}! (ノಠ益ಠ)ノ彡＼＼٩(๑`^´๑)۶／／'.format(message, patee))
    else:
        return sendRandomError(message)

def hug(message, idString):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    try:
        patee = message.channel.guild.get_member(int(idString))
    except:
        return sendRandomError(message)

    with open("users.json") as json_file:
        try:
            json_members = json.load(json_file)
        except ValueError:
            json_members = {}

    json_members[idString] = json_members.get(idString, 0) + 3

    with open("users.json", "w") as  outfile:
        json.dump(json_members, outfile)


    if patee != None:
        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just hugged themselves.'.format(message))
            return message.channel.send('[+3pp] {0.author.mention} just hugged themselves...  	(つ . •́ _ʖ •̀ .)つ'.format(message, patee))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just hugged {1}.'.format(message, patee))
            return message.channel.send('[+3pp] {0.author.mention} hugs {1.mention}!  (づ^-^(^ ^*)つ ♡'.format(message, patee))
    else:
        return sendRandomError(message)

def sesh(message, idString):
    time = datetime.now().strftime("[%D %H:%M:%S]")
    try:
        patee = message.channel.guild.get_member(int(idString))
    except:
        return sendRandomError(message)

    with open("users.json") as json_file:
        try:
            json_members = json.load(json_file)
        except ValueError:
            json_members = {}

    json_members[idString] = json_members.get(idString, 0) + 10

    with open("users.json", "w") as  outfile:
        json.dump(json_members, outfile)

    if patee != None:
        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just seshed alone.'.format(message))
            return message.channel.send('[+10pp] {0.author.mention} just seshed alone.  ౦０o ｡ (‾́。‾́  )y~~'.format(message, patee))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just hugged {1}.'.format(message, patee))
            return message.channel.send('[+10pp] {0.author.mention} seshes with {1.mention}! ( ≖ ͜ʖ≖)౦０౦０o ｡(°ε° )y~~'.format(message, patee))
    else:
        return sendRandomError(message)

#TODO convert to commaands


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith('%'):
        return

    args = message.content.split(' ')
    try:
        idString = re.sub("[^0-9]", "", args[1]) or None
    except:
        return

    if message.content.startswith('%pats'):
        if len(args) == 1:
            await checkPats(message)
            return

        try:
            user = message.channel.guild.get_member(int(idString))
            await checkPats(message,user)
            return
        except:
            await sendRandomError(message)
            return
    elif message.content.startswith('%pat'):
        try:
            await pat(message, idString or None)
            return
        except:
            await sendRandomError(message)
            return
    elif message.content.startswith('%slap'):
        try:
            await slap(message, idString or None)
            return
        except:
            await sendRandomError(message)
            return
    elif message.content.startswith('%hug'):
        try:
            await hug(message, idString or None)
            return
        except:
            await sendRandomError(message)
            return
    elif message.content.startswith('%kick'):
        try:
            await kick(message, idString or None)
            return
        except:
            await sendRandomError(message)
            return
    elif message.content.startswith('%sesh'):
        try:
            await sesh(message, idString or None)
            return
        except:
            await sendRandomError(message)
            return

client.run(token)
