import yfinance as yf
from load_data import load_data_from_excel
import json

def get_details(symbol):
    stock = yf.Ticker(f"{symbol}.NS")
    info = stock.info
    name = info.get("longName")
    symbol = symbol
    exchange = "NSE"
    sector = info.get("sector")
    industry = info.get("industry")
    marketcap = info.get("marketCap")

    return [name, symbol, exchange, sector, industry, marketcap]


def details_list(index):
    company_list = []
    i = 1
    for company in index:
        details = get_details(company)        
        val = {
            "model": "indexes.nifty_50",
            "pk": i,
            "fields": {
                "name": details[0],
                "symbol": details[1],
                "exchange": details[2],
                "sector": details[3],
                "industry": details[4],
                "market_cap": details[5]
            }
        }
        i += 1
        company_list.append(val)
        print(company, " added")
    return company_list


if __name__ == '__main__':
    symbols = load_data_from_excel()
    nifty_50 = symbols['nifty_50']
    nifty_next = symbols['nifty_next']
    nifty_midcap = symbols['nifty_midcap']
    nifty_smallcap = symbols['nifty_smallcap']
    nifty_bank = symbols['nifty_bank']
    nifty_finance = symbols['nifty_finance']
    nifty_psu_bank = symbols['nifty_psu_bank']
    nifty_it = symbols['nifty_it']
    nifty_auto = symbols['nifty_auto']
    nifty_metal = symbols['nifty_metal']
    nifty_pharma = symbols['nifty_pharma']

    index_list = [nifty_next, nifty_midcap, nifty_smallcap, nifty_bank,
                  nifty_finance, nifty_psu_bank, nifty_it, nifty_auto, nifty_metal, nifty_pharma]
    
    companys_data_list = details_list(index_list[9])
    print("data writing into json")

    json_string = json.dumps(companys_data_list, indent=2)
    output_file_path = 'json/nifty_pharma.json'
    with open(output_file_path, 'w') as json_file:
        json_file.write(json_string)
    print(" data writing completed")
