from random import randint
import time 

score=0
tries=5
for i in range(tries): 
    num1=randint(1,10)
    num2=randint(1,10)
    product= num1* num2
    # start_time=time()
    response=(input(f'Q{i+1}/{tries}: What is {num1}*{num2} ?'))
    # end_time=time()
    if response == "":
            print(" No answer given, counted as incorrect.")
            continue
    try:
        ans= int(response)
        if ans== product:
            print(f" Correct ^-^")
            score+=1

        else:
            print(f"Wrong 0-0, the correct answer was {product}")

    except ValueError:
        print("Please Enter a Number")
        
print(f"\n Your Final score: {score}/{tries}")