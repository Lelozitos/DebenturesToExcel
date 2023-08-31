import os
from xlsxwriter import *

class ExcelConverter:
    @staticmethod
    def convertMultiple():
        a

    @staticmethod
    def convertOne():
        workbook = Workbook("excel.xlsx")
        os.chdir("./history")

        for fileName in reversed(os.listdir()):
            with open(fileName, "r", encoding="utf-8") as file:
                # # for i in enumerate(file):
                # for i in range(sum(1 for _ in file)):   # gets total lines in file
                #     line = file.readline()
                #     if i > 27:
                #         print(line)

                for i in range(27): # removes initial rubbish
                    file.readline()

                lines = file.read().splitlines()
                # for line in file.read().splitlines():
                #     print(line)
            
            headers = ("Código", "Nome", "Vencimento", "Índice", "Taxa de Compra", "Taxa de Venda", "Taxa Indicativa", "Desvio Padrão", "Inter. Indic. • Mínimo", "Inter. Indic. • Máximo", "PU", "% PU Par", "Duration", "% Reune")
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
                        temp["Índice"] = line
                    case 4:
                        temp["Taxa de Compra"] = line
                    case 5:
                        temp["Taxa de Venda"] = line
                    case 6:
                        temp["Taxa Indicativa"] = line
                    case 7:
                        temp["Desvio Padrão"] = line
                    case 8:
                        temp["Inter. Indic. • Mínimo"] = line
                    case 9:
                        temp["Inter. Indic. • Máximo"] = line
                    case 10:
                        temp["PU"] = line
                    case 11:
                        temp["% PU Par"] = line
                    case 12:
                        temp["Duration"] = line
                    case 13:
                        temp["% Reune"] = line
                        data.append(temp)
                    case other: # blank spaces between 2 items
                        pass
            
            print(data)
            worksheet = workbook.add_worksheet(fileName[:-4])   # create worksheet in excel for this file

            for index, header in enumerate(headers):    # populate header
                worksheet.write(0, index, header)

            for row, entry in enumerate(data):  # populate sheet
                for column, header in enumerate(headers):
                    worksheet.write(row+1, column, entry[header])

            # break  # test for just 1st file

        os.chdir("../")
        workbook.close()