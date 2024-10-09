'''
  Lesson: If statments
  Author: Aiden
  Date Created: Oct 9, 2024
  Date Last Modified: Oct 9, 2024
'''

def q1(): 
  #Write Assignment code here

  num = int(input("In: "))
  if not num%2:
    print(f"{num} is even")
  else:
    print(f"{num} is odd")


def q2(): 
  #Write Assignment code here
  name = input("In: ")
  if name == "Kalisz":
    print("teacher")
  if name != "Kalisz":
    print("student")


#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
'''