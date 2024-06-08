import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 파일의 정확한 경로 지정
font_path = 'https://github.com/githun30/JOME025/blob/main/NanumGothic.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

# 로드된 폰트 이름 출력
print("Loaded font name:", font_prop.get_name())
