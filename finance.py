# This is my personal finance management tool
# IT works by reading my whatsapp chat history on which I have recorded my expenses
# And then it will generate a excel file with the expenses exported from the chat so that I can track them easily
# This is just a tool so that I don't have to bear the overhead or friction of listing my expenses on a separate app
# The format of messages in the chat would be cost_of_item item_name eg: 70 coffee with each expense as a separate message


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
