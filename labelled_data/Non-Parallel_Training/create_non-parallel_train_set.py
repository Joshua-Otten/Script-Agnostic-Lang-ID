# creates non-parallel training files from first 997 lines of each data set

# Telugu
f = open('te.txt','r')
n = open('Telugu/tel_Telu_non-parallel.txt','w')

line = f.readline()
for i in range(997):
    n.write(line)
    line = f.readline()

f.close()
n.close()

# Tamil
f = open('ta.txt','r')
n = open('Tamil/tam_Taml_non-parallel.txt','w')

line = f.readline()
for i in range(997):
	n.write(line)
	line = f.readline()

f.close()
n.close()

# Malayalam
f = open('ml.txt','r')
n = open('Malayalam/mal_Mlym_non-parallel.txt','w')

line = f.readline()
for i in range(997):
    n.write(line)
    line = f.readline()

f.close()
n.close()

# For Kannada, we use the FLORES 200 sentences


