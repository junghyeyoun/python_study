# Singer type의 객체 생성
class Singer:
    title_song = '아리랑'  # 멤버 변수 (public)
    
    def sing(self):
        msg = '노래는 '
        print(msg, self.title_song)
        
    