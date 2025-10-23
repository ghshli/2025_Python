class BankAccount:
    def __init__(self, owner):
        self.__balance = 0
        self.owner = owner
        print(f"{self.owner} 계좌가 생성되었습니다.")

    def get_balance(self):
        return self.__balance
    
    def get_balance(amount):
        if self.__balance >=0:
            return self.__balance
    
    def deposit(amount):
        if amount >=0:
            return amount
        
    def withdraw(amount):
        if self.balance >= amount :
            self.balance -= amount
            print(f"{self.owner} 통장에 {amount}원이 입금돠었습니다.")
        else:
            print("잔액 부족")

a = BankAccount("A")
b = BankAccount("B")

a.desposit(100)
b.desposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())