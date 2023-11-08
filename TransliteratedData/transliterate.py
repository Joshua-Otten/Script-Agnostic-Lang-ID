# Code to transliterate files (specifically Tamil and Malayalam to the other four languages, for both dev and devtest sets
# must: 'pip install aksharamukha'

from aksharamukha import transliterate

# tamil .dev
tamil = open('tam_Taml.dev','r')
malayalam = open('tam_Mlym.dev','w')
kannada = open('tam_Knda.dev','w')
telugu = open('tam_Telu.dev','w')
lines = tamil.readlines()
for line in lines:
    malayalam.write(transliterate.process('Tamil','Malayalam',line, True))
    kannada.write(transliterate.process('Tamil','Kannada',line, True))
    telugu.write(transliterate.process('Tamil','Telugu',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()

# tamil .devtest
tamil = open('tam_Taml.devtest','r')
malayalam = open('tam_Mlym.devtest','w')
kannada = open('tam_Knda.devtest','w')
telugu = open('tam_Telu.devtest','w')
lines = tamil.readlines()
for line in lines:
    malayalam.write(transliterate.process('Tamil','Malayalam',line, True))
    kannada.write(transliterate.process('Tamil','Kannada',line, True))
    telugu.write(transliterate.process('Tamil','Telugu',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()


# malayalam .dev
malayalam = open('mal_Mlym.dev','r')
tamil = open('mal_Taml.dev','w')
kannada = open('mal_Knda.dev','w')
telugu = open('mal_Telu.dev','w')
lines = malayalam.readlines()
for line in lines:
    tamil.write(transliterate.process('Malayalam','Tamil',line, True))
    kannada.write(transliterate.process('Malayalam','Kannada',line, True))
    telugu.write(transliterate.process('Malayalam','Telugu',line, True))

malayalam.close()
tamil.close()
kannada.close()
telugu.close()

# malayalam .devtest
malayalam = open('mal_Mlym.devtest','r')
tamil = open('mal_Taml.devtest','w')
kannada = open('mal_Knda.devtest','w')
telugu = open('mal_Telu.devtest','w')
lines = malayalam.readlines()
for line in lines:
    tamil.write(transliterate.process('Malayalam','Tamil',line, True))
    kannada.write(transliterate.process('Malayalam','Kannada',line, True))
    telugu.write(transliterate.process('Malayalam','Telugu',line, True))

malayalam.close()
tamil.close()
kannada.close()
telugu.close()


# telugu .dev
telugu = open('tel_Telu.dev','r')
tamil = open('tel_Taml.dev','w')
malayalam = open('tel_Mlym.dev','w')
kannada = open('tel_Knda.dev','w')
lines = telugu.readlines()
for line in lines:
    malayalam.write(transliterate.process('Telugu','Malayalam',line, True))
    kannada.write(transliterate.process('Telugu','Kannada',line, True))
    tamil.write(transliterate.process('Telugu','Tamil',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()

# telugu .devtest
telugu = open('tel_Telu.devtest','r')
tamil = open('tel_Taml.devtest','w')
malayalam = open('tel_Mlym.devtest','w')
kannada = open('tel_Knda.devtest','w')
lines = telugu.readlines()
for line in lines:
    malayalam.write(transliterate.process('Telugu','Malayalam',line, True))
    kannada.write(transliterate.process('Telugu','Kannada',line, True))
    tamil.write(transliterate.process('Telugu','Tamil',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()


# kannada .dev
kannada = open('kan_Knda.dev','r')
telugu = open('kan_Telu.dev','w')
tamil = open('kan_Taml.dev','w')
malayalam = open('kan_Mlym.dev','w')
lines = kannada.readlines()
for line in lines:
    malayalam.write(transliterate.process('Kannada','Malayalam',line, True))
    telugu.write(transliterate.process('Kannada','Telugu',line, True))
    tamil.write(transliterate.process('Kannada','Tamil',line, True))

tamil.close()
malayalam.close()
kannada.close()
telugu.close()

# kannada .devtest
print('about to start')
kannada = open('kan_Knda.devtest','r')
telugu = open('kan_Telu.devtest','w')
tamil = open('kan_Taml.devtest','w')
malayalam = open('kan_Mlym.devtest','w')
print('opened the files')
lines = kannada.readlines()
for line in lines:
    malayalam.write(transliterate.process('Kannada','Malayalam',line, True))
    tamil.write(transliterate.process('Kannada','Tamil',line, True))
    telugu.write(transliterate.process('Kannada','Telugu',line, True))
print('done, ready to close')
tamil.close()
malayalam.close()
kannada.close()
telugu.close()
