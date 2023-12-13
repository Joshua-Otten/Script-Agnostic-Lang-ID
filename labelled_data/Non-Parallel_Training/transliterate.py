# Code to transliterate files (specifically Tamil and Malayalam to the other four languages, for both dev and devtest sets
# must: 'pip install aksharamukha'

from aksharamukha import transliterate

# tamil file
tamil = open('Tamil/tam_Taml_non-parallel.txt','r')
malayalam = open('Tamil/tam_Mlym_non-parallel.txt','w')
kannada = open('Tamil/tam_Knda_non-parallel.txt','w')
telugu = open('Tamil/tam_Telu_non-parallel.txt','w')
lines = tamil.readlines()
for line in lines:
    malayalam.write(transliterate.process('Tamil','Malayalam',line, True))
    kannada.write(transliterate.process('Tamil','Kannada',line, True))
    telugu.write(transliterate.process('Tamil','Telugu',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()


# malayalam file
malayalam = open('Malayalam/mal_Mlym_non-parallel.txt','r')
tamil = open('Malayalam/mal_Taml_non-parallel.txt','w')
kannada = open('Malayalam/mal_Knda_non-parallel.txt','w')
telugu = open('Malayalam/mal_Telu_non-parallel.txt','w')
lines = malayalam.readlines()
for line in lines:
    tamil.write(transliterate.process('Malayalam','Tamil',line, True))
    kannada.write(transliterate.process('Malayalam','Kannada',line, True))
    telugu.write(transliterate.process('Malayalam','Telugu',line, True))

malayalam.close()
tamil.close()
kannada.close()
telugu.close()


# telugu file
telugu = open('Telugu/tel_Telu_non-parallel.txt','r')
tamil = open('Telugu/tel_Taml_non-parallel.txt','w')
malayalam = open('Telugu/tel_Mlym_non-parallel.txt','w')
kannada = open('Telugu/tel_Knda_non-parallel.txt','w')
lines = telugu.readlines()
for line in lines:
    malayalam.write(transliterate.process('Telugu','Malayalam',line, True))
    kannada.write(transliterate.process('Telugu','Kannada',line, True))
    tamil.write(transliterate.process('Telugu','Tamil',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()

