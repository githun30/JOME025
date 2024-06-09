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
from tqdm import trange

# URL에서 폰트 파일을 다운로드하고 저장하는 함수
def download_font(url, save_path):
    if not os.path.exists(save_path):
        try:
            urllib.request.urlretrieve(url, save_path)
            st.write(f"Font downloaded and saved to {save_path}")
        except Exception as e:
            st.error(f"Failed to download font: {e}")

# 폰트를 로드하고 매트플롯립에서 사용할 수 있도록 설정하는 함수
def load_custom_font(font_path):
    fm.fontManager.addfont(font_path)  # 폰트를 매니저에 추가
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)  # 폰트를 설정
    return font_name

def main():
    # NanumGothic 폰트 URL 및 로컬 저장 경로 지정
    font_url = 'https://github.com/githun30/JOME025/raw/main/NanumGothic.ttf'  # URL에서 직접 raw 파일을 가져와야 함
    font_path = 'NanumGothic.ttf'
    
    # 폰트 다운로드 및 로드
    download_font(font_url, font_path)
    font_name = load_custom_font(font_path)
    
# tqdm의 기본 모드 사용
tqdm.pandas() 

# main 함수 호출
if __name__ == "__main__":
    main()

# tqdm의 기본 모드 사용
tqdm.pandas() 

st.header("언론중재법 개정안에 대한 공동발의 연결망 분석 및 언론보도 분석")
st.subheader(' - 컴퓨테이셔널저널리즘(JOME025) 기말 프로젝트👨‍💻')

st.write('### 1️⃣ "언론중재법 개정안"이란❔')
from PIL import Image

st.image('https://raw.githubusercontent.com/githun30/JOME025/main/PCM20210901000411990_P4.jpg', width=300)
st.text('출처: 연합뉴스')

st.write('''###### - "언론중재 및 피해구제 등에 관한 법률(약칭: 언론중재법)"
제1조(목적) 언론사 등의 언론보도 또는 그 매개(媒介)로 인하여
    침해되는 명예 또는 권리나 그 밖의 법익(法益)에 관한 다툼이 있는 경우
    이를 조정하고 중재하는 등의 실효성 있는 구제제도를 확립함으로써
    언론의 자유와 공적(公的) 책임을 조화함을 목적으로 함.
         ''')

st.write('''###### - 추진배경  
 - "받아쓰기"식 보도에서 비롯된 2014년 세월호 '오보' 참사  
 - 추락하는 언론에 대한 신뢰도와 위상
 - 공정한 언론 생태계 조성을 위한 언론 개혁 필요  
         ''')

st.write('''###### 👉 언론으로 인한 다툼과 피해를 최소화시키며, 언론의 자유와 책임의 조화를 위한 법률.''') 

# GitHub의 원본 URL에서 원시 파일 URL로 변경
url = "https://github.com/githun30/JOME025/raw/d39d96b230859f9e45b37c77447de9da071b3b00/2023%EB%85%84%20%EC%A1%B0%EC%A0%95%EC%A4%91%EC%9E%AC%EC%B2%98%EB%A6%AC%ED%98%84%ED%99%A9(1981%EB%85%84~2023%EB%85%84).xlsx"

# URL에서 파일을 다운로드
response = requests.get(url)
file_data = BytesIO(response.content)
df2 = pd.read_excel(file_data, engine='openpyxl')

# Use iloc to select B8:C50 (row 7 to 49 and column 1 to 2)
df2_selected = df2.iloc[6:49, 1:3]

# Set the column names for better understanding
df2_selected.columns = ['Year', 'Value']

df2_selected['Year'] = pd.to_numeric(df2_selected['Year'], errors='coerce')
df2_selected['Value'] = pd.to_numeric(df2_selected['Value'], errors='coerce')

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df2_selected['Year'], df2_selected['Value'], marker='o', linestyle='-')
plt.title('연도별 조정청구 건수')
plt.xlabel('연도')
plt.ylabel('조정청구 건수')
plt.grid(True)
st.pyplot(plt)
st.text('출처: 언론중재위원회')

st.write('''###### 👉 언론보도에 대한 조정 신청은 2014년 세월호 이슈로 인해 최대치 기록했으며, 이후로도 전반적인 우상향 형태로 증가하는 추세를 보이고 있다.''')
st.write('''###### 👉 시민이 언론조정 등의 분쟁이 발생하게 되면 피해가 막심하므로 언론은 사회적 책임을 갖고 이를 최소화할 의무가 있다.''')
st.write("")
st.write("")

st.write('''###### - 주요내용과 쟁점  
 - 언론의 고의·중과실(취재 과정에서 법률을 위반한 경우 등)로 인한 허위·조작 보도로 피해를 입는 경우 최대 5배까지 징벌적 손해배상 가능  
 - 기사 열람 차단 청구권 도입  
 - 정정보도 청구 기간, 방식 확대  
         ''')

st.image('https://raw.githubusercontent.com/githun30/JOME025/main/%EC%96%B8%EB%A1%A0%EC%A4%91%EC%9E%AC%EB%B2%95%20%EA%B0%9C%EC%A0%95%EC%95%88%20%EC%A3%BC%EC%9A%94%20%EB%82%B4%EC%9A%A9%EA%B3%BC%20%EB%AC%B8%EC%A0%9C%EC%A0%90(%EC%A4%91%EC%95%99%EC%9D%BC%EB%B3%B4).jpg', width=300)
st.text('출처: 중앙일보')
st.write('''###### 👉 개정안은 피해구제를 목적으로 하는 법률 목적에 따라, 피해 최소화(열람 차단 청구권), 손해배상액에 초점이 맞춰져 있다(이혜리, 2021).''')
st.write('''###### 👉 그러나 성추문, 비리범죄와 같은 사회고발적 문제에 대한 언론의 취재와 보도를 제한할 수 있다는 우려 제기되기도 했다(유성운, 2011).''')
st.write("")

st.write('''###### - 전개내용 
 - 언론의 고의·중과실(취재 과정에서 법률을 위반한 경우 등)로 인한 허위·조작 보도로 피해를 입는 경우 최대 5배까지 징벌적 손해배상 가능  
 - 기사 열람 차단 청구권 도입  
 - 정정보도 청구 기간, 방식 확대  
         ''')
st.image('https://raw.githubusercontent.com/githun30/JOME025/main/%EC%96%B8%EB%A1%A0%EC%A4%91%EC%9E%AC%EB%B2%95%20%EC%B2%98%EB%A6%AC%20%EC%A3%BC%EC%9A%94%EC%9D%BC%EC%A7%80.jpg', width=300)
st.text('출처: 연합뉴스')

st.write('''###### 👉 2021년 7월 27일부터 2021년 9월 29일까지의 약 2개월 동안 법안 처리를 둘러싼 갈등과 파행 속 최종 본회의 상정 무산(법안 폐기)되었다.''')
st.write('''###### 👉 언론미디어 특별위원회(언론특위)가 구성되었으나, 국정감사 및 20대 대통령 선거 등의 이슈로 유의미한 결과를 내지는 못했다(강한들, 2021; 정철운, 2022).''')
st.write("")

st.write('### 2️⃣ 공동발의안 연결망 분석')


# Raw URL로 업데이트
url2 = 'https://raw.githubusercontent.com/githun30/JOME025/0897f079417d359a05577649ac1125d3f911cd6b/21%EB%8C%80%20%EA%B5%AD%ED%9A%8C%EC%9D%98%EC%9B%90%20%EB%AA%85%EB%8B%A8.xlsx'
url3 = 'https://raw.githubusercontent.com/githun30/JOME025/0897f079417d359a05577649ac1125d3f911cd6b/21%EB%8C%80%20%EA%B5%AD%ED%9A%8C%20%EB%B0%9C%EC%9D%98%EB%B2%95%EB%A5%A0%EC%95%88.xlsx'

response = requests.get(url2)
member_file_data = BytesIO(response.content)

response = requests.get(url3)
law_file_data = BytesIO(response.content)

members_df = pd.read_excel(member_file_data)
print(members_df.head())

laws_df = pd.read_excel(law_file_data)
print(laws_df.head())

# 특정 법률안 필터링 ("언론중재 및 피해구제 등에 관한 법률 일부개정법률안")
law_name = "언론중재 및 피해구제 등에 관한 법률 일부개정법률안"
law_df = laws_df[laws_df['법률안명'].str.contains(law_name)]
print(law_df.head())

# 정당별 색상 딕셔너리 생성
party_colors = {
    '더불어민주당': 'blue',
    '더불어민주연합': 'blue',
    '국민의힘': 'red',
    '자유통일당': 'pink',
    '개혁신당': 'orange',
    '녹색정의당': 'green',
    '무소속': 'gray',
    '새로운미래': 'cyan',
    '새진보연합': 'lightgreen',
    '조국혁신당': 'navy',
    '진보당': 'black'
}

# 국회의원 이름과 정당을 매핑하는 딕셔너리 생성
member_party = dict(zip(members_df['의원명'], members_df['정당']))

# 관련된 컬럼 추출 (대표발의자와 공동발의자)
proposer_column = '대표발의자'
cosponsors_column = '공동발의자'

# 네트워크 그래프 생성
G = nx.Graph()

# 노드와 엣지를 그래프에 추가
node_counts = {}
proposers = set()

for index, row in law_df.iterrows():
    proposer = row[proposer_column].strip()
    proposers.add(proposer)
    cosponsors = [cosponsor.strip() for cosponsor in row[cosponsors_column].split(',')]  # 공동발의자가 콤마로 구분된 문자열이라 가정
    
    # 등장 횟수 계산
    if proposer in node_counts:
        node_counts[proposer] += 1
    else:
        node_counts[proposer] = 1
        
    G.add_node(proposer, shape='s', party=member_party.get(proposer, '무소속'))  # 대표발의자는 사각형으로 표시
    
    for cosponsor in cosponsors:
        if cosponsor in node_counts:
            node_counts[cosponsor] += 1
        else:
            node_counts[cosponsor] = 1
            
        G.add_node(cosponsor, shape='o', party=member_party.get(cosponsor, '무소속'))  # 공동발의자는 원형으로 표시
        G.add_edge(proposer, cosponsor)

# 등장 횟수에 따른 노드 크기 정의
node_sizes = [node_counts[node] * 5000 for node in G.nodes]

# 대표발의자와 공동발의자를 다른 모양으로 구분
pos = nx.spring_layout(G, seed=42)  # 일관된 레이아웃을 위해 시드 값 설정
node_shapes = set((aShape[1]["shape"] for aShape in G.nodes(data=True)))

plt.figure(figsize=(20, 14))  # 그림 크기 확대
for shape in node_shapes:
    shaped_nodes = [sNode[0] for sNode in G.nodes(data=True) if sNode[1]["shape"] == shape]
    shaped_sizes = [node_counts[node] * 350 for node in shaped_nodes]
    shaped_colors = np.array([party_colors[G.nodes[node]["party"]] for node in shaped_nodes])
    nx.draw_networkx_nodes(G, pos,
                           node_shape=shape,
                           nodelist=shaped_nodes,
                           node_size=shaped_sizes,
                           node_color=shaped_colors)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='NanumGothic', font_weight='bold')  # 폰트 크기 확대

plt.title('대표발의자 및 공동발의자의 네트워크', fontsize=15)

# 정당별 색상 테이블 추가
ax = plt.gca()  # 현재 그래프의 축을 가져옴

# 정당별 색상 설명 테이블을 그리기 위해 텍스트 위치 설정
y_offset = 1.1  # 그래프 상단 위의 여백 설정
x_pos = 1.05  # 그래프 오른쪽 여백 설정

# 정당별 색상 정보를 추가
for i, (party, color) in enumerate(party_colors.items()):
    plt.text(x_pos, y_offset - i * 0.05, f'{party}: {color}', fontsize=12, color=color, transform=ax.transAxes)
st.pyplot(plt)



# 네트워크 중심성 계산
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Find the top 3 members for each centrality measure
def get_top_3_with_party(centrality):
    top_3 = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:3]
    return [(member, value, member_party.get(member, '무소속')) for member, value in top_3]

top_3_degree_centrality = get_top_3_with_party(degree_centrality)
top_3_betweenness_centrality = get_top_3_with_party(betweenness_centrality)
top_3_closeness_centrality = get_top_3_with_party(closeness_centrality)
top_3_eigenvector_centrality = get_top_3_with_party(eigenvector_centrality)

# Display metrics and members in Streamlit
st.write("Top 3 Degree Centrality:")
for member, value, party in top_3_degree_centrality:
    st.write(f"{member} ({party}): {value}")

st.write("Top 3 Betweenness Centrality:")
for member, value, party in top_3_betweenness_centrality:
    st.write(f"{member} ({party}): {value}")

st.write("Top 3 Closeness Centrality:")
for member, value, party in top_3_closeness_centrality:
    st.write(f"{member} ({party}): {value}")

st.write("Top 3 Eigenvector Centrality:")
for member, value, party in top_3_eigenvector_centrality:
    st.write(f"{member} ({party}): {value}")

st.write('''###### 👉 법률안 개정 공동발의 연결망은 진보정당(더불어민주당, 조국혁신당, 새로운미래 등)와 보수정당(국민의힘, 자유통일당 등)으로 분리되어 있었다.''')
st.write('''###### 👉 당시 기자 출신 김영호 의원(더불어민주당, 재선)이 4개의 중심성 지수 모두에서 가장 높게 나타났다.''')


st.write("")

st.write('### 3️⃣ 언론보도 분석')

st.write('##### 🎤 분석대상: "언론중재법" 포함 뉴스')
st.write('##### 📅 분석기간: 2020년 5월 30일 ~ 2024년 5월 29일(21대 국회의원 임기)')
st.write('##### 📰 분석매체: 조선일보, 중앙일보, 동아일보, 한겨레, 경향신문') 
st.write('##### 💻 분석방법: BIGKinds 뉴스 수집 - 빈도분석 및 워드클라우드')
st.write('######  📍 불용어: 언론, 중재, 언론중재, 언론중재법, 중재법, 이날, 개정안')
st.write('######  📍 동의어: 민주당(더불어민주당), 의회(국회)')

st.write("")

st.write('##### ■ 보도에서 가장 많이 등장한 상위 30명')

url = "https://raw.githubusercontent.com/githun30/JOME025/66f3da66ecf08320aaeb9f3a8a7ce72591d79625/%EC%96%B8%EB%A1%A0%EC%A4%91%EC%9E%AC%EB%B2%95%20%EB%B3%B4%EB%8F%84.xlsx"

# requests를 사용하여 데이터를 받아온다
response = requests.get(url)
data = BytesIO(response.content)

# pandas로 Excel 파일 읽기
df = pd.read_excel(data)

df = df[['일자', '인물', '키워드']]

df.columns = ['date', 'person', 'token']
df['person'] = df['person'].str.split(",").tolist()

col1, col2 = st.columns(2)

with col1:

    try:
        # URL에서 파일을 다운로드
        response = requests.get(url)
        response.raise_for_status()  # 요청에 실패할 경우 예외 발생

        # 엑셀 파일을 판다스 데이터프레임으로 읽기
        df = pd.read_excel(BytesIO(response.content))

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

            # 상위 30명의 인물 데이터프레임으로 변환
            if top_30_person_list:
                key_person_df = pd.DataFrame(top_30_person_list, columns=['person', 'count'])
                key_person_df.index = list(range(1, len(key_person_df) + 1))

                st.dataframe(key_person_df)
            else:
                st.write("상위 30명의 인물을 추출할 수 없습니다. 필터링된 인물 리스트가 비어 있습니다.")
        else:
            st.write("데이터에 '일자', '인물', '키워드' 열이 없습니다.")
    except Exception as e:
        st.write(f"오류가 발생했습니다: {e}")

top_token = []

# stqdm 사용하여 진행 상황 표시
for i in stqdm(range(len(df)), desc="Processing tokens"):
    try:
        tokenloc = df['token'].iloc[i]
        top_token += tokenloc  # 토큰 리스트에 추가
    except Exception as e:
        st.error(f"Error at row {i}: {e}")

with col2:
    st.write("""
            👉 보도에서 자주 등장한 인물 30명을 추출한 결과, 전현직 대통령(노무현,이명박,박근혜,문재인,윤석열)/국회의장(박병석)/여야 원내대표(윤호중,김기현) 등을 확인 가능했다.  
            반면, 앞서 살펴본 법률안 공동발의에 대한 각 연결망 지수(연결, 사이, 인접, 아이겐벡터)에서 높은 값을 기록한 의원들은 상위 30명에 들지 못했다.  
            이 분석을 통해 언론보도가 실제 법률 발의보다 법률안을 둘러싼 관계인들을 다루는 데 초점이 맞춰져 있음을 알 수 있었다.
        """)
    
st.write("")

st.write('##### ■ 보도 추이')
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 일자 기준 처리
date_counts = df['date'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(date_counts.index, date_counts.values, marker='o', linestyle='-', color='b')
ax.set_title('일자별 기사 수 추이')
ax.set_xlabel('일자')
ax.set_ylabel('기사 수')
plt.xticks(rotation=45)
plt.grid(True)

st.pyplot(fig)

st.write('''###### 👉 언론보도는 2021년 7월부터 9월까지의 기간에 집중되었다.''')  
st.write('''###### 👉 개정안 처리와 관련한 주요 시기에만 언론보도의 대상이 되었음을 확인할 수 있었다(언론중재법 처리 주요 일지 참조)''')
st.write("")


# 데이터 불러오기
url = "https://raw.githubusercontent.com/githun30/JOME025/66f3da66ecf08320aaeb9f3a8a7ce72591d79625/%EC%96%B8%EB%A1%A0%EC%A4%91%EC%9E%AC%EB%B2%95%20%EB%B3%B4%EB%8F%84.xlsx"
response = requests.get(url)
data = BytesIO(response.content)

# pandas로 Excel 파일 읽기
df = pd.read_excel(data)

# 필요한 컬럼 선택 및 이름 변경
df = df[['일자', '언론사', '키워드']]
df.columns = ['date', 'press', 'token']

# 'token' 컬럼을 리스트로 변환
df['token'] = df['token'].str.split(",").tolist()

# 불용어 및 동의어 설정
stopwords = set(['언론', '언론중재법', '중재', '언론중재', '중재법', '이날', '개정안'])
synonyms = {
    '더불어민주당': '민주당',
    '의회': '국회'
}

# 동의어 대체 및 불용어 제거 함수
def replace_synonyms(tokens, synonyms, stopwords=set()):
    if not isinstance(tokens, list):
        print(f"tokens의 데이터 타입이 예상과 다릅니다: {type(tokens)}. 리스트가 필요합니다.")
        return tokens  # 또는 빈 리스트 반환 등의 처리
    return [synonyms.get(word.strip(), word.strip()) for word in tokens if word.strip().lower() not in stopwords]

# 데이터 유형 확인
print(df['token'].apply(type).value_counts())

# 동의어 및 불용어 처리
df['token'] = df['token'].apply(lambda tokens: replace_synonyms(tokens, synonyms, stopwords) if isinstance(tokens, list) else tokens)

# 토큰 리스트에서 불용어 제거
df['token'] = df['token'].apply(lambda tokens: [word for word in tokens if word.lower() not in stopwords])

# 키워드 빈도 수집
top_token = []
for i in trange(len(df)):
    try:
        tokenloc = df['token'].iloc[i]
        top_token += tokenloc
    except Exception as e:
        print(f"Error processing row {i}: {e}")

# Streamlit 앱에서 결과 출력
st.write('##### ■ 키워드 빈도분석')

col1, col2 = st.columns(2)

with col1:
    top_keyword = Counter(top_token)
    key_df = pd.DataFrame(top_keyword.most_common(50))
    key_df.columns = ['keyword', 'count']
    key_df.index = list(range(1, len(key_df)+1))
    st.write(key_df)

# "token" 리스트를 문자열로 변환하여 결합
df['token_string'] = df['token'].apply(lambda x: " ".join(x))

# 'token_string' 열을 공백으로 연결하여 하나의 문자열로 만들기
text = ' '.join(df['token_string'])

with col2:
    st.write("""
         👉 언론보도에 등장한 상위 50개 단어는 다음과 같이 분류할 수 있다.  
            - 정치 관련: '민주당(6,610건)', '의원(4,645건)', '처리(3,375건)', '대선(1,205건)'  
            - 법률안 관련: '징벌(1,914건)', '손해(1,803건)', '배상(1,747건)'  
            - 언론 관련: '자유(2,537건)', '허위(1,168건)'  
    👉 '비판(2,120건)', '반대(1,071건)', '지적(1,053건)' 등의 단어로 언론은 전반적으로 부정적인 입장을 보도했음을 짐작할 수 있다. 
    """)

st.write("")


st.write('##### ■ 5대 신문사 보도 워드클라우드')
# 워드클라우드 생성
# 한글 폰트를 사용하여 워드클라우드 생성
wordcloud = WordCloud(
    font_path = 'NanumGothic.ttf',  # 한글 폰트 경로 지정
    width=1000,
    height=500,
    background_color='white',
    colormap='viridis',
    random_state=42,
).generate(text)
    
# 워드클라우드를 numpy 배열로 변환하여 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud.to_array(), interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)
    
st.write("")

st.write('### 4️⃣ 결론과 함의점')
st.write('''###### 👉 언론보도는 McCombs & Shaw(1972)가 제시한 언론의 의제설정기능(Agenda-setting)에 따르면, 수용자는 언론이 주요하게 보도하는 이슈를 중요하게 생각한다.  
                    언론에게 "언론중재법"은 "언론재갈법"이 될 수도 있는 주요한 의제이나, 관련 보도가 해당 법률이 쟁점화된 시점에만 보도되었다는 것은 바람직해보이지 않다.  
                    시민의 알권리와 언론의 자유를 함께 보호하기 위해서는 언론 스스로가 나서서 해당 법률에 대한 정보와 개정의 필요성을 선제적으로 보도할 필요가 있다.''')  

st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
    }
    .image-container img {
        height: 200px;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="image-container"><img src="https://raw.githubusercontent.com/githun30/JOME025/main/%EB%B0%A9%ED%86%B5%EC%9C%84%20mbc.jpg" alt="MBC"></div>',
        unsafe_allow_html=True
    )
    st.text('출처: MBC')

with col2:
    st.markdown(
        '<div class="image-container"><img src="https://raw.githubusercontent.com/githun30/JOME025/main/%EC%9E%85%ED%8B%80%EB%A7%89.jpg" alt="미디어오늘"></div>',
        unsafe_allow_html=True
    )
    st.text('출처: 쿠팡플레이')

st.write('''###### 👉 언론보도는 McCombs & Shaw(1972)가 제시한 언론의 의제설정기능(Agenda-setting)에 따르면, 수용자는 언론이 주요하게 보도하는 이슈를 중요하게 생각한다.  
                    언론에게 "언론중재법"은 "언론재갈법"이 될 수도 있는 주요한 의제이나, 관련 보도가 해당 법률이 쟁점화된 시점에만 보도되었다는 것은 바람직해보이지 않다.  
                    시민의 알권리와 언론의 자유를 함께 보호하기 위해서는 언론 스스로가 나서서 해당 법률에 대한 정보와 개정의 필요성을 선제적으로 보도할 필요가 있다.''')  


st.image('https://raw.githubusercontent.com/githun30/JOME025/main/%EC%96%B8%EB%A1%A0%EC%9E%90%EC%9C%A0%EC%A7%80%EC%88%98%20%EC%88%9C%EC%9C%84.jpg')
st.text('출처: 미디어오늘')


st.write('''###### - 참고자료
강한들. (2021). 언론단체 “한 달 넘게 출범 못한 언론특위…국회 약속은 결국 빈말”, 경향신문, 2021년 11월 3일, https://www.khan.co.kr/national/media/article/202111032116025  
        김세영. (2024). 방심위, '바이든-날리면' MBC에 '최고 수위' 과징금‥YTN에는 '관계자 징계', MBC, 2024년 2월 20일, https://imnews.imbc.com/news/2024/econo/article/6572878_36452.html  
        유성은. (2021). 대통령도 퇴임 뒤엔 손배 청구 가능, 의혹 보도 족쇄 우려, 중앙일보, 2021년 8월 27일, https://www.joongang.co.kr/article/25001925  
        이은미. (2021). 진용 갖춘 8인 협의체…언론중재법 '18일의 전쟁' 돌입, 연합뉴스, 2021년 9월 7일, https://www.yna.co.kr/view/AKR20210907140000001  
        이혜리. (2021). 가짜뉴스 '피해 구제'?··· 언론중재법, 누구를 위한 법이냐, 경향신문, 2021년 8월 25일, https://www.khan.co.kr/national/media/article/202108251737001  
        서영민. (2021). 급변하는 언론 환경…유튜브 등 1인 미디어는 어떻게?, KBS, 2021년 9월 18일, https://news.kbs.co.kr/news/pc/view/view.do?ncd=5283438  
        정철운. (2022). 입법권 한계 ‘유감’으로 끝난 국회 언론·미디어특위, 미디어오늘, 2022년 5월 24일, https://www.mediatoday.co.kr/news/articleView.html?idxno=304164  
        정철운. (2024). 윤석열 정부 2년 만에… 세계 언론자유지수 62위 ‘추락’, 미디어오늘, 2024년 5월 3일, https://www.mediatoday.co.kr/news/articleView.html?idxno=317777  
         ''')
