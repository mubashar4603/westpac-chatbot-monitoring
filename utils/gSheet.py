import gspread


#for reading the specific value from sheet
def read_data_from_specific_cell(cell):
    google_credentials = gspread.service_account(
        filename="/home/mubashar4603/PycharmProjects/monitoring-bot/gspreadrw-ad4a54ce9b94.json")
    sheet_id = google_credentials.open_by_key("1vvgKxr0NKm2bLQ6h_vfF2eXdaxop0EesOtYcpul0y5c")

    current_sheet = sheet_id.worksheet("test")
    cell_value = current_sheet.acell(cell).value
    return cell_value
# test = read_data_from_specific_cell("B2")
# print(type(test))



#For reading the complete column data
def read_column_data(column_letter):
    google_credentials = gspread.service_account(
        filename="/home/mubashar4603/PycharmProjects/monitoring-bot/gspreadrw-ad4a54ce9b94.json")
    sheet = google_credentials.open_by_key("1vvgKxr0NKm2bLQ6h_vfF2eXdaxop0EesOtYcpul0y5c")
    worksheet = sheet.worksheet("test")

    data_list = []
    row = 2  # Start from the second row to skip the header

    while True:
        cell_value = worksheet.acell(f"{column_letter}{row}").value
        if cell_value is None or cell_value == '':
            break
        data_list.append(cell_value)
        row += 1

    return data_list

# Example usage
# result = read_column_data("C")  # Read from column A
# print(type(result))