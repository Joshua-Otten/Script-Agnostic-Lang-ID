import json 
import fasttext
from huggingface_hub import hf_hub_download
fasttext.FastText.eprint = lambda x: None

overall_data = []
for pair in [('mal', 'Mlym'), ('tam', 'Taml'),('tel', 'Telu')]: #('kan', 'Knda'), 
    with open(f"../labelled_data/LIMIT/{pair[0]}.txt") as f:
        test_data = [x.strip() for x in f.readlines()]
        overall_data.append((test_data, f'__label__{pair[0]}',f'__label__{pair[0]}_{pair[1]}' ))

model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
fasttextwiki = fasttext.load_model(model_path)
modelbase =  fasttext.load_model(f"../models/baseline_model.bin")
modelupscale = fasttext.load_model(f"../models/upscaled_model.bin")
nall = fasttext.load_model(f"../models/noisy_model_all.bin")
flatten = fasttext.load_model(f"../models/flatten_model_Telu.bin")

print("Overall Data Length (LIMIT): ", sum([len(x[0]) for x in overall_data]))

results = {}
results['baseline'] = []
results['upscale'] = []
results['flatten'] = []
results['noise'] = []
results['wiki'] = []

print("\nEvaluating all models on LIMIT")
print("Model: Accuracy")
for key in [('baseline', modelbase), ('upscale',modelupscale), ('flatten',flatten), ('noise',nall), ('wiki', fasttextwiki)]:
    for entry in overall_data:
        entry_data = entry[0]
        gold = entry[1]
        gold2 = entry[2]
        acc = 0
        for x in entry_data: 
            pred = key[1].predict(x)[0][0]
            if pred == gold or pred == gold2:
                acc += 1
        acc = acc/len(entry_data)
        results[key[0]].append(acc)
    print(f"{key[0]}: {sum(results[key[0]])*100/4:.2f}")
