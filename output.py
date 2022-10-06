import pandas as pd
import glob


white 	= pd.read_excel("/Documentos/Trebas/Dev/Jupyter/ex_01/winequality-red.xlsx")
red   	= pd.read_excel("/Documentos/Trebas/Dev/Jupyter/ex_01/winequality-white.xlsx")
final 	= pd.concat([white,red])
#output 	= "/Documentos/Trebas/Dev/Jupyter/ex_01/winequality.xlsx"

print(final)
