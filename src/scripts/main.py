import requests
from bs4 import BeautifulSoup
url = "https://www.mcxindia.com"

#step1 : get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)


#step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettyfy)

#Step3: HTML TREE Traversal
#commonly used types of objects:
title = soup.title #Get the title of the HTML page
print(type(title))#1. Tag
print(type(title.string))#2. NavigableString
print(type(soup))#3. BeautifulSoup

#4. comment
markup ="<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

#Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

print(soup.find('p'))#get first element in the HTML page
print(soup.find('p')['class'])#get classes of any HTML page

#find all the elements with class m-searchSec
print(soup.find_all("p", class_="m-searchSec"))

#get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())#get all text from the tags/soup

#Get all anchor tags from the page
anchors = soup.find_all('a')
print(anchors)

#.contents - a tag's children are available as a list
#.children - a tag's children are available as a generator
#both will give the same result
applynow = soup.find(id='applynow')
print(applynow)
print(applynow.children)
print(applynow.contents)


#getting the elements from any id present in page
for element in applynow.contents:
    print(element)

#getting the strings present in that id which is present in page
for item in applynow.strings:
     print(item)

#getting the parents of the perticular id in page
for item in applynow.parents:
    print(item.name)

#getting the next and previous siblings of any id in page
print(applynow.next_sibling)    

print(applynow.next_sibling.next_sibling) 

print(applynow.previous_sibling.previous_sibling)


#get all the links on the page:
all_links = set()

for link in anchors:
    href = link.get('href')

    if href is not None and href != '#':
        if href[0] == '/':
            linkText = "https://www.mcxindia.com" + link.get('href')
            all_links.add(linkText)

        elif 'https://' in href or 'http://' in href:
            all_links.add(href)

        elif href[0] != '/' and not ('https://' in href or 'http://' in href):
            linkText = "https://www.mcxindia.com" + '/' + link.get('href')
            all_links.add(linkText)

    
# if link.get('href') != '#' and link.get('href') is not None:
#         linkText = "https://www.mcxindia.com" + link.get('href')
#         all_links.add(linkText)

#Save all the links into a text file
text_file = open("all_links.txt", "w")
for link in all_links:
    print(link)
    text_file.write(link+"\n")
text_file.close()


#Manipulating the elements using css selector

elem1 = soup.select('#applynow')
print(elem1)

elem2 = soup.select('.aspNetHidden')
print(elem2)


