import os
from xlsxwriter import *

class ExcelConverter:
    @staticmethod
    def convertMultiple():
        a

    @staticmethod
    def convertOne():
        excelName = "debentures.xlsx"
        workbook = Workbook(excelName)
        os.chdir("./history")

        for fileName in reversed(os.listdir()):
            with open(fileName, "r", encoding="utf-8") as file:
                for i in range(27): # removes initial rubbish
                    file.readline()

                lines = file.read().splitlines()
            
            # headers = ("Código", "Nome", "Vencimento", "Índice", "Taxa de Compra", "Taxa de Venda", "Taxa Indicativa", "Desvio Padrão", "Inter. Indic. • Mínimo", "Inter. Indic. • Máximo", "PU", "% PU Par", "Duration", "% Reune")
            headers = ("Código", "Nome", "Vencimento", "Índice", "Taxa Indicativa", "Duration")
            data = []

            # temp = {
            #     "Código": "",
            #     "Nome": "",
            #     "Vencimento": "",
            #     "Índice": "",
            #     "Taxa de Compra": "",
            #     "Taxa de Venda": "",
            #     "Taxa Indicativa": "",
            #     "Desvio Padrão": "",
            #     "Inter. Indic. • Mínimo": "",
            #     "Inter. Indic. • Máximo": "",
            #     "PU": "",
            #     "% PU Par": "",
            #     "Duration": "",
            #     "% Reune": "",
            # }

            for index, line in enumerate(lines[:-2]):    # remove final csv (final 2 lines)
                if line == "\xa0": line = ""
                match index % 15:   # catching info based on n° of line
                    case 0:
                        temp = dict.fromkeys(headers, "")   # same as comment above
                        temp["Código"] = line
                    case 1:
                        temp["Nome"] = line
                    case 2:
                        temp["Vencimento"] = line
                    case 3:
                        temp["Índice"] = line[:-6]
                    case 4:
                        # temp["Taxa de Compra"] = line
                        pass
                    case 5:
                        # temp["Taxa de Venda"] = line
                        pass
                    case 6:
                        temp["Taxa Indicativa"] = float(line.replace(",", ".")) or "N/D"
                    case 7:
                        # temp["Desvio Padrão"] = line
                        pass
                    case 8:
                        # temp["Inter. Indic. • Mínimo"] = line
                        pass
                    case 9:
                        # temp["Inter. Indic. • Máximo"] = line
                        pass
                    case 10:
                        # temp["PU"] = line
                        pass
                    case 11:
                        # temp["% PU Par"] = line
                        pass
                    case 12:
                        temp["Duration"] = line
                    case 13:
                        # temp["% Reune"] = line
                        data.append(temp)
                    case other: # blank spaces between 2 items
                        pass
            
            # print(data)
            worksheet = workbook.add_worksheet(fileName[:-4])   # create worksheet in excel for this file

            for index, header in enumerate(headers):    # populate header
                worksheet.write(0, index, header)

            for row, entry in enumerate(data):  # populate sheet
                for column, header in enumerate(headers):
                    worksheet.write(row+1, column, entry[header])

            # break  # test for just 1st file

        os.chdir("../")
        workbook.close()
        print(f"Created Excel file named {excelName}")