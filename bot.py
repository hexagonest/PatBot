import discord, asyncio, os, json, re, random

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
token=os.getenv('DISCORD_TOKEN')
client=discord.Client(fetch_offline_members=True)

#dunno what to do with this method lol, doesn't work when declared inside the class
def randomFace():
    faces = ["\n ヽ(~_~(・_・ )ゝ""\n⁽⁽◝( • ω • )◜⁾⁾","\n└(＾＾)┐","\n(~‾▽‾)~","\n ヽ( ⌒o⌒)人(⌒-⌒ )ﾉ","\n＼(＾▽＾)／","\n☆ ～('▽^人)","\nヽ(・∀・)ﾉ"]
    return faces[random.randint(0,len(faces))]

class PatBot:
    def sendRandomError(self,message):
        return message.channel.send([" 	(⁄ ⁄•⁄ω⁄•⁄ ⁄) i don't know what to do!"," 	(⁄ ⁄•⁄ω⁄•⁄ ⁄) what is happening?","(*/ω＼) that's not right..."," 	☆ｏ(＞＜；)○ i'm not happy with the look of this... ","(ᗒᗣᗕ)՞ why is this so hard?","(＃＞＜) ... i don't know what to do... don't look at me like that!"][random.randint(0,5)])

    def checkPats(self, message, user):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        if user == message.author:
            print('|'+ time +'| >{0.author} just checked his pat points.'.format(message))
            with open("users.json") as json_file:
                try:
                    json_members = json.load(json_file)
                except ValueError:
                    json_members = {}
                if(json_members.get(str(message.author.id), 0) != 1):
                    return message.channel.send("{0.author.mention}, you have {1} pat points! {2}".format(message, json_members.get(str(message.author.id), 0), randomFace()))
                else:
                    return message.channel.send("{0.author.mention}, you have {1} pat point! {2}".format(message, json_members.get(str(message.author.id), 0), randomFace()))
        else:
            #print(user)
            print("|"+ time +"| >{0.author} just checked {1}'s pat points.".format(message, user))
            with open("users.json") as json_file:
                try:
                    json_members = json.load(json_file)
                except ValueError:
                    json_members = {}
                if(json_members.get(str(message.author.id), 0) != 1):
                    return message.channel.send("{0.mention} has {1} pat points! {2}".format(user, json_members.get(str(user.id), 0), randomFace()))
                else:
                    return message.channel.send("{0.mention} has {1} pat point! {2}".format(user, json_members.get(str(user.id), 0), randomFace()))

    def pat(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) + 1


        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        if patee == message.author:
            print('|'+ time +'| >{0.author} patted themselves.'.format(message))
            return message.channel.send('[+1pp] {0.author.mention} patted themselves... \n(￢_￢;) (つд｀)'.format(message))
        else:
            print('|'+ time +'| >{0.author} just patted {1}.'.format(message, patee))
            return message.channel.send('[+1pp] {0.author.mention} pats {1.mention}! \n(≧ω≦)ԅ( ˘⌣˘)'.format(message, patee))

    def slap(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) - 1

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        if patee == message.author:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just slapped themselves.'.format(message))
            return message.channel.send('[-1 pp] {0.author.mention} just slapped themselves... \n(つ✖╭╮✖)   	╮(￣ω￣;)╭'.format(message))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just slapped {1}.'.format(message, patee))
            return message.channel.send('[-1 pp] {0.author.mention} slaps {1.mention}! \nᕦ(ò_óˇ)ᕤ    Σ(°་།°)'.format(message, patee))

    def kick(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) - 3

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)


        if patee == message.author:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just kicked themselves.'.format(message))
            return message.channel.send('[-3 pp] {0.author.mention} just kicked themselves... \n_:(´ཀ`」 ∠):_     ლ(ಠ_ಠლ) '.format(message))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just kicked {1}. Ouch'.format(message, patee))
            return message.channel.send('[-3 pp] {0.author.mention} kicks {1.mention}! \n(ノಠ益ಠ)ノ彡＼＼٩(๑`^´๑)۶／／'.format(message, patee))

    def hug(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) + 3

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        if patee == message.author:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just hugged themselves.'.format(message))
            return message.channel.send('[+3pp] {0.author.mention} just hugged themselves...  \n(つ . •́ _ʖ •̀ .)つ'.format(message))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just hugged {1}.'.format(message, patee))
            return message.channel.send('[+3pp] {0.author.mention} hugs {1.mention}! \n (づ^-^(^ ^*)つ ♡'.format(message, patee))


    def sesh(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) + 10

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just seshed alone.'.format(message))
            return message.channel.send('[+10pp] {0.author.mention} just seshed alone. \n ౦０o ｡ (‾́。‾́  )y~~'.format(message))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just hugged {1}.'.format(message, patee))
            return message.channel.send('[+10pp] {0.author.mention} seshes with {1.mention}! \n ( ≖ ͜ʖ≖)౦０౦０o ｡(°ε° )y~~'.format(message, patee))

    def mlem(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) + 1

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} just mlemed.'.format(message))
            return message.channel.send('[+1pp] {0.author.mention} mlems\n (≧ڡ≦*)'.format(message))
        else:
            ##debug
            print('|'+ time +'| >{0.author} just mlemed {1}.'.format(message, patee))
            return message.channel.send('[+1pp] {0.author.mention} mlems at {1.mention}!\n  (ˆڡˆ)｡⌒☆(´ ω `)'.format(message, patee))

    def muang(self, message, userId):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        try:
            patee = userId
        except:
            return

        if patee.mention == message.author.mention:
            ##debug cmd line
            print('|'+ time +'| >{0.author} muang'.format(message))
            return message.channel.send('muang! \n (^=◕ᴥ◕=^) V●ᴥ●V muang!'.format(message))

    #TODO convert to commaands

@client.event
async def on_ready():
    time = datetime.now().strftime("[%D %H:%M:%S]")
    print('|'+ time +'|-[hexadecimalbot] patBot online.')

patbot = PatBot()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith('%'):
        return

    args = message.content.split(' ')
    userId = message.mentions[0] if 0 < len(message.mentions) else message.author


    #if an argument is present, assign target to user. If not, assign target to sender of message.

    if message.content.startswith('%pats'):
        try:
            await patbot.checkPats(message,userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%pat'):
        try:
            await patbot.pat(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%slap'):
        try:
            await patbot.slap(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%hug'):
        try:
            await patbot.hug(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%kick'):
        try:
            await patbot.kick(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%sesh'):
        try:
            await patbot.sesh(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%mlem'):
        try:
            await patbot.mlem(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return
    elif message.content.startswith('%muang'):
        try:
            await patbot.muang(message, userId)
            return
        except:
            await patbot.sendRandomError(message)
            return

client.run(token)
