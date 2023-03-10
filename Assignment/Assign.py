import openpyxl as op

wb = op.load_workbook("Ass.xlsx")

print(wb)
work1 = wb["Q.1"]


print(work1)

print(work1['A1'].value)
