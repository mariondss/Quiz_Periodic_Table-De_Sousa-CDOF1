# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:05:02 2024

@author: mario
"""
score = 0 

question1 = ["What does the letter H represent in the periodic table?", "Helium", "Hydrogen", "Hafnium", "Holmium", "Hydrogen"]
question2 = ["What does the letter C represent in the periodic table?", "Calcium", "Cobalt", "Carbon", "Curium", "Carbon"]
question3 = ["What does the letter N represent in the periodic table?", "Neon", "Nickel", "Nitrogen", "Nihonium", "Nitrogen"]
question4 = ["What does the letter O represent in the periodic table?", "Oxygen", "Osmium", "Oganesson", "Ruthenium", "Oxygen"]
question5 = ["What does the letter K represent in the periodic table?", "Krypton", "Kryptonite", "Potassium", "Kurium", "Potassium"]

questionList = [question1,question2,question3,question4,question5]

def displayQ(question):
    result = question[0] + "\n"
    for i in question[1:-1]:
        result += "- " + i + "\n"
    return result
    

for i in questionList:
    print("\n")
    print(displayQ(i) + "\nEnter your answer :")
    answer = input()
    if(answer == i[5]) : score += 1
print("\n")


print("Your score is ", score)