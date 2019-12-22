#!/usr/bin/python
import requests as req
import json
import sys
from lxml import html
from asterisk.agi import * #you need to install pyst2 

#agi = AGI() #pyst2

def set_var(name_var, value):    
    sys.stdout.write("SET VARIABLE %s %s \"\"\n" %(name_var,value)) 
    sys.stdout.flush()
    sys.stdout.write("SET VARIABLE %s %s \"\"\n" %(name_var,value)) 
    sys.stdout.flush()
    pass 





asterisk_env = {}
code1=""
code2=""



try:
    code1=str(sys.argv[1]) 
    code2=str(sys.argv[2])

except: 
    
    while True:
        line = sys.stdin.readline().strip()         
        if not len(line):
            break
        try:
            var_name,var_value = line.split(':',1)
            asterisk_env[var_name] = var_value 
        except:
            pass 

    try: 
        code1 = str(asterisk_env["num1"])
        code2 = str(asterisk_env["num2"])
    except:
        pass 



try:

    try: #pyst2
        #code1 = agi.get_variable('num1')
        #code2 = agi.get_variable('num2')
        pass 
    except:
        pass
    
    url = "https://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4="+code1+"&cp3="+code2+"&method:searchPC2=Procurar"
    page = req.post(url)
    tree = html.fromstring(page.content)
    info1 = tree.xpath('//h4[@class="subheader"]/text()')
    info2 = tree.xpath('//h3[@class="subheader"]/text()')

    # concatenation 
    string = "" 
    for a in info1:
        string += a + " "
    for a in info2:
        string += a + " "



    #agi.set_variable('str', string) #pyst2
    set_var('str', string)

except:
    pass


