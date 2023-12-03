import fasttext
fasttext.FastText.eprint = lambda x: None

baseline = fasttext.load_model('../models/baseline_model.bin')
upscaled = fasttext.load_model('../models/upscaled_model.bin')

# Baseline model
print('Testing Baseline on noiseless data:')
print(baseline.test("../labelled_data/noiseless.test"))

print('Testing Baseline on all language test sets over all scripts:')
print(baseline.test("../labelled_data/Upscaled/Upscale.test"))

# Script-Upscaled model
print('Testing Script-Upscaled model on noiseless data:')
print(upscaled.test("../labelled_data/noiseless.test"))

print('Testing Script-Upscaled model on all language test sets over all scripts:')
print(upscaled.test("../labelled_data/Upscaled/Upscale.test"))
