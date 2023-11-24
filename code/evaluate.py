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
    
def avg_accuracy(data, model):
    correct = 0
    total = 0
    for line in data:
        label = line[0]
        sentence = line[1]
        prediction = model.predict(sentence.strip("\n"))[0][0]
        if prediction == label:
            correct += 1
        total += 1
    print(100*correct/total)
    print()
    

for script in ["Taml", "Knda", "Mlym", "Telu"]:
    model = fasttext.load_model(f"../models/flatten_model_{script}.bin")
    with open(f"../labelled_data/Flatten/flatten_all_{script}.devtest", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
    print(f"Flatten Accuracy for Script = {script}")
    accuracy(data, model)


########## Upscale Testing ##############
# 25 percent
model = fasttext.load_model("../models/upscaled_model25.bin")
with open("../labelled_data/noiseless.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 25% training data, accuracy for noiseless test set")
accuracy(data, model)

model = fasttext.load_model("../models/upscaled_model25.bin")
with open("../labelled_data/Upscaled/Upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 25% training data, accuracy for complete test set")
accuracy(data, model)

# 50%
model = fasttext.load_model("../models/upscaled_model50.bin")
with open("../labelled_data/noiseless.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 50% training data, accuracy for noiseless test set")
accuracy(data, model)

model = fasttext.load_model("../models/upscaled_model50.bin")
with open("../labelled_data/Upscaled/Upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 50% training data, accuracy for complete test set")
accuracy(data, model)

# 75%
model = fasttext.load_model("../models/upscaled_model75.bin")
with open("../labelled_data/noiseless.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 75% training data, accuracy for noiceless test set")
accuracy(data, model)

model = fasttext.load_model("../models/upscaled_model75.bin")
with open("../labelled_data/Upscaled/Upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscaled on 75% training data, accuracy for complete test set")
accuracy(data, model)

# 100%
model = fasttext.load_model("../models/upscaled_model.bin")
with open("../labelled_data/noiseless.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscale Accuracy for noiseless test set")
accuracy(data, model)

model = fasttext.load_model("../models/upscaled_model.bin")
with open("../labelled_data/Upscaled/Upscale.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Upscale accuracy for complete test set")
accuracy(data, model)

model = fasttext.load_model("../models/noisy_model_all.bin")
with open("../labelled_data/noiseless.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Noisy Model for original FLORES set")
accuracy(data, model)


########## Testing Models on UDHR ##############

model = fasttext.load_model("../models/baseline_model.bin")
with open("../labelled_data/UDHR/udhr.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Baseline (flores) on UDHR")
avg_accuracy(data, model)

model = fasttext.load_model("../models/upscaled_model.bin")
with open("../labelled_data/UDHR/udhr.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Full Script-Upscaled model on UDHR")
avg_accuracy(data, model)

model = fasttext.load_model("../models/flatten_model_Telu.bin")
with open("../labelled_data/UDHR/udhr.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Model flattened on Telu evaluated on UDHR")
avg_accuracy(data, model)

model = fasttext.load_model("../models/noisy_model_all.bin")
with open("../labelled_data/UDHR/udhr.test", "r") as f:
    data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Noise ALL model on UDHR")
avg_accuracy(data, model)
