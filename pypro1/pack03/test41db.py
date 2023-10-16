# 원격 database(mariadb)와 연동
# sangdata 자료 출력
import MySQLdb
'''
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='seoho123', database='test')
print(conn)
conn.close
'''

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306, # 안쓰면 기본값 3306
    'charset':'utf8',
    'use_unicode':True
}
try: 
    conn = MySQLdb.connect(**config) # 원격 DB 연결 객체
    # print(conn)
    cursor = conn.cursor() # SQL문 실행 및 select 결과 기억
    
    # 자료 삭제
    code = '6'
    # sql = "delete from sangdata where code="+code # 비권장 : secure coding 가이드라인에 위배
    
    # 방법1
    # sql = "delete from sangdata where code=%s"
    # count = cursor.execute(sql, code)
    
    # 방법2
    '''
    sql = "delete from sangdata where code ='{0}' ".format(code)
    count = cursor.execute(sql)
    if count != 0:
        print('삭제 성공')
        conn.commit()
    else:
        print('삭제 실패')
     '''
      
    # 자료 수정
    '''
    sql = "update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    sql_data = ('python',12,50000,6)
    result = cursor.execute(sql, sql_data)
    print(result)
    conn.commit()
    '''
    
    # 자료 추가
    # sql = "insert into sangdata values(6,'산상1',5,5000)"
    # cursor.execute(sql)
    '''  
    sql = "insert into sangdata values(%s,%s,%s,%s)"
    # sql_data = (6,'신상1',5,'5000')
    sql_data = 6,'신상1',5,'5000'
    cursor.execute(sql,sql_data)
    conn.commit()
    '''
    # 자료 읽기
    sql = 'select code,sang,su,dan from  sangdata'
    cursor.execute(sql)
    
    # 출력1
    for data in cursor.fetchall():
        print(data)
        print('%s %s %s %s'%data)
    print()
    
    # 출력2
    for r in cursor:
        # print(r)
        print([0],r[1],r[2],r[3])
    print()
    
    # 출력3
    for (code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
    print()
    
    # 출력 3-1
    for a, kbs, su, 단가 in cursor:
        print(a,kbs,su,단가)
    
    
except Exception as err:
    print('에러 : ',err)
  
finally:
    conn.close()