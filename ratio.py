import pylast
import time

API_KEY = "6dc1e3b9b940ff26677ce445d3193ed0"
API_SECRET = "7d98564589a01bcecd38b0b79928c848"

username = "ialireza13"
password_hash = pylast.md5("KAMALHASHEMI 75")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

f = open("list_10.txt", "r")
data = open("data.txt", "w+")

ii = 0
name_ = f.readline()
while name_ != '':
    try:
        name_ = name_.replace('\n','')
        artist = network.get_artist(name_)
        scrobbles_ = artist.get_playcount()
        listeners_ = artist.get_listener_count()
        ratio_ = scrobbles_ / listeners_
        data.write("%s\t%d\t%d\t%f\n" % (name_, scrobbles_, listeners_, ratio_))
        ii = ii + 1
        print("%d - %s\t%d\t%d\t%f" % (ii, name_, scrobbles_, listeners_, ratio_))
        name_ = f.readline()
    except:
        time.sleep(5)

data.close()
