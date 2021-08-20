# Regex version of string strip() method

import re

def RegexStrip(text, arg1):
    # If no character is passed as argument, spaces on both sides of string will be removed
    if(arg1 == ''):
        stripRegex = re.compile(r'(^\s*)')      # removes spaces on left
        stripRegex2 = re.compile(r'(\s*$)')     # removes spaces on right
        so = stripRegex.sub('',text)  
        soFinal = stripRegex2.sub('',so)
        # quotes added on both sides to check if spaces were removed
        print("'",soFinal,"'", sep='')
    
    # If a character is passed as argument, those characters will be removed
    else:
        stripRegex = re.compile(arg1, re.I)
        so = stripRegex.sub('', string)
        print("'",so,"'", sep='')

string = input('Enter a string : ')
replace = input('Enter character to be removed from string\n(or) If nothing entered spaces on both sides will be removed : ')
RegexStrip(string, replace)