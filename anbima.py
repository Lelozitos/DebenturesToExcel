import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
from datetime import timedelta

months = ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez")

class AnbimaBot():
    today = date.today()

    def __init__(self, days = 0):
        self.today = self.getDaysBefore(days)
        self.dateURL = f"{self.getDaysBefore(1).day}{months[self.getDaysBefore(1).month - 1]}{self.getDaysBefore(1).year}"

        self.link = f"https://www.anbima.com.br/informacoes/merc-sec-debentures/resultados/mdeb_{self.dateURL}_di_percentual.asp"
        self.request = requests.get(self.link)
        self.page = BeautifulSoup(self.request.text, "html.parser")

        self.name = f"{self.page.find('h2').text} - {self.dateURL}"

    def getDaysBefore(self, days):
        return self.today - timedelta(days = days)

    def tableToCSV(self):
        csv_writer =  csv.writer(open(f"history/{self.dateURL}.txt", 'w', encoding="utf-8"))
        for tr in self.page.find_all("tr"):
            data = []

            for td in tr.find_all("td"):
                data.append(td.text)

            if(data):
                print("{}".format(",".join(data)))
                csv_writer.writerow(data)
                continue

    def __str__(self):
        return f"{self.name}\n{self.link}"
    
    # def headerToArray(self):
    #     self.headers = []
    #     header = self.page.find_all("table")[0].find("tr")

    #     for items in header:
    #         try:
    #             self.headers.append(items.get_text())
    #         except:
    #             continue

    # def tableToArray(self):
    #     self.dataTable = []
    #     HTML_data = self.page.find_all("table")[0].find_all("tr")[1:]

    #     for element in HTML_data:
    #         sub_data = []
    #         for sub_element in element:
    #             try:
    #                 sub_data.append(sub_element.get_text())
    #             except:
    #                 continue
    #         self.dataTable.append(sub_data)