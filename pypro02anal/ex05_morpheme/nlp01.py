# 한글 형태소 분석 
# 형태소 : 의미를 가지는 요소로서는 더 이상 분석할 수 없는 가장 작은 말의 단위. / 문법적·관계적인 뜻만을 나타내는 단어 또는 단어의 부분.
# 한글 형태소 분석 도구로 KoNLpy
from konlpy.tag import Kkma, Okt, Komoran

kkma = Kkma()
print(kkma.sentences('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 입력 문장을 문장 단위로 분리합니다.
print(kkma.pos('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장을 형태소로 분석하고, 각 형태소의 품사를 태깅합니다.
print(kkma.nouns('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다.야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장에서 명사 형태소만 추출합니다.
print(kkma.morphs('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장을 형태소로 분석하고, 형태소 단위로 분리합니다.

print()
okt = Okt()
print(okt.phrases('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 입력 문장에서 어구(구)를 추출합니다.
print(okt.pos('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장을 형태소로 분석하고, 각 형태소의 품사를 태깅합니다.
print(okt.pos('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.',stem=True))
# 형태소 분석 시 어간 추출을 수행합니다. (원형으로)
print(okt.nouns('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다.야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장에서 명사 형태소만 추출합니다.
print(okt.morphs('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장을 형태소로 분석하고, 형태소 단위로 분리합니다.

print()
ko = Komoran()
print(ko.pos('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.')) 
#  문장을 형태소로 분석하고, 각 형태소의 품사를 태깅합니다.
print(ko.nouns('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다.야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.')) 
# 문장에서 명사 형태소만 추출합니다.
print(okt.morphs('랩틸리언은 대중매체에 의해 잘 알려진 이미지의 파충류형 외계인이다. 야훼라는 인간형 외계인과 대립관계라는 이야기가 있다.'))
# 문장을 형태소로 분석하고, 형태소 단위로 분리합니다.
