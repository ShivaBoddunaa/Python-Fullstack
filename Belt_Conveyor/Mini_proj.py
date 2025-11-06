# import os
# import time


# rooms=4
# current=0
# belt=int(input("enter the value"))

# def draw_BC(items):
    
#     for room in range(rooms):
#         if room == items:
#             print(f" |📦|")
#         else:
#             print(f"|  |") 
            
# print("The Belt Conveyor is moving")   

# print(f" moving to next room {belt}")  
# time.sleep(2)
# draw_BC(belt)
    
    
    

import os
import time

rooms = 4
current = 0
belt = int(input("Enter the room number: "))  # convert input to integer

def draw_BC(item):
    for room in range(rooms):
        if room == item:       # compare with the integer
            print(f" |📦|")
        else:
            print(f"|  |")

print("The Belt Conveyor is moving")

print(f"Moving to room {belt}")
time.sleep(2)
draw_BC(belt)
