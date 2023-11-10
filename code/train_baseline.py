import fasttext

# NOTE: want skipgram model, but not specified directly in the code
model = fasttext.train_supervised(input="../labelled_data/baseline.train")
model.save_model("../baseline_model.bin")

