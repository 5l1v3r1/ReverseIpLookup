# Coded By Mr.KaitoX
# Working API -> HackerTarget - Reverse Ip Lookup
# No Recoded Please Credits to the Author :> It's Cannot make you Good Programmer :V

import os, sys, random, time,re
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def banners():
    os.system('clear')
    clear = '\x1b[1;0m'
    colors = [36, 32, 34, 35, 31, 37]
    banner = """
    
    ______     ______     __   __   ______     ______     ______     ______     __     ______  
   /\  == \   /\  ___\   /\ \ / /  /\  ___\   /\  == \   /\  ___\   /\  ___\   /\ \   /\  == \ 
   \ \  __<   \ \  __\   \ \ \\'/   \ \  __\   \ \  __<   \ \___  \  \ \  __\   \ \ \  \ \  _-/ 
    \ \_\ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_\  \ \_\   
     \/_/ /_/   \/_____/   \/_/      \/_____/   \/_/ /_/   \/_____/   \/_____/   \/_/   \/_/   

                   [Coded By : Kaito legion] [Team : Pinoy Rootsec]
                                                                                            
    """
    for N, line in enumerate(banner.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


def webNotEmpty(website):

    if len(website) >= 1:
        return "valid"
    else:
        return "!valid"

def validWebsite(website):

    web = webNotEmpty(website)
    if web is "valid":
        if not (re.match(r"(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)", website)):
            exit(wrong_URL)
    else:
        exit(empty_Website)
def removeHTTP(website):
    website = cleanURL(website); return(website)

def addHTTP(website):
    website = cleanURL(website)
    website = ("http://" + website); return(website)

def cleanURL(website):
    web = validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    website = website.replace("www.", ""); return(website)

def write(var, data):
    if var == None:
        pass
    elif var != None:
        print(str(data))
        f = open("Grab.txt", "a")
        f.write(data+'\n')
        f.close()

def reverseHackTarget(website):
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for s in list:
            if len(s) != 0:
                write(var="+", data=s)
    else:
        write(var="@", data="Website you Entered have no Domains :(")


def Main():
    banners()
    site = raw_input('[>] Enter site:# ')
    reverseHackTarget(site)
    	


if __name__ == '__main__':
    Main()


