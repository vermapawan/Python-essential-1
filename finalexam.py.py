secret_number=777
guess=int(input("""
+====================================+
|    Welcome to my game, muggle !    |
|    Enter an integer number         |
|    and guess what number I' ve     |
|    picked for you                  |
|    so, what is the secret number ? |
+====================================|
"""))
counter=1
while guess!=secret_number:
    if guess<secret_number:
        print("Ha ha! you're stuck in my loop! The secret number is less than your guess")
    elif guess>secret_number:
            print("Ha ha! you're stuck in my loop! the secret number is greater than your guess")
    guess=int(input("Try Again "))
    counter=counter+1
print('Well done, muggle! you are free now.',guess,' is the correct answer. you succeded in',counter,' attempts.')    
