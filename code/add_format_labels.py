# This program takes a given a language and folders as input, and creates formatted labelled files according to fastText classification expectations
# Note that since the goal is script-agnosticism, the label should be the document's language, and not its script.
# arguments: [directory path (including '/')] [new path] [label]
import sys

scripts = ['Knda','Mlym','Taml','Telu']
types = types = ['.dev','.devtest'] #['_non-parallel.txt']
path = sys.argv[1]
new_path = sys.argv[2]
language = sys.argv[3]
# these loops ensure we get all files for a given language
for type in types:
    for script in scripts:
        filename = language+'_'+script+type
        file = open(path+filename,'r')
        new = open(new_path+'labelled_'+filename,'w')
        lines = file.readlines()
        file.close()
        for line in lines:
            new.write('__label__'+language+' '+line)
        new.close()

