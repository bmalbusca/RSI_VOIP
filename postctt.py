#!/usr/bin/env python
import requests as req
import json
import sys
from lxml import html
from asterisk.agi import * 

#agi = AGI()
try:
	code1=str(sys.argv[1]) 
	code2=str(sys.argv[2])
	#code1 = ''
	#code2 = ''
	#agi.verbose(code1)

	url = "https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4="+code1+"&cp3="+code2+"&method:searchPC2=Procurar"

	url2 =  "https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4=1000&cp3=048&method:searchPC2=Procurar"

	page = req.post(url2)
	tree = html.fromstring(page.content)
	info1 = tree.xpath('//h4[@class="subheader"]/text()')
	info2 = tree.xpath('//h3[@class="subheader"]/text()')


	string = "A" 
	for a in info1:
    		string += a + " "
	for a in info2:
    		string += a + " "


	#print("SET VARIABLE STRING A" + string)
	#agi.set_variable('STRING', code1)
	sys.stdout.write("SAY NUMBER %s \"\"\n" %'2') 
	sys.stdout.flush()
	sys.stdout.write("SAY NUMBER %s \"\"\n" %'2') 
        sys.stdout.flush()

except:
 	sys.stdout.write("SAY NUMBER %s \"\"\n" %'2') 
        sys.stdout.flush()
        sys.stdout.write("SAY NUMBER %s \"\"\n" %'2') 
        sys.stdout.flush()

	pass

