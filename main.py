from utils.stock_data import collect_all_data


if __name__ == "__main__":
    target=["^GSPC", "^DJI", "^IXIC", "^RUT"]
    start_date = "1980-01-01"
    end_date = "2020-12-31"
    interval = "1wk"
    
    # collect_all_data(start_date, end_date, interval=interval)

