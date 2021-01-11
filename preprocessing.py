import re
import csv

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


with open("../mlchallenge_set_2021.tsv", encoding="latin-1") as tsvfile:
    tsvreader = csv.reader((x.replace('\0', '') for x in tsvfile), delimiter="\t", quotechar='"')
    i = 0
    items = list()
    for line in tsvreader:            
        try:
            description = line[3]

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
            
            
            pass
        except:
            pass


        i += 1

        if i == 30:
            break

print("done with regEx")

for item in items:
    item.printItem()






        




