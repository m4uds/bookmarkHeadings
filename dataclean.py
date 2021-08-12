import pandas as pd
from sklearn.utils import shuffle





data = pd.read_csv("/Users/m./Google Drive/DataProject_thandi/headings_rawv2.csv")
data = shuffle(data["WORDS"])

output = ""

for i in data:
    
    output = output +" "+ i 
    
out = pd.DataFrame(data = [output])
out.to_clipboard(index = False)
#
