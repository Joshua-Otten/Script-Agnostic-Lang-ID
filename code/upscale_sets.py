# this compiles upscaled training data
import random

# training set data
# similar to train_baseline.py, but compiling data for the upscaling experiment

# reading in the data
##########################
# first Tamil
train_set = open('../labelled_data/Upscaled/upscale_tam.dev','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Tamil/labelled_tam_Taml.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Tamil/labelled_tam_Telu.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Tamil/labelled_tam_Mlym.dev','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Tamil/labelled_tam_Knda.dev','r')
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
f = open('../labelled_data/Upscaled/upscale_tam.dev','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##########################
# now Telugu

# reading in the data
train_set = open('../labelled_data/Upscaled/upscale_tel.dev','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Telugu/labelled_tel_Taml.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Telugu/labelled_tel_Telu.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Telugu/labelled_tel_Mlym.dev','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Telugu/labelled_tel_Knda.dev','r')
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
f = open('../labelled_data/Upscaled/upscale_tel.dev','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##############################
# next is Malayalam

# reading in the data
train_set = open('../labelled_data/Upscaled/upscale_mal.dev','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Malayalam/labelled_mal_Taml.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Malayalam/labelled_mal_Telu.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Malayalam/labelled_mal_Mlym.dev','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Malayalam/labelled_mal_Knda.dev','r')
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
f = open('../labelled_data/Upscaled/upscale_mal.dev','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()

##################################
# Lastly, Kannada
# reading in the data
train_set = open('../labelled_data/Upscaled/upscale_kan.dev','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Kannada/labelled_kan_Taml.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Kannada/labelled_kan_Telu.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Kannada/labelled_kan_Mlym.dev','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Kannada/labelled_kan_Knda.dev','r')
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
f = open('../labelled_data/Upscaled/upscale_kan.dev','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()



################################
# Finally, compile all of these upscaled dev sets into one training set
################################


# reading in the data
train_set = open('../labelled_data/Upscaled/Upscale.train','w')
# start with the Tamil script
tamil_file = open('../labelled_data/Upscaled/upscale_tam.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Upscaled/upscale_tel.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Upscaled/upscale_mal.dev','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Upscaled/upscale_kan.dev','r')
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
f = open('../labelled_data/Upscaled/Upscale.train','r')
l = f.readlines()
print('length of the new set is',len(l),'which is four times',lang_lines)
f.close()
