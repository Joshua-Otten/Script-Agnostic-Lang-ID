import fasttext

scripts = ["Taml", "Mlym", "Knda", "Telu"]
for script in scripts:
    model = fasttext.train_supervised(input="../labelled_data/Flatten/flatten_all_" + script + ".dev")
    model.save_model("../models/flatten_model_" + script + ".bin")

    # Training Accuracy (96+)
    print(model.test("../labelled_data/Flatten/flatten_all_" + script + ".dev"))
