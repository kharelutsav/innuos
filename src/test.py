import json
with open("src\Data.json", "r") as read1:
    data1 = json.load(read1)

with open("TestData.json", "r") as read2:
    data2 = json.load(read2)

data1.update(data2)

print(data1)

with open("src\Data.json", "w") as read:
    read.write(json.dumps(data1, indent=4))

with open("src\Data.json", "r") as read3:
    data3 = json.load(read3)

print(data3)
