# Anbima WebScraper
## 📊 Get Anbima list of debentures in Excel

Run locally to create an Excel file with all the last days indexes.

## ✨ Demo

![Sem Nome](https://github.com/Lelozitos/DebenturesToExcel/assets/33338306/8e1a518e-7230-482c-819c-92224a22c98b)


## ⚙️ Installation

Needs Python 3+ to run

Install the dependencies by copying code below or by opening `InstallRequirements.bat`

```sh
python -m pip install beautifulsoup4
python -m pip install requests
python -m pip install xlsxwriter
```

## 🔧 Usage
On `main.py`:
| Function name | Description                    |
| ------------- | ------------------------------ |
| `AnbimaBot(i)` | Instantiates a WebScraper bot from `i` days ago |
| `bot.tableToCSV()` | Creates a file in `./history` with all the information |
| `ExcelConverter.convertOne()` | Converts every file in `./history` to 1 Excel file |

## 🚀 Improvements

- Improve excel compatibility 

## 🤔 Problems

- Very static - meaning that if the site changes it could break the code
- Not expandable

## 🥅 Goal

> Write a code that is able to extract the _"taxas indicativas"_ calculated and published every 
day by Anbima at (https://www.anbima.com.br/pt_br/informar/taxas-de-debentures.htm).
>
> After that, the code must be able to paste the informations in a Excel file, which will be analysed
at another time.
