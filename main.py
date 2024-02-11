import random

def read_file(file_name):

    """return the contents of csv file as a 2D list"""
    #CSV: comma seperated values - a text file format that uses
    #     comma to seperate value

    #string strip: remove spaces at the begining and at the end of string
    #string split: split a string into a list where each word is a list item

    list = []
    file = open(file_name)
    for item in file:
        #remove all whitespace, then split into a list, then append to big list 
        item = item.strip().split(",")
        list.append(item)


    return list 

def get_random_state(states):
    """Returns a randomly state:capital pair from the 2D list"""
    return random.choice(states)

def get_random_choices(states, correct_capital):
    """returns a list of 4 possible answers (1 correct - 3 incorrect)"""
    #initilize the list with one correct answer
    possible_answers = [correct_capital]
    i = 0
    while i < 3:
        #get a random state from states
        state = random.choice(states)
        #since the state is a list
        #to access captical, get second element
        if state[1] not in possible_answers:
            possible_answers.append(state[1])
            i += 1
    random.shuffle(possible_answers)
    return possible_answers

def ask_question(correct_state, possible_answers):
    """promts user to enter A-D"""
    #\n : new line
    #\t tab character - give some space
    print("The capital of " + correct_state + " is: \n\tA. " + possible_answers[0] + "  B. " + possible_answers[1] + "  C. " + possible_answers[2] + "  D. " + possible_answers[3])
    options = ["A","B","C","D"]
    while True: 
        choice = input("Enter selection: ").upper()
        if choice not in options:
            print("Invalid Input. Enter choice A-D")
        else:
            #get the index of that element
            return options.index(choice)
def main():
    states = read_file("statecapitals.txt")
    points = 0 
    print("- State Captital Quiz -")
    for i in range(10):
        #split a state and its capital
        correct_state, correct_capital = get_random_state(states)
        #get a list of 4 choices with 1 correct - 3 incorrect
        possible_choices = get_random_choices(states, correct_capital)
        #get the choice from user 
        #print(f"{i+1} ." )
        choice = ask_question(correct_state, possible_choices)
        #check if the user choice match with the correct answe
        if choice == possible_choices.index(correct_capital):
            print("Correct!")
            points += 1
        else:
            print("Incorrect! The correct answer is: " + correct_capital +".")

    print(f"End of test. You got {points} correct." )


main()
