
import cld3
import langid
from pyfranc import franc
import fasttext 

# The main selection data will be performance on the training corpus (clean FLORES200)
SELECTION_DATA = "../labelled_data/baseline.train"

accuracies = {
    'cld3': 0,
    'langid.py': 0,
    'franc': 0,
    'fasttext': 0,
    'heliots': 0
}

cld3_maps = {
    'ta': '__label__tam',
    'kn': '__label__kan',
    'ml': '__label__mal',
    'te': '__label__tel',
}

fasttext_model = fasttext.load_model("../models/lid.176.ftz")

with open(SELECTION_DATA, "r") as read_data:
    data = read_data.readlines()
    length_data = len(data)
    for x in data:
        label = x.split(' ')[0]
        text = "".join(x.split(' ')[1:]).strip()
        
        # Model1 cld3
        cld3_pred_raw = cld3.get_language(text)[0]
        if cld3_pred_raw in cld3_maps.keys():
            cld3_pred_mapped = cld3_maps[cld3_pred_raw]
            if cld3_pred_mapped == label:
                accuracies['cld3'] += 1
            
        # Model2 langid.py
        langid_pred_raw = langid.classify(text)[0]
        if langid_pred_raw in cld3_maps.keys():
            langid_pred_mapped = cld3_maps[langid_pred_raw]
            if langid_pred_mapped == label:
                accuracies['langid.py'] += 1
        
        # Model3 franc
        franc_pred_mapped = "__label__" + franc.lang_detect(text)[0][0]
        if franc_pred_mapped == label:
            accuracies['franc'] += 1
        
        # Model4 fasttext
        fasttext_pred_raw = fasttext_model.predict(text)[0][0].replace("__label__","")
        if fasttext_pred_raw in cld3_maps.keys():
            fasttext_pred_mapped =  cld3_maps[fasttext_pred_raw]
            if fasttext_pred_mapped == label:
                accuracies['fasttext'] += 1
            
        
# Model5 HeliOTS 
with open("../labelled_data/heliots/baseline_predictions.train.heliots", "r") as heliots_pred_fp:
    preds_heliots = heliots_pred_fp.readlines()
    for i in range(len(preds_heliots)):
        preds_heliots[i] = "__label__" + preds_heliots[i]

with open("../labelled_data/heliots/baseline_labels.train.heliots", "r") as heliots_labels_fp:
    labels_heliots = heliots_labels_fp.readlines()
     
for i in range(len(labels_heliots)):
    if labels_heliots[i] == preds_heliots[i]:
        accuracies['heliots'] += 1
         
print("CLD3", accuracies['cld3']/length_data)
print("LangID.py", accuracies['langid.py']/length_data)
print("Franc", accuracies['franc']/length_data)
print("fastText", accuracies['fasttext']/length_data)
print("HeliOTS", accuracies['heliots']/length_data)
    
    
    