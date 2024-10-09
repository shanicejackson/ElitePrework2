def asking_nameAge():
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}")
    age = int(input("How old are you? "))
    print(f"You are {age} years old")
asking_nameAge()

questions = ["When is Election Day?     ",            
 "What is Best Social Media Platform of 2024?      ",
 "What is the desired Career of 2024?     ", 
 "Who is most likely to go to the SuperBowl in the NFL 24/25 Season?   "]

print("What can I help you with today")

def menu():
    while True:
        print('These are the most Frequent questions of the last 3 months: ')
        print(", " .join(questions))
        questions_answer = input("Please choose a question. 1-4 Ex: 1 for question 1: or Type 'Exit' to end. ")
        if questions_answer == "1":
            print('[November 5th, 2024]')
        elif questions_answer == "2":
            print('[Facebook]')
        elif questions_answer == "3":
            print('[Nurse Practitioner]')
        elif questions_answer == '4':
            print('[The Kansas Chiefs]')
        elif questions_answer == "Exit":
            print("Thank you. Goodbye")
            return
        else:
            print("[Invalid Answer. Please enter a number '1-4' or 'Exit']")
    
menu()    
