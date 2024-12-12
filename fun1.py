
import random

def sorting_hat():
    print("Welcome to the Sorting Hat Ceremony!\n")
    
    # Ask the user some questions to determine their house
    print("Answer the following questions truthfully, and I will sort you into a house!\n")

    # Simple questions to decide the house
    questions = [
        "What is most important to you? (bravery, loyalty, wisdom, ambition): ",
        "What would you prefer to do? (explore new lands, help others, study, lead a team): ",
        "Pick your favorite animal: (lion, badger, eagle, snake): "
    ]

    answers = []
    
    for question in questions:
        answer = input(question).lower()
        answers.append(answer)
    
    # Simple rules based on answers to assign house
    houses = {
        "gryffindor": 0,
        "hufflepuff": 0,
        "ravenclaw": 0,
        "slytherin": 0
    }
    
    # We will use the answers to assign scores to the houses
    for answer in answers:
        if "bravery" in answer or "lion" in answer:
            houses["gryffindor"] += 1
        elif "loyalty" in answer or "badger" in answer:
            houses["hufflepuff"] += 1
        elif "wisdom" in answer or "eagle" in answer:
            houses["ravenclaw"] += 1
        elif "ambition" in answer or "snake" in answer:
            houses["slytherin"] += 1

    # Find the house with the highest score
    sorted_houses = sorted(houses, key=houses.get, reverse=True)
    sorted_house = sorted_houses[0]
    
    print("\nThe Sorting Hat has decided...\n")
    
    # A little suspense for fun!
    print("Hmm... This is a tricky one...\n")
    print(f"You're a {sorted_house.capitalize()}!")
    
# Run the Sorting Hat
sorting_hat()
