"""
You can use this script on the labeled data.
It will look through the dev and devtest files for every language
Then, it will pool together files from all scripts and all languages into a single training data file, keeping the 4*4 = 16 class labels separate.
""" 

import random

DESTPATH = "../labelled_data/Separate/separate"
SOURCEPATH = "../labelled_data/"

scripts = ["Taml", "Mlym", "Knda", "Telu"]
langs = [("Tamil", "tam"), ("Telugu", "tel"), ("Kannada", "kan"), ("Malayalam", "mal")]

for extension in [".dev", ".devtest"]:
    with open(DESTPATH + extension,"w") as destfile:
        all_lang_data = []
        for lang in langs:
            langname = lang[0]
            langcode = lang[1]
            
            script_data = []
            for script in scripts:    
                with open(SOURCEPATH + langname + "/" + "labelled_" + langcode + "_" + script + extension,'r') as f:
                    readlines = f.readlines()
                    
                    # reformatting to include script-lang label 
                    for i in range(len(readlines)):
                        label = readlines[i].split(' ')[0]
                        text = "".join(readlines[i].split(' ')[1:])
                        readlines[i] = "__label__" +  langcode + "_" + script + " " + text 
                    
                    all_lang_data += readlines
                    
        random.shuffle(all_lang_data)
        for x in all_lang_data:
            destfile.write(x)


