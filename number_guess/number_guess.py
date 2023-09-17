import random
number=random.randint(0,100)
#print(number)
def funn():
    guess_try=int(input("input the number: "))
    try_count=1
    while guess_try != number:
        guess_try=int(input("whoops, wrong. try again: "))
        try_count+=1
    else:
        print(f"yay, you took {try_count} tries to guess the correct number - {guess_try}")
funn()