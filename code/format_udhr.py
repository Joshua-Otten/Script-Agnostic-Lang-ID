f = open('../labelled_data/UDHR/udhr-lid.csv','r')
lines = f.readlines()
f.close()
n = open('../labelled_data/UDHR/udhr.test','w')

supported_langs = ['tel','tam','mal','kan']
count = 0
for line in lines:
    example = line.split(',')
    sentence = example[1]
    lang_id = example[2]
    if lang_id in supported_langs:
        n.write('__label__'+lang_id+' '+sentence+'\n')
        count += 1
        
print(count)
n.close()
    
