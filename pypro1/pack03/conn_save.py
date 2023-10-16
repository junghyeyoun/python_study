# db 연결 정보(dict로 구성) 객체를 파일로 저장

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306, # 안쓰면 기본값 3306
    'charset':'utf8',
    'use_unicode':True
}

import pickle

with open(r'mydb.dat',mode='wb') as obj:
    pickle.dump(config, obj)
    
