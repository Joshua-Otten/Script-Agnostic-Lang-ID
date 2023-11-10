"""
You can use this script on any *_Taml.* files. 
It will look through the file and remove any superscripts that
may have been introduced due to transliteration from languages 
with more sounds than Tamil. 

Ex. Tamil has only one letter to represent the following 4 sounds
common in the other 3 Dravidian languages: 
    tel kan  mal tam 
k    క   ಕ   ക   க 
kh   ఖ  ಖ   ഖ   க₂ 
g    గ   ಗ   ഗ   க₃
gh   ఘ  ಘ  ഘ   க₄

The subscripts/superscripts are introduced to differentiate the four sounds. 
These are 5 such sequences. Unicode uses superscripts instead of subscript 

""" 

import os
import re

def filter_store(list_of_items):
    if ".DS_Store" in list_of_items:
        list_of_items.remove(".DS_Store")
    return list_of_items

def cleanup(filepath):
    print(filepath)
    
    with open(filepath, "r") as f:
        data = [line.replace("²","").replace("³","").replace("⁴","").strip() for line in f.readlines()]

    with open(filepath, "w") as f:
        for x in data:
            f.write(x + "\n")
    
if __name__ == "__main__":
    PATH = "../TransliteratedData/"
    for directory in filter_store(os.listdir(PATH)):
        DIRPATH = f"{PATH}{directory}/"
        files = filter_store(os.listdir(DIRPATH))  
        expression = ".*_Taml.*"
        for file in files:
            search = re.search(expression, file)
            if search is not None:
                cleanup(f"{DIRPATH}{file}")
            
                
                