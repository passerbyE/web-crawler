import requests as req
import bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
heards = {'cookie': 'over18=1'}
request = req.get(url, headers=heards)
data = bs4.BeautifulSoup(request.text, "html.parser")

title = data.find_all("div", class_="title")
lister = 0
for i in title:
    lister += 1
    print(lister, i.text.strip())

chiose = int(input("輸入你想看的文章編號: "))
print(title[chiose-1].text.strip())
rlOfpage =  "https://www.ptt.cc" + title[chiose-1].a['href']
print(rlOfpage)
保存 = input("是否保存txt\n")

if "是" in 保存 or "y" in 保存:
    requestpage = req.get(rlOfpage, headers=heards)
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
            content += str(element).strip() + "\n"
    
    print(content)
    
    with open(str(title[chiose-1].text.strip()) + ".txt", "w", encoding="utf-8") as file:
        file.write(content)