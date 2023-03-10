import pandas as pd

#read the excel file as data frame
df = pd.read_excel("Assign.xlsx","Q.2")

df = df[(df["Pay Group"] != "CHECK PAY GROUP") & (df["Invoice Source"] != "ERS")]

#checks the output
print(df)


### Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Q2.xlsx', engine='openpyxl')

### Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Q.2', index = False)
##
### Close the Pandas Excel writer and output the Excel file.
writer.save()


close = input("Press any key to exit")
