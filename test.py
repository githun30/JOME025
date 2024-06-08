import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 파일의 정확한 경로 지정
font_path = '/full/path/to/NanumGothic.ttf'

# FontProperties 인스턴스 생성
font_prop = font_manager.FontProperties(fname=font_path)

# matplotlib의 기본 폰트 변경
plt.rcParams['font.family'] = font_prop.get_name()

# 간단한 그래프 그리기
plt.figure()
plt.title('테스트 그래프', fontproperties=font_prop)
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
