#!/usr/bin/env python


def main():
    """Start a colour guessing game."""
    print("Guess the genre!")
    
from tabulate import tabulate
hint = ["Pilihan","Genre"]
jadual = []
jadual.append([1,"pop"])
jadual.append([2,"jpop"])
jadual.append([3,"hip hop"])
jadual.append([4,"nasyid"])
jadual.append([5,"jazz"])
jadual.append([6,"rnb"])
jadual.append([7,"indie"])
jadual.append([8,"rock"])
print(tabulate(jadual,hint,"fancy_grid"))
            
questions = {
    "This genre's harmony is not too complicated and the tempo varies?":['a. hip hop ', 'b. pop', 'c. nasyid', 'd. jpop','b'],
    "This genre is continuous and strong beat.":['a. indie', 'b. rock', 'c. pop', 'd. hip hop', 'd'],
    "This genre's song lyrics are more expressive and free.":['a. jpop', 'b. jazz', 'c. rnb', 'd. rock', 'd'],
    "This genre has a monophonic texture.":['a. pop', 'b. indie', 'c. hip hop', 'd. nasyid', 'd'],
    "This genre is characterized by swing and blue notes, complex chords, call and response vocals, polyrhythms and improvisation.":['a. jazz', 'b. hip hop', 'c. rnb', 'd. rock', 'a'],
    "This genre has more emphasis on good vocal quality and more relaxed lyrics.":['a. pop', 'b. indie', 'c. rnb', 'd. nasyid', 'c'],
    "This genre is characterized by its guitar-driven melodies and rhythms, DIY ethos, introspective lyrics, and electric sound.":['a. hip hop', 'b. indie', 'c. rock', 'd. jpop', 'b'],
    "This genre features chord changes and vocal delivery closer to traditional Japanese music than American pop or rock.":['a. jpop', 'b. nasyid', 'c. rnb', 'd. jazz', 'a'],


} # 1

score = 0 # 2 
for question_number,question in enumerate(questions): # 3
    print ("Question",question_number+1) # 4
    print (question)
    for options in questions[question][:-1]: # 5
        print (options)
    user_choice = input("Make your choice : ")
    if user_choice == questions[question][-1]: # 6
        print ("Congratulations! You are very good when it comes to music and guessing. Well done!!")
        score += 1 #7 here's the relevant part of the question
    else: # 8
        print ("Your answer is wrong.... but it's okay! You could answer the next question correctly. Never give up!!!")

print(int(input("Your score is: " + str(score)))) #9
        













main()