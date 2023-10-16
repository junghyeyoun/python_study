# 우편번호 자료 읽기
# 키보드로 '동 이름'을 입력해, 해당 동 자료들만 모두 읽기

try:
    dongname = input('동 이름을 입력 : ')
    # print(dongname)

    with open('zipcode.txt', mode='r', encoding='utf-8') as obj:
        line = obj.readline()
        # print(line)
        while line:
            lines = line.split(' ')  # 공백을 기준으로 나눠
            # print(lines) ['135-806', '서울', '강남구', '개포1동', '경남아파트', 'NULL\n']
            # str.startwswith(str or tuple) 형식으로 사용하면 되고, 반환값으로는 true or false
            if lines[3].startswith(dongname):
                # print(lines)
                print('[' + lines[0] + ']' + lines[1] + ' ' +
                      lines[1] + ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4])
                # print(f"[{lines[0]}] {lines[1]} {lines[2]} {lines[3]} {lines[4]}")
            line = obj.readline()
except Exception as e:
    print('err : ', e)