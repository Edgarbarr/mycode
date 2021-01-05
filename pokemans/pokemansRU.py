#!/usr/bin/env python3
pokemans = {
        "Pikachu": 0,
        "Snorlax": 0,
        "Squirtle": 0,
        "Charizard": 0,
        "Bulbasaur": 0
        }
questions = [[
        "Would you kill ten people to save 1?", {
            "Yes": "Pikachu",
            "Depends who the 1 is": "Squirtle",
            "I'll kill 11": "Charizard",
            "I can't chose between lives": "Bulbasaur",
            "I don't want to be involved": "Snorlax"}
            ],
            [
        "What is love?", {
            "How I feel about coffee ;D": "Pikachu",
            "Baby don't hurt me": "Squirtle",
            "I don't even love anything": "Charizard",
            "It's when you deeply care about someone": "Bulbasaur",
            "IDK": "Snorlax"}
            ],
            [
        "What is the main reason so many people moved to California in 1849?", {"California land was fertile, plentiful, and inexpensive": "Pikachu",
            "Gold was discovered in central California": "Squirtle",
            "The east was preparing for a civil war":"Charizard",
            "They wanted to establish religious settlements": "Bulbasaur",
            "idk": "Snorlax"}
        ]]
print("Which pokemon are you quiz:\n")
num = 0;
while(num < len(questions)):
    current = questions[num]
    print(current[0])
    q = 1
    for ans in current[1]:
        print(f"Press {q}: {ans}")
        q+=1
    reply = input("Choose number")
    current = questions[num]
    num+=1
print("congratz your a pikachu")
    

