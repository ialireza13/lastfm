import pylast
import time
import numpy as np

API_KEY = "6dc1e3b9b940ff26677ce445d3193ed0"
API_SECRET = "7d98564589a01bcecd38b0b79928c848"

username = "ialireza13"
password_hash = pylast.md5("KAMALHASHEMI 75")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# artist_list = np.loadtxt('artists.txt', dtype=str, delimiter="\n")

count = 5000
artist_list = list()
seed_list = ["Led Zeppelin", "Herbie Hancock", "Nils Frahm", "Chet Baker", "Eminem",
             "The Beatles", "Queen",
             "Arctic Monkeys",
             "Kendrick Lamar", "Camel", "Radiohead", "Elvis Presley",
             "Michael Jackson", "David Bowie", "Bob Dylan", "B. B. King", "Johnny Cash",
             "King Crimson", "Porcupine Tree", "Slipknot", "Opeth", "Tool", "Slayer", "Lamb Of God"]
ii = 0
min_play_count = 5000
np.random.seed(int(time.time()))
seed_ = seed_list[0]
seed_list.__delitem__(0)
print("Jumped to {}!".format(seed_))
not_found = 0

while ii < count:
    try:
        jj = 0
        print(ii)
        not_found = not_found + 1
        if artist_list.count(seed_) == 0:
            if network.get_artist(seed_).get_playcount() > min_play_count:
                artist_list.append(seed_)
                ii = ii + 1
                not_found = 0
        similar = network.get_artist(seed_).get_similar(15)
        for s in similar:
            name_ = s.item.name
            if artist_list.count(name_) == 0:
                if s.item.get_playcount() > min_play_count:
                    artist_list.append(name_)
                    ii = ii + 1
                    not_found = 0
        if not_found > 2:
            if seed_list.__len__() > 0:
                rand_ = np.int(np.random.uniform(0, seed_list.__len__()))
                seed_ = seed_list[rand_]
                seed_list.__delitem__(rand_)
                print("Jumped to {}!".format(seed_))
            else:
                print("Not found!")
                break
        else:
            rand_ = np.int(np.random.uniform(0, similar.__len__()))
            seed_ = similar[rand_].item.name
    except:
        time.sleep(5)

f = open("list.txt", "w+")
for i in artist_list:
    f.write("%s\n" % (i))
f.close()
