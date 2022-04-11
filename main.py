# %%
from DuctClass import Duct
from BOQClass import BOQ
from DataClass import Data

BoQs = []
TotalBoQ = [0,0,0,0,0]
TotalCost = [0,0,0,0,0]
a = Data()
filename = ['Duct Schedule Medium Pressure Insulated Rect_UPDATED.csv','Duct Fitting Schedule Low Pressure Insulated Cladded Rect_UPDATED.csv',]

for j in range(0,len(filename)):
    BoQs.append(BOQ(0,0,0,0,0))
    dimensions = a.getdimensions(filename[j])
    areas = a.getarea(filename[j])
    counts = a.getcount(filename[j])
    ducts = []

    for i in range(0,len(areas)-1):
        ducts.append(Duct(areas[i],dimensions.iat[i,0], dimensions.iat[i,0], counts[i]))

        BoQs[j].add_to_cat(ducts[i].categorize(),ducts[i].returnarea())

for l in range(0,len(BoQs)):
    for k in range(0,5):
        TotalBoQ[k] += BoQs[l].returncat()[k]
        TotalCost[k] += BoQs[l].returncost()[k]

a.generateoutput(TotalBoQ,TotalCost)


