# Hash table collision handling using chaining
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t.arr)
print(t["march 6"])

nyc_weather = [
    ('Jan 1', 27),
    ('Jan 2', 31),
    ('Jan 3', 23),
    ('Jan 4', 34),
    ('Jan 5', 37),
    ('Jan 6', 38),
    ('Jan 7', 29),
    ('Jan 8', 30),
    ('Jan 9', 35),
    ('Jan 10', 30)]

# Exercise: Hash Table

# Write a program that can answer following,
# What was the average temperature in first week of Jan

# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

# A list would be the best data structures for this problem in order to use sum() and max()
temp = []
for weather in nyc_weather:
    temp.append(weather[1])
print('Week Average', sum(temp[:7])/8)
print('Max temp in the last 10 days was', max(temp))


# Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

# A dictionary (Hash table) would be the best data structure for fast searching using hashing
hash_table = HashTable()
for weather in nyc_weather:
    hash_table[weather[0]] = weather[1]
print('Weather on Jan 9 was', hash_table['Jan 9'])
print('Weather on Jan 4 was', hash_table['Jan 4'])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and its count as show below.
# Think about the best data structure that you can use to solve this problem and figure
# out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8


# Using a dictionary to keep track of the key values pairs is the best data structure to use
poem = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth; Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same, And both that morning equally lay In leaves no step had trodden black. Oh, I kept the first for another day! Yet knowing how way leads on to way, I doubted if I should ever come back. I shall be telling this with a sigh Somewhere ages and ages hence: Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference."
poem_hash_table = HashTable()

words = poem.split()
for word in words:
    if poem_hash_table.__getitem__(word):
        poem_hash_table.__setitem__(word, poem_hash_table.__getitem__(word)+1)
    else:
        poem_hash_table.__setitem__(word, 1)
print(poem_hash_table.arr)


# Implement hash table where collisions are handled using linear probing.
# We learnt about linear probing in the video tutorial.
# Take the hash table implementation that uses chaining and modify methods to use linear probing.
# Keep MAX size of arr in hashtable as 10.
# Solution


