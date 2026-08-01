# Setting: you are an adventurer in a fantasy world and the law doesn't like you operating without being legitimate, you need a guild name and the hand of law doesn't forgive magical tax evasion...

greeting = input(
    "Hello there, Chosen One!\n I am an employee in the Magical Bureau of Adventure and we need you to create a Guild Name for the not so legal entrepreneurship you got going here!\n To do that we will need you to share some details with us!\n ENTER ->")
name = input("What is your name?\n")
occupation = input("What is your occupation?\n")
print(
    "Thank you very much, you are officially registered under the name:" + " " + name + "'s" + " " + occupation + "s!\nNow please go with this form and get your ID from the Bureau or you will be fined for being a " + occupation + " without the appropriate permits!\n")
# Example ->>
# What is your name?
# Michael
# What is your occupation?
# Dragon Slayer
# Thank you very much, you are officially registered under the name: Michael's Dragon Slayers!
# Now please go with this form and get your ID from the Bureau or you will be fined for being a Dragon Slayer without the appropriate permits!

# PS: I know that I'm taking into account very specific word inputs and that it will look a bit jarring with other occupations
