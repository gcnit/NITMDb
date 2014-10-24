import urllib
import json
import os
import sys
import datetime

garbage = [ "yify", "xvid", "xmas", "x264", "www", "webrip", "warrlord", "vip3r", "v2", "usabitcom", "usabit", "unrated", "unique", "ts", "trippleaudio", "tots", "torrentfive", "tode", "titan", "thewretched", "teh", "taste", "subs", "stylishsalh", "stylish release", "srkfan", "spidy", "song4", "silver rg", "series", "secretmyth", "scream", "scr", "sc0rp", "sam", "s4a", "rises", "rips", "rip", "revott", "rets", "release", "rel", "readnfo", "r6", "r5", "ptpower", "psig", "pseudo", "pristine", "playxd", "phrax", "oscars", "noir", "nl", "neroz", "mxmg", "mp4", "mp3", "mov", "moh", "merry", "maxspeed", "line", "limited", "kingdom", "imb", "hsbs", "hr", "hq", "hindi", "hellraz0r", "hdrip", "hd", "h264", "greenbud", "goku61", "glowgaze", "gb", "ganool", "fxg", "ftw", "feel", "fasm", "extratorrentrg", "extratorrent", "extratorrenrg", "extended", "exclusive", "etrg", "esub", "enghindiindonesian", "eng", "ee", "e sub xrg", "dxva", "dvdscr", "dvdrip", "dvd", "didee", "diamond", "ddr", "crazy torrent", "cool guy", "com", "cocain", "chivvez", "charmeleon", "cc", "brrip", "bluray", "bito", "bida", "bestdivx", "bdrip", "badmeetsevil", "b89", "axxo", "arigold", "archivist", "aqos", "amx", "amiable", "alliance", "ac3", "absurdity", "aac", "a2zrg", "7o9", "720p", "576p", "5.1", "4playhd", "480p", "3lt0n", "3li", "3d", "1xcd", "1cdrip", "1cd", "171", "1337x", "1080p", "1080", "1.4", "007", ">", "<", "+", "~", "}", "|", "{", "`", "_", "]", "\"", "[", "@", "?", ";", ":", ".", "*", ")", "(", "&", "$", "!", "-" ]
extensions = [".wmv", ".webm", ".svi", ".roq", ".rmvb", ".rm", ".qt", ".ogv", ".ogg", ".nsv", ".mxf", ".mpv", ".mpg", ".mpeg", ".mpe", ".mp4", ".mp2", ".mov", ".mng", ".mkv", ".m4v", ".m4p", ".m2v", ".flv", ".drc", ".avi", ".asf", ".3gp", ".3g2"]
omdb = "http://www.omdbapi.com/?t="
thisyear = (datetime.datetime.now().year) + 1
moviefolder = sys.argv[1]

def clean(movie,extension):
    movie = movie.lower()
    movie = movie.replace(extension, " ")
    for garb in garbage:
        movie = movie.replace(garb, " ")
    for year in range(1900, thisyear):
        movie = movie.replace(str(year), " ")
    movie = movie.lstrip().rstrip()
    return movie

def rate(moviefolder):
    for movie in os.listdir(moviefolder):
        moviename = os.path.join(moviefolder,movie)
        if os.path.isdir(moviename):
            rate(moviename)
        elif os.path.isfile(moviename):
            for extension in extensions:
                if extension in movie:
                    movie = clean(movie,extension)
                    url = omdb + movie
                    response = urllib.urlopen(url).read()
                    jsonvalues = json.loads(response)
                    if jsonvalues["Response"] == "True":
                        name = jsonvalues['Title']
                        imdbrating = jsonvalues['imdbRating']
                        newmovie = os.path.join(moviefolder, imdbrating + " " + name + extension)
                        os.rename(moviename, newmovie)
                    break

if __name__ == '__main__':            
    rate(moviefolder)
