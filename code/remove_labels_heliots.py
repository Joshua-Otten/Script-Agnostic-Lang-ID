labels = []
with open("../labelled_data/baseline.train", "r") as read_file:
    data = read_file.readlines()
    for i in range(len(data)):
        labels.append(data[i].split(' ')[0])
        data[i] = "".join(data[i].split(' ')[1:]  )   
    
with open("../labelled_data/baseline_nolabels.train.heliots", "w") as out_file:
    for x in data:
        out_file.write(x)

with open("../labelled_data/baseline_labels.train.heliots", "w") as out_file:
    for x in labels:
        out_file.write(x + "\n")
        