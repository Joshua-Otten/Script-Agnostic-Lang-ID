import fasttext
fasttext.FastText.eprint = lambda x: None

separate = fasttext.load_model('../models/separate_model.bin')

print('Testing Baseline on noiseless data:')


# Read noiseless data and predict separately with label. 
actual = {
    '__label__tam': 0,
    '__label__kan': 0,
    '__label__mal': 0,
    '__label__tel': 0
}

predicted = {
    '__label__tam': 0,
    '__label__kan': 0,
    '__label__mal': 0,
    '__label__tel': 0
}


with open("../labelled_data/UDHR/udhr.test", "r") as read_fp:
    lines = read_fp.readlines()
    for line in lines:
        label = line.split(' ')[0]
        text = "".join(line.split(' ')[1:]).strip()
        
        response = separate.predict(text)
        predicted_label = response[0][0]

        actual[label] += 1        
        if label in predicted_label:
            predicted[label] += 1
    
    overall = 0
    overall_denom = 0
    for langlabel in actual.keys():
        acc = predicted[langlabel]/actual[langlabel]
        print("accuracy: ", acc)
        
        overall_denom += actual[langlabel]
        overall += predicted[langlabel]

    print("overall acc", overall/overall_denom)
    
# print('Testing Baseline on separate-devtest data:')
print(separate.test("../labelled_data/Separate/separate.devtest"))

# print('Testing Baseline on UDHR test data')
# print(separate.test("../labelled_data/UDHR/udhr.test"))




