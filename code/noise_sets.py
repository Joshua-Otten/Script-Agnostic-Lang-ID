"""
You can use this script on the labeled data.
It will look through the dev and devtest files for every language
Then, it will create files at different noise levels for each language. 

For each sentence: 
- Pick a base script (uniformly)
- Sample which words to swap based on noise level
- For each word w, transliterate to one of the three non-base scripts            
            
Output Files:
- noise_25.dev 
- noise_50.dev
- noise_75.dev 
- noise_100.dev 
- noise_all.dev
""" 

import random
import math

DESTPATH = "../labelled_data/Noise/noise_"
SOURCEPATH = "../labelled_data/"

scripts = ["Taml", "Mlym", "Knda", "Telu"]
langs = [("Tamil", "tam"), ("Telugu", "tel"), ("Kannada", "kan"), ("Malayalam", "mal")]

all_data_combined = {}        
for lang in langs:
    lang_data = {}
    langname = lang[0]
    langcode = lang[1]
    for script in scripts:
        with open(SOURCEPATH + langname + "/" + "labelled_" + langcode + "_" + script + ".dev", "r") as f:
            lang_data[script] = f.readlines()
    all_data_combined[langcode] = lang_data
for extension in [".dev", ".devtest"]:
    for noise in ["25", "50", "75", "100"]:
        with open(DESTPATH + noise + extension, "w") as noisyfile:
            overall_data = [] 
            for _, langcode in langs:
                for i in range(len(all_data_combined[langcode][scripts[0]])):
                    basescript = random.choice(scripts)
                    scripts_reduced = [x for x in scripts if x!= basescript]
                    splitdata = all_data_combined[langcode][basescript][i].split(" ")
                    if noise != "100":
                        chosen_indices = random.sample(list(range(1,len(splitdata))), math.floor(int(noise)*len(splitdata)/100))
                    else:
                        chosen_indices = list(range(1,len(splitdata)))
                    error = 0
                    for ix in chosen_indices:
                        chosen_script = random.choice(scripts_reduced)
                        try:
                            splitdata[ix] =  all_data_combined[langcode][chosen_script][i].split(" ")[ix]
                        except IndexError:
                            error += 1
                            continue
                    overall_data.append(" ".join(splitdata))
        
            random.shuffle(overall_data)
            for line in overall_data:
                noisyfile.write(line)

    with open(DESTPATH + "all" + extension, "w") as noisyfile:
        overall_data = [] 
        for noise in ["25", "50", "75", "100"]:
            with open(DESTPATH + noise + extension, "r") as f:
                overall_data += f.readlines()
        # extension2 = ".test"
        # if extension == ".dev":
        #     extension2 = ".train"
        # with open(SOURCEPATH + "Upscaled/upscale" + extension2, "r") as f:
        #     overall_data += f.readlines()
        random.shuffle(overall_data)
        for line in overall_data:
            noisyfile.write(line)
