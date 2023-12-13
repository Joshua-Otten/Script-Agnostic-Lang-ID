import fasttext
from datasets import load_dataset
from huggingface_hub import hf_hub_download

fasttext.FastText.eprint = lambda x: None
dataset = load_dataset('cis-lmu/GlotStoryBook')

overall_data = []
data = {}
data['tam'] = []
data['mal'] = []
data['kan'] = []
data['tel'] = []
for x in dataset['train']:
    code = x['ISO639-3']
    if code in data.keys():
        data[code].append(x['Text'])
print("Language  Data-Length")
for x in data.keys():
    print(x, len(data[x]))
    
for pair in [('mal', 'Mlym'), ('tam', 'Taml'),('tel', 'Telu'), ('kan', 'Knda')]: 
    overall_data.append((data[pair[0]], f'__label__{pair[0]}',f'__label__{pair[0]}_{pair[1]}' ))
    
model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
fasttextwiki = fasttext.load_model(model_path)
modelbase =  fasttext.load_model(f"../models/baseline_model.bin")
modelupscale = fasttext.load_model(f"../models/upscaled_model.bin")
nall = fasttext.load_model(f"../models/noisy_model_all.bin")
flatten = fasttext.load_model(f"../models/flatten_model_Telu.bin")
non_parallel = fasttext.load_model(f"../models/non-parallel_upscaled_model.bin")

# # test on GlotStorybooks
results = {}
results['baseline'] = []
results['upscale'] = []
results['flatten'] = []
results['noise'] = []
results['wiki'] = []
results['nonparallel'] = []

print("\nTesting on GlotStorybooks")
print("Model:  Accuracy")
for key in [('nonparallel',non_parallel)]:#[('baseline', modelbase), ('upscale',modelupscale), ('flatten',flatten), ('noise',nall), ('wiki', fasttextwiki),('nonparallel', non_parallel)]:[('baseline', modelbase), ('upscale',modelupscale), ('flatten',flatten), ('noise',nall), ('wiki', fasttextwiki)]:
    for entry in overall_data:
        entry_data = entry[0]
        gold = entry[1]
        gold2 = entry[2]
        acc = 0
        for x in entry_data: 
            pred = key[1].predict(x.replace("\n"," "))[0][0]
            if pred == gold or pred == gold2:
                acc += 1
        acc = acc/len(entry_data)
        results[key[0]].append(acc)
    print(f"{key[0]}: {sum(results[key[0]])*100/4:.2f}")
