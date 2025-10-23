class Employee:
    empCount = 0  # 전체 직원 수 저장하는 클래스 변수

    def __init__(self, name, salary):
        self.name = name       # 직원 이름 저장
        self.salary = salary   # 직원 월급 저장
        Employee.empCount += 1  # 직원이 한 명 생길 때마다 +1

    def displayEmp(self):
        # 직원 정보 출력
        print(f"Name: {self.name}, Salary: {self.salary}")


# 직원 객체 2명 생성
emp1 = Employee("Kim", 5000)
emp2 = Employee("Lee", 6000)

# 각 직원 정보 출력
emp1.displayEmp()
emp2.displayEmp()

# 총 직원 수 출력
print("Total employees:", Employee.empCount)