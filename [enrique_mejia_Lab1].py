  # -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:56:40 2022

@author: enriq
"""
#
accumalator = 0

user_name = input("Please enter your name: ")
print("Hello " +user_name+ "," " Welcome to the python pizza chooser.")

pizza_choice = input("We serve cheese, pepperoni, and supreme. What would you like?: ")
print("Of course one, " +pizza_choice+ " pizza will be out in no time!")

add_pizza = "yes"


while(add_pizza == "yes"):
        add_pizza = input("Would you like to add on another pizza?: ")
        if(add_pizza == "yes"):
            pizza_choice = input("What type of pizza will that be for you?: " )
            print("Right on, lets add that to your order.")
            accumalator += 1
            
        if(add_pizza == "yes"):
            add_pizza = input("Lets add another for a discount?: ")
            pizza_choice = input("What would you like that to be?: " )
            print("That's a good one. Let's add that to your order.")
            accumalator += 2
            
        
        
else:
    if(add_pizza == "no"):
        print("Thank you " +user_name+ ".")
        print("The " ,accumalator, " you ordered will be ready in 30 minutes.")