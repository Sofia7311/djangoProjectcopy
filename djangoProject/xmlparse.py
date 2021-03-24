import xml.etree.ElementTree as ET
mytree = ET.parse('../tradexml1.xml')
myroot = mytree.getroot()

node = myroot.findall(".//Annual/")

for x in node:
    for y in x.attrib:
        if y == 'expectDate':
            print(x.get(y))



