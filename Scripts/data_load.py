# class student:
#     def __init__(self, ism, familya, baho):
#         self.ism = ism
#         self.familya = familya
#         self.baho = baho

#     def get_avarage(self):
#         print(f"{sum(self.baho) / len(self.baho):.1f}")
    

# s1 = student('ali', 'aliyev', [4,3,4,5,4,3])
# print(s1.ism)
# print(s1.baho)
# s1.get_avarage()

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance


#     def deposit(self, sum):
#         self.sum = sum
#         self.balance += sum
#         # return f"{self.owner}ning balance {self.balance} ga teng"
    
#     def __str__(self):
#         return f"{self.owner}ning balance {self.balance} ga teng"
    

# class banking(BankAccount):
#     def __init__(self, owner, familya, balance=0):
#         self.familya = familya
#         super().__init__(owner, balance)

#     def introduce(self):
#         print(f"Salom men Ali {self.familya} {self.balance} pulim bor")

# s = BankAccount('bunyod')
# s.deposit(10000)
# print(s)

# s1 = banking("Vali", "Nurdinov", 33)
# print(s1)



import pyautogui























