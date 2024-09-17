# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:52:40 2022

@author: enriq
"""

def Database(name, location, value):
    
    saved_database = [] #Creating an empty list
    
    inFile = open(r'C:\Users\enriq\OneDrive\Desktop\StudentGradebook.txt', 'r') #Opening a file in read mode
    
    for lines in inFile: #We are going to loop through every line in the file
        
        saved_database.extend(lines.split('\t'))
        
        print(saved_database)
        
    print('\n----------------------')
    inFile.close()
        
    grade_book = saved_database
    
        
    if name in saved_database:
        with open(r'C:\Users\enriq\OneDrive\Desktop\StudentGradebook.txt', 'w') as f: #Open the file in write mode
            
            name_index = grade_book.index(name)
            grade_index = name_index + location
            grade_book[grade_index] = value
            
    else:
        print("That name is not in the grade book.")
                
        
        for elements in saved_database:  #Iterate through every element in the database
            
            f.write('%s\t' % elements) #Write each value to the database back into delimited form

                
    f.close()
    
    
        
#This function will let the user access the working_database and change any 
#grade contained in the function       
def getUserGrades():
    
    student_name = input("Enter the student name: ")
    student_grade = int(input("Enter the student grade you wish to change: "))
    new_grade = int(input(f'Enter the new grade for {student_name}, grade {student_grade}: '))

    Database(student_name, student_grade, new_grade)
                          
    #This function will let the user access the working_database
    #and change any grade contained in the function
    
    pass

if __name__=='__main__':
    
    getUserGrades()