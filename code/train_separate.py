import fasttext

# NOTE: want skipgram model, but not specified directly in the code
model = fasttext.train_supervised(input="../labelled_data/Separate/separate.dev", autotuneValidationFile="../labelled_data/Separate/separate.dev",autotuneDuration=5)
model.save_model("../models/separate_model.bin")