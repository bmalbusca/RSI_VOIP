import requests as req
import json
#import agi
import sys
from lxml import html

#agi = AGI()
code1=str(sys.argv[1]) 
code2=str(sys.argv[2])
print(code1, code2)

url = "https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4="+code1+"&cp3="+code2+"&method:searchPC2=Procurar"

#url2 =  "https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4=1000&cp3=048&method:searchPC2=Procurar"

page = req.post(url)
tree = html.fromstring(page.content)
info1 = tree.xpath('//h4[@class="subheader"]/text()')
info2 = tree.xpath('//h3[@class="subheader"]/text()')


string = "" 
for a in info1:
    string += a + " "
for a in info2:
    string += a + " "


print("string",len(string),string)
#agi.set_variable("STRING", string)
