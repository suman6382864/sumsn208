import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':

    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    os.system('xdg-open https://facebook.com/groups/994845054533001/')
    from SUMAN import login
    login()
elif bit == '32bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    os.system('xdg-open https://facebook.com/groups/994845054533001/')
    from SUMAN32 import login
    login()
else:
    print('[×] Connection Error')
    exit()
