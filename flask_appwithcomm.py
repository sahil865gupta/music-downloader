# Property of TMW Army
# handle a POST request
from flask import Flask, request, redirect
# A library that helps extracting data from web
from urllib.request import urlopen
import requests
# A library that helps in scraping web elements
from bs4 import BeautifulSoup
spam = []

# Add youtube channels to not download list
# Handle a POST Request
from flask import Flask, request, redirect
from urllib.request import urlopen  # A library that helps extracting data from web

import requests
from bs4 import BeautifulSoup  # A library that helps in scraping web elements

spam = []
spam.append("UCwLw7qgi9103XrItTR6Ij4Q")


def similar(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    words = str1.split()
    ctr = 0
    match = 0
    for word in words:
        if word in str2:
            match += 1
        ctr += 1
        match = match + 1
        ctr = ctr + 1
    if match >= (ctr - 1):
        return 1
    else:
        return 0


app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    t = request.args.get('name')
    t = t.replace(" ", "+")
    url = "https://www.youtube.com/results?search_query=" + t + "lyric"
    response = urlopen(url)
    page_source = response.read()
    t = t.replace("+", " ")
    # print(url)
    soup = BeautifulSoup(page_source, 'html.parser')
    # print(soup)
    c = 1
    for h3 in soup.find_all('h3'):
        # print(c)
        c += 1
        # print(h3)
        if(c > 4 and c < 25):
            # print("c is" + str(c))
            link = h3.a
            # print(link)
            url_end = link.get('href')
            # name=link.string
            ids = url_end[9:]
            print(ids)
            desc = "https://www.googleapis.com/youtube/v3/videos?\part=snippet&id="
            +ids
            +"&fields=items/snippet/title,items/snippet/channelId,items/snippet/description&key=AIzaSyCdkj_kXilFk4KH3zFn8a6SAEwAxsSx3tw"
            # print(link)
            r = requests.get(desc)
            obj = r.json()
            # print obj
    soup = BeautifulSoup(page_source, 'html.parser')
    c = 1
    for h3 in soup.find_all('h3'):
        c = c + 1
        if (c > 4 and c < 25):
            link = h3.a
            url_end = link.get('href')
            ids = url_end[9:]
            print(ids)
            desc = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + ids + "&fields=items/snippet/title,items/snippet/channelId,items/snippet/description&key=AIzaSyCdkj_kXilFk4KH3zFn8a6SAEwAxsSx3tw"
            r = requests.get(desc)
            obj = r.json()
            descr = obj["items"][0]["snippet"]["description"]
            nam = obj["items"][0]["snippet"]["title"]
            channelId = str(obj["items"][0]["snippet"]["channelId"])
            sums = nam + " " + descr

            if ("cover" not in sums.lower() and "acoustic" not in sums.lower() and "lyric" in sums.lower() and channelId not in spam):
                if (similar(t, nam) == 1):
                    testurl = "https://mp3skull.onl/api/youtube/frame/#/?id=" + ids
                    return redirect(testurl)


if (__name__ == '__main__'):
    app.run(debug=True)
