# this compiles baseline training data, as well as noiseless testing data
import random

# training set data

# reading in the data
train_set = open('../labelled_data/baseline.train','w')
tamil_file = open('../labelled_data/Tamil/labelled_tam_Taml.dev','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Telugu/labelled_tel_Telu.dev','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Malayalam/labelled_mal_Mlym.dev','r')
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
f = open('../labelled_data/baseline.train','r')
l = f.readlines()
print('length of the new set is',len(l),'which should be four times',lang_lines)
f.close()


# reading in the data
test_set = open('../labelled_data/noiseless.test','w')
tamil_file = open('../labelled_data/Tamil/labelled_tam_Taml.devtest','r')
tamil = tamil_file.readlines()
tamil_file.close()
telugu_file = open('../labelled_data/Telugu/labelled_tel_Telu.devtest','r')
telugu = telugu_file.readlines()
telugu_file.close()
malayalam_file = open('../labelled_data/Malayalam/labelled_mal_Mlym.devtest','r')
malayalam = malayalam_file.readlines()
malayalam_file.close()
kannada_file = open('../labelled_data/Kannada/labelled_kan_Knda.devtest','r')
kannada = kannada_file.readlines()
kannada_file.close()

lang_lines = len(telugu)
# now add the various lines to the training set, but mix it together
for i in range(len(tamil)): # essentially for all train lines
    options = ['tamil','telugu','malayalam','kannada']
    for j in range(4):
        choose = random.choice(options)
        if choose == 'tamil':
            test_set.write(tamil[0])
            tamil.pop(0)
        elif choose == 'telugu':
            test_set.write(telugu[0])
            telugu.pop(0)
        elif choose == 'malayalam':
            test_set.write(malayalam[0])
            malayalam.pop(0)
        else:
            test_set.write(kannada[0])
            kannada.pop(0)
        options.pop(options.index(choose))


test_set.close()

# for verification:
f = open('../labelled_data/noiseless.test','r')
l = f.readlines()
print('length of the new set is',len(l),'which should be four times',lang_lines)
f.close()
