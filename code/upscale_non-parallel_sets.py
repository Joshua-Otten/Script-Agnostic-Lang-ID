# this compiles Non-Parallel_Training training data
import random

# training set data
# similar to train_baseline.py, but compiling data for the upscaling experiment

# reading in the data
##########################
# first Tamil
train_set = open('../labelled_data/Non-Parallel_Training/upscale_tam_non-parallel.txt','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Non-Parallel_Training/Tamil/labelled_tam_Taml_non-parallel.txt','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Non-Parallel_Training/Tamil/labelled_tam_Telu_non-parallel.txt','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Non-Parallel_Training/Tamil/labelled_tam_Mlym_non-parallel.txt','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Non-Parallel_Training/Tamil/labelled_tam_Knda_non-parallel.txt','r')
kannada = kannada_file.readlines()
kannada_file.close()

lang_lines = len(telugu)
# now add the various lines to the training set, but mix it together
for i in range(len(tamil)): # essentially for all train lines
    options = ['tamil','telugu','malayalam','kannada']
    for j in range(4):
        choose = random.choice(options)
        if choose == 'tamil':
            train_set.write(tamil[0])
            tamil.pop(0)
        elif choose == 'telugu':
            train_set.write(telugu[0])
            telugu.pop(0)
        elif choose == 'malayalam':
            train_set.write(malayalam[0])
            malayalam.pop(0)
        else:
            train_set.write(kannada[0])
            kannada.pop(0)
        options.pop(options.index(choose))


train_set.close()

# for verification:
f = open('../labelled_data/Non-Parallel_Training/upscale_tam_non-parallel.txt','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##########################
# now Telugu

# reading in the data
train_set = open('../labelled_data/Non-Parallel_Training/upscale_tel_non-parallel.txt','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Non-Parallel_Training/Telugu/labelled_tel_Taml_non-parallel.txt','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Non-Parallel_Training/Telugu/labelled_tel_Telu_non-parallel.txt','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Non-Parallel_Training/Telugu/labelled_tel_Mlym_non-parallel.txt','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Non-Parallel_Training/Telugu/labelled_tel_Knda_non-parallel.txt','r')
kannada = kannada_file.readlines()
kannada_file.close()

lang_lines = len(telugu)
# now add the various lines to the training set, but mix it together
for i in range(len(tamil)): # essentially for all train lines
    options = ['tamil','telugu','malayalam','kannada']
    for j in range(4):
        choose = random.choice(options)
        if choose == 'tamil':
            train_set.write(tamil[0])
            tamil.pop(0)
        elif choose == 'telugu':
            train_set.write(telugu[0])
            telugu.pop(0)
        elif choose == 'malayalam':
            train_set.write(malayalam[0])
            malayalam.pop(0)
        else:
            train_set.write(kannada[0])
            kannada.pop(0)
        options.pop(options.index(choose))


train_set.close()

# for verification:
f = open('../labelled_data/Non-Parallel_Training/upscale_tel_non-parallel.txt','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##############################
# next is Malayalam

# reading in the data
train_set = open('../labelled_data/Non-Parallel_Training/upscale_mal_non-parallel.txt','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Non-Parallel_Training/Malayalam/labelled_mal_Taml_non-parallel.txt','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Non-Parallel_Training/Malayalam/labelled_mal_Telu_non-parallel.txt','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Non-Parallel_Training/Malayalam/labelled_mal_Mlym_non-parallel.txt','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Non-Parallel_Training/Malayalam/labelled_mal_Knda_non-parallel.txt','r')
kannada = kannada_file.readlines()
kannada_file.close()

lang_lines = len(telugu)
# now add the various lines to the training set, but mix it together
for i in range(len(tamil)): # essentially for all train lines
    options = ['tamil','telugu','malayalam','kannada']
    for j in range(4):
        choose = random.choice(options)
        if choose == 'tamil':
            train_set.write(tamil[0])
            tamil.pop(0)
        elif choose == 'telugu':
            train_set.write(telugu[0])
            telugu.pop(0)
        elif choose == 'malayalam':
            train_set.write(malayalam[0])
            malayalam.pop(0)
        else:
            train_set.write(kannada[0])
            kannada.pop(0)
        options.pop(options.index(choose))


train_set.close()

# for verification:
f = open('../labelled_data/Non-Parallel_Training/upscale_mal_non-parallel.txt','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##################################
# Lastly, for Kannada we already have the FLORES200 training set, so there is nothing to do.


################################
# Finally, compile all of these Non-Parallel_Training dev sets into one training set
################################


# reading in the data
train_set = open('../labelled_data/Non-Parallel_Training/Upscale.train','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Non-Parallel_Training/upscale_tam_non-parallel.txt','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Non-Parallel_Training/upscale_tel_non-parallel.txt','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Non-Parallel_Training/upscale_mal_non-parallel.txt','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Non-Parallel_Training/upscale_kan_non-parallel.txt','r')
kannada = kannada_file.readlines()
kannada_file.close()

lang_lines = len(telugu)
# now add the various lines to the training set, but mix it together
for i in range(len(tamil)): # essentially for all train lines
    options = ['tamil','telugu','malayalam','kannada']
    for j in range(4):
        choose = random.choice(options)
        if choose == 'tamil':
            train_set.write(tamil[0])
            tamil.pop(0)
        elif choose == 'telugu':
            train_set.write(telugu[0])
            telugu.pop(0)
        elif choose == 'malayalam':
            train_set.write(malayalam[0])
            malayalam.pop(0)
        else:
            train_set.write(kannada[0])
            kannada.pop(0)
        options.pop(options.index(choose))


train_set.close()

# for verification:
f = open('../labelled_data/Non-Parallel_Training/Upscale.train','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

