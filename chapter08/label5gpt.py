import os
from tkinter import *

# 🧭 현재 파일이 있는 폴더 경로 가져오기
path = os.path.dirname(os.path.abspath(__file__))
print("현재 파이썬 파일 경로:", path)

# 📁 실제로 파이썬이 찾으려는 이미지 파일 경로 확인
img_path = os.path.join(path, "wl.gif")
print("이미지 경로:", img_path)

# 🚨 파일이 없을 경우 경고 출력
if not os.path.exists(img_path):
    print("❌ 이미지 파일을 찾을 수 없습니다! 아래 경로에 wl.gif가 있는지 확인하세요.")
    print(img_path)
else:
    print("✅ 이미지 파일을 찾았습니다!")

# 🖼️ Tkinter 윈도우 생성
root = Tk()

# 이미지 로드
photo = PhotoImage(file=img_path)

# 시 내용
message = """삶이 그대를 속일지라도
슬퍼하거나 노하지 말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
"""

# 이미지 + 텍스트 라벨 배치
w = Label(root, image=photo, justify="left")
w.pack(side="right")

w2 = Label(root, padx=10, text=message)
w2.pack(side="left")

root.mainloop()