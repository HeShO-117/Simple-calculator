import os, time
logo1 = """                    ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗                 
                     ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝                 
                     ███████╗██║██╔████╔██║██████╔╝██║     █████╗                   
                     ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝                   
                     ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗                 
                     ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝"""                 
logo2 = """
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"""

os.system("clear")
print()
print('\033[94m', logo1, '\033[0m')
time.sleep(0.5)
print(logo2)
time.sleep(0.5)
print()

#input from user
print("\t\t\t:::Select The Calculation:::")
print('\033[33m ')
print("\t\t\t[1]Add")
print("\t\t\t[2]Subtract")
print("\t\t\t[3]Multiply")
print("\t\t\t[4]Divide")
print("\t\t\t[5]Power")

#definition

def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

def power (x, y):
    return x ** y

choice = int(input("\033[0m\033[96m\n\t\t\t[+]Enter Your Choice :"))
num1 = int(input("\033[0m\033[36m\n\t\t\t[+]Enter first Number :"))
num2 = int(input("\033[0m\033[36m\t\t\t[+]Enter second Number :"))

if choice == 1:
    print('\t\t\t', "\033[91m#Answer is ", num1, "+", num2, "=", add(num1, num2))
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")

elif choice == 2:
    print('\t\t\t', "\033[91m#Answer is ", num1, "-", num2, "=", subtract(num1, num2))
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")

elif choice == 3:
    print('\t\t\t', "\033[91m#Answer is ", num1, "×", num2, "=", multiply(num1, num2))
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")

elif choice == 4:
    print('\t\t\t', "\033[91m#Answer is ", num1, "÷", num2, "=", divide(num1, num2))
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")

elif choice == 5:
    print('\t\t\t', "\033[91m#Answer is ", num1, "^", num2, "=", power(num1, num2))
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")

else:
    print("\033[91m\t\t\t invalid input")
    print("\033[0m")
    a = str(input("\033[92m\t\t\tEnter for run again:"))
    os.system("python3 demo.py")