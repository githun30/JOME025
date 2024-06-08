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

@st.cache(allow_output_mutation=True, ignore_hash=True)  # 캐시 설정 변경
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_abs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._rebuild()  # 폰트 매니저 재구성

def main():
    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]
    # 'NanumGothic' 폰트를 직접 지정
    fontname = 'NanumGothic'
    plt.rc('font', family=fontname)

    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)

    st.dataframe(tips)

if __name__ == "__main__":
    main()
