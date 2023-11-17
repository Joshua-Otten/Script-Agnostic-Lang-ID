import fasttext

model = fasttext.train_supervised(input="../labelled_data/Upscaled/Upscale.train")
model.save_model("../upscaled_model.bin")
print('complete dataset:')
print(model.test("../labelled_data/Upscaled/Upscale.test"))

# 25% of the dataset
model = fasttext.train_supervised(input="../labelled_data/Upscaled/Percent_25/Upscaled25.train")
model.save_model("../upscaled_model25.bin")
print('25% of the training data:')
print(model.test("../labelled_data/Upscaled/Upscale.test"))

# 50% of the dataset
model = fasttext.train_supervised(input="../labelled_data/Upscaled/Percent_50/Upscaled50.train")
model.save_model("../upscaled_model50.bin")
print('50% of the training data:')
print(model.test("../labelled_data/Upscaled/Upscale.test"))

# 75% of the dataset
model = fasttext.train_supervised(input="../labelled_data/Upscaled/Percent_75/Upscaled75.train")
model.save_model("../upscaled_model75.bin")
print('75% of the training data:')
print(model.test("../labelled_data/Upscaled/Upscale.test"))
