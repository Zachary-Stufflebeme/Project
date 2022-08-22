import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
import seaborn as sns
import matplotlib.pyplot as plt

#this function will prepare all of my data in a way that i can Plug into our classification tools
def prep_telco(telco):
    df = telco
    #in the line below I am getting rid of all columns in which values are identical in order to avoid an excessively large and confusing dataframe
    df = df.T.drop_duplicates().T
    #In the following 13 lines I am encoding my categorical variables so that I can use this dataframe in our classification methods without problems
   
    df['is_female'] = df.gender.map({'Female': 1, 'Male': 0})
    df['has_partner'] = df.partner.map({'Yes': 1, 'No': 0})
    df['has_dependents'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['has_phone_service'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['uses_paperless_billing'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['did_churn'] = df.churn.map({'Yes': 1, 'No': 0})
    df['has_mult_lines'] = df.multiple_lines.map({'No' : 0, 'Yes' : 1,'No phone': 2 })
    df['has_online_security'] = df.online_security.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    df['has_online_backup'] = df.online_backup.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    df['has_device_protection'] = df.device_protection.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    df['has_tech_support'] = df.tech_support.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    df['can_stream_tv'] = df.streaming_tv.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    df['can_stream_movie'] = df.streaming_movies.map({'No' : 0, 'Yes' : 1, 'No Internet Service' : 2})
    
    #grabbing customer ID for my CSV
    iddf = pd.DataFrame()
    iddf['customer_id'] = df['customer_id']
    
    #in the line below I am dropping all columns I have just made new encoded columns for.
    
    df = df.drop(['gender','partner','dependents','phone_service','paperless_billing','churn', 'contract_type', 'internet_service_type', 'multiple_lines','online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv','streaming_movies' ], axis = 1)
    
    #In the line below I am turning object valuetypes into floats, as well as cleaning up some weird vales that were not allowing me to do so. there were only 11 values that were incorrect for total_charges so I set them to 0.
    
    df['monthly_charges'] = df.monthly_charges.astype(float)
    df.total_charges = df.total_charges.str.strip()
    df[df['total_charges'].str.len() == 0] = 0
    df['total_charges'] = df['total_charges'].astype(float)
    df[['monthly_charges', 'total_charges']] = scaler.fit_transform(df[['monthly_charges', 'total_charges']])
   
    
    #After looking at the data I realized most of my nulls were coming from peole who did not have internet and it seems this resulted in many columns refering to their streaming capabilities and device protections to be NaN's
    df = df.fillna(0)
    
    return df
    #this is the function I will call in My exploration to effectively split my datafram to the specifications set in the function  at the bottom of the page
def split_telco(newdf):
    
    train, validate, test = my_train_test_split(newdf, 'did_churn')
    return train, validate, test
    #below is the function that splits the data into a specified size
def my_train_test_split(df, target):
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test

def feat_dist(df):
    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()
