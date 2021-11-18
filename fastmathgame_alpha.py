import random
from time import sleep
import threading
import sys
import keyboard
print("Hi! Welcome to Fast Math Game. Just sum each all of the numbers that given to you in 10 seconds. Have fun!")
ctrl=0
ctrl2=0
ctrl3=0
total=0
entry=0
point=0
number_pieces=2
time=0
thread_1_ctrl=0
thread_1_exe_ctrl=0
def countdown(): 
    global time
    global thread_1_ctrl
    global thread_1_exe_ctrl
    global ctrl3
    global entry
    while time<=9:
        sleep(1)
        time+=1
        if thread_1_ctrl==1:
            thread_1_exe_ctrl=0
            sys.exit()
        if ctrl3==1:
            time=0
            ctrl3=0
    if time==10:
        print("\nFailed. Your Score:",point)
        keyboard.press_and_release("0,enter")
        sys.exit()
def taking_entry():
    global time
    global entry
    global thread_1_exe_ctrl
    if thread_1_exe_ctrl==0:
        thread_1.start()
        thread_1_exe_ctrl=1
    entry=int(input("Result: "))
thread_1 = threading.Thread(target=countdown)
def main():
    global thread_1_ctrl
    global point
    global time
    global ctrl
    global ctrl2
    global ctrl3
    global total
    global entry
    global number_pieces
    while ctrl<=number_pieces:
        if ctrl2==1:
            #print(total)
            taking_entry()
            if entry==total and entry!=0:
                point+=1
                ctrl=0
                ctrl2=0
                ctrl3=1
                total=0
                continue
            else:
                ctrl=0
                ctrl2=0
                total=0
                thread_1_ctrl=1
                print("Failed. Your Score:",point)
                break   
        if ctrl==number_pieces:
            ctrl=0
            ctrl2=1
            continue
        if point==10 or point==25 or point==50 or point==75 or point==100:
            number_pieces+=1
        while ctrl<number_pieces:
            number=random.randint(1,1000)
            print(number)
            total=total+number
            ctrl+=1
main()