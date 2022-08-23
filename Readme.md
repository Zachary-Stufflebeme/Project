 #                                             TELCO PROJECT:
                                           
  In this project I will be looking at the telco data in order to learn more about what drives customer churn. It will be useful to  first identify the most relevant features in my data by putting the data into a logistic regression classifier and looking at the log odds. I will than use the most relevant features in order to create several models that I can teak around until I find the parameters that most accurately predict customer churn.
                                           
#                                                     Pipeline:
Plan:
                                            
Aquire: acquire data through functions saved in my acquire.py along with my encrypted credentials.

Prepare: Prepare and clean my data in such a way that I can plug it in to my classification models without causing error and with the prepared data still holding true to its original meaning.

Explore: Ask statistical questions of my data and create visualizations of the results in order to improve comprehension by people reading the report without clarifications from my presentation.

Model:Create models that try to accurately predict customer churn, along with visuals that highlight important findings and help the audiance understand their significance. Validate that all of your models are accurate not just on your train data but on outside data as well.

Deliver: Put all of my findings together in a final report where I make things as easy to understand as possible.

#                                         QUESTIONS TO ANSWER:

1. Does Tenure correlate with Paperless billing?
    Hnull - There is no correlation between Tenure and Paperless billing
    Halt  - There is a correlation between Tenure and Paperless billing

2. is distribution of people using paperless billing the same amongst people who do and dont churn?
   Hnull - the distribution of people using paperless billing is the same amongst people that do and dont churn
   Halt - the distribution of people using paperless billing is not the same amongst people that do and dont churn

3. is the didtribution of monthly charges the same amongst people that do and dont churn?
   Hnull - the distribution monthly charges is the same amongst people that do and dont churn
   Halt - the distribution of monthly charges is the same amongst people that do and dont churn
   
4. What is the most relevant feature to customer churn?
#                                                     Data Library

     Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   customer_id               7043 non-null   object 
 1   senior_citizen            7043 non-null   int64  
 2   tenure                    7043 non-null   int64  
 3   internet_service_type_id  7043 non-null   int64  
 4   contract_type_id          7043 non-null   int64  
 5   payment_type_id           7043 non-null   int64  
 6   monthly_charges           7043 non-null   float64
 7   total_charges             7043 non-null   float64
 8   is_female                 7043 non-null   int64  
 9   has_partner               7043 non-null   int64  
 10  has_dependents            7043 non-null   int64  
 11  has_phone_service         7043 non-null   int64  
 12  uses_paperless_billing    7043 non-null   int64  
 13  did_churn                 7043 non-null   int64  
 14  has_mult_lines            7043 non-null   float64
 15  has_online_security       7043 non-null   float64
 16  has_online_backup         7043 non-null   float64
 17  has_device_protection     7043 non-null   float64
 18  has_tech_support          7043 non-null   float64
 19  can_stream_tv             7043 non-null   float64
 20  can_stream_movie          7043 non-null   float64
dtypes: float64(9), int64(11), object(1)

   
#                                                    Key Findings:
 
Monthly charges had the highest positive relationship with customer churn according to my logistic regression coefficients. If I were to use the information in my report to make a business decion I would reduce our monthly charges in order to try and reducr customer churn.
 
#                                                  How To Reproduce:
In order to reproduce my report you will need:
- a personal env with your credentials to access the SQL database.
- you will need to download and move my aquire.py prepare.py into the same directory
-Than you will need to run my report from the same directory.

