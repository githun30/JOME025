# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도

def unique(list):
    x = np.array(list)
    return np.unique(x)

# 폰트를 로드하고 매트플롯립에서 사용할 수 있도록 설정하는 함수
def load_custom_font(font_path):
    fm.fontManager.addfont(font_path)  # 폰트를 매니저에 추가
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)  # 폰트를 설정
    return font_name

def main():
    # NanumGothic 폰트 경로 지정 (로컬에 존재해야 함)
    font_path = 'C:/Users/KMGHO/Downloads/NanumGothic.ttf'
    
    # 폰트 로드 및 설정
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
if __name__ == "__main__":
    main()
