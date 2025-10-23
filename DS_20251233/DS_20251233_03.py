class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def show_info(self):
        print(f"학번: {stu_id}, 이름: {self.name}")

    class UndergraduateStudent(self, major):
        self.major = major
        def introduce():
            print(f"저는 학부생 {self.name}입니다. 전공은 {self.major}학과입니다.")

    class GraduateStudent(self, advisor):
        self.advisor = advisor
        def introduce():
            print(f"저는 대학원생 {self.name}입니다. 지도교수님은 {self.advisor}입니다.")

stu1 = UndergraduateStudent("202501", "김민수", "컴퓨터공학과")
stu2 = GraduateStudent("202401", "이수정", "홍길동")
stu1.show_info()
stu1.infoduce()
stu2.show_info()
stu2.infoduce()