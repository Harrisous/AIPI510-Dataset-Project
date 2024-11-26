# AIPI510-Dataset-Project

## 1. Project Aim

- Dig deep into current useful finance data retrieving libraries/APIs
- Prepare data for time series and other analysis in the future 

## 2. API/Library reference
1. yfinance
    - It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.
    - External tutorial link: https://algotrading101.com/learn/yfinance-guide/
    - Library official website: https://pypi.org/project/yfinance/
    - For this project, some stock is probably delisted

2. investpy
    - it connects to investcom to get data
    - Currently ConnectionError: ERR#0015: error 403, try again later

## 3. Running instruction
1. Create venv `python -m venv .venv` and activate it `source .venv/bin/activate`. 

2. Install packages using `pip install -r requirements.txt`.

3. Run main.py using `python main.py` to collect data. Interval and start/end data can be modified. 