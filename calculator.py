#imports for the spinner
import sys
import time
import threading
import itertools

#menu and options
print("Welcome to the Calculator!")
print("What operation do you need to do? ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Whole Division")
print("5. Floating Division")
print("6. Exponentiation")
print("7. Modulus")
choice = int(input("Please select an operation (1/2/3/4/5/6/7):"))

#inputs from user
number1 = float(input("Please insert the first number: "))
number2 = float(input("Please insert the second number: "))

#spinner animation
def spin(stop_event, message="Calculating"):
    for frame in itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{frame} {message}")
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")  # clear line

stop = threading.Event()
t = threading.Thread(target=spin, args=(stop,))
t.start()

time.sleep(3)  # your actual work goes here

print("\r")
if choice == 1:
    print(number1 + number2)

elif choice == 2:
    print(number1 - number2)

elif choice == 3:
    print(number1 * number2)

elif choice == 4:
    if number2 == 0:
        print("Can't divide a number by 0, you dummy🫵")
    else: 
        print(number1 // number2)






stop.set()
t.join()

#if statements to perform calculations

#error handling for invalid inputs
