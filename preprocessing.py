import re
import csv

class item: 
    def __init__(self, attribs): 
        self.attribs = attribs
        
    def __eq__(self, other):
        if(len(self.attribs) == len(other.attribs)):
            keys = self.attribs.keys()
            for key in keys:
                try:
                    if self.attribs[key] != other.attribs[key] and key != "index":
                        return False
                except:
                    return False
            return True
        else: 
            return False
        
    def printItem(self):
        print(attribs["index"])


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
                attribs["size"] = re.split(":", re.search("(?i)size[^:]*:[^,]*,", description).group())[1][:-1]    
                pass
            except:
                pass
            
            try:
                attribs["brand"] = re.split(":", re.search("(?i)brand[^:]*:[^,]*,", description).group())[1][:-1]                       
                pass
            except:
                pass
            
            try:
                attribs["color"] = re.split(":", re.search("(?i)color[^:]*:[^,]*,", description).group())[1][:-1]                        
                pass
            except:
                pass
            
            try:
                attribs["width"] = re.split(":", re.search("(?i)width[^:]*:[^,]*,", description).group())[1][:-1]                          
                pass
            except:
                pass
            
            try:
                attribs["material"] = re.split(":", re.search("(?i)material[^:]*:[^,]*,", description).group())[1][:-1]
                pass
            except:
                pass
            
            try:
                attribs["style"] = re.split(":", re.search("(?i)style[^:]*:[^,]*,", description).group())[1][:-1]
                pass
            except:
                pass

            try:
                attribs["style 2"] = re.split(":", re.search("(?i)style 2[^:]*:[^,]*,", description).group())[1][:-1]
                pass
            except:
                pass
                    



            thing = item(attribs)
            items.append(thing)
            
            
            pass
        except:
            pass


        i += 1

        if i == 2500:
            break

print("done with regEx")

groups = list()
skiplst = list()

i = 0
lin = len(items)


for item1 in items:
    if item1 in skiplst:
        pass
    else:
        skiplst.append(item1)
        for item2 in items:
            if item2 in skiplst and skiplst[skiplst.index(item2)].attribs["index"] == item2.attribs["index"]:
                pass
            else:
                try:
                    if item1 in groups[-1]:
                        pass
                    else:
                        groups.append([item1]) 
                except:
                    groups.append([item1])#group is empty
                    
                
                if item1 == item2:
                     #print("NEVER")
                     groups[-1].append(item2)
                     skiplst.append(item2)
    print((i/lin)*100, "%")
    i += 1
    
        
    
 
    

##intt = 0
##for group in groups:
##    if len(group) > 1:
##        print("group ", intt, ": \n{")
##        for item in group:
##            print("     ", item.attribs)
##        print("}")
##    intt += 1
print(len(groups))




        




