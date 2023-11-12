import fasttext

model = fasttext.train_supervised(input="../labelled_data/Upscaled/Upscale.train")
model.save_model("../upscaled_model.bin")

print(model.test("../labelled_data/Upscaled/Upscale.test"))
