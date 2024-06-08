import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 파일의 정확한 로컬 경로 지정
font_path = 'C:/Users/KMGHO/Downloads/NanumGothic.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

# 로드된 폰트 이름 출력
try:
    print("Loaded font name:", font_prop.get_name())
except Exception as e:
    print("Error loading font:", e)
