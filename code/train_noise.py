import fasttext

noise = ["25", "50", "75", "100", "all"]
for n in noise:
    model = fasttext.train_supervised(input="../labelled_data/Noise/noise_" + n + ".dev")
    model.save_model("../models/noisy_model_" + n + ".bin")

    # Training Accuracy (96+)
    print(model.test("../labelled_data/Noise/noise_" + n + ".dev"))
