import investpy
import pandas as pd

def load_interest_rate_data(from_date="01/01/1980", to_date="12/31/2020"):
    interest_rates = investpy.get_bonds()
    return interest_rates

bond_data = investpy.get_bond_historical_data(bond='U.S. 10Y', from_date='01/01/2020', to_date='01/01/2021')
print(bond_data.head())