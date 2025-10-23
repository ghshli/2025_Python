class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []  # 성적 리스트 초기화

    def add_score(self, score):
        self.scores.append(score)
        print(f"{self.name}의 성적 {score}이 추가되었습니다.")

    def cal_avg(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


# 학생 객체 만들기
student = Student("kim")

# 성적 추가
student.add_score(90)
student.add_score(85)
student.add_score(78)

# 평균 계산
avg = student.cal_avg()

# 결과 출력
print(f"{student.name}의 평균 성적: {avg:.2f}")
