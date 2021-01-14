import re
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

class item: 
    def __init__(self, attribs): 
        self.attribs = attribs
        
    def __eq__(self, other):
        if True:
            return True            
        else: 
            return False
        
    def printItem(self):
        print(self.attribs["description"], ", ", self.attribs["index"])


with open("./mlchallenge_set_2021.tsv", encoding="latin-1") as tsvfile:
    tsvreader = csv.reader((x.replace('\0', '') for x in tsvfile), delimiter="\t", quotechar='"')
    i = 0
    items = list()
    list_item_descriptions = list()
    for line in tsvreader:            
        try:
            description = line[3][1:-1]

            attribs = {}
            attribs["index"] = line[4]
            attribs["category"] = line[0]

            if i == 9:
                attribs["category"] = "2"

            try:
                attribs["description"] = re.split("(,(?=[^,]*:))", description)
                pass
            except:
                pass

            thing = item(attribs)
            items.append(thing)

            # create a list of all the descriptions of items
            for eachitem in thing.attribs["description"]:
                list_item_descriptions.append(eachitem)

            pass
        except:
            pass

        i += 1

        if i%10000 == 0:
            print("On item ", i)

print("done with regEx")


# for item in items:
#     item.printItem()

# Initialize the vectorizer
vectorizer = CountVectorizer(token_pattern=r"(?u)\b[a-zA-Z0-9_'.]{1,}\b")

# fit every word of the description from the item listings into the vectorizer
vectorizer.fit(list_item_descriptions)

# Now, we can inspect how our vectorizer vectorized the text
# This will print out a list of words used, and their index in the vectors
print('Vocabulary: ')
print(len(vectorizer.vocabulary_))

# If we would like to actually create a vector, we can do so by passing the
# text into the vectorizer to get back counts
vector = vectorizer.transform(items[0].attribs["description"])
# sum the vector across the 0th axis to combine all words into one vector of length of the vocabulary
npvector = np.array(vector.toarray()).sum(axis=0)
print(npvector)

# Our final vector:
print('Full vector: ')
print(vector.toarray())