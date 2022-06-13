import random
print("Welcome to Rock, Paper, Scissors - The Python Game")
username = input('What is your name: ')

while True:
    possible_options = ['R','P','S']

    while True:
        user_choice = input("Pick an option: ").upper()
        if user_choice not in possible_options:
            print("Invalid option, try again")
            continue
        else:
            break


    cpu_choice = random.choice(possible_options)
    print(f"{username} ({user_choice}) : CPU ({cpu_choice})")
    if user_choice ==  cpu_choice:
        print(f"It is a tie!")
        if user_choice == cpu_choice:
            continue
        else:
            break
    elif user_choice == 'R':
        if cpu_choice == "S":
            print(f'{username} wins!')
        else:
            print(f'CPU wins!')
    elif user_choice == "P":
        if cpu_choice == "S":
            print(f'CPU wins!')
        else: 
            print(f'{username} wins!')
    elif user_choice == "S":
        if cpu_choice == "P":
            print(f'{username} wins!')
        else:
            print(f'{username} wins!')
    break
print(f"Thanks for playing, {username}! ")
    
