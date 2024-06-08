# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도
import urllib.request

def unique(list):
    x = np.array(list)
    return np.unique(x)

# URL에서 폰트 파일을 다운로드하고 저장하는 함수
def download_font(url, save_path):
    if not os.path.exists(save_path):
        try:
            urllib.request.urlretrieve(url, save_path)
            st.write(f"Font downloaded and saved to {save_path}")
        except Exception as e:
            st.error(f"Failed to download font: {e}")
    else:
        st.write(f"Font already exists at {save_path}")

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
    
    # 폰트가 제대로 로드되고 설정되었는지 확인
    st.write(f"로딩된 폰트: {font_name}")

    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)

    st.dataframe(tips)

if __name__ == "__main__":
    main()
