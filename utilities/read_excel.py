import openpyxl

def get_data():
    workbook = openpyxl.load_workbook("C://Users//HP//PycharmProjects//E26_7pm_9pm//Demo_Tricentis_Framework//test_data//login_data.xlsx")
    worksheet = workbook["Sheet1"]

    data = []

    for row in worksheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data

# [("user1","pass1"),("user2","pass2"),("user3","pass3")]

