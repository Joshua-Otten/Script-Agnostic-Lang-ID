import fasttext 

# Monkeypatch 
fasttext.FastText.eprint = lambda x: None

 # Predict in loop. Save the outputs. Compare to gold labels to produce scores (script-wise)
def accuracy(data, model):
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
    for k in ["__label__tam", "__label__kan", "__label__mal", "__label__tel"]:
        print(f"{correct[k]*100/total[k]:.2f}")
    print()
    
for script in ["Taml", "Knda", "Mlym", "Telu"]:
    model = fasttext.load_model(f"../models/flatten_model_{script}.bin")
    with open(f"../labelled_data/Flatten/flatten_all_{script}.devtest", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
    print(f"Flatten Accuracy for Script = {script}")
    accuracy(data, model)
    
model = fasttext.load_model("../models/upscaled_model.bin")
with open("../labelled_data/Upscaled/upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Accuracy for Script=ALL")
accuracy(data, model)

   