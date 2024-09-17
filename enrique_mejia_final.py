# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:53:33 2022

@author: enriq
"""
def main():
    
    list1 = [2, 4, 12, 18, 24]
    list2 = [9, 17]
    
    list3 = list1 + list2
    print(list3)
    
    get_sum = sum(list1 + list2)
    print(get_sum)

    mean = (get_sum/7)
    print(mean)

    for i in range(list1, list2):
        
        print(i)
    
    
if __name__=='__main__':
    
    main()