                                           TELCO PROJECT:
                                           
  In this project I will be looking at the telco data in order to learn more about what drives customer churn. It will be useful to  first identify the most relevant features in my data by putting the data into a logistic regression classifier and looking at the log odds. I will than use the most relevant features in order to create several models that I can teak around until I find the parameters that most accurately predict customer churn.
                                           
                                           Pipeline:
                                            
Step 1: acquire data through functions saved in my acquire.py along with my encrypted credentials.

Step 2: Prepare and clean my data in such a way that I can plug it in to my classification models without causing error and with the prepared data still holding true to its original meaning.

Step 3:Create models that try to accurately predict customer churn, along with visuals that highlight important findings and help the audiance understand their significance.

Step 4: Validate that all of your models are accurate not just on your train data but on outside data as well.

Step 5: Put all of my findings together in a final report where I make things as easy to understand as possible.

                                         QUESTIONS TO ANSWER:

1. What is the most relavant feature to customer churn?

2. What service is being used the most by customers that churn?

3. does a higer tenure correlate with a higher rate of churn?
                                        
                                        Key Findings:
 
Monthly charges had the highest positive relationship with customer churn according to my logistic regression coefficients. Meaning that lowering monthly prices could reduce customer churn.

