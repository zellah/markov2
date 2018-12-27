import requests, re
from bs4 import BeautifulSoup

samples = []
# most recent thread
for i in range(22):
    result = requests.get("https://forums.somethingawful.com/showthread.php?threadid=3827922&userid=50446&perpage=40&pagenumber=" + str(i+1))
    soup = BeautifulSoup(result.content, "html.parser")
    samples += soup.find_all("td", class_='postbody')
# the goldmined one
for i in range(25):
    result = requests.get("https://forums.somethingawful.com/showthread.php?threadid=3175682&userid=50446&perpage=40&pagenumber=" + str(i+1))
    soup = BeautifulSoup(result.content, "html.parser")
    samples += soup.find_all("td", class_='postbody')
# now i have all the zposts
allPosts = ""
for i in range(len(samples)):
    allPosts += str(samples[i]) + "\n\n"

allPosts = re.sub(r'\<[^)]*\>', '', allPosts)
allPosts = re.sub(r'\{[^)]*\}', '', allPosts)

text_file = open("zaurgPosts.txt", "w")
text_file.write(allPosts)
text_file.close()
