import fasttext
from huggingface_hub import hf_hub_download

# Predict in loop. Save the outputs. Compare to gold labels to produce scores (script-wise)
def accuracy(data, model):
    correct = {}
    total = {}
    for line in data:
        label = line[0]
        sentence = line[1]
        prediction = model.predict(sentence.strip("\n"))[0][0]
        prediction = prediction[:12]
        
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
    

model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
model = fasttext.load_model(model_path)
model.save_model("../models/wiki_model.bin")


# test on Noiseless Data
model = fasttext.load_model(f"../models/wiki_model.bin")
with open(f"../labelled_data/noiseless.test", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Test on Noiseless Data")
accuracy(data, model)

# test on Upscaled Data (from Flores 200)
model = fasttext.load_model(f"../models/wiki_model.bin")
with open(f"../labelled_data/Upscaled/upscale.test", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
print("Test on the Upscaled test set (all scripts)")
accuracy(data, model)

# test on UDHR Data
model = fasttext.load_model(f"../models/wiki_model.bin")
with open(f"../labelled_data/UDHR/udhr.test", "r") as f:
        data = [(x.split(" ")[0], " ".join(x.split(" ")[1:])) for x in f.readlines()]
accuracy(data, model)
