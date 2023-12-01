from datasets import load_dataset

n = open('../labelled_data/UDHR/udhr2.test','w')

dataset = load_dataset('cis-lmu/udhr-lid',split='test')
count = {}
count['tel'] = 0
count['mal'] = 0
count['tam'] = 0
count['kan'] = 0
for x in dataset:
    if x['iso639-3'] in count.keys():
        count[x['iso639-3']] += 1
        n.write('__label__'+x['iso639-3']+' '+x['sentence']+'\n')
print(count)
n.close()

