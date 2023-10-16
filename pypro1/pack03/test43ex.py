# jikwon 테이블을 대상으로 사번과 이릅을 입력(로그인)해 해마다 자료가 있다면
# 해당 직원이 근무하는 부서 직원을 직급별  오름차순으로 모두 출력, 직급이 같으면 이름별 오름차순 출력
# 출력 형태 :  사번, 이름, 부서명, 직급, 성별
#                    5     홍길동   총무부     대리   122
#                   인원수 : * 명
# 다음으로 해당직원이 관리하는 고객자료 출력
# 출력 형태 :  고객번호 고객명    고객전화    나이
#                    3       신기해       111-1111  23

import MySQLdb
import pickle

with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        # print(conn)
        cursor = conn.cursor()
        
        sabun = input('사번 입력 : ')
        irum = input('이름 입력 : ')
        # sabun = '1'
        # irum = '홍길동'
        sql = """
        select buser_num from jikwon 
        where jikwon_no={0} and jikwon_name = '{1}'
        """.format(sabun, irum)
        # print(sql)
        cursor.execute(sql)
        buser_data = cursor.fetchall()
        # print(buser_data)
        # print(len(buser_data))
        
        if len(buser_data) == 0:
            print(irum +'과'  +sabun+' 정보를 가진 고객은 없습니다.')
            return
        
        buser_num = buser_data[0][0]
        sql = """
        SELECT jikwon_no, jikwon_name, jikwon_jik, jikwon_gen
        FROM jikwon
        WHERE buser_num = {0}
        ORDER BY jikwon_jik ASC, jikwon_name ASC
        """.format(buser_num)
        #print(sql)
        cursor.execute(sql)
        jikwon_datas = cursor.fetchall()
        # print(jikwon_datas) 
        # print(len(jikwon_datas))
        print('직원자료')
        print('사번, 이름, 부서명, 직급, 성별')
        if len(jikwon_datas) == 0:
            print('해당 부서의 직원 자료는 없습니다.')
            return
        for (jikwon_no, jikwon_name, jikwon_jik, jikwon_gen) in jikwon_datas:
            print(jikwon_no, jikwon_name, jikwon_jik, jikwon_gen)
            
        print('인원수 : ' +str(len(jikwon_datas)))
        
        if len(buser_data) == 0:
            print(irum + '님의 부서직원 자료가 없습니다.')
            return
        
        sql = """
        SELECT gogek_no, gogek_name, gogek_tel,
        CONCAT(YEAR(CURDATE()) - CAST(CONCAT('19', SUBSTRING(gogek_jumin, 1, 2)) AS SIGNED), '세') AS age
        FROM gogek
        WHERE gogek_damsano = {0}
        """.format(sabun)
        # print(sql)
        cursor.execute(sql)
        gogek_datas = cursor.fetchall()
        # print(gogek_datas)
        # print(len(gogek_datas))
        print()
        print('고객자료')
        print('고객번호, 고객명, 고객전화, 나이')
        if len(gogek_datas) == 0:
            print('담당 고객자료가 없습니다.')
            return
        for (gogek_no, gogek_name, gogek_tel, gogek_jumin) in gogek_datas:
            print(gogek_no, gogek_name, gogek_tel, gogek_jumin)
            
        print('인원수 : '+str(len(gogek_datas)))
        
    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    chulbal()

