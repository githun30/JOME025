import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 파일의 정확한 로컬 경로 지정
font_path = 'C:/Users/KMGHO/Downloads/NanumGothic.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

# matplotlib의 기본 폰트 설정
plt.rcParams['font.family'] = font_prop.get_name()

# 테스트 그래프 생성
plt.figure()
plt.title('테스트 그래프', fontproperties=font_prop)
plt.plot([1, 2, 3], [4, 5, 6])
