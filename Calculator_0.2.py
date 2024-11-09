while True:

    first_n = int(input("First Number:" ))
    second_n = int(input("Second Number:"))
    question = str(input("What do you need? (add, sub, mul, div): "))
    choices = ("add", "sub", "mul", "div")
    emojis = {"add" : "➕", "sub" :"➖" , "mul" :"✖️" , "div" : "➗" }




    if question == str("add"):
        result = first_n + second_n
        print(first_n, f"{emojis[question]} " , second_n , "=" , result)

    elif question == str("sub"):
        result = first_n - second_n
        print(first_n, f"{emojis[question]} " , second_n , "=" , result)

    elif question == str("mul"):
        result = first_n * second_n
        print(first_n, f"{emojis[question]} " , second_n , "=" , result)

    elif question == str("div"):
        result = first_n / second_n
        print(first_n, f"{emojis[question]} " , second_n , "=" , result)

    should_continue = input("Continue? (y/n): ") .lower()
    if should_continue == "n":
        break

