# test1
import random 

def easy():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    return [num1,num2]


signs=["+","-","*"]
num=random.randint(0,len(signs)-1)
sign=signs[num]

easy_numbers = easy()

running=True

while running:
    print("1. Easy 2. Medium 3. Hard 4. Exit")
    question_type=int(input("what question type would you like:"))
    if question_type==1:
        try: 
            easy_answer=int(input(f"{easy_numbers[0]}{sign}\
            {easy_numbers[1]}="))
        except ValueError:
            print("you have not entered an integer")
        except:
            print("an error has occurred")
        if easy_answer==easy_numbers[0]:
            pass
        else:
            print("wrong answer")
    elif question_type==2:
        pass
    elif question_type==3:
        pass
    else:
        print("program closing...")
        running=False