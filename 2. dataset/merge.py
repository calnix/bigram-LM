import os
# find all the txt files in the dataset folder
inputs = []
for file in os.listdir("Dashlane"):
    if file.endswith(".txt"):
        inputs.append(os.path.join("Dashlane", file))

# concatanate all txt files in a file called merged_file.txt
with open('merged_dash.txt', 'w') as outfile:
    for fname in inputs:
        with open(fname, encoding="utf-8", errors='ignore') as infile:
            outfile.write(infile.read())