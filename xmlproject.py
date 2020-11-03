import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
total = 0
index = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_784969.xml"
xmldata = urllib.request.urlopen(url, context=ctx).read()
#print(xmldata)

tree = ET.fromstring(xmldata)
counts = tree.findall('.//count')
'''num = counts[0].text
print(type(num))

print(type(counts))
print(type(tree))
for num in counts.findall('comment'):
    print(num.find('count').text)'''

for count in counts:
    #number = count[index].text
    number = count.text
    #print(type(number)
    number = int(number)
    total = total + number
    index = index + 1
print("Sum of all counts in xml is", total)