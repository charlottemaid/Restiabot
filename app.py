
import ch
import random
import sys
import os
import re
import time
import json
import urllib
import traceback
import __future__
import shelve
from time import localtime, strftime
import ch
import random
import sys
import os
import re
import time
import json
import urllib
import traceback
import __future__
import shelve
from time import localtime, strftime
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from xml.etree import cElementTree as ET
from urllib.request import unquote
from random import choice
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
import re

################################
lockdown = False
activated = True
################################

def getUptime():
  """
 Returns the number of seconds since the programs started.
 """
  #do return startTime if you want the process start time
  
  return time.time() - startTime

################################
##File Stuff##

startTime = time.time()

pd = dict()
wordtodaytime = dict()
wife = dict()
ping = dict()
oco = dict()
family = dict()
pdf = dict()
waifu = dict()

########################################
########## BLACKLIST ###################

blacklist = dict()
try:
  f = open("blacklist.txt", "r")
  blacklist = eval(f.read())
  f.close()
except:pass

########################################
########## RANK ########################

developer = []
file = open("developer.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    developer.append(name.strip())
print("[INF]Loading Developer...")
file.close()

########################################

admin = []
file = open("admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
print("[INF]Loading Admin...")
file.close()

########################################

mod = []
file = open("mod.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    mod.append(name.strip())
print("[INF]Loading Mod...")
file.close()

#######################################

assistant = []
file = open("assistant.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    assistant.append(name.strip())
print("[INF]Loading Assistant...")
file.close()

########################################


registered = []
file = open("registered.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    registered.append(name.strip())
print("[INF]Loading Registered...")
file.close()

########################################

blacklist = []
file = open("blacklist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    blacklist.append(name.strip())
print("[INF]Loading Blacklist...")
file.close()

########################################

whitelist = []
file = open("whitelist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    whitelist.append(name.strip())
print("[INF]Loading Whitelist...")
file.close()

########################################
############# STATUS ROOM ##############

rooms = []
file = open("rooms.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    rooms.append(name.strip())
print("[INF]Loading Rooms...")
file.close()

#########################################

locks = []
file = open("locks.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    locks.append(name.strip())
print("[INF]Loading Locks...")
file.close()

#########################################
########### SN Notifs ###################

sasaran = dict()
f = open ("notes.txt", "r") #read-only
print("[INF]Loading Notes...")
time.sleep(1)
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()
 
notif = []
f = open("notif.txt", "r")
print("[INF]Loading Notifs...")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

#########################################
################# NICK ##################

nicks=dict()
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()

def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user



#############################################################
##========================Variables========================##

botname = "Tanpaid" #Put your bot name here

botpassword = "bayu1997!" #Put your bot password here

cek_mods = dict() #Don't mess with this variable. This one is related with *mods command.

error = ("Expectation failed.")    #Error message

command_list = ['help','wl/register','uwl/unregister','bl/blacklist','chain','ubl/unblacklist','unchain','rank','setrank','pm','broadcast','say','reverse/rsay','find','multichat','ban','unban','join','leave','lock','unlock','rooms','save','mods','activate','restrict','lockdown','wake']

prefix = "." ##You set the prefix here

##===========================End===========================##
#############################################################
  
#setting colors
  
class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("FFCC00")
    self.setFontColor("33CCFF")
    self.setFontFace("Comic")
    self.setFontSize(12)
    self.enableBg()  
    self.enableRecording()
    
  def saveAll(self):
    room = self._Room
    f = open("blacklist.txt", "w")
    f.write("\n".join(blacklist))
    f.close()
    f = open("developer.txt", "w")
    f.write("\n".join(developer))
    f.close()
    f = open("admin.txt", "w")
    f.write("\n".join(admin))
    f.close()
    f = open("mod.txt", "w")
    f.write("\n".join(mod))
    f.close()
    f = open("assistant.txt", "w")
    f.write("\n".join(assistant))
    f.close()
    f = open("registered.txt", "w")
    f.write("\n".join(registered))
    f.close()
    f = open("rooms.txt", "w")
    f.write("\n".join(self.roomnames))
    f.close()

  def findUser(self, args):
          stuff = urllib.request.urlopen("http://" + args + ".chatango.com/").read().decode()
          if "buyer" in stuff:
                  return "<f x11FF0000='1'>%s <f x11000000='1'>é um usuário." % args.title()
          elif "group" in stuff:
                  return "<f x11FF0000='1'> %s <f x11000000='1'>é um chat, é o seu link interno é: <f x11FF0000='1'>%s" % (args.title(), ch.getServer(args))
          elif not "buyer" in stuff or not "group" in stuff:
                  return "%s isso existe?" % args.title()

  def getAccess(self, room, user):
    vroom = room
    if user.name in developer and not user.name in blacklist: return 6
    elif user.name in admin and not user.name in blacklist: return 5
    elif user.name in mod and not user.name in blacklist: return 4
    elif user.name in assistant and not user.name in blacklist: return 3
    elif user.name in registered and not user.name in blacklist: return 2
    elif user.name not in whitelist and not user.name in blacklist: return 1
    elif user.name in blacklist: return -1
    else: return 0

#############################################  
##connecting and disconnecting crap##
  
  def onConnect(self, room):
    print("[+] Mad Hatter Connected to "+room.name)
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("<br/>||<font color='#87ceeb'><b>OWNER</b></font>: <b>"+ (self.getRoom(rmd).ownername) +"</b> <br/>||<b>Mods</b>: "+", ".join(self.getRoom(rmd).modnames), True)
        self.leaveRoom(rmd)
        cek_mods.pop(i)
      return
    
  def onReconnect(self, room):
    print("[+] RestiaBot Reconnected to "+room.name)
    
  def onDisconnect(self, room):
    print("[+] MRestiaBot Disconnected from "+room.name)
    
  def onBan(self, room, user, target):
    print(user.name+" got banned in "+room.name)
    

  def onConnectFail(self, room):
    print("[ERR] Room Not Found")
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("room tidak tersedia")
        cek_mods.pop(i)
      return

  

##End##
#############################################

#############################################
##setting up commands##
  
  def onMessage(self, room, user, message):
   try:
    if user == self.user:
        return
    global activated
    global lockdown
    global developer
    global admin
    global mod
    global assistant
    global registered
    global whitelist
    try:
      if room.getLevel(self.user) > 0:
        print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][%s] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, message.ip, user.name.title(), message.body))
      else:
        print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][User_IP: Null] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, user.name.title(), message.body))
    except:
      pass


##################################################################################################################################################################################
        
    ##Commands | You design great commands for your bot in this part
    if message.body[0] == "." or message.body[0] == "" or message.body[0] == "" : #prefix usage in this line (for this case I use "*" as prefix)
        data = message.body[1:].split(" ", 1) #This part splits message body into [0]prefix and [1:]data ([1:] <- this means the message body's second character and after) and data will be split into 2 (cmd(data[0]), args(data[1])) which is very usefull. (Many thanks to TryHardHusky)
        if len(data) == 2: #If there are more than 1 data (This is where we will get args)
          cmd, args = data[0], data[1] #the first data (data[0]) will be the cmd (specified command) and the next data will be args (it doesn't matter how many word next to the cmd, It'd eventually be args)
        else: #If there is only 1 data (No args)
          cmd, args = data[0], "" #the arg will simply be "" (Empty)
        cmd == cmd.lower()

 

##########################################################################################################################################
################################################## SYSTEN ################################################################################ 
            

        if cmd == "restart":      
         if self.getAccess(room, user) >= 6:
            room.message("Restart in proses... ")
            for room in self.rooms:
                time.sleep(2)
                room.reconnect()
   


##########################################################################################################################################
################################################################# NICKS ##################################################################

        elif cmd == "nick":
        ## if user.name in reg or user.name in friends or user.name in trusted or user.name in owners:
            if args:
                nick = args 
                user = user.name 
                nicks[user] = json.dumps(nick)
                room.message("<f x11FF0000='1'> "+user+"   <f x11000000='1'> mulai sekarang char akan memanggilmu <f x11FF0000='1'> "+str(args)+" ", True)
                try: 
                    print("[SAVING] NICKS...")
                    f = open("nicks.txt", "w")
                    for user in nicks:
                        nick = json.loads(nicks[user])
                        f.write(json.dumps([user,nick]) + "\n")
                except:
                       room.message("Error untuk save nick.");return
            else:
              room.message("<f x11FF0000='1'>"+user.name+" <f x11000000='1'> untuk menggunakan ini jenis perintah .nick + nama yang ingin Anda pake.", True)



##################################################TALK bot #################################################################################
            
        if "tanpaid" in message.body:
           room.message("tanpaid sedang off atau afk :D, " +message.body)
        if "Tanpaid" == message.body.lower(): #for example if someone said "hello" in the chatroom
           room.message("Tanpaid sedang off atau afk :D "+user.name.title()) #the bot will answer with "Hello User1Name"
        if "@tanpaid" == message.body.lower():
           room.message("@tanpaid sedang off atau afk :D "+user.name.title())
        if "" == message.body:
         self.stop()




################################################## FINAL #################################################################################
################################################## FINAL #################################################################################


   except Exception as e:
         try:
          et, ev, tb = sys.exc_info()
          lineno = tb.tb_lineno
          fn = tb.tb_frame.f_code.co_filename
          room.message("[Error] %s Line %i - %s"% (fn, lineno, str(e)))
          return
         except:
          room.message("Undescribeable error detected !!")
          return

  


#  def onLeave(self, room, user):
#    print("[+] "+user.name+" left "+room.name)
#    if room.usercount >= 20:
#      return
#    room.message(user.name+" has left the room.")

  def onFloodWarning(self, room):
    room.reconnect()
    room.setSilent(True)
    self.setTimeout(15, room.setSilent, False)
    self.setTimeout(16, room.message, "I'm back.")
    print("[+] Reconnecting...")

  def onMessageDelete(self, room, user, msg):
    print("MESSAGE DELETED: " + user.name + ": " + msg.body)
  
  def onPMMessage(self, pm, user, body):
    print("PM - "+user.name+": "+body)
    pm.message(user, "I'm a Bot Created by Isa. Please PM my owner instead!")

def hexc(e):
  et, ev, tb = sys.exc_info()
  if not tb: print(str(e))
  while tb:
    lineno = tb.tb_lineno
    fn = tb.tb_frame.f_code.co_filename
    tb = tb.tb_next
  print("(%s:%i) %s" % (fn, lineno, str(e)))
  
if __name__ == "__main__":
   try:
     os.system("clear")
     TestBot.easy_start(rooms, botname, botpassword)
   except KeyboardInterrupt:
     print("Console initiated a kill.")
   except Exception as e:
     hexc(e)
