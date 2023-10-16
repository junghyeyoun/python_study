# test40su.txt 파일을 한 행씩 읽어 각 행의 숫자의 합을 출력
try:
    with open(r'test40su.txt',mode='r', encoding='utf-8' ) as obj:
        line = obj.readline()

        while line:
            # lines = line.split('\t')
            result = [float(i) for i in line.split()]
            result = sum(result)
            print(result)
            line = obj.readline()
except Exception as e:
    print(e)