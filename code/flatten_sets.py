"""
You can use this script on the labeled data.
It will look through the dev and devtest files for every language
Then, it will pool together files from one particular script from each language into a single training data file

Ex. To create the flatten_all_Taml.dev file: Go through all *_Taml.dev files i.e. tel_Taml, mal_Taml, kan_Taml, tel_Taml and pool them into one file
In theory, this should reduce the vocabulary space and allow for lexical overlap in the embedding distributions
""" 

import random

DESTPATH = "../labelled_data/Flatten/flatten_"
SOURCEPATH = "../labelled_data/"

scripts = ["Taml", "Mlym", "Knda", "Telu"]
langs = [("Tamil", "tam"), ("Telugu", "tel"), ("Kannada", "kan"), ("Malayalam", "mal")]

for extension in [".dev", ".devtest"]:
    for script in scripts:
        with open(DESTPATH + "all_" + script + extension,"w") as destfile:
            all_lang_data = []
            for lang in langs:
                langname = lang[0]
                langcode = lang[1]
            
                with open(SOURCEPATH + langname + "/" + "labelled_" + langcode + "_" + script + extension,'r') as f:
                    all_lang_data += f.readlines()
                
            random.shuffle(all_lang_data)
            for x in all_lang_data:
                destfile.write(x)


