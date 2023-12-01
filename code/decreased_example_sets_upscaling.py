# create training lists of 25%, 50%, and 75% of the examples, randomly selected.
#This is for understanding the effect of training size on the original Script-Upscaled model

import random

def write_percent(percent,lines,file):
    new_file = open(file,'w')
    percent = int(percent*len(lines))
    print(percent,'should be 25% of',len(lines))

    for i in range(percent):
        # randomly select an example
        ex = random.choice(lines)
        # write the example to the new file
        new_file.write(ex)
        # get rid of the example so it doesn't get selected twice
        lines.pop(lines.index(ex))
    new_file.close()


# after writing each file, read the lines and save in a list for future use
##### Telugu #####
# Telugu script
file = open('../labelled_data/Telugu/labelled_tel_Telu.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tel_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tel_Telu.dev','r')
tel_Telu25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tel_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tel_Telu.dev','r')
tel_Telu50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tel_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tel_Telu.dev','r')
tel_Telu75 = latest.readlines()
latest.close()

# Kannada script
file = open('../labelled_data/Telugu/labelled_tel_Knda.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tel_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tel_Knda.dev','r')
tel_Knda25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tel_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tel_Knda.dev','r')
tel_Knda50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tel_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tel_Knda.dev','r')
tel_Knda75 = latest.readlines()
latest.close()

# Malayalam script
file = open('../labelled_data/Telugu/labelled_tel_Mlym.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tel_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tel_Mlym.dev','r')
tel_Mlym25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tel_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tel_Mlym.dev','r')
tel_Mlym50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tel_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tel_Mlym.dev','r')
tel_Mlym75 = latest.readlines()
latest.close()

# Tamil script
file = open('../labelled_data/Telugu/labelled_tel_Taml.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tel_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tel_Taml.dev','r')
tel_Taml25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tel_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tel_Taml.dev','r')
tel_Taml50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tel_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tel_Taml.dev','r')
tel_Taml75 = latest.readlines()
latest.close()


##### Kannada #####
# Telugu script
file = open('../labelled_data/Kannada/labelled_kan_Telu.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/kan_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_25/kan_Telu.dev','r')
kan_Telu25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/kan_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_50/kan_Telu.dev','r')
kan_Telu50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/kan_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_75/kan_Telu.dev','r')
kan_Telu75 = latest.readlines()
latest.close()

# Kannada script
file = open('../labelled_data/Kannada/labelled_kan_Knda.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/kan_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_25/kan_Knda.dev','r')
kan_Knda25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/kan_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_50/kan_Knda.dev','r')
kan_Knda50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/kan_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_75/kan_Knda.dev','r')
kan_Knda75 = latest.readlines()
latest.close()

# Malayalam script
file = open('../labelled_data/Kannada/labelled_kan_Mlym.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/kan_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_25/kan_Mlym.dev','r')
kan_Mlym25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/kan_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_50/kan_Mlym.dev','r')
kan_Mlym50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/kan_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_75/kan_Mlym.dev','r')
kan_Mlym75 = latest.readlines()
latest.close()

# Tamil script
file = open('../labelled_data/Kannada/labelled_kan_Taml.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/kan_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_25/kan_Taml.dev','r')
kan_Taml25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/kan_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_50/kan_Taml.dev','r')
kan_Taml50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/kan_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_75/kan_Taml.dev','r')
kan_Taml75 = latest.readlines()
latest.close()


##### Malayalam #####
# Telugu script
file = open('../labelled_data/Malayalam/labelled_mal_Telu.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/mal_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_25/mal_Telu.dev','r')
mal_Telu25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/mal_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_50/mal_Telu.dev','r')
mal_Telu50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/mal_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_75/mal_Telu.dev','r')
mal_Telu75 = latest.readlines()
latest.close()

# Kannada script
file = open('../labelled_data/Malayalam/labelled_mal_Knda.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/mal_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_25/mal_Knda.dev','r')
mal_Knda25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/mal_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_50/mal_Knda.dev','r')
mal_Knda50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/mal_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_75/mal_Knda.dev','r')
mal_Knda75 = latest.readlines()
latest.close()

# Malayalam script
file = open('../labelled_data/Malayalam/labelled_mal_Mlym.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/mal_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_25/mal_Mlym.dev','r')
mal_Mlym25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/mal_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_50/mal_Mlym.dev','r')
mal_Mlym50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/mal_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_75/mal_Mlym.dev','r')
mal_Mlym75 = latest.readlines()
latest.close()

# Tamil script
file = open('../labelled_data/Malayalam/labelled_mal_Taml.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/mal_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_25/mal_Taml.dev','r')
mal_Taml25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/mal_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_50/mal_Taml.dev','r')
mal_Taml50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/mal_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_75/mal_Taml.dev','r')
mal_Taml75 = latest.readlines()
latest.close()


##### Tamil #####
# Telugu script
file = open('../labelled_data/Tamil/labelled_tam_Telu.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tam_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tam_Telu.dev','r')
tam_Telu25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tam_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tam_Telu.dev','r')
tam_Telu50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tam_Telu.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tam_Telu.dev','r')
tam_Telu75 = latest.readlines()
latest.close()

# Kannada script
file = open('../labelled_data/Tamil/labelled_tam_Knda.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tam_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tam_Knda.dev','r')
tam_Knda25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tam_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tam_Knda.dev','r')
tam_Knda50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tam_Knda.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tam_Knda.dev','r')
tam_Knda75 = latest.readlines()
latest.close()

# Malayalam script
file = open('../labelled_data/Tamil/labelled_tam_Mlym.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tam_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tam_Mlym.dev','r')
tam_Mlym25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tam_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tam_Mlym.dev','r')
tam_Mlym50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tam_Mlym.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tam_Mlym.dev','r')
tam_Mlym75 = latest.readlines()
latest.close()

# Tamil script
file = open('../labelled_data/Tamil/labelled_tam_Taml.dev','r')
original = file.readlines()
file.close()

write_percent(0.25,original.copy(),'../labelled_data/Upscaled/Percent_25/tam_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_25/tam_Taml.dev','r')
tam_Taml25 = latest.readlines()
latest.close()

write_percent(0.50,original.copy(),'../labelled_data/Upscaled/Percent_50/tam_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_50/tam_Taml.dev','r')
tam_Taml50 = latest.readlines()
latest.close()

write_percent(0.75,original.copy(),'../labelled_data/Upscaled/Percent_75/tam_Taml.dev')
latest = open('../labelled_data/Upscaled/Percent_75/tam_Taml.dev','r')
tam_Taml75 = latest.readlines()
latest.close()



############################################
###### Now compile the training sets #######
############################################

# 25% Training Set
train_set = open('../labelled_data/Upscaled/Percent_25/Upscaled25.train','w')

print('tam_Telu:',tam_Telu25)
# now add the various lines to the training set, but mix it together
for i in range(249): # essentially for all train lines
    options = ['tam_Telu','tam_Knda','tam_Mlym','tam_Taml','tel_Telu','tel_Knda','tel_Mlym','tel_Taml','mal_Telu','mal_Knda','mal_Mlym','mal_Taml','kan_Telu','kan_Knda','kan_Mlym','kan_Taml']
    for j in range(16):
        choose = random.choice(options)
        if choose == 'tam_Telu':
            train_set.write(tam_Telu25[0])
            #print('line:',tam_Telu25[0])
            tam_Telu25.pop(0)
        elif choose == 'tam_Knda':
            train_set.write(tam_Knda25[0])
            #print('line:',tam_Knda25[0])
            tam_Knda25.pop(0)
        elif choose == 'tam_Mlym':
            train_set.write(tam_Mlym25[0])
            #print('line:',tam_Mlym25[0])
            tam_Mlym25.pop(0)
        elif choose == 'tam_Taml':
            train_set.write(tam_Taml25[0])
            #print('line:',tam_Taml25[0])
            tam_Taml25.pop(0)
        elif choose == 'tel_Telu':
            train_set.write(tel_Telu25[0])
            #print('line:',tel_Telu25[0])
            tel_Telu25.pop(0)
        elif choose == 'tel_Knda':
            train_set.write(tel_Knda25[0])
            #print('line:',tel_Knda25[0])
            tel_Knda25.pop(0)
        elif choose == 'tel_Mlym':
            train_set.write(tel_Mlym25[0])
            #print('line:',tel_Mlym25[0])
            tel_Mlym25.pop(0)
        elif choose == 'tel_Taml':
            train_set.write(tel_Taml25[0])
            #print('line:',tel_Taml25[0])
            tel_Taml25.pop(0)
        elif choose == 'mal_Telu':
            train_set.write(mal_Telu25[0])
            #print('line:',mal_Telu25[0])
            mal_Telu25.pop(0)
        elif choose == 'mal_Knda':
            train_set.write(mal_Knda25[0])
            #print('line:',mal_Knda25[0])
            mal_Knda25.pop(0)
        elif choose == 'mal_Mlym':
            train_set.write(mal_Mlym25[0])
            #print('line:',mal_Mlym25[0])
            mal_Mlym25.pop(0)
        elif choose == 'mal_Taml':
            train_set.write(mal_Taml25[0])
            #print('line:',mal_Taml25[0])
            mal_Taml25.pop(0)
        elif choose == 'kan_Telu':
            train_set.write(kan_Telu25[0])
            #print('line:',kan_Telu25[0])
            kan_Telu25.pop(0)
        elif choose == 'kan_Knda':
            train_set.write(kan_Knda25[0])
            #print('line:',kan_Knda25[0])
            kan_Knda25.pop(0)
        elif choose == 'kan_Mlym':
            train_set.write(kan_Mlym25[0])
            print('line:',kan_Mlym25[0])
            kan_Mlym25.pop(0)
        else:
            train_set.write(kan_Taml25[0])
            #print('line:',kan_Taml25[0])
            kan_Taml25.pop(0)
            
        options.pop(options.index(choose))

train_set.close()
# verifying
f = open('../labelled_data/Upscaled/Percent_25/Upscaled25.train','r')
l = f.readlines()
print('new file has',len(l),'lines')




# 50% Training Set
train_set = open('../labelled_data/Upscaled/Percent_50/Upscaled50.train','w')

# now add the various lines to the training set, but mix it together
for i in range(498): # essentially for all train lines
    options = ['tam_Telu','tam_Knda','tam_Mlym','tam_Taml','tel_Telu','tel_Knda','tel_Mlym','tel_Taml','mal_Telu','mal_Knda','mal_Mlym','mal_Taml','kan_Telu','kan_Knda','kan_Mlym','kan_Taml']
    for j in range(16):
        choose = random.choice(options)
        if choose == 'tam_Telu':
            train_set.write(tam_Telu50[0])
            tam_Telu50.pop(0)
        elif choose == 'tam_Knda':
            train_set.write(tam_Knda50[0])
            tam_Knda50.pop(0)
        elif choose == 'tam_Mlym':
            train_set.write(tam_Mlym50[0])
            tam_Mlym50.pop(0)
        elif choose == 'tam_Taml':
            train_set.write(tam_Taml50[0])
            tam_Taml50.pop(0)
        elif choose == 'tel_Telu':
            train_set.write(tel_Telu50[0])
            tel_Telu50.pop(0)
        elif choose == 'tel_Knda':
            train_set.write(tel_Knda50[0])
            tel_Knda50.pop(0)
        elif choose == 'tel_Mlym':
            train_set.write(tel_Mlym50[0])
            tel_Mlym50.pop(0)
        elif choose == 'tel_Taml':
            train_set.write(tel_Taml50[0])
            tel_Taml50.pop(0)
        elif choose == 'mal_Telu':
            train_set.write(mal_Telu50[0])
            mal_Telu50.pop(0)
        elif choose == 'mal_Knda':
            train_set.write(mal_Knda50[0])
            mal_Knda50.pop(0)
        elif choose == 'mal_Mlym':
            train_set.write(mal_Mlym50[0])
            mal_Mlym50.pop(0)
        elif choose == 'mal_Taml':
            train_set.write(mal_Taml50[0])
            mal_Taml50.pop(0)
        elif choose == 'kan_Telu':
            train_set.write(kan_Telu50[0])
            kan_Telu50.pop(0)
        elif choose == 'kan_Knda':
            train_set.write(kan_Knda50[0])
            kan_Knda50.pop(0)
        elif choose == 'kan_Mlym':
            train_set.write(kan_Mlym50[0])
            kan_Mlym50.pop(0)
        else:
            train_set.write(kan_Taml50[0])
            kan_Taml50.pop(0)
            
        options.pop(options.index(choose))

train_set.close()
# verifying
f = open('../labelled_data/Upscaled/Percent_50/Upscaled50.train','r')
l = f.readlines()
print('new file has',len(l),'lines')





# 75% Training Set
train_set = open('../labelled_data/Upscaled/Percent_75/Upscaled75.train','w')

# now add the various lines to the training set, but mix it together
for i in range(747): # essentially for all train lines
    options = ['tam_Telu','tam_Knda','tam_Mlym','tam_Taml','tel_Telu','tel_Knda','tel_Mlym','tel_Taml','mal_Telu','mal_Knda','mal_Mlym','mal_Taml','kan_Telu','kan_Knda','kan_Mlym','kan_Taml']
    for j in range(16):
        choose = random.choice(options)
        if choose == 'tam_Telu':
            train_set.write(tam_Telu75[0])
            tam_Telu75.pop(0)
        elif choose == 'tam_Knda':
            train_set.write(tam_Knda75[0])
            tam_Knda75.pop(0)
        elif choose == 'tam_Mlym':
            train_set.write(tam_Mlym75[0])
            tam_Mlym75.pop(0)
        elif choose == 'tam_Taml':
            train_set.write(tam_Taml75[0])
            tam_Taml75.pop(0)
        elif choose == 'tel_Telu':
            train_set.write(tel_Telu75[0])
            tel_Telu75.pop(0)
        elif choose == 'tel_Knda':
            train_set.write(tel_Knda75[0])
            tel_Knda75.pop(0)
        elif choose == 'tel_Mlym':
            train_set.write(tel_Mlym75[0])
            tel_Mlym75.pop(0)
        elif choose == 'tel_Taml':
            train_set.write(tel_Taml75[0])
            tel_Taml75.pop(0)
        elif choose == 'mal_Telu':
            train_set.write(mal_Telu75[0])
            mal_Telu75.pop(0)
        elif choose == 'mal_Knda':
            train_set.write(mal_Knda75[0])
            mal_Knda75.pop(0)
        elif choose == 'mal_Mlym':
            train_set.write(mal_Mlym75[0])
            mal_Mlym75.pop(0)
        elif choose == 'mal_Taml':
            train_set.write(mal_Taml75[0])
            mal_Taml75.pop(0)
        elif choose == 'kan_Telu':
            train_set.write(kan_Telu75[0])
            kan_Telu75.pop(0)
        elif choose == 'kan_Knda':
            train_set.write(kan_Knda75[0])
            kan_Knda75.pop(0)
        elif choose == 'kan_Mlym':
            train_set.write(kan_Mlym75[0])
            kan_Mlym75.pop(0)
        else:
            train_set.write(kan_Taml75[0])
            kan_Taml75.pop(0)
            
        options.pop(options.index(choose))

train_set.close()
# verifying
f = open('../labelled_data/Upscaled/Percent_75/Upscaled75.train','r')
l = f.readlines()
print('new file has',len(l),'lines')
