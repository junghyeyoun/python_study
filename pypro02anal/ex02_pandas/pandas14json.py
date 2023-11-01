#JSON 문서 읽기 : 서울시 제공 도서관 정보 5개 읽기
import json 
import urllib.request as req 

url = 'https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json'
plainText = req.urlopen(url).read()

jsonData = json.loads(plainText) # json decoding : str -> dict
print(jsonData)
print(type(jsonData)) # <class 'dict'>

libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData) 
name = libData[0].get('LBRRY_NAME')
print(name)

print('\n도서관명\t전화\t주소\n')
datas = []
for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name+'\t'+tel+'\t'+addr)
    imsi=[name,tel,addr]
    datas.append(imsi)
    
import pandas as pd 
df = pd.DataFrame(datas, columns=['이름',' 전화','주소'])