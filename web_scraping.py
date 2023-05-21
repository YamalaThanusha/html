import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=iphone+14+plus&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=iphone+14+plus%7CMobiles&requestId=396df035-58df-4fcd-9d46-7d06da95be0e&as-searchtext=iphone%2014")
# print(response)

soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
names=soup.find_all("div",class_="_4rR01T")
name=[]
for i in names[0:18]:
    d=i.get_text()
    name.append(d)
# print(name)    


prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:18]:
    d=i.get_text()
    price.append(d)
# print(price)


ratings=soup.find_all("div",class_="_3LWZlK")
rate=[]
for i in ratings[0:18]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

reviews=soup.find_all("span",class_="_2_R_DZ")
review=[]
for i in reviews[0:18]:
    d=i.get_text()
    review.append(d)
    # print(review)

features=soup.find_all("li",class_="rgWa7D")
feature=[]
for i in features[0:18]:
    d=i.get_text()
    feature.append(d)
    # print(feature)

links=soup.find_all("a",class_="_1fQZEK")
link=[]
for i in links[0:18]:
    d="https://www.flipkart.com"+i["href"]
    link.append(d)
    print(link)

images=soup.find_all("img",class_="_396cs4")
image=[]
for i in images[0:18]:
    d=i["src"]
    image.append(d)
    # print(image)


# print(df)
data={"Names":name,
      "Price":price,
      "Ratings":rate,
      "Features":feature,
      "Reviews":review,
      "Images":image,
      "Links":link
      }
# print(len(name),len(price),len(rate),len(feature),len(review),len(image),len(link))
# print(data)
df = pandas.DataFrame(data)
# print(df)

df.to_csv("Mobiles_data.csv")



































































































