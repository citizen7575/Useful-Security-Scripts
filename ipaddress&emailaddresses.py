#!/usr/bin/env python3

# importing the module 
import re
import sys 

# declaring the regex pattern for IP addresses 
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# declaring the regex pattern for email address 
pattern2 = re.compile(r'(\S*@\S*\.com)')

# opening and reading the file
# from user input
if len(sys.argv) > 1:
    filelocation = sys.argv[1]
    with open(filelocation) as fo: 
        # initializing the list object 
        lst=[] 
        lst2=[]
        # extracting the IP addresses 
        contents = fo.read().rstrip()  
        lst.append(pattern.findall(contents))
        lst2.append(pattern2.findall(contents))

        # displaying the extracted IP addresses and Shipt email addresses  
        lst = lst[0]
        print(lst)
    
        lst2 = lst2[0]
        print(lst2) 

# from command line argument
elif len(sys.argv) == 1: 
    filelocation = input("Enter file name:")
    with open(filelocation) as fo: 
        # initializing the list object 
        lst=[]
        lst2=[] 
        
        # extracting the IP addresses 
        contents = fo.read().rstrip()   
        lst.append(pattern.findall(contents))
        lst2.append(pattern2.findall(contents))

        # displaying the extracted IP addresses and Shipt email addresses 
        lst = lst[0]
        print(lst)
        
        lst2 = lst2[0]
        print(lst2)
