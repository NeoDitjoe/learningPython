dictionary_example = {
  "key1": "value 1",
  "key2": "value2",
  "key3": "value3"
}

dictionary_example['name'] = 'Neo'
dictionary_example['age'] = 24

print(dictionary_example)
print("My name is %s" %(dictionary_example["name"]))
print("And by the way I'm %i and %s" %(dictionary_example["age"], dictionary_example["key1"]))