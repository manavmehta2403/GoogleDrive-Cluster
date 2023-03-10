import pandas as pd
import openpyxl as op

#read the excel file as data frame
df = pd.read_excel("Assign.xlsx","Q.1")

#remark the data frame column using map and duplicated() method 
df['Remark'] = df["Vendor Name"].duplicated(keep = False).map({True:'Duplicate', False : 'Unique'})


#checks the output
print(df)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Q1.xlsx', engine='openpyxl')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Q.1', index = False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

###load excel file
##wb = op.load_workbook('Q1.xlsx')
##
###sheet number
##sheet = wb['Q.1']
##
##sheet.auto_size = True
##sheet.bestFit = True
##
##wb.save('Q1.xlsx')

close = input("Press any key to exit")
