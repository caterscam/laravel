from colorama import Fore, Style, Back
import os
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
#Just DOOOO It hahahaha
def screen_clear():
    _ = os.system('cls')

screen_clear()

print(f'''
                     {yl}                 .xKo.            ,kKc
                                        'OW0;         .lXNd.
                                         :OOOc       .dOOx.
                               ..        .dl:Oc     .xk:dc        ..
                               ;l         od.:k;    ok.;k;        'l.
                               :0c.      .kd. cx.  :x' ,Ol       .xk.
                               .dK0xddddk0k'  .o:.;o:   cOOxddddkKKc
                                 .;:cccc:'.    'cld:     .,:cccc:,.
                                                ....
                                                            {red}    Xproad Version (Cleaned by 0Xtn)
                                                                {wh}          https://t.me/dxdteam
               / /   ____ __________ __   _____  / /  /  |/  /___  ____  _____/ /____  _____ {yl}
              / /   / __ `/ ___/ __ `/ | / / _ \/ /  / /|_/ / __ \/ __ \/ ___/ __/ _ \/ ___/ {ble}
    {wh}         / /___/ /_/ / /  / /_/ /| |/ /  __/ /  / /  / / /_/ / / / (__  ) /_/  __/ /
    {ble}        /_____/\__,_/_/   \__,_/ |___/\___/_/  /_/  /_/\____/_/ /_/____/\__/\___/_/  {red}V2
                                          {wh}Welcome to the {red}hell{res}
                             {gr}Free :D{res} {ble}Lifetime{res}, {red}High Quality Private Tool{res}   
                                          
                                          
{red}[{yl}1{red}]:{res} Mass Grabber Valid All SMTPs , Twilio, Aws Keys, Nexmo, MySql

{red}[{yl}2{red}]:{res} Mass Aws Keys Quota Checker ++ Auto Root Aws Console (Admin Dashboard (RDPs,VPS, SES ...))

{red}[{yl}3{red}]:{res} Mass SMTPs Checker                            |               {red}[{yl}8{red}]:{res} Mass Advanced Dorker
                                                                      
{red}[{yl}4{red}]:{res} Mass Sendgrid Api Checker                     |               {red}[{yl}9{red}]:{res} Mass Reverse Domains => IPs
                                                                      
{red}[{yl}5{red}]:{res} Mass Twilio Checker                           |               {red}[{yl}10{red}]:{res} Mass IPS Ranger
                                                                      
{red}[{yl}6{red}]:{res} Mass Nexmo Balance Checker                    |               {red}[{yl}11{red}]:{res} Mass Laravel, Wordpress Filter

{red}[{yl}7{red}]:{res} Zone-H Grabber                                |               {red}[{yl}12{red}]:{res} MASS BYPASS & UPLOAD SHELL (LARAVEL)
                                      
                                      {red}[{yl}13{red}]:{res} Check Updates..
''')

choice = input(f'{gr}Give Me Your Choice{wh}/{red}0xtn> {gr}${res} ')
if choice == '1':
    link = input(f'{gr}Give Me Your List.txt{wh}/{red}0xtn> {gr}${res} ')
    os.system(f'cmd /k "py Scripts/grabber.py {link}"')
if choice == '2':
    os.system('cmd /k "py Scripts/aws2.py"')
if choice == '3':
    os.system('cmd /k "py Scripts/checker.py"')
if choice == '4':
    os.system('cmd /k "py Scripts/sendg.py"')
if choice == '5':
    os.system('cmd /k "py Scripts/api.py"')
if choice == '6':
    os.system('cmd /k "py Scripts/nexmo.py"')
if choice == '7':
    os.system('cmd /k "py Scripts/zone.py"')
if choice == '8':
    os.system('cmd /k "py Scripts/scanner.py"')
if choice == '9':
    os.system('cmd /k "py Scripts/ipfromdomain.py"')
if choice == '10':
    os.system('cmd /k "perl Scripts/ranger.pl"')
if choice == '11':
    os.system('cmd /k "py Scripts/laravelcms.py"')
if choice == '12':
    os.system('cmd /k "py Scripts/up.py"')
if choice == '13':
    print(f'Please Contact {red}0xtn{res} For More Tools ;)\n                   {ble}https://t.me/DXDTEAM{res}')