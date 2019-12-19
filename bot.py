import discord, asyncio, os, json, re, random

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
token=os.getenv('DISCORD_TOKEN')
client=discord.Client(fetch_offline_members=True)

class PatBot:
    def randomFace(self):
        faces = ["\n ヽ(~_~(・_・ )ゝ""\n⁽⁽◝( • ω • )◜⁾⁾","\n└(＾＾)┐","\n(~‾▽‾)~","\n ヽ( ⌒o⌒)人(⌒-⌒ )ﾉ","\n＼(＾▽＾)／","\n☆ ～('▽^人)","\nヽ(・∀・)ﾉ"]
        return faces[random.randint(0,len(faces))]

    def sendRandomError(self,message):
        return message.channel.send([" 	(⁄ ⁄•⁄ω⁄•⁄ ⁄) i don't know what to do!"," 	(⁄ ⁄•⁄ω⁄•⁄ ⁄) what is happening?","(*/ω＼) that's not right..."," 	☆ｏ(＞＜；)○ i'm not happy with the look of this... ","(ᗒᗣᗕ)՞ why is this so hard?","(＃＞＜) ... i don't know what to do... don't look at me like that!"][random.randint(0,5)])

    def updatePatCount(self, message, userId, amount):
        with open("users.json") as json_file:
            try:
                json_members = json.load(json_file)
            except ValueError:
                json_members = {}

        json_members[userId.id] = json_members.get(str(userId.id), 0) + amount

        with open("users.json", "w") as  outfile:
            json.dump(json_members, outfile)

        return json_members[userId.id]

    def sendMessage(self, message, userId, content):
        return message.channel.send(content)

    def logMessage(self, content):
        time = datetime.now().strftime("[%D %H:%M:%S]")
        return print('|{0}| : {1}'.format(time, content))

    def checkPats(self, message, userId):
        patCount = self.updatePatCount(message, userId, 0)
        if userId == message.author:
            self.logMessage('{0.author} just checked his pat points.'.format(message))
            if patCount != 1:
                return self.sendMessage(message, userId, "{0.author.mention}, you have {1} pat points! {2}".format(message, patCount, self.randomFace()))
            else:
                return self.sendMessage(message, userId, "{0.author.mention}, you have {1} pat point! {2}".format(message, patCount, self.randomFace()))
        else:
            self.logMessage("{0.author} just checked {1}'s pat points.".format(message, userId))
            if patCount != 1:
                return self.sendMessage(message, userId, "{0.mention} has {1} pat points! {2}".format(userId, patCount, self.randomFace()))
            else:
                return self.sendMessage(message, userId, "{0.mention} has {1} pat point! {2}".format(userId, patCount, self.randomFace()))


    def pat(self, message, userId):
        self.updatePatCount(message, userId, 1) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} patted themselves.'.format(message))
            return self.sendMessage(message, userId, '[+1pp] {0.author.mention} patted themselves... \n(￢_￢;) (つд｀)'.format(message))
        else:
            self.logMessage('{0.author} just patted {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[+1pp] {0.author.mention} pats {1.mention}! \n(≧ω≦)ԅ( ˘⌣˘)'.format(message, userId))


    def slap(self, message, userId):
        self.updatePatCount(message, userId, -1) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} just slapped themselves.'.format(message))
            return self.sendMessage(message, userId, '[-1 pp] {0.author.mention} just slapped themselves... \n(つ✖╭╮✖)   	╮(￣ω￣;)╭'.format(message))
        else:
            self.logMessage('{0.author} just slapped {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[-1 pp] {0.author.mention} slaps {1.mention}! \nᕦ(ò_óˇ)ᕤ    Σ(°་།°)'.format(message, userId))

    def kick(self, message, userId):
        self.updatePatCount(message, userId, -3) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} just kicked themselves.'.format(message))
            return self.sendMessage(message, userId, '[-3 pp] {0.author.mention} just kicked themselves... \n_:(´ཀ`」 ∠):_     ლ(ಠ_ಠლ) '.format(message))
        else:
            self.logMessage('{0.author} just kicked {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[-3 pp] {0.author.mention} kicks {1.mention}! \n(ノಠ益ಠ)ノ彡＼＼٩(๑`^´๑)۶／／'.format(message, userId))

    def hug(self, message, userId):
        self.updatePatCount(message, userId, 3) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} just hugged themselves.'.format(message))
            return self.sendMessage(message, userId, '[+3pp] {0.author.mention} just hugged themselves...  \n(つ . •́ _ʖ •̀ .)つ'.format(message))
        else:
            self.logMessage('{0.author} just hugged {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[+3pp] {0.author.mention} hugs {1.mention}! \n (づ^-^(^ ^*)つ ♡'.format(message, userId))

    def sesh(self, message, userId):
        self.updatePatCount(message, userId, 10) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} just seshed by themselves.'.format(message))
            return self.sendMessage(message, userId, '[+10pp] {0.author.mention} just seshed alone. \n ౦０o ｡ (‾́。‾́  )y~~'.format(message))
        else:
            self.logMessage('{0.author} just seshed with {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[+10pp] {0.author.mention} seshes with {1.mention}! \n ( ≖ ͜ʖ≖)౦０౦０o ｡(°ε° )y~~'.format(message, userId))

    def mlem(self, message, userId):
        self.updatePatCount(message, userId, 15) #1 means +1 on the patcount of the target user.

        if userId == message.author: #check if the user is the target of the command
            self.logMessage('{0.author} just mlemed'.format(message))
            return self.sendMessage(message, userId, '[+15pp] {0.author.mention} mlems\n (≧ڡ≦*)'.format(message))
        else:
            self.logMessage('{0.author} just mlemed at {1}.'.format(message, userId))
            return self.sendMessage(message, userId, '[+15pp] {0.author.mention} mlems at {1.mention}!\n  (ˆڡˆ)｡⌒☆(´ ω `)'.format(message, userId))

    def muang(self, message, userId):
        if userId == message.author:
            self.logMessage('{0.author} muang'.format(message))
            return self.sendMessage(message, userId, 'muang! \n (^=◕ᴥ◕=^) V●ᴥ●V muang!')

patbot = PatBot()

@client.event
async def on_ready():
    patbot.logMessage("patbot online ...")

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
