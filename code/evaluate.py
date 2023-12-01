import fasttext 

# Monkeypatch 
fasttext.FastText.eprint = lambda x: None

 # Predict in loop. Save the outputs. Compare to gold labels to produce scores (script-wise)
def accuracy(data, model, name=""):
    correct = {}
    total = {}
    for line in data:
        label = line[0]
        sentence = line[1]
        prediction = model.predict(sentence.strip("\n"))[0][0]
        if label in total.keys():
            total[label] += 1
        else:
            total[label] = 1
        if prediction == label:
            if prediction in correct.keys():
                correct[prediction] += 1
            else:
                correct[prediction] = 1

    vals = [ ]
    for k in ["__label__tam", "__label__kan", "__label__mal", "__label__tel"]:
        try:
            v = correct[k]*100/total[k]
            print(f"{k}: {v:.2f}", end = "\t")
            vals.append(v)
        except KeyError:
            print(f"{k}: None ", end = "\t" )
            vals.append(0)
    print(f"Average ({name}): {sum(vals)/4:.2f}")
    return vals
    
def flattenresults():
    print("\nResults for Flatten experiment")
    model_base = fasttext.load_model(f"../models/baseline_model.bin")
    for script in ["Taml", "Knda", "Mlym", "Telu"]:
        model = fasttext.load_model(f"../models/flatten_model_{script}.bin")
        with open(f"../labelled_data/Flatten/flatten_all_{script}.devtest", "r") as f:
            data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
        accuracy(data, model_base, "baseline")
        accuracy(data, model, f"flatten-{script}")
 
def noiseresults():
    print("\nResults for Noise Experiment")
    results = {}
    results['baseline'] = []
    results['n25'] = []
    results['n50'] = []
    results['n75'] = []
    results['n100'] = []
    results['all'] = []
    results['upscale'] = []
    
    modelbase =  fasttext.load_model(f"../models/baseline_model.bin")
    modelupscale = fasttext.load_model(f"../models/upscaled_model.bin")
    n25 = fasttext.load_model(f"../models/noisy_model_25.bin")
    n50 = fasttext.load_model(f"../models/noisy_model_50.bin")
    n75 = fasttext.load_model(f"../models/noisy_model_75.bin")
    n100 = fasttext.load_model(f"../models/noisy_model_100.bin")
    nall = fasttext.load_model(f"../models/noisy_model_all.bin")

    # clean
    print(f"Dataset: Upscale")
    with open(f"../labelled_data/Upscaled/Upscale.test", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
    results['baseline'] += accuracy(data, modelbase, "baseline")
    results['upscale'] += accuracy(data, modelupscale, "upscale")
    results['n25'] += accuracy(data, n25, "n@25")
    results['n50'] += accuracy(data, n50, "n@50")
    results['n75'] += accuracy(data, n75, "n@75")
    results['n100'] += accuracy(data, n100, "n@100")
    results['all'] += accuracy(data, nall, "n@all")

    for dataset in ["25", "50", "75", "100", "all"]:
        print(f"Dataset: Noise@{dataset}")
        with open(f"../labelled_data/Noise/noise_{dataset}.devtest", "r") as f:
            data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
    
        results['baseline'] += accuracy(data, modelbase, "baseline")
        results['upscale'] += accuracy(data, modelupscale, "upscale")
        results['n25'] += accuracy(data, n25, "n@25")
        results['n50'] += accuracy(data, n50, "n@50")
        results['n75'] += accuracy(data, n75, "n@75")
        results['n100'] += accuracy(data, n100, "n@100")
        results['all'] += accuracy(data, nall, "n@all")
            
    print("\n")
    for key in results.keys():
        print(f"{key}: {sum(results[key])/len(results[key]):.2f}", end = "\t")
    print("\n")
# Generate Results for Table 2: Flatten
flattenresults()

# Generate Results for Table 4: Noise
noiseresults()

model = fasttext.load_model("../models/upscaled_model.bin")
with open("../labelled_data/Upscaled/upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Accuracy for 'all' scripts")
accuracy(data, model)

   