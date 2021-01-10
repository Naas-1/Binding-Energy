import time
Z_num=int(input("Enter The Atomic Number Z:"))
A=int(input("Enter The Mass Numbers A:"))
C=float(input("Enter The nucleus's mass :"))
N=A-Z_num
Sum= (Z_num*1.00728+N*1.00866)-C
print("Change in Mass is :{}u".format(Sum))
print("Binding Energy is :{}MeV".format(Sum*931.5))
El=Sum*931.5
print("Binding Energy per nucleon is :{}MeV/nucleon".format(El/A))
time.sleep(10)
print("press Enter to leave")
input()