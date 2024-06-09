import streamlit as st
import pandas as pd              # pandas(판다스): 표 형태의 데이터를 다루는 패키지
import networkx as nx
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
from datetime import datetime    # datetime(데이터타임): 날짜와 시간 과년 기능 제공
import numpy as np               # numpy(넘파이): 수치 해석 기능 제공
from collections import Counter  
from stqdm import stqdm
from tqdm import tqdm
from wordcloud import WordCloud
import os
import matplotlib.font_manager as fm
from konlpy.tag import Kkma
from konlpy.tag import Okt
import seaborn as sns 
import urllib.request

# 엑셀 파일이 있는 URL 지정
file_url = "https://raw.githubusercontent.com/githun30/JOME025/66f3da66ecf08320aaeb9f3a8a7ce72591d79625/%EC%96%B8%EB%A1%A0%EC%A4%91%EC%9E%AC%EB%B2%95%20%EB%B3%B4%EB%8F%84.xlsx"

# URL에서 파일을 다운로드
response = requests.get(file_url)
response.raise_for_status()  # 요청에 실패할 경우 예외 발생

# 엑셀 파일을 판다스 데이터프레임으로 읽기
df = pd.read_excel(BytesIO(response.content))

# 원본 데이터 확인
st.write("URL에서 다운로드한 파일의 데이터:")
st.write(df.head())  # 처음 몇 줄 확인

# 데이터 처리
if all(col in df.columns for col in ['일자', '인물', '키워드']):
    df = df[['일자', '인물', '키워드']]
    df.columns = ['date', 'person', 'token']

    df['person'] = df['person'].fillna("").apply(lambda x: x.split(",") if isinstance(x, str) else [])

    # 인물 리스트에서 공백 제거 및 1글자 이하 필터링
    top_person = [person.strip() for sublist in df['person'] if isinstance(sublist, list) 
                  for person in sublist if person.strip() and len(person.strip()) > 1]


    top_30_person = Counter(top_person)
    top_30_person_list = top_30_person.most_common(30)

    # 결과 확인
    st.write("가장 많이 언급된 상위 30명의 인물:")
    st.write(top_30_person_list)

    key_person_df = pd.DataFrame(top_30_person_list, columns=['person', 'count'])
    key_person_df.index = list(range(1, len(key_person_df) + 1))

    st.title("뉴스 기사에서 가장 많이 언급된 상위 30명의 인물")
    st.write("이 테이블은 뉴스 기사 데이터셋에서 가장 많이 언급된 상위 30명의 인물을 보여줍니다.")
    st.dataframe(key_person_df)
else:
    st.write("데이터에 '일자', '인물', '키워드' 열이 없습니다.")
