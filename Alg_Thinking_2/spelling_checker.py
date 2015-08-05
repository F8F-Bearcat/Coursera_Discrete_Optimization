import requests

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
url = 'http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt'
my_headers = {'User-Agent': ua,'Accept-Language':'en-US,en;q=0.8','Referer':'https://www.google.com','Connection':'keep-alive','Accept': '*.*', 'Accept-Encoding':'gzip, deflate, sdch'}

r = requests.get( url, headers=my_headers)

word_dict = {}
for line in r.iter_lines():
    #if line: print line
    key = len(line)
    if key in word_dict:
        old = word_dict[key]
        old = old | set([line])
        word_dict[key] = old
    else:
        word_dict[key] = set([line])

word_list = []
for item in word_dict:
    word_list.append([item, len(word_dict[item])])

word_list.sort()
print word_list


