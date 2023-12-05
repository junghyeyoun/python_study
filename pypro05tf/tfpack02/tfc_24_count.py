# -*- coding: utf-8 -*-
"""tfc_24_count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZboywfWX_thpzJ46M8j2u71u_o9K-BuE
"""

# 단어의 빈도수로 자연어 특징 추출
# CountVectorizer : 문서 집합에서 단어 토큰을 생성하고 각 단어의 수를 세어 BOW 인코딩 벡터를 만든다.
# TfidfVectorizer : CountVectorizer와 비슷하지만 TF-IDF 방식으로 단어의 가중치를 조정한 BOW 인코딩 벡터를 만든다.
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# CountVectorizer : 단순한 특징으로 corpus에서 단위별 등장횟수를 카운팅하여 수치벡터(BOW)화 함
# 단위는 임의적, 단어, 글자, 자소, 문서, 문장 ...
content = ['How to format my hard disk','Hard disk format problems']

count_vec = CountVectorizer(analyzer='word', min_df=1)
print(count_vec)

tran = count_vec.fit_transform(raw_documents=content)
print(tran)
print(count_vec.get_feature_names_out())
# ['disk' 'format' 'hard' 'how' 'my' 'problems' 'to']
#    0        1       2     3     4      5        6 -> 사전순으로 인덱싱
print(tran.toarray())
print(content)
# 장점 : 쉽고 빠른 구축, 예상보다 문서의 특징을 잘 나타내어 전통적으로 활용됨
# 단점 : 문맥 의미 반영 문제, 회소 행렬 문제

# TfidfVectorizer : CountVectorizer의 단점을 해결하기 위한 기법
# 특정 문서 내에서 특정 단어의 빈도인 TF(Term Frequency)와 전체 문서 내에서 특정 단어의 빈도인 DF(Document Frequency)의
# 역수를 활용하여 어떠한 단어가 얼마나 중요한지를 나타낸 통계적 수치 -> 비율로 나타냄+

# 문서에서 자주 나오는 단어에 높은 가중치를 주되, 모든 문서에서 자주 나타나는 단어에 대해서는 패널티를 주는 방시긍로 값 부여
tfidf_vec = TfidfVectorizer(analyzer='word', min_df=1)
tran_idf = tfidf_vec.fit_transform(raw_documents=content)
print(tran_idf)
print(tfidf_vec.get_feature_names_out()) # 건수가 아니라 건수(빈도)에 대한 확률값을 출력
print(tran_idf.toarray())