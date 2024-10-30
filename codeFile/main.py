import requests as req
import bs4


print("等我一下，我找個資料")
url = "https://www.ptt.cc/bbs/Stock/index.html"

stop = True

#抓網站內容
headers = {'cookie': 'over18=1'}
request = req.get(url, headers=headers)

data = bs4.BeautifulSoup(request.text, "html.parser")

moredata = True

print("資料來源: "+ data.title.text)

#找到文章標題
titleforreading = data.find_all("div", class_="title")
lister = 0
for title in titleforreading:
    lister += 1
    print(lister, title.text.strip())
        
while stop:
    chiose = int(input('輸入你想看的文章編號'))
    urlOfpage =  "https://www.ptt.cc" + titleforreading[chiose-1].a['href']
    print("///////////////以下是文章內容//////////////////")
    print("標題: "+titleforreading[chiose-1].text.strip(), "\n")

    #抓取文章內容
    requestpage = req.get(urlOfpage, headers=headers)
    datapage = bs4.BeautifulSoup(requestpage.text, "html.parser")

    # 找到文章內容
    main_content = datapage.find("div", id="main-content")

    # 移除不需要的標籤，但保留 <a> 標籤
    for tag in main_content.find_all(["div", "span"]):
        tag.extract()

    content = ""
    for element in main_content.contents:
        if element.name == "a" and "href" in element.attrs:
            content += element["href"] + "\n"
        else:
            content += str(element).strip()

    print(content)
    ans = input("是否繼續")
    if "是" in ans or "y" in ans:
        stop = True
    else:
        stop = False