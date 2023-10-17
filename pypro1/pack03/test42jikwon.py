# 키보드로 부서번호를 입력받아, 해당 부서의 자료 출력
import MySQLdb
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
'''
# db 연결정보 별도의 파일로 작성해 불러오기 => secure coding guide 때문
import pickle
with open(r'mydb.dat',mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        print(conn)
        cursor = conn.cursor()
        
        buser_no = input('부서번호 입력 : ')
        #buser_no = '10'
        sql = """
        select jikwon_no,jikwon_name,buser_num,jikwon_pay,jikwon_jik from jikwon
        where buser_num = {0}
        """.format(buser_no)
        # print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        #  print(datas)
        print(len(datas))
        
        if len(datas) == 0:
            print(buser_no + ' 번 부서는 없어요')
            return # sys.exit() 도 가능
        for jikwon_no,jikwon_name,buser_num,jikwon_pay,jikwon_jik in datas:
            print(jikwon_no,jikwon_name,buser_num,jikwon_pay,jikwon_jik)
            
        print('인원수 : '+str(len(datas)))
        
    except Exception as e:
        print('err : ',e)
    finally:
        cursor.close()
        conn.close()
if __name__ == '__main__':
    chulbal()