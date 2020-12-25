# Red-Hot-Brownies
EBAY ML Competition

This repository will take a dataset of over 1 million item listings from EBay and sort them into clusters, where a cluster will contain items that are PLE (Product Level Equivalent). These PLE are defined under manufacturer specifications (make, model, color, memory size, etc.). Items that may fall into the same cluster may not have the same condition, item location, or other specific details not pertinent to the manufacturer specifications.

# Preprocess.py

This file will generate a list of information from the tsv files provided by EBay. We will be excluding image url/information as creating a neural network based on images would most likely create mostly mutually exclusive clusters dependent on those images. The columns we will include in the preprocessed listing will include columns 1, 4, 5 (category, attributes, item indexing). The attributes will be separated properly using the procedure described in the Annexure - using regex to separate the categories for the item. As there is some noise in our dataset, we will try to find common cases to ignore/sort through.

# Methodology

