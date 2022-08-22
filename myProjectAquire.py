import pandas as pd
import numpy as np
from env import host, username, password
import os
#allows me to connect to database w encrypted credentials
def get_connection(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
 #this function allows me to pull requested values by merging tables with linked value sets   
def new_telco_data():
    return pd.read_sql('''
select * from customers
join customer_churn using(customer_id)
join customer_contracts using(customer_id)
join customer_details using(customer_id)
join customer_payments using(customer_id)
join customer_signups using(customer_id)
join customer_subscriptions using(customer_id)


''', get_connection('telco_churn'))
# this function formats the data I've pulled into a dataframe that I can work with In jupyter notebook
def get_telco_data():
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = new_telco_data()
        df.to_csv(filename)
        return df