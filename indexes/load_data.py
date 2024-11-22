from pathlib import Path
import pandas as pd

def get_data(input_file):
    df = pd.read_csv(input_file)
    nifty_50 = df.iloc[:, 0].dropna().tolist()
    nifty_next = df.iloc[:, 1].dropna().tolist()
    nifty_midcap = df.iloc[:, 2].dropna().tolist()
    nifty_smallcap = df.iloc[:, 3].dropna().tolist()
    nifty_bank = df.iloc[:, 4].dropna().tolist()
    nifty_finance = df.iloc[:, 5].dropna().tolist()
    nifty_psu_bank = df.iloc[:, 6].dropna().tolist()
    nifty_it = df.iloc[:, 7].dropna().tolist()
    nifty_auto = df.iloc[:, 8].dropna().tolist()
    nifty_metal = df.iloc[:, 9].dropna().tolist()
    nifty_pharma = df.iloc[:, 10].dropna().tolist()

    data = {
        "nifty_50": nifty_50,
        "nifty_next": nifty_next,
        "nifty_midcap": nifty_midcap,
        "nifty_smallcap": nifty_smallcap,
        "nifty_bank": nifty_bank,
        "nifty_finance": nifty_finance,
        "nifty_psu_bank": nifty_psu_bank,
        "nifty_it": nifty_it,
        "nifty_auto": nifty_auto,
        "nifty_metal": nifty_metal,
        "nifty_pharma": nifty_pharma
    }
    return data

def load_data_from_excel():
    file = "media/indexes.csv"  # file path
    return get_data(file)

# if __name__ == '__main__':
#     file = "indexes.csv"
#     x = load_data_from_excel()
#     print(x['nifty_50'])