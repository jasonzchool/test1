import random 

def easy():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    return [num1,num2]

def medium():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    return [num1,num2]

def hard():
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    return [num1,num2]

def questiontype():
        try: 
            answer=int(input(f"{numbers[0]} {sign}\
{numbers[1]}="))
        except ValueError:
            print("you have not entered an integer")
        except:
            print("an error has occurred")

        if sign=="+" and answer==(numbers[0]+numbers[1]):
            print("correct!")
            counter+=1
        elif sign=="-" and answer==(numbers[0]-numbers[1]):
            print("correct!")
            counter+=1
        elif sign=="*" and answer==(numbers[0]*numbers[1]):
            print("correct!")
            counter+=1
        else:
            print("wrong answer")
    



question_type=" "
counter=0
running=True

while running:
    print("1. Easy 2. Medium 3. Hard 4. Exit")

    while question_type!=int:    
        try:
            question_type=int(input("what question type would you like:"))
            break
        except ValueError:
            print("please write an integer")
        except:
            print("an error occurred")
        
    if question_type==1:
        for i in range(10):
            numbers = easy()
            signs=["+","-","*"]
            num=random.randint(0,len(signs)-1)
            sign=signs[num]
            questiontype()
        print(f"you got {counter} questions right!")
            
        
    elif question_type==2:
        for i in range(10):
            numbers = medium()
            signs=["+","-","*"]
            num=random.randint(0,len(signs)-1)
            sign=signs[num]
            questiontype()
        print(f"you got {counter} questions right!")
        
    elif question_type==3:
        for i in range(10):
            numbers = hard()
            signs=["+","-","*"]
            num=random.randint(0,len(signs)-1)
            sign=signs[num]
            questiontype()
        print(f"you got {counter} questions right!")
        

      

    else:
        print("program closing...")
        running=False