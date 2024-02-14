sample_dict = {
    "name":"John",
    "age":12,
    "city":"Dublin"
}
#printing dictionary
print(sample_dict)
print(sample_dict["name"])
print(sample_dict["city"])

#get the list of keys
print(sample_dict.keys())
#get the list of values
print(sample_dict.values())

#adding new key and value pair
sample_dict["profession"]="baker"
print(sample_dict)

#delete a key and value pair
del(sample_dict["profession"])
print(sample_dict)

#change a value of the dictionary
sample_dict["city"]="Columbus"
print(sample_dict)

#creating list as a value of dictionary
sample_dict["marks"]=[98.97, 98.73, 103.87, 99.56]
print(sample_dict)
print(sample_dict["marks"])
print(sample_dict["marks"][1])
print(sample_dict["marks"][3])

#creating a nested dictionary
classroom = {
    "sam":{
        "age":11, 
        "marks":[99.73,92.65,96.58,98.93,90.12]
    },
    "peter":{
        "age":12,
        "marks":[89.73,91.27,97.72,95.37,79.34]
    }
}
print(classroom)
print(classroom["sam"])
print(classroom["peter"]["marks"])
print(classroom["peter"]["marks"][3])