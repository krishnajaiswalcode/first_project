import random

subjects = [
    "shahrukh khan",
    "virat kohli",
    "nirmala sitaraman",
    "a mumbai cat",
    "prime minister modi",
    "a group of monkeys",
    "auto rickshaw driver from bhopal"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "celebrates"
]


places = [
    " at red fort",
    " in mumbai local train",
    " a plate of samosa",
    " inside parliament",
    " at ganga ghat",
    " during IPL match",
    " at india ghat"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    headline = f" BREAKING NEWS :  {subject} {action}{place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no) :  ").strip().lower()
    if user_input == "no":
        break

print ( "\nThanks for using the fake News Heading Generator")

