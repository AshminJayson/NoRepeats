import xlsxwriter

expenses = []


with open('./expense.txt', 'r') as f:
    for line in f.readlines():
        seps = line.split(' ')
        date, time, item, cost = seps[0][:-1], seps[1], seps[5], seps[4]
        expenses.append([date, time, item, cost])

workbook = xlsxwriter.Workbook('expenses.xlsx')
worksheet = workbook.add_worksheet("Expenses")

headers = ["Date", "Time", "Item", "Cost"]
total_cost = 0
for col, header in enumerate(headers):
    worksheet.write(0, col, header)
for row, data in enumerate(expenses):
    total_cost += float(data[3])
    for col, value in enumerate(data):
        worksheet.write(row + 1, col, value)

worksheet.write(len(expenses) + 1, 0, f"Total {total_cost}")
workbook.close()


        