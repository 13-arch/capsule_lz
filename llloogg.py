import os
import datetime
import pandas as pd


user=os.getlogin()


def now_time():
    now_date=datetime.datetime.now().strftime('%d.%m.%Y')
    return now_date
def sec():
    now_datetime=str(datetime.datetime.now()).split()
    current_time= now_datetime[1]
    return current_time


def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        if os.path.isfile('logs.csv'):
            file_df = pd.read_csv('logs.csv')
            data = {'id': [len(file_df)], "pc_username": [user], "function_name": [func_name],"date": [now_time()],"time":[sec()]} 
            df = pd.DataFrame(data)
            df.to_csv('logs.csv', mode='a', index=False, header=False)
        else:
            data = {"pc_username": [user], "function_name": [func_name],"date": [now_time()],"time":[sec()]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv')
        return result
    return wrapper