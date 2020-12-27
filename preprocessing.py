import re
import csv


with open("mlchallenge_set_2021.tsv", encoding="latin-1") as tsvfile:
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
            else:
                i += 1
            

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
                    

            #print(attribs)
            items.append(attribs)

            if attribs("category") == "4":
                print(description)
            
            
            pass
        except:
            pass
        




