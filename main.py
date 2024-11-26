from utils.stock_data import collect_all_data
from utils.interest_rates import save_bond_yield_data
from utils.exchange import save_fx_data

if __name__ == "__main__":
    start_date = "1980-01-01"
    end_date = "2020-12-31"
    interval = "1mo"
    
    collect_all_data(start_date, end_date, interval=interval)
    save_bond_yield_data(start=start_date, end=end_date, interval=interval)
    save_fx_data(start=start_date, end=end_date, interval=interval)

