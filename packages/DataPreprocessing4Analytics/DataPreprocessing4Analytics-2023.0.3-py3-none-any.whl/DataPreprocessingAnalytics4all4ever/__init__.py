# ---------    Importing libraries   ------------------------
#analytics4all4ever@gmail.com
import re
import os
import csv
import sys
import nltk
import spacy
import random
import string
import unicodedata
import math as m
import numpy as np
import pandas as pd
import dateutil as du
import datetime as dt
import seaborn as sns
import calendar as cal
from textblob import Word
import statistics as stats
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from datetime import timedelta as td
from pandas.tseries.offsets import *
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.stem.snowball import SnowballStemmer
pd.options.display.float_format = '{:.5f}'.format
print(os.getcwd())
import warnings
warnings.filterwarnings('ignore')
# import data_processing as DP

# import datetime
# from datetime import timedelta as TD
# 
# start_time = datetime.datetime.now()
# print("start_time: ", start_time)
# 
# 
# import os
# import pandas as pd
# import numpy as np
# import sys
# 
# #from google.colab import drive
# #drive.mount('/content/drive')
# #import sys
# #sys.path.append('/content/drive/My Drive/Colab Notebooks/')
# 
# try:
#     #Google Drive libraries
#     from google.colab import drive
#     drive.mount('/content/drive')
# 
#     #Folders
#     Curret_Folder = os.getcwd()
#     Dataset_Folder = '/content/drive/My Drive/Datasets'
#     ML_Folder = '/content/drive/My Drive/Colab Notebooks'
#     #print('Dataset_Folder Path:',Dataset_Folder)
#     #print('ML_Folder Path:',ML_Folder)
# 
#     #Data Loading
#     os.chdir(Dataset_Folder)
#     print("Data is importing from Google Drive.......")
#     df = pd.read_csv('titanic.csv')
#     print("df.shape:",df.shape)
# 
#     #Importing Custom_Module_Data_PreProcessing_ML
#     os.chdir(ML_Folder)
#     #import Custom_Methods_Final as DPP
#     import Custom_Module_Data_PreProcessing_ML as DPP
# except:
#     #Folders
#     Curret_Folder = os.getcwd()
#     Dataset_Folder = 'C:\\Users\\laxma\Python Work\\Datasets'
#     ML_Folder = 'C:\\Users\\laxma\\Python Work\\Data Analysis\\Machine Learning'
# 
#     #Data Loading
#     os.chdir(Dataset_Folder)
#     print("Data is importing from Local Computer.......")
#     df = pd.read_csv('titanic.csv')
#     print("df.shape:",df.shape, "\n")
# 
#     #Importing Custom_Module_Data_PreProcessing_ML
#     os.listdir(ML_Folder)
#     import Custom_Module_Data_PreProcessing_ML as DPP
# 
# Data_pre_pro = DPP.data_preprocessing()
# stats = DPP.simple_statistics()
# 
# df.columns = Data_pre_pro.rename_columns(df)
# numeric_cols,categoric_cols,id_date_zip_cols,only_num_cals,only_cat_cals,list_all_cols = Data_pre_pro.columns_seperation(df)
# 
# print("numeric_cols:\n", numeric_cols,
#       "\n\ncategoric_cols:\n", categoric_cols,
#       "\n\nid_date_zip_cols:\n", id_date_zip_cols,
#       "\n\nonly_num_cals:\n", only_num_cals,
#       "\n\nonly_cat_cals:\n", only_cat_cals,
#      "\n\nlist_all_cols:\n", list_all_cols
#      )
# print("Impoeted custom library & applied methods on the data !!!!!!!!!!!!!!!! ")
# 
# import datetime
# from datetime import timedelta as TD
# end_time = datetime.datetime.now()
# print("end_time: ", end_time)
# TD = pd.to_datetime(end_time) - pd.to_datetime(start_time)
# 
# print("\n\nTime Consumption: "+ str(TD.components[0]) + "Days " + str(TD.components[1]) + "H:"\
#       + str(TD.components[2]) + "M:"   + str(TD.components[3]) + "S")
#       
# # titnic.csv

# # Sample Data for Classification - Titanic

# # Sample Data for Regression - Housing Price

# df = pd.read_csv('USA_Housing.csv')
# df.head()

# In[2]:


class data_preprocessing:
    import numpy as np
    import pandas as pd
    import re
    import math as m

# -------------------- Data Processing --------------------------
    def rename_columns(self, df) :
        updated_columns_names = df.columns.str.title().str.replace(" " , "_").str.replace("'" , "")\
                             .str.replace("-" , "").str.replace("." , "")\
                             .str.replace("(" , "").str.replace(")" , "")\
                             .str.replace("(" , "").str.replace(")" , "")
        return updated_columns_names

    def update_column_names(self,df):
        df1 = pd.DataFrame(list(df.columns))
        df1.columns = ['Column_Name']
        df1['Columns_Updated']  =df1['Column_Name'].apply(lambda X : X.title())
        df1['Columns_Updated']  =df1['Columns_Updated'].apply(lambda X : re.sub("\s","_",X))
        df1['Columns_Updated']  =df1['Columns_Updated'].apply(lambda X : re.sub("\.|\'|\-\(|\)", "" ,X.title()))
        df.columns = list(df1['Columns_Updated'])
        return df.columns

    def columns_seperation(self,df):
        numeric_cols = list(df.select_dtypes(include = 'number').columns)
        categoric_cols = list(df.select_dtypes(exclude = 'number').columns)
        list_all_cols = list(df.columns)
        id_date_zip_cols = []
        for i in list(df.columns):
            if ('date' in i.lower()) or ('id' in i.lower())or ('zip' in i.lower())or ('pos' in i.lower()):
                id_date_zip_cols.append(i)
            #print(i)
        only_num_cals = list(set(numeric_cols).difference(set(id_date_zip_cols)))
        only_cat_cals = list(set(categoric_cols).difference(set(id_date_zip_cols)))
        return (numeric_cols,categoric_cols,id_date_zip_cols,only_num_cals,only_cat_cals,list_all_cols)

    def null_counts(self , df , perc_threshold_remove_nulls =0):
        df = pd.DataFrame(df)
        df_nulls = pd.DataFrame(df.isnull().sum()).reset_index().rename(columns = {"index" : 'Col_Name', 0: 'Count_Nulls'})
        df_nulls['Perc_Nulls'] = (df_nulls['Count_Nulls']/df.shape[0])*100
        df_nulls = df_nulls.sort_values(by = 'Perc_Nulls' , ascending = False).reset_index(drop = True)

        col_gt_5pct_nulls = df_nulls.loc[df_nulls['Perc_Nulls' ]>perc_threshold_remove_nulls
                                         ,['Col_Name' , 'Perc_Nulls']]
        col_gt_5pct_nulls = col_gt_5pct_nulls.sort_values(by = 'Perc_Nulls' , ascending = False)
        req_cols = list(set(df.columns).difference(set(col_gt_5pct_nulls['Col_Name'].tolist()))  )
        rem_cols = list(col_gt_5pct_nulls.Col_Name)
        #print("list of columns which are having nulls more than 5% : \n" ,
             #df_nulls.loc[df_nulls['Perc_Nulls']>5 , :].columns          )
        return (df_nulls , req_cols , rem_cols)

    def handling_null_values(self,df, remv_cols = [],
                             numer_null_replace = 'mean' ,
                             categoric_null_replace = 'mode',
                             data_req = 'full'):
        if (len(remv_cols)>0) & (data_req == 'full'):
            rem_data = df[remv_cols]
        else:
            rem_data = pd.DataFrame()

        req_col = list(set(df.columns).difference(set(remv_cols)))
        df = df[req_col]
        num_col = df.select_dtypes(include ='number').columns
        cat_col = df.select_dtypes(exclude ='number').columns

        df_cat = df[cat_col]
        df_num = df[num_col]
    # -------------- Handling nulls - Numerical Data ------------

        numer_null_replace = str(numer_null_replace).strip().lower()
        for i in num_col:
            if numer_null_replace =='mean':
                df_num[i].fillna(df_num[i].mean(), inplace = True)
            elif numer_null_replace =='median':
                df_num[i].fillna(df_num[i].median(), inplace = True)
            elif numer_null_replace =='mode':
                df_num[i].fillna(df_num[i].mode().values[0], inplace = True )
    # -------------- Handling nulls - Categorical Data ------------

        categoric_null_replace = str(categoric_null_replace).strip().lower()
        for j in cat_col:
            if categoric_null_replace =='mode':
                mode = df_cat[j].mode().values[0]
                df_cat[j] = df_cat[j].fillna(mode)

        df_final = pd.DataFrame()

        if data_req == 'full':
            df_final = pd.concat([df_num,df_cat,rem_data], axis = 1)
        elif data_req == 'selected':
            df_final = pd.concat([df_num,df_cat], axis = 1)
        else:
            df_final = pd.concat([df_num,df_cat], axis = 1)

        return df_final

    def df_col_val_perc(self, df,col = None, total_num_records = False):
        df = pd.DataFrame(df)
        try:
            if len(col) >0:
                tab = df[col].value_counts().reset_index().rename(columns = {"index" :col, col: "Value_Counts"})
                tab['Value_Perc'] = np.round((tab['Value_Counts'] / tab['Value_Counts'].sum()) *100,2)
                tab = tab.sort_values(by = 'Value_Counts', ascending = False)
                tab['Cum_Perc'] = tab['Value_Perc'].cumsum()
                tab['Ranks'] = range(1,tab.shape[0]+1,1)
                if total_num_records ==True:
                    tab['Total_Num_Reocrds'] = tab['Value_Counts'].sum()
                    return tab
                else:
                    return tab
        except:
            if col == None:
                first_col  = df.columns[0]
                tab = df[first_col].value_counts().reset_index().rename(columns = {"index" :first_col, first_col: "Value_Counts"})
                tab['Value_Perc'] = np.round((tab['Value_Counts'] / tab['Value_Counts'].sum()) *100,2)
                tab = tab.sort_values(by = 'Value_Counts', ascending = False)
                tab['Cum_Perc'] = tab['Value_Perc'].cumsum()
                tab['Ranks'] = range(1,tab.shape[0]+1,1)
                if total_num_records ==True:
                    tab['Total_Num_Reocrds'] = tab['Value_Counts'].sum()
                    return tab
                else:
                    return tab
                
    def replacing_nulls_in_numeric_cols(self,df, numeric_cols = [],replace_nulls_by = 'mean'):
        numeric_cols = list(numeric_cols)
        df = pd.DataFrame(df)
        for i in numeric_cols:
            df[i] = df[i].astype(np.float64)
                #--------- Replacing nulls -----------
            if replace_nulls_by.lower().strip() == 'mean':
                df[i] = df[i].fillna(df[i].mean())
            elif replace_nulls_by.lower().strip() == 'median':
                df[i] = df[i].fillna(df[i].median())  


    def numer_scaling(self, df, remv_cols = [], num_data_scaling = 'minmax' ,data_req = 'full'):
        try:
            remv_cols = list(remv_cols)
            if len(remv_cols) !=0:
                data_rem = df.copy()
                data_rem = data_rem[remv_cols]
            else:
                data_rem = pd.DataFrame()

            req_col = list(set(df.columns).difference(set(remv_cols)))
            df = df[req_col]
            num_col = df.select_dtypes(include ='number').columns
            cat_col = df.select_dtypes(exclude ='number').columns

            df_cat = df[cat_col]
            df_num = df[num_col]
            df_num_updated = pd.DataFrame(df_num)
            # -------------- Handling nulls - Numerical Data ------------
            num_data_scaling = str(num_data_scaling).strip().lower()

            if ('max' in num_data_scaling) | ('min' in num_data_scaling):
                from sklearn.preprocessing import MinMaxScaler
                scaling = MinMaxScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif ('norm' in num_data_scaling ) | ('stand' in num_data_scaling ):
                from sklearn.preprocessing import StandardScaler
                scaling = StandardScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif ('rob' in num_data_scaling ):
                from sklearn.preprocessing import RobustScaler
                scaling = RobustScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif('max' in num_data_scaling ) & ('abs' in num_data_scaling ) :
                from sklearn.preprocessing import MaxAbsScaler
                scaling = MaxAbsScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            data_req = str(data_req).strip().lower()
            if data_req == 'full':
                df_final = pd.concat([df_num_updated,df_cat,data_rem ], axis = 1)
                return df_final
            elif data_req == 'selected':
                df_final = pd.concat([df_num_updated,df_cat], axis = 1)
                return df_final
        except:
            print("Please enter the right information !!!!!!!!")
            
            
    def numerical_scaling(self, df, cols = [], num_data_scaling = 'minmax'):
        try:
            df_cols = df.columns
            req_cols = list(cols)
            not_req_cols = set(df_cols).difference(set(req_cols))
            df_cat = df[list(not_req_cols)]
            df_num = df[req_cols]
            df_num_updated = pd.DataFrame(df_num)
            # -------------- Handling nulls - Numerical Data ------------
            num_data_scaling = str(num_data_scaling).strip().lower()

            if ('max' in num_data_scaling) | ('min' in num_data_scaling):
                from sklearn.preprocessing import MinMaxScaler
                scaling = MinMaxScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif ('norm' in num_data_scaling ) | ('stand' in num_data_scaling ):
                from sklearn.preprocessing import StandardScaler
                scaling = StandardScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif ('rob' in num_data_scaling ):
                from sklearn.preprocessing import RobustScaler
                scaling = RobustScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif('max' in num_data_scaling ) & ('abs' in num_data_scaling ) :
                from sklearn.preprocessing import MaxAbsScaler
                scaling = MaxAbsScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            df_final = pd.concat([df_num_updated,df_cat], axis = 1)
            return df_final

        except:
            print("Please enter the right information !!!!!!!!")
            
    def numerical_values_bins(self,df, cols =[] , no_bins_col_wise = [], default_no_bins = 3):
        bins_ = {}    
        cols = list(cols)
        no_bins_col_wise = list(no_bins_col_wise)
        #print(type(no_bins_col_wise) , len( no_bins_col_wise))
        if (len(no_bins_col_wise)==0) | (no_bins_col_wise==None) | (len(cols) != len(no_bins_col_wise)):
            no_bins = list([default_no_bins]*len(cols))
        else:
            no_bins = no_bins_col_wise
        #print(no_bins)
        for i, v in enumerate(cols):
            bins_[v] = self.df_col_val_perc(pd.cut(df[v],no_bins[i]))
            bins_[v]['Ranks']=list(range(len(bins_[v]['Ranks'])))
            bins_[v][v]= bins_[v][v].astype(str)
            bins_[v].columns = ['Range', 'Counts', 'Perc', 'Cum_Perc', 'Mapping_Value']
            bins_[v] = bins_[v][['Range','Mapping_Value','Counts', 'Perc', 'Cum_Perc']]      
            df[v] = pd.cut(df[v],no_bins[i], labels = list(range(no_bins[i])))  
        print(bins_)

    def DF_Count_Uniq_Values_By_col(self, df):
        df = pd.DataFrame(df)
        cols = df.columns
        df_n_unique = {}
        for i in cols:
            df_n_unique[i] = df[i].nunique()

        DF_Count_Uniq_Values_By_col = pd.Series(df_n_unique).reset_index().rename(columns = {"index": 'Column_Name' ,
                                                                                             0:"#Unique_Values"})
        return DF_Count_Uniq_Values_By_col

# ---------------------- Decision Tree related ----------------
    def entropy(self, df,col = None ):
        try:
            if len(col)>0:
                labeled_data = self.df_col_val_perc(df, col)
                entropy = []
                for i in range(labeled_data.shape[0]):
                    total_counts = labeled_data['Value_Counts'].sum()
                    #print(labeled_data['Value_Counts'][i])
                    pro_ratio = labeled_data['Value_Counts'][i]/total_counts
                    entropy.append(-(pro_ratio*np.log2(pro_ratio)))
                return np.sum(entropy)
        except:
            print("Pass the column name to calculate the entropy")

    def entropy_all_cols(self, df):
        cols = list(df.columns)
        entropy_cols = {}
        for i in cols:
            entropy_cols[i] = (self.entropy(df,i))

        entropy_cols = pd.Series(entropy_cols).reset_index().rename(columns = {"index": 'Predictor_Name' , 0:"Entropy"})
        entropy_cols = entropy_cols.sort_values(by = 'Entropy' , ascending = True)
        return entropy_cols

    def descriptive_statistics(self,df, cols = [] , full_info = False, num_decm_points = 2):
        if (len(cols)==0) | (type(cols) !=list) :
            print("Please supply the list of the columns, for which you want o see the Descriptive Statistics")
        else:
            if full_info == False:
                for i in cols:
                    print(i ,":")
                    q3_ = df[i].quantile(.75)
                    q1_ = df[i].quantile(.25)
                    iqr_ = q3_ - q1_
                    low_iqr_ = q1_ - (1.5*iqr_)
                    upp_iqr_ = q3_ + (1.5*iqr_)
                    outliers_range = (df[i]> upp_iqr_) | (df[i]< low_iqr_)
                    outliers = list(df.loc[outliers_range , i])
                    print('iqr:', iqr_ , ', #outliers:', len(outliers) , "\n")
            elif full_info == True:
                for i in cols:
                    #print(i,":")
                    q3_ = df[i].quantile(.75)
                    q1_ = df[i].quantile(.25)
                    iqr_ = q3_ - q1_
                    low_fence_iqr_ = q1_ - (1.5*iqr_)
                    upp_fence_iqr_ = q3_ + (1.5*iqr_)
                    outliers_range = (df[i]> upp_fence_iqr_) | (df[i]< low_fence_iqr_)
                    outliers = list(df.loc[outliers_range , i])
                    outliers_neg = list(df.loc[df[i]> upp_fence_iqr_ , i])
                    outliers_pos = list(df.loc[df[i]< low_fence_iqr_ , i])
                    info_1 = {'Min' : np.round(df[i].min(),2),
                            'Q1' : np.round(df[i].quantile(.25),num_decm_points),
                            'Median' : np.round(df[i].quantile(.5),num_decm_points),
                            'Q3' : np.round(df[i].quantile(.75),num_decm_points),
                            'Max' : np.round(df[i].quantile(1),num_decm_points),
                            'Mean' :np.round( df[i].mean(),num_decm_points),
                            'STD' : np.round(df[i].std(),num_decm_points),
                            'Variance' : np.round(df[i].var(),num_decm_points),
                            'Count' : df[i].count(),
                            'IQR' : np.round(iqr_,num_decm_points),
                            'IQR_Lower_Fence' : np.round(low_fence_iqr_,num_decm_points),
                            'IQR_Upper_Fence' : np.round(upp_fence_iqr_,num_decm_points),
                            'Skewness' : np.round(df[i].skew(),num_decm_points),
                            'Kurtosis' : np.round(df[i].kurt(),num_decm_points),
                            '#NonOutliers' : df[i].shape[0]-len(outliers),
                            'NonOutliers_Perc' : np.round(((df[i].shape[0]-len(outliers)) / df[i].shape[0])*100,num_decm_points),
                            '#Outliers' : len(outliers),
                            'Outliers_Perc' : np.round((len(outliers) / df[i].shape[0])*100,num_decm_points),
                            '#Outliers_neg' : len(outliers_neg),
                            '#Outliers_pos' : len(outliers_pos)
                        }
                    print(info_1 , "\n")

    def Outlier_Detect_And_Show_Repl_Value(self,
                df,
                cols = [],
                detect_method = 'iqr',
                replace_outlier_by = 'mean',
                replace_nulls_by = 'mean'
               ):
        data_info = {}
        cols = list(cols)
        df = pd.DataFrame(df)
        #df1 = pd.DataFrame(df[cols])
        #print("Using",detect_method.upper(), "to detect the Outliers and" ,
             # 'Nulls are replaced by', replace_nulls_by.upper(),
             # 'Outliers are replaced by', replace_outlier_by.upper()
             #)
        for i in cols:
            df1 = pd.DataFrame(df[i])
            df1[i] = df1[i].astype(np.float64)
            #print(i, "\n\n")

            #--------- Replacing nulls -----------
            if replace_nulls_by == 'mean':
                df1[i] = df1[i].fillna(df1[i].mean())
            elif replace_nulls_by == 'median':
                df1[i] = df1[i].fillna(df1[i].median())

            #--------- Descriptive Statistics -----------
            means_ = np.mean(df[i])
            std_ = np.std(df1[i])
            medians_ = np.median(df1[i])
            q3_ = df1[i].quantile(.75)
            q1_ = df1[i].quantile(.25)
            iqr_ = q3_ - q1_
            low_iqr_ = q1_ - (1.5*iqr_)
            upp_iqr_ = q3_ + (1.5*iqr_)
            df1['ZScores'] = df1[i].apply(lambda X : ((X - means_)/std_))

            values_after_replacing_Outliers = 'Values_Updated'

            if detect_method == 'iqr':
                df1['Outlier_or_Not'] = np.where(((df1[i]> upp_iqr_) | (df1[i]< low_iqr_)),'Y','N')
                if replace_outlier_by =='mean':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',means_,df1[i])
                elif replace_outlier_by =='median':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',medians_,df1[i])

            elif detect_method == 'zscore':
                df1['Outliers_or_Not'] = np.where(((df1['ZScores']> 3) | (df1['ZScores']< -3)),'Y','N')
                if replace_outlier_by =='mean':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outliers_or_Not']=='Y', means_,df1[i])
                elif replace_outlier_by =='median':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outliers_or_Not']=='Y', medians_,df1[i])

            data_info[i] = df1
        return (data_info)
    def outlier_replace_in_Num_Cols(self, df , cols = [],
                     detect_method = 'iqr',
                    replace_outlier_by = 'mean',
                    replace_nulls_by = 'mean'
                                     ):
        for i in cols:
          j  = self.Outlier_Detect_And_Show_Repl_Value(df, cols = [i],
                      detect_method = detect_method,
                      replace_outlier_by = replace_outlier_by,
                      replace_nulls_by = replace_nulls_by)
          #print(pd.DataFrame(j[i])['Values_Updated'])
          df[i] = pd.DataFrame(j[i])['Values_Updated'].values


# In[ ]:





# In[3]:


class simple_statistics:
    import numpy as np
    import pandas as pd
    import re
    import math as m
       
    def Data_Sum_Count(self, X):
        X = list(X)
        count_ = 0
        sum_ = 0
        for i in range(len(X)):
            sum_ = sum_+X[i]   
            count_ = count_+1
        return(sum_,count_)
    
    def Data_Unique_Values(self, X):
        X = list(X)
        unique_values = []
        for i in X:
            if i not in unique_values:
                unique_values.append(i)
        return unique_values     
    
    def Data_Max_Min(self, X):
        X = sorted(list(X))
        max_ = X[len(X)-1]
        min_ = X[0]
        return (max_ , min_)    
    
    def Data_Arith_Mean(self ,X):
        self.sum_, self.count_ = self.sum_count(X)
        return(self.sum_/self.count_)
    
    def Data_Harmonic_Mean(self ,X):
        self.sum_, self.count_ = self.sum_count(X)
        return(self.count_/self.sum_)    
    
    def Data_Geometric_Mean(self ,X):        
        sum_1, counts_1= self.Data_Sum_Count(X)
        prod_all_mem = 1        
        for i in range(counts_1):
            prod_all_mem = prod_all_mem * X[i]            
        gem_mean = prod_all_mem**(1/counts_1)
        return (counts_1,prod_all_mem,gem_mean)    
        
    def Data_Median(self, X):        
        X = sorted(list(X))
        if len(X)%2==0:
            return (x[len(X)/2] + x[(len(X)/2)+1])/2
        elif len(X)%2==1:
            return X[int((len(X) +1)/2)]
               
    def Data_Sort(self, X):
        X = sorted(list(X))
        return X
    
    def Data_Mode(self, X):
        X = self.Data_Sort(list(X))
        set_x = set(X)
        counts = {}
        for i in range(len(set_x)):
            counts[set_x[i]] = X.count(set_x[i])
        return counts
    
    def Data_Freq_Values(self , X):
        X = list(X)
        counts= {}
        for i in set(X):
            counts[i] = X.count(i)
        freq_tab = pd.Series(counts).reset_index().rename(columns = {"index": 'Value' , 0:"Frequency"})
        freq_tab = freq_tab.sort_values(by = 'Frequency' , ascending = False)
        freq_tab['Frequency_Perc'] = round((freq_tab['Frequency']/freq_tab['Frequency'].sum())*100,2)
        freq_tab['Ranks'] = range(1, freq_tab.shape[0]+1)
        return freq_tab
        
    def Data_Mode_Values(self , X):
        freq_tab = self.Data_Freq_Values(X)
        max_,min_ = self.Data_Max_Min(X = freq_tab['Frequency'])
        mode_values = list(freq_tab.loc[freq_tab['Frequency'] == max_ , 'Value' ])
        return mode_values    

    def Data_Range(self, X):
        X = sorted(list(X))
        max_ = X[len(X)-1]
        min_ = X[0]
        return (max_ - min_)    
    
    def Data_Percentile(X, perc = 50):
        cnt = stats.Data_Sum_Count(X)[1]
        X = stats.Data_Sort(X)
        mem = (cnt *(perc/100))
        
        if (mem - int(mem)) ==0:
            return X[int(mem)-1]
        elif (mem - int(mem)) !=0:
            return (X[int(mem)] + X[int(mem)+1])/2
    
    def Data_Var_Std(self, X):
        self.mean_ = self.Arithermatic_Mean(X)
        self.sum_ = 0
        for i in range(len(X)):
            self.sum_ = self.sum_+ ((X[i] - self.mean_)**(2))
        
        self.Data_Variance = self.sum_
        self.Data_STD= self.sum_**(1/2)
        return (self.Data_Variance, self.Data_STD)
    
    def Data_Sample_Sim_Rand(self , X, perc = 15):
        X = list(X)
        
        perc = int(perc/100 *  ((len(X)+1)))
        random =list(np.random.randint(0 , len(X)+1 , perc))
        print(random)
        req = []
        for i in random:
            if i in X:
                req.append(i)        
        return req
    
    def Desciptive_Stats(self,df ,cols = ['Sales' , 'Profit' , 'Discount' , 'Quantity'] ):
        data_info = {}
        for i in cols:
            print(i,":")      
            q3_ = df[i].quantile(.75)
            q1_ = df[i].quantile(.25)
            iqr_ = q3_ - q1_
            low_fence_iqr_ = q1_ - (1.5*iqr_)
            upp_fence_iqr_ = q3_ + (1.5*iqr_)   
            outliers_range = (df[i]> upp_fence_iqr_) | (df[i]< low_fence_iqr_)                
            outliers = list(df.loc[outliers_range , i])
            outliers_neg = list(df.loc[df[i]> upp_fence_iqr_ , i])
            outliers_pos = list(df.loc[df[i]< low_fence_iqr_ , i])
            info_1 = {
                      'Count' : df[i].count(),
                      'Q0(Min)' : np.round(df[i].quantile(0),2),
                      'Q1' : np.round(df[i].quantile(.25),2),
                      'Q2(Median)' : np.round(df[i].quantile(.5),2),
                      'Q3' : np.round(df[i].quantile(.75),2),
                      'Q4(Max)' : np.round(df[i].quantile(1),2),
                      'Mean' :np.round( df[i].mean(),2),
                      'STD' : np.round(df[i].std(),2),
                      'Variance' : np.round(df[i].var(),2),
                      #'MAD': np.round(df[i].var(),2),            
                      'IQR' : np.round(iqr_,2),
                      'IQR_Lower_Fence' : np.round(low_fence_iqr_,2),
                      'IQR_Upper_Fence' : np.round(upp_fence_iqr_,2),
                      'Skewness' : np.round(df[i].skew(),2),
                      'Curtosis' : np.round(df[i].kurt(),2),
                      '#NonOutliers' : df[i].shape[0]-len(outliers),                            
                      'NonOutliers_Perc' : np.round(((df[i].shape[0]-len(outliers)) / df[i].shape[0])*100,2),                            
                      '#Outliers' : len(outliers),
                      'Outliers_Perc' : np.round((len(outliers) / df[i].shape[0])*100,2),
                      '#Outliers_neg' : len(outliers_neg),
                      '#Outliers_pos' : len(outliers_pos)
                     }   

            data_info[i] = info_1
        return (data_info)    
        
    def factorial(self , X):
        if X<0:
            print('Please enter a positive Value.')
        elif X== 1:
            return 1
        else:
            return X * self.factorial(X-1)
        
    def Binomial_Distribution(self , n=1,p=.1,r = 1):
        import math as m
        ncr = (self.factorial(n))/(self.factorial(n-r) * self.factorial(r))
        pq = m.pow(p, r)* m.pow( (1-p), (n-r))        
        return (ncr * pq)


    
class Data_Pre_Processing:
    import numpy as np
    import pandas as pd
    import re
    import math as m
    
# -------------- Basic indormation about the Data - Central Tendency ---------------    
    def Data_Sum_Count(self, X):
        X = list(X)
        count_ = 0
        sum_ = 0
        for i in range(len(X)):
            sum_ = sum_+X[i]   
            count_ = count_+1
        return(sum_,count_)
    
    def Data_Unique_Values(self, X):
        X = list(X)
        unique_values = []
        for i in X:
            if i not in unique_values:
                unique_values.append(i)
        return unique_values     
    
    def Data_Max_Min(self, X):
        X = sorted(list(X))
        max_ = X[len(X)-1]
        min_ = X[0]
        return (max_ , min_)    
    
    def Data_Arith_Mean(self ,X):
        self.sum_, self.count_ = self.sum_count(X)
        return(self.sum_/self.count_)
    
    def Data_Harmonic_Mean(self ,X):
        self.sum_, self.count_ = self.sum_count(X)
        return(self.count_/self.sum_)    
    
    def Data_Geometric_Mean(self ,X):        
        sum_1, counts_1= self.Data_Sum_Count(X)
        prod_all_mem = 1        
        for i in range(counts_1):
            prod_all_mem = prod_all_mem * X[i]            
        gem_mean = prod_all_mem**(1/counts_1)
        return (counts_1,prod_all_mem,gem_mean)    
        
    def Data_Median(self, X):        
        X = sorted(list(X))
        if len(X)%2==0:
            return (x[len(X)/2] + x[(len(X)/2)+1])/2
        elif len(X)%2==1:
            return X[int((len(X) +1)/2)]
               
    def Data_Sort(self, X):
        X = sorted(list(X))
        return X
    
    def Data_Mode(self, X):
        X = self.Data_Sort(list(X))
        set_x = set(X)
        counts = {}
        for i in range(len(set_x)):
            counts[set_x[i]] = X.count(set_x[i])
        return counts
    
    def Data_Freq_Values(self , X):
        X = list(X)
        counts= {}
        for i in set(X):
            counts[i] = X.count(i)
        freq_tab = pd.Series(counts).reset_index().rename(columns = {"index": 'Value' , 0:"Frequency"})
        freq_tab = freq_tab.sort_values(by = 'Frequency' , ascending = False)
        freq_tab['Frequency_Perc'] = round((freq_tab['Frequency']/freq_tab['Frequency'].sum())*100,2)
        freq_tab['Ranks'] = range(1, freq_tab.shape[0]+1)
        return freq_tab
        
    def Data_Mode_Values(self , X):
        freq_tab = self.Data_Freq_Values(X)
        max_,min_ = self.Data_Max_Min(X = freq_tab['Frequency'])
        mode_values = list(freq_tab.loc[freq_tab['Frequency'] == max_ , 'Value' ])
        return mode_values    

    def Data_Range(self, X):
        X = sorted(list(X))
        max_ = X[len(X)-1]
        min_ = X[0]
        return (max_ - min_)

    def Univariate_Basic_Statistics(self,df ,cols = ['Sales' , 'Profit' , 'Discount' , 'Quantity'] ):
        data_info = {}
        for i in cols:
            #print(i,":")      
            q3_ = df[i].quantile(.75)
            q1_ = df[i].quantile(.25)
            iqr_ = q3_ - q1_
            low_fence_iqr_ = q1_ - (1.5*iqr_)
            upp_fence_iqr_ = q3_ + (1.5*iqr_)   
            outliers_range = (df[i]> upp_fence_iqr_) | (df[i]< low_fence_iqr_)                
            outliers = list(df.loc[outliers_range , i])
            outliers_neg = list(df.loc[df[i]> upp_fence_iqr_ , i])
            outliers_pos = list(df.loc[df[i]< low_fence_iqr_ , i])
            mode_ = self.Data_Mode_Values(df[i])[0]
            info_1 = {
                      'Count' : df[i].count(),
                      'Q0(Min)' : np.round(df[i].quantile(0),2),
                      'Q1' : np.round(df[i].quantile(.25),2),
                      'Q2(Median)' : np.round(df[i].quantile(.5),2),
                      'Q3' : np.round(df[i].quantile(.75),2),
                      'Q4(Max)' : np.round(df[i].quantile(1),2),
                      'Mean' :np.round( df[i].mean(),2),
                      'Mode' : mode_,
                      'STD' : np.round(df[i].std(),2),
                      'Variance' : np.round(df[i].var(),2),
                      #'MAD': np.round(df[i].var(),2),            
                      'IQR' : np.round(iqr_,2),
                      'IQR_Lower_Fence' : np.round(low_fence_iqr_,2),
                      'IQR_Upper_Fence' : np.round(upp_fence_iqr_,2),
                      'Skewness' : np.round(df[i].skew(),2),
                      'Curtosis' : np.round(df[i].kurt(),2),
                      '#NonOutliers' : df[i].shape[0]-len(outliers),                            
                      'NonOutliers_Perc' : np.round(((df[i].shape[0]-len(outliers)) / df[i].shape[0])*100,2),                            
                      '#Outliers' : len(outliers),
                      'Outliers_Perc' : np.round((len(outliers) / df[i].shape[0])*100,2),
                      '#Outliers_neg' : len(outliers_neg),
                      '#Outliers_pos' : len(outliers_pos)
                     }   

            data_info[i] = info_1
        return (data_info)    
        
    def factorial(self , X):
        if X<0:
            print('Please enter a positive Value.')
        elif X== 1:
            return 1
        else:
            return X * self.factorial(X-1)
# -------------------- Data Processing --------------------------
    def rename_columns(self, df) :
        updated_columns_names = df.columns.str.title().str.replace(" " , "_").str.replace("'" , "")\
                                                .str.replace("-" , "").str.replace("." , "")\
                                                .str.replace("(" , "").str.replace(")" , "")
        return updated_columns_names

    def update_column_names(self,df):
        import re
        df1 = pd.DataFrame(list(df.columns))
        df1.columns = ['Column_Name']
        df1['Columns_Updated']  =df1['Column_Name'].apply(lambda X : X.title())
        df1['Columns_Updated']  =df1['Columns_Updated'].apply(lambda X : re.sub("\s","_",X))
        df1['Columns_Updated']  =df1['Columns_Updated'].apply(lambda X : re.sub("\.|\'|\-\(|\)", "" ,X.title()))
        df.columns = list(df1['Columns_Updated'])
        return df.columns

    def columns_seperation(self,df):
        numeric_cols = list(df.select_dtypes(include = 'number').columns)
        categoric_cols = list(df.select_dtypes(exclude = 'number').columns)
        list_all_cols = list(df.columns)
        id_date_zip_cols = []
        for i in list(df.columns):
            if ('date' in i.lower()) or ('id' in i.lower())or ('zip' in i.lower())or ('pos' in i.lower()):
                id_date_zip_cols.append(i)
            #print(i)
        num_cols_model = list(set(numeric_cols).difference(set(id_date_zip_cols)))
        cat_cols_model = list(set(categoric_cols).difference(set(id_date_zip_cols)))
        return (numeric_cols,categoric_cols,id_date_zip_cols,num_cols_model,cat_cols_model,list_all_cols)

    def null_counts(self , df , perc_threshold_remove_nulls =0):
        df = pd.DataFrame(df)
        df_nulls = pd.DataFrame(df.isnull().sum()).reset_index().rename(columns = {"index" : 'Col_Name', 0: 'Count_Nulls'})
        df_nulls['Perc_Nulls'] = (df_nulls['Count_Nulls']/df.shape[0])*100
        df_nulls = df_nulls.sort_values(by = 'Perc_Nulls' , ascending = False).reset_index(drop = True)

        col_gt_5pct_nulls = df_nulls.loc[df_nulls['Perc_Nulls' ]>perc_threshold_remove_nulls
                                         ,['Col_Name' , 'Perc_Nulls']]
        col_gt_5pct_nulls = col_gt_5pct_nulls.sort_values(by = 'Perc_Nulls' , ascending = False)
        req_cols = list(set(df.columns).difference(set(col_gt_5pct_nulls['Col_Name'].tolist()))  )
        rem_cols = list(col_gt_5pct_nulls.Col_Name)
        #print("list of columns which are having nulls more than 5% : \n" ,
             #df_nulls.loc[df_nulls['Perc_Nulls']>5 , :].columns          )
        return (df_nulls , req_cols , rem_cols)

    def handling_null_values(self,df, remv_cols = [],
                             numer_null_replace = 'mean' ,
                             categoric_null_replace = 'mode',
                             data_req = 'full'):
        if (len(remv_cols)>0) & (data_req == 'full'):
            rem_data = df[remv_cols]
        else:
            rem_data = pd.DataFrame()

        req_col = list(set(df.columns).difference(set(remv_cols)))
        df = df[req_col]
        num_col = df.select_dtypes(include ='number').columns
        cat_col = df.select_dtypes(exclude ='number').columns

        df_cat = df[cat_col]
        df_num = df[num_col]
    # -------------- Handling nulls - Numerical Data ------------

        numer_null_replace = str(numer_null_replace).strip().lower()
        for i in num_col:
            if numer_null_replace =='mean':
                df_num[i].fillna(df_num[i].mean(), inplace = True)
            elif numer_null_replace =='median':
                df_num[i].fillna(df_num[i].median(), inplace = True)
            elif numer_null_replace =='mode':
                df_num[i].fillna(df_num[i].mode().values[0], inplace = True )
    # -------------- Handling nulls - Categorical Data ------------

        categoric_null_replace = str(categoric_null_replace).strip().lower()
        for j in cat_col:
            if categoric_null_replace =='mode':
                mode = df_cat[j].mode().values[0]
                df_cat[j] = df_cat[j].fillna(mode)

        df_final = pd.DataFrame()

        if data_req == 'full':
            df_final = pd.concat([df_num,df_cat,rem_data], axis = 1)
        elif data_req == 'selected':
            df_final = pd.concat([df_num,df_cat], axis = 1)
        else:
            df_final = pd.concat([df_num,df_cat], axis = 1)

        return df_final

    def df_col_val_perc(self, df,col = None, total_num_records = False):
        df = pd.DataFrame(df)
        try:
            if len(col) >0:
                tab = df[col].value_counts().reset_index().rename(columns = {"index" :col, col: "Value_Counts"})
                tab['Value_Perc'] = np.round((tab['Value_Counts'] / tab['Value_Counts'].sum()) *100,2)
                tab = tab.sort_values(by = 'Value_Counts', ascending = False)
                tab['Cum_Perc'] = tab['Value_Perc'].cumsum()
                tab['Ranks'] = range(1,tab.shape[0]+1,1)
                if total_num_records ==True:
                    tab['Total_Num_Reocrds'] = tab['Value_Counts'].sum()
                    return tab
                else:
                    return tab
        except:
            if col == None:
                first_col  = df.columns[0]
                tab = df[first_col].value_counts().reset_index().rename(columns = {"index" :first_col, first_col: "Value_Counts"})
                tab['Value_Perc'] = np.round((tab['Value_Counts'] / tab['Value_Counts'].sum()) *100,2)
                tab = tab.sort_values(by = 'Value_Counts', ascending = False)
                tab['Cum_Perc'] = tab['Value_Perc'].cumsum()
                tab['Ranks'] = range(1,tab.shape[0]+1,1)
                if total_num_records ==True:
                    tab['Total_Num_Reocrds'] = tab['Value_Counts'].sum()
                    return tab
                else:
                    return tab
                
    def replacing_nulls_in_numeric_cols(self,df, numeric_cols = [],replace_nulls_by = 'mean'):
        numeric_cols = list(numeric_cols)
        df = pd.DataFrame(df)
        for i in numeric_cols:
            mode_ = self.Data_Mode_Values(df[i])[0]
            df[i] = df[i].astype(np.float64)
                #--------- Replacing nulls -----------
            if replace_nulls_by.lower().strip() == 'mean':
                df[i] = df[i].fillna(df[i].mean())
            elif replace_nulls_by.lower().strip() == 'median':
                df[i] = df[i].fillna(df[i].median())
            elif replace_nulls_by.lower().strip() == 'mode':
                df[i] = df[i].fillna(mode_)


    def numer_scaling(self, df, remv_cols = [], num_data_scaling = 'minmax' ,data_req = 'full'):
        try:
            remv_cols = list(remv_cols)
            if len(remv_cols) !=0:
                data_rem = df.copy()
                data_rem = data_rem[remv_cols]
            else:
                data_rem = pd.DataFrame()

            req_col = list(set(df.columns).difference(set(remv_cols)))
            df = df[req_col]
            num_col = df.select_dtypes(include ='number').columns
            cat_col = df.select_dtypes(exclude ='number').columns

            df_cat = df[cat_col]
            df_num = df[num_col]
            df_num_updated = pd.DataFrame(df_num)
            # -------------- Handling nulls - Numerical Data ------------
            num_data_scaling = str(num_data_scaling).strip().lower()

            if ('max' in num_data_scaling) | ('min' in num_data_scaling):
                from sklearn.preprocessing import MinMaxScaler
                scaling = MinMaxScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif ('norm' in num_data_scaling ) | ('stand' in num_data_scaling ):
                from sklearn.preprocessing import StandardScaler
                scaling = StandardScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif ('rob' in num_data_scaling ):
                from sklearn.preprocessing import RobustScaler
                scaling = RobustScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            elif('max' in num_data_scaling ) & ('abs' in num_data_scaling ) :
                from sklearn.preprocessing import MaxAbsScaler
                scaling = MaxAbsScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = num_col)

            data_req = str(data_req).strip().lower()
            if data_req == 'full':
                df_final = pd.concat([df_num_updated,df_cat,data_rem ], axis = 1)
                return df_final
            elif data_req == 'selected':
                df_final = pd.concat([df_num_updated,df_cat], axis = 1)
                return df_final
        except:
            print("Please enter the right information !!!!!!!!")
            
            
    def numerical_scaling(self, df, cols = [], num_data_scaling = 'minmax'):
        try:
            df_cols = df.columns
            req_cols = list(cols)
            not_req_cols = set(df_cols).difference(set(req_cols))
            df_cat = df[list(not_req_cols)]
            df_num = df[req_cols]
            df_num_updated = pd.DataFrame(df_num)
            # -------------- Handling nulls - Numerical Data ------------
            num_data_scaling = str(num_data_scaling).strip().lower()

            if ('max' in num_data_scaling) | ('min' in num_data_scaling):
                from sklearn.preprocessing import MinMaxScaler
                scaling = MinMaxScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif ('norm' in num_data_scaling ) | ('stand' in num_data_scaling ):
                from sklearn.preprocessing import StandardScaler
                scaling = StandardScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif ('rob' in num_data_scaling ):
                from sklearn.preprocessing import RobustScaler
                scaling = RobustScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            elif('max' in num_data_scaling ) & ('abs' in num_data_scaling ) :
                from sklearn.preprocessing import MaxAbsScaler
                scaling = MaxAbsScaler()
                df_num_updated = pd.DataFrame(scaling.fit_transform(df_num) , columns = req_cols)

            df_final = pd.concat([df_num_updated,df_cat], axis = 1)
            return df_final

        except:
            print("Please enter the right information !!!!!!!!")
            
    def numerical_values_bins(self,df, cols =[] , no_bins_col_wise = [], default_no_bins = 3):
        bins_ = {}    
        cols = list(cols)
        no_bins_col_wise = list(no_bins_col_wise)
        #print(type(no_bins_col_wise) , len( no_bins_col_wise))
        if (len(no_bins_col_wise)==0) | (no_bins_col_wise==None) | (len(cols) != len(no_bins_col_wise)):
            no_bins = list([default_no_bins]*len(cols))
        else:
            no_bins = no_bins_col_wise
        #print(no_bins)
        for i, v in enumerate(cols):
            bins_[v] = self.df_col_val_perc(pd.cut(df[v],no_bins[i]))
            bins_[v]['Ranks']=list(range(len(bins_[v]['Ranks'])))
            bins_[v][v]= bins_[v][v].astype(str)
            bins_[v].columns = ['Range', 'Counts', 'Perc', 'Cum_Perc', 'Mapping_Value']
            bins_[v] = bins_[v][['Range','Mapping_Value','Counts', 'Perc', 'Cum_Perc']]      
            df[v] = pd.cut(df[v],no_bins[i], labels = list(range(no_bins[i])))  
        print(bins_)

    def DF_Count_Uniq_Values_By_col(self, df):
        df = pd.DataFrame(df)
        cols = df.columns
        df_n_unique = {}
        for i in cols:
            df_n_unique[i] = df[i].nunique()

        DF_Count_Uniq_Values_By_col = pd.Series(df_n_unique).reset_index().rename(columns = {"index": 'Column_Name' ,
                                                                                             0:"#Unique_Values"})
        return DF_Count_Uniq_Values_By_col

# ---------------------- Decision Tree related ----------------
    def entropy(self, df,col = None ):
        try:
            if len(col)>0:
                labeled_data = self.df_col_val_perc(df, col)
                entropy = []
                for i in range(labeled_data.shape[0]):
                    total_counts = labeled_data['Value_Counts'].sum()
                    #print(labeled_data['Value_Counts'][i])
                    pro_ratio = labeled_data['Value_Counts'][i]/total_counts
                    entropy.append(-(pro_ratio*np.log2(pro_ratio)))
                return np.sum(entropy)
        except:
            print("Pass the column name to calculate the entropy")

    def entropy_all_cols(self, df):
        cols = list(df.columns)
        entropy_cols = {}
        for i in cols:
            entropy_cols[i] = (self.entropy(df,i))

        entropy_cols = pd.Series(entropy_cols).reset_index().rename(columns = {"index": 'Predictor_Name' , 0:"Entropy"})
        entropy_cols = entropy_cols.sort_values(by = 'Entropy' , ascending = True)
        return entropy_cols

    def descriptive_statistics(self,df, cols = [] , full_info = False, num_decm_points = 2):
        if (len(cols)==0) | (type(cols) !=list) :
            print("Please supply the list of the columns, for which you want o see the Descriptive Statistics")
        else:
            if full_info == False:
                for i in cols:
                    print(i ,":")
                    q3_ = df[i].quantile(.75)
                    q1_ = df[i].quantile(.25)
                    iqr_ = q3_ - q1_
                    low_iqr_ = q1_ - (1.5*iqr_)
                    upp_iqr_ = q3_ + (1.5*iqr_)
                    outliers_range = (df[i]> upp_iqr_) | (df[i]< low_iqr_)
                    outliers = list(df.loc[outliers_range , i])
                    print('iqr:', iqr_ , ', #outliers:', len(outliers) , "\n")
            elif full_info == True:
                for i in cols:
                    #print(i,":")
                    q3_ = df[i].quantile(.75)
                    q1_ = df[i].quantile(.25)
                    iqr_ = q3_ - q1_
                    low_fence_iqr_ = q1_ - (1.5*iqr_)
                    upp_fence_iqr_ = q3_ + (1.5*iqr_)
                    outliers_range = (df[i]> upp_fence_iqr_) | (df[i]< low_fence_iqr_)
                    outliers = list(df.loc[outliers_range , i])
                    outliers_neg = list(df.loc[df[i]> upp_fence_iqr_ , i])
                    outliers_pos = list(df.loc[df[i]< low_fence_iqr_ , i])
                    info_1 = {'Min' : np.round(df[i].min(),2),
                            'Q1' : np.round(df[i].quantile(.25),num_decm_points),
                            'Median' : np.round(df[i].quantile(.5),num_decm_points),
                            'Q3' : np.round(df[i].quantile(.75),num_decm_points),
                            'Max' : np.round(df[i].quantile(1),num_decm_points),
                            'Mean' :np.round( df[i].mean(),num_decm_points),
                            'STD' : np.round(df[i].std(),num_decm_points),
                            'Variance' : np.round(df[i].var(),num_decm_points),
                            'Count' : df[i].count(),
                            'IQR' : np.round(iqr_,num_decm_points),
                            'IQR_Lower_Fence' : np.round(low_fence_iqr_,num_decm_points),
                            'IQR_Upper_Fence' : np.round(upp_fence_iqr_,num_decm_points),
                            'Skewness' : np.round(df[i].skew(),num_decm_points),
                            'Kurtosis' : np.round(df[i].kurt(),num_decm_points),
                            '#NonOutliers' : df[i].shape[0]-len(outliers),
                            'NonOutliers_Perc' : np.round(((df[i].shape[0]-len(outliers)) / df[i].shape[0])*100,num_decm_points),
                            '#Outliers' : len(outliers),
                            'Outliers_Perc' : np.round((len(outliers) / df[i].shape[0])*100,num_decm_points),
                            '#Outliers_neg' : len(outliers_neg),
                            '#Outliers_pos' : len(outliers_pos)
                        }
                    print(info_1 , "\n")

    def Outlier_Detect_And_Show_Repl_Value(self,
                df,
                cols = [],
                detect_method = 'iqr',
                replace_outlier_by = 'mean',
                replace_nulls_by = 'mean'
               ):
        data_info = {}
        cols = list(cols)
        df = pd.DataFrame(df)
        #df1 = pd.DataFrame(df[cols])
        #print("Using",detect_method.upper(), "to detect the Outliers and" ,
             # 'Nulls are replaced by', replace_nulls_by.upper(),
             # 'Outliers are replaced by', replace_outlier_by.upper()
             #)
        for i in cols:
            df1 = pd.DataFrame(df[i])
            df1[i] = df1[i].astype(np.float64)
            #print(i, "\n\n")

            #--------- Replacing nulls -----------
            if replace_nulls_by == 'mean':
                df1[i] = df1[i].fillna(df1[i].mean())
            elif replace_nulls_by == 'median':
                df1[i] = df1[i].fillna(df1[i].median())

            #--------- Descriptive Statistics -----------
            means_ = np.mean(df[i])
            std_ = np.std(df1[i])
            medians_ = np.median(df1[i])
            q3_ = df1[i].quantile(.75)
            q1_ = df1[i].quantile(.25)
            iqr_ = q3_ - q1_
            low_iqr_ = q1_ - (1.5*iqr_)
            upp_iqr_ = q3_ + (1.5*iqr_)
            df1['ZScores'] = df1[i].apply(lambda X : ((X - means_)/std_))
            mode_2 = self.Data_Mode_Values(df1[i])[0]

            values_after_replacing_Outliers = 'Values_Updated'

            if detect_method == 'iqr':
                df1['Outlier_or_Not'] = np.where(((df1[i]> upp_iqr_) | (df1[i]< low_iqr_)),'Y','N')
                if replace_outlier_by =='mean':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',means_,df1[i])
                elif replace_outlier_by =='median':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',medians_,df1[i])
                elif replace_outlier_by =='mode':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',mode_2,df1[i])

            elif detect_method == 'zscore':
                df1['Outliers_or_Not'] = np.where(((df1['ZScores']> 3) | (df1['ZScores']< -3)),'Y','N')
                if replace_outlier_by =='mean':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outliers_or_Not']=='Y', means_,df1[i])
                elif replace_outlier_by =='median':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outliers_or_Not']=='Y', medians_,df1[i])
                elif replace_outlier_by =='mode':
                    df1[values_after_replacing_Outliers] = np.where(df1['Outlier_or_Not']=='Y',mode_2,df1[i])

            data_info[i] = df1
        return (data_info)
    
    def outlier_replace_in_Num_Cols(self, df , cols = [],
                     detect_method = 'iqr',
                    replace_outlier_by = 'mean',
                    replace_nulls_by = 'mean'
                                     ):
        for i in cols:
            j  = self.Outlier_Detect_And_Show_Repl_Value(df, cols = [i],
                      detect_method = detect_method,
                      replace_outlier_by = replace_outlier_by,
                      replace_nulls_by = replace_nulls_by)
            df[i] = pd.DataFrame(j[i])['Values_Updated'].values    
    
# def numerical_values_bins(df , cols =[] , no_bins_col_wise = [], default_no_bins = 3):
#     bins_ = {}    
#     cols = list(cols)
#     no_bins_col_wise = list(no_bins_col_wise)
#     #print(type(no_bins_col_wise) , len( no_bins_col_wise))
#     if (len(no_bins_col_wise)==0) | (no_bins_col_wise==None) | (len(cols) != len(no_bins_col_wise)):
#         no_bins = list([default_no_bins]*len(cols))
#     else:
#         no_bins = no_bins_col_wise
#     #print(no_bins)
#     for i, v in enumerate(cols):
#         bins_[v] = Data_pre_pro.df_col_val_perc(pd.cut(df[v],no_bins[i]))
#         bins_[v]['Ranks']=list(range(len(bins_[v]['Ranks'])))
#         bins_[v][v]= bins_[v][v].astype(str)
#         bins_[v].columns = ['Range', 'Counts', 'Perc', 'Cum_Perc', 'Mapping_Value']
#         bins_[v] = bins_[v][['Range','Mapping_Value','Counts', 'Perc', 'Cum_Perc']]      
#         df[v] = pd.cut(df[v],no_bins[i], labels = list(range(no_bins[i])))  
#     print(bins_)

#     def replacing_nulls_in_numeric_cols(self,
#                     df,
#                     numeric_cols = [],
#                     replace_nulls_by = 'mean'
#                    ):
#         numeric_cols = list(numeric_cols)
#         df = pd.DataFrame(df)
#         for i in numeric_cols:
#             df[i] = df[i].astype(np.float64)
#                 #--------- Replacing nulls -----------
#             if replace_nulls_by == 'mean':
#                 df[i] = df[i].fillna(df[i].mean())
#             elif replace_nulls_by == 'median':
#                 df[i] = df[i].fillna(df[i].median())        

# In[ ]:

       
class Text_Mining_Variables:
    import re
    import os
    import csv
    import sys
    import nltk
    import spacy
    import random
    import string
    import unicodedata
    import math as m
    import numpy as np
    import pandas as pd
    from textblob import Word
    from textblob import TextBlob
    from bs4 import BeautifulSoup
    from nltk.stem import PorterStemmer
    from spacy.lang.en.stop_words import STOP_WORDS
    from nltk.stem.snowball import SnowballStemmer
    remove_punctuation = string.punctuation

    import re
    re_syntax_extract_urls = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    re_syntax_email_ids = r"([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
    re_syntax_get_urls = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # re_syntax_get_urls =r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    re_extract_numbers = r"[\d]+"
    re_extract_numbers_including_decimals = r"[-+]?(\d+\.?\d*|\.\d+)"
    wh_words = ['who', 'what', 'when', 'why', 'how', 'which', 'where', 'whom']
# removing stop words
    import nltk
    from nltk.corpus import stopwords
    stop_words_1 = list(set(stopwords.words('english')))

    import spacy
    en = spacy.load('en_core_web_sm')
    stop_words_2 = list(set(en.Defaults.stop_words))
    stop_words_total =  list(set(stop_words_2 + stop_words_1))
# # print( "len(stop_words):" , len(stop_words_total),
# #     "\nlen(stop_words_2)-SPACY:" , len(stop_words_2),
# #     "\nlen(stop_words_1)-NLTK:" , len(stop_words_1)
# #      )

# removing stop words
    #https://gist.github.com/sebleier/554280
#     import nltk
#     from nltk.corpus import stopwords
#     stop_words_1 = list(set(stopwords.words('english')))

#     import spacy
#     en = spacy.load('en_core_web_sm')
#     stop_words_2 = list(set(en.Defaults.stop_words))
#     stop_words_total =  list(set(stop_words_2 + stop_words_1))
    # print( "len(stop_words):" , len(stop_words_total),
    #     "\nlen(stop_words_2)-SPACY:" , len(stop_words_2),
    #     "\nlen(stop_words_1)-NLTK:" , len(stop_words_1)
    #      )
    
    # import requests
    # stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
    # stopwords = set(stopwords_list.decode().splitlines())
    # stopwords    
    
    emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"
                                   u"\U0001F300-\U0001F5FF"
                                   u"\U0001F680-\U0001F6FF"
                                   u"\U0001F1E0-\U0001F1FF"
                                   u"\U00002500-\U00002BEF"
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f" 
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)
    chat_abbrevations = {' 4u ': ' i have a question for you. ',
     ' ^^ ': ' read line above ',
     ' 121 ': ' one to one ',
     ' <3 ': ' love ',
     ' 2 ': ' to ',
     ' 2mrw ': ' tomorrow ',
     ' 4 ': ' for ',
     ' afk ': ' away from keyboard ',
     ' aka ': ' also known as ',
     ' asap ': ' as soon as possible ',
     ' a/s/l ': ' age sex location ',
     ' ayt ': ' are you there  ',
     ' b2w ': ' back to work ',
     ' b4 ': ' before ',
     ' bbl ': ' be back later ',
     ' bbs ': ' be back soon ',
     ' bf ': ' boyfriend ',
     ' bff ': ' best friend(s) forever ',
     ' brb ': ' be right ',
     ' btw ': ' by the way ',
     ' cmb ': ' call me back ',
     ' cmiiw ': " correct me if i am wrong ",
     ' cu ': ' see you ',
     ' cu l8r ': ' see you later ',
     ' cuz ': ' because ',
     ' cos ': ' because ',
     ' cwyl ': ' chat with you later ',
     ' dc ': ' disconnected ',
     ' diy ': ' do it yourself ',
     ' dm ': ' direct message ',
     ' f2f ': ' face to face ',
     ' faq ': ' frequently asked questions ',
     ' fb ': ' facebook ',
     ' fyi ': ' for your information ',
     ' fyeo ': ' for your eyes only ',
     ' gb ': ' goodbye ',
     ' gf ': ' girlfriend ',
     ' gg ': ' gotta go ',
     ' gl ': ' good luck ',
     ' gr8 ': ' great! ',
     ' hbd ': ' happy birthday ',
     ' hhhhhh ': ' very funny ',
     ' how r u ': ' how are you  ',
     ' ic ': ' i see ',
     ' idk ': " i do not know ",
     ' imho ': ' in my humble opinion ',
     ' ik ': ' i know ',
     ' im ': ' instant message ',
     ' iow ': ' in other words ',
     ' j k ': ' just kidding ',
     ' k ': ' ok ',
     ' l8r ': ' later or goodbye ',
     ' lol ': ' laugh out loud ',
     ' m/f ': ' male or female ',
     ' mins ': ' minutes ',
     ' msg ': ' message ',
     ' nv ': ' nevermind ',
     ' oic ': ' oh, i see ',
     ' otw ': ' on the way ',
     ' p2p ': ' person to person ',
     ' plz ': ' please ',
     #' plz': ' please ',
     ' pm ': ' private message ',
     ' rofl ': ' rolling on the floor laughing ',
     ' ruok ': ' are you okay ',
     ' sup ': " what is up ",
     ' zup ': " what is up ",
     ' syl ': ' see you later ',
     ' tgif ': " thank goodness it is friday ",
     ' thx ': ' thanks ',
     ' thnx ': ' thanks ',
     ' ttfn ': ' ta ta for now ',
     ' ttyl ': ' talk to you later ',
     ' tyt ': ' take your time ',
     ' u ': ' you ',
     ' u2 ': ' you too ',
     ' ur ': " your   you are ",
     ' w  ': ' with ',
     ' w/o ': ' without ',
     ' wru ': ' where are you ',
     ' xo ': ' hugs and kisses love ',
     ' zzz ': ' tired or bored ',
     ' gm ': ' good morning ',             
     ' ga ': ' good afternoon ',     
     ' ge ': ' good evening ',     
     ' gn ': ' good night ', 
     ' gm, ': ' good morning ',
     ' ga, ': ' good afternoon, ',
     ' ge, ': ' good evening, ', 
     ' gn, ': ' good night, ',
     ' gn.': ' good night. ',
     ' gm.': ' good morning. ',
     ' ge.': ' good evening. ',
     ' ga.': ' good afternoon. ' ,
     ' nlp ' : ' natural language processing ',
     ' pls': ' please',
     ' pls,': ' please,',
     ' pls.': ' please.',
     ' r ' : ' you ',
     ' hru '   : ' how are you ',
      ' n ' : ' and ',
      "B'day" : "Birthday"
                   }
    contractions_1 = {
    "ain't": "am not",
    "aren't": "are not",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "how's": "how does",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that would",
    "that'd've": "that would have",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    " u ": " you ",
    " ur ": " your ",
    " n ": " and ",
    " ok " : " okay ",
    " nope " : " no ",
    " asap ": " as soon as possible ",
    " eod ": " end of the day ",
    " fyi ": " for your information ",
    " omg ": " oh my god !!! ",
    " gn ": " good night ",
    " ge ": " good evening " ,
    " gm ": " good morning " ,
}

# ----------------------------------------------------       
class dummy1:
    pass
# ----------------------------------------------------
class Data_Pre_Processing_Text_Mining(Text_Mining_Variables):
    import re
    import os
    import csv
    import sys
    import nltk
    import spacy
    import random
    import string
    import unicodedata
    import math as m
    import numpy as np
    import pandas as pd
    from textblob import Word
    from textblob import TextBlob
    from bs4 import BeautifulSoup
    from nltk.stem import PorterStemmer
    from spacy.lang.en.stop_words import STOP_WORDS
    from nltk.stem.snowball import SnowballStemmer
    remove_punctuation = string.punctuation
   
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    nltk.download('punkt')
    nlp = spacy.load("en_core_web_sm")

    chat_abbrevations = Text_Mining_Variables.chat_abbrevations
    re_syntax_email_ids = Text_Mining_Variables.re_syntax_email_ids
    re_syntax_extract_urls = Text_Mining_Variables.re_syntax_extract_urls
    contractions_1 = Text_Mining_Variables.contractions_1
    emoji_pattern = Text_Mining_Variables.emoji_pattern
    stop_words_total = list(Text_Mining_Variables.stop_words_total)
    re_extract_numbers_including_decimals = Text_Mining_Variables.re_extract_numbers_including_decimals
    
    
    def cosine_similarity(self, V1,V2):
        import numpy as np
        #V1, V2 should be Numpy arrays and contain numerical values to perform VECTOR DOT products
        V1 = np.array(V1)
        V2 = np.array(V2)
        result = np.dot(1, V2) / (np.sVqrt(np.sum(V1**2)) * np.sqrt(np.sum(V2**2)))
        return result

    def spelling_correction(self,text):
        from textblob import TextBlob
        text = str(TextBlob(text).correct()).strip()
        return text

    def remove_html_tags(self,text):
        from bs4 import BeautifulSoup
        text = BeautifulSoup(text, 'lxml').get_text()
        return text.strip()

    def remove_accented_chars(self,text):
        import unicodedata
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return text

    def remove_spaces_repetition(self,text):
        text = " ".join(text.strip().split())
        return text

    def remove_punctuations(self,text):
        import string,re
        remove_punctuation = string.punctuation
        for i in remove_punctuation:
            text = text.replace(i, "").replace("  ", "").strip()
        text = re.sub(r"[\s]{1,}", " " , str(text)).strip()
        return text
    def get_email_ids(self,text):
        import string,re
        emails_ids = re.findall(Text_Mining_Variables.re_syntax_email_ids, text.lower())
        return emails_ids
        
    def count_email_ids(self,text):
        import string,re
        emails_ids = re.findall(Text_Mining_Variables.re_syntax_email_ids,text.lower())
        return len(emails_ids)        
        
    def remove_email_ids(self,text):
        import string,re
        text_formatted = re.sub(Text_Mining_Variables.re_syntax_email_ids, "",text.lower())
        return text_formatted
        
    def get_urls(self,text):
        import string,re
        text = text.lower()
        urls = re.findall(Text_Mining_Variables.re_syntax_extract_urls, text)
        return urls
        
    def count_urls(self,text):
        import string,re
        text = text.lower()
        urls = re.findall(Text_Mining_Variables.re_syntax_extract_urls, text)
        return len(urls)

    def remove_urls(self,text):
        import string,re
        text = text.lower()
        urls = re.sub(Text_Mining_Variables.re_syntax_extract_urls, "", text)
        return urls

    def count_words(self,text):
        import string,re
        words = str(text).split()
        return len(words)

    def count_characters(self,text):
        import string,re
        #words = self.remove_spaces_repetition(str(text))
        raw_text = re.sub(r"[^\w\s\_]*", "" , str(text)).strip()
        raw_text = re.sub(r"[\s]{1,}", " " , str(raw_text)).strip()
        return len(raw_text)

    def count_characters2(self,text):
        import string,re
        text1 = self.remove_punctuations(text)
        words = str(text1).split()
        final_text = ["".join(i) for i in words]
        return len(final_text)
        
    def count_stop_words(self,text):
        import spacy
        from spacy.lang.en.stop_words import STOP_WORDS
        counts = len([i for i in text.split() if i in self.stop_words_total])
        return counts
        
    def count_Non_stop_words(self,text):
        import spacy
        from spacy.lang.en.stop_words import STOP_WORDS
        counts = len([i for i in text.split() if i not in self.stop_words_total])
        return counts         
        
    def count_punctuations(self,text):
        import re
        k = len(text) - len(re.sub(r"[^\w\s]+" , "", re.sub("[\s]+" , " " , text)))
        return k

    def remove_stop_words(self,text):
        import spacy
        from spacy.lang.en.stop_words import STOP_WORDS
        #Text_Mining_Variables.stop_words_total
        text = " ".join([i for i in text.split() if i not in self.stop_words_total])
        return text.strip()
    def count_upper_case_words(self,text, min_num_chars = 2):
        k =len([i for i in text.split() if i.isupper() and len(i)>min_num_chars])
        #k1 =([i for i in text.split() if i.isupper() and len(i)>2])
        return k
        
    def count_sentences(self,text):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        k =len([i for i in doc.sents])
        return k

    def count_sentences_nltk(self,text):
        from nltk.tokenize import sent_tokenize
        k =len(sent_tokenize(text))
        return k  
        
    def get_upper_case_words(self,text, min_num_chars = 2):
        k =([i for i in text.split() if i.isupper() and len(i)>=min_num_chars])
        return k

    def custom_contractions(self,text):
        if type(text) is str:
            text = text.lower()
            for key in Text_Mining_Variables.contractions_1:
                value = Text_Mining_Variables.contractions_1[key]
                text = text.replace(key,value)
            return text
        else: return text

    def remove_retweets(self,text):
        import string,re
        text = re.sub("RT" , "", text)
        return text

    def count_hash_tags(self,text):
        k = len([i for i in text.split() if i.startswith("#")])
        return k

    def count_mentions(self,text):
        k = len([i for i in text.split() if i.startswith("@")])
        return k

    def get_numericals(self,text):
        import re
        numericals = list(re.findall(self.re_extract_numbers_including_decimals,text.lower()) )        
        return (numericals)
        
    def get_numericals_2(self,text):
        import re
        numericals = [i for i in text.split() if i.isdigit()]     
        return (numericals) 
       
    def count_numericals(self,text):
        import re
        numericals = re.findall(self.re_extract_numbers_including_decimals,text.lower())       
        return len(numericals)
        
    def count_numericals_2(self,text):
        import re
        numericals = [i for i in text.split() if i.isdigit()]   
        return len(numericals)
        
    def remove_numericals(self,text):
        import re
        text = re.sub(self.re_extract_numbers_including_decimals,"", text.lower())       
        return text

    def count_verbs(self,text):
        from textblob import TextBlob
        k = len([i for i in text.split() if TextBlob(i).tags[0][1] in ['VB','VBD','VBG','VBN','VBP' ,'VBZ']])
        return k
        
    def count_digits(self,text):
        from textblob import TextBlob
        k = len([i for i in text.split() if TextBlob(i).tags[0][1] in ['CC','CD']])
        return k

    def count_adjectives(self,text):
        from textblob import TextBlob
        k = len([i for i in text.split() if TextBlob(i).tags[0][1] in ['JJ','JJR' , 'JJR']])
        return k
        
    def count_pronouns(self,text):
        from textblob import TextBlob
        k = len([i for i in text.split() if TextBlob(i).tags[0][1] in ['PRP','PRP$' , 'POS']])
        return k        

    def get_root_word(self, text_):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        
        # try:
        #     nlp = spacy.load('en_core_web_lg')
        #     print('large is imported')
                 
        # except (ModuleNotFoundError, ValueError):
        #     print('large is not imported, trying to import medium')
        #     nlp = spacy.load('en_core_web_md')
        #     print('medium')
        # except:
        #     print('large, medium are not imported, and trying to import small')
        #     nlp = spacy.load('en_core_web_sm')
        #     print('small')   
        text_list = []
        doc = nlp(text_)
        
        for token in doc:
            lemma = str(token.lemma_)
            if lemma == '-PRON-' or lemma == 'be':
                lemma = token.text
            text_list.append(lemma)
        return (" ".join(text_list))

    def nltk_snowball_stemmer(self, text):
        from nltk.stem.snowball import SnowballStemmer
        snowball_stemmer = SnowballStemmer(language='english')
        text = " ".join([snowball_stemmer.stem(token) for token in text.split()])
        return text    
 
    def textblob_lemma(self,text):
        from nltk.stem.snowball import SnowballStemmer
        from textblob import Word
        snowball_stemmer = SnowballStemmer(language='english')
        text = str(" ".join([Word(token).lemmatize() for token in text.split()])).strip()
        return text

    def spacy_lemma(self,text):
        import spacy
        #!python -m spacy download en_core_web_sm
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        text = str(" ".join([token.lemma_ for token in doc])).strip() 
        return text.strip()
        
    def remove_most_repeated_rare_words(self, df, col = None, number_of_words_remov = 5):
        A = " ".join(df[col])
        t = list(pd.Series(A.split()).value_counts()[:number_of_words_remov].index)
        b = list(pd.Series(A.split()).value_counts()[-number_of_words_remov:].index)
        b = b+t
        #len(b)
        f = list(df[col].apply(lambda X : " ".join([i for i in X.split() if i not in b])))
        df[col] = f
        return df
    import re

    def get_actual_text_chat_abbrevations(self,text):    
        for i in Text_Mining_Variables.chat_abbrevations:
            text = text.lower()
            key = i.lower()
            value = Text_Mining_Variables.chat_abbrevations[i].lower()
            text = text.replace(key,value)
        return text
    def remove_punctuations_2(self,text):
        import re
        text = re.sub(r'[^\w\s]', '', text)
        #text = re.sub(r'[\s\s]', '', text)
        return text

    def count_punctuations_2(self,text):
        import re        
        extract_pncts = re.findall(r'[^\w\s]',text)
        new_text = re.sub(r'[^\w\s]', "", text)
        return len(extract_pncts) 
        
#     def remove_emojis_1(self,text):
#         import csv,os,sys,re
#         try:
#             from cleantext import clean
#         except:
#             ! pip install cleantext
#             from cleantext import clean
            
#         import re
#         text = clean(text, no_emoji=True)
#         return text
    
    def remove_emojis_2(self,text):
        import csv,os,sys,re
        text = self.emoji_pattern.sub(r'', text)
        return text
        
    #def get_emojis(self,text):
        #import csv,os,sys,re
        #emojis = list(self.emoji_pattern.findall(text))
        #return emojis
        
    def count_nouns_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        nouns = [i for i in doc if i.pos_ in ['NOUN']]
        return len(nouns)
        
    def count_pronouns_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['PRON' ]]
        return len(k)

    def count_propernouns_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['PROPN' ]]
        return len(k)

    def count_adjectives_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        ADJ = [i for i in doc if i.pos_ in ['ADJ']]
        return len(ADJ)
        
    def count_auxliary_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['AUX']]
        return len(k)

    def count_verbs_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['VERB']]
        return len(k)
        
    def count_adverbs_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['ADV']]
        return len(k)
        
    def count_numericals_spacy(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = [i for i in doc if i.pos_ in ['NUM']]
        return len(k)
        
    def count_verbs_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['VBN', 'VBP', 'VBG', "VB"]])
        return k
        
    def count_nouns_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['NN', 'NNS', 'NNP', "NNPS"]])
        return k 
        
    def count_pronouns_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['PRP', 'PRP$', 'WP']])
        return k
        
    def count_adverbs_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['RBS', 'RB','RBR','WRB']])
        return k 

    def count_adjectives_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['JJ', 'JJS','JJR']])
        return k 
        
    def count_conjuctions_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['CC']])
        return k 

    def count_interjections_nltk(self,text):
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        k = len([i[0] for i in nltk.pos_tag(text.split()) if i[1] in  ['UH']])
        return k

    def remove_text_garbage(self,text):
        import re
        import os
        import csv
        import sys
        import nltk
        import spacy
        import random
        import string
        import unicodedata
        import math as m
        import numpy as np
        import pandas as pd
        from textblob import Word
        from textblob import TextBlob
        from bs4 import BeautifulSoup
        from nltk.stem import PorterStemmer
        from spacy.lang.en.stop_words import STOP_WORDS
        from nltk.stem.snowball import SnowballStemmer
        remove_punctuation = string.punctuation
        
        text = " ".join(text.lower().strip().split())
        #print("converting into lowercase: Done")
        
        text = self.spelling_correction(text)
        #print("spelling_correction: Done")
        
        text = BeautifulSoup(text, 'lxml').get_text().strip()  
        #print("remove_html_tags: Done") 
        
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        #print("remove_accented_chars: Done") 
        
        text = " ".join(text.strip().split())       
        for i in remove_punctuation:
            text = text.replace(i, "").replace("  ", "").strip()
        #print("remove_punctuation: Done")  
            
        text = re.sub(r"[\s]{1,}", " " , str(text)).strip()
        #print("remove_spaces_repetition: Done")
        
        text = re.sub(Text_Mining_Variables.re_syntax_extract_urls, "", text)
        #print("remove_urls: Done")
        
        text = " ".join([i for i in text.split() if i not in self.stop_words_total])
        #print("remove_stop_words_total: Done")
        
        text = text.strip()
        text = re.sub("RT" , "", text)
        #print("remove_sretweets: Done")
        
        text = re.sub(r'[^\w\s]', '', text)
        #print("remove_punctuations: Done")
        
        text = self.emoji_pattern.sub(r'', text).strip()
        #print("remove_emoji_pattern: Done")
        
        text = re.sub(Text_Mining_Variables.re_syntax_email_ids, "",text).strip()
        #print("remove_email_ids: Done")
         
        text = " ".join(text.lower().strip().split())        
        #text = self.spelling_correction(text).strip()
        return text
        
    def simple_clean(self, text):
        import string
        import re
        remove_punctuation = string.punctuation
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        tokens = [i.lemma_.lower().strip() for i in doc ]
        tokens = [i for i in tokens if i not in self.stop_words_total and i not in remove_punctuation]
        #tokens = " ".join(tokens)
        #for i in remove_punctuation:
            #if i in tokens:
                #tokens =tokens.replace(i, "").replace("  ", "").strip()
        return tokens
        
    
#--------------------------------------------------------------------------------------------
    def Text_Basic_Pre_Processing(self,df, text_column_name = None,
                              count_stop_words = False,count_Non_stop_words= False, 
                              count_sentences = False, count_numericals= False, 
                              count_punctuations= False,
                               
                              count_nouns = False,count_pronouns= False,
                              count_verbs= False,count_adverbs =False,
                              count_adjectives= False,count_auxliary = False,
                              spelling_correction = False,                              
                                                           
                              twitter_messages = False,count_hash_tags= False,count_mentions= False,
                              get_email_ids = False, get_urls = False,
                              process_chat_abbrevations = False,
                              remove_most_repeated_rare_words= False ,
                              number_of_words_remov = 10):
                              
        print("Text Data Preprocessing for Text Analytics is started ................ :)\n")
        
        df[text_column_name] = df[text_column_name].astype(str)
        
        df['len_Acual_Message'] = df[text_column_name].apply(lambda X : len(str(X)))
        
        df['Words_Count'] = df[text_column_name].apply(lambda X : self.count_words(str(X)))
        print("Words_Count: Done")
        
        df['Literal_Count'] = df[text_column_name].apply(lambda X : self.count_characters(str(X)))
        print("Literal_Count: Done")
        
        if count_sentences == True:
            df['count_sentences'] = df[text_column_name].apply(lambda X : self.count_sentences_nltk(str(X)))
            print("count_sentences: Done")
        
        if count_punctuations == True:
            #import spacy
            #nlp = spacy.load("en_core_web_sm")
            df['count_punctuations'] = df[text_column_name].apply(lambda X : \
                                        (self.count_punctuations_2(str(X))))
            print("count_punctuations: Done") 
        
        df['AVG_Chars_Count'] = df['Literal_Count'] / df['Words_Count']
        df['AVG_Chars_Count'] = df['AVG_Chars_Count'].astype(np.int64)
        print("AVG_Chars_Count: Done")
        
        df[text_column_name] = df[text_column_name].apply(lambda X : self.remove_emojis_2(text = str(X)))
        print("remove_emojis: Done")
        
        df['Upper_case_Words_Count'] = df[text_column_name].apply(lambda X : self.count_upper_case_words(str(X)))
        print("Upper_case_Words_Count: Done")
        
        df['Get_Upper_case_Words'] = df[text_column_name].apply(lambda X : self.get_upper_case_words(str(X)))
        print("get_upper_case_words: Done")        
        
        if get_email_ids == True:
            df['email_ids'] = df[text_column_name].apply(lambda X : (self.get_email_ids(str(X))))
            print("get_email_ids: Done")

        if get_urls == True:
            df['urls'] = df[text_column_name].apply(lambda X : (self.get_urls(str(X))))
            print("get_urls: Done")
      
        df['count_email_ids'] = df[text_column_name].apply(lambda X : len(self.get_email_ids(str(X))))
        print("count_email_ids: Done")
        
        df['count_urls'] = df[text_column_name].apply(lambda X : len(self.get_urls(str(X))))
        print("count_urls: Done")
        
        df[text_column_name] = df[text_column_name].apply(lambda X : (self.remove_email_ids(str(X))))
        print("remove_email_ids: Done")

        df[text_column_name] = df[text_column_name].apply(lambda X : (self.remove_urls(str(X))))
        print("remove_urls: Done")
        
        df[text_column_name] = df[text_column_name].apply(lambda X : (self.remove_html_tags(str(X))))
        print("remove_html_tags: Done")
        
        df[text_column_name] = df[text_column_name].apply(lambda X : self.remove_retweets(str(X)))
        print("remove_retweets: Done")  
        
        if (twitter_messages ==True) and (count_hash_tags==True) :
            df['count_hash_tags'] = df[text_column_name].apply(lambda X : self.count_hash_tags(str(X)))
            print("count_hash_tags: Done")
            
        if (twitter_messages ==True) and (count_mentions==True) :            
            df['count_mentions'] = df[text_column_name].apply(lambda X : self.count_mentions(str(X)))
            print("count_mentions: Done")            
        
        df['Processed_Message'] = df[text_column_name].apply(lambda X : (str(X).lower()))
        
        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : \
                                        self.custom_contractions(str(X)))    
        print("custom_contractions: Done")
        
        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : (self.remove_spaces_repetition(str(X))))
        print("remove_spaces_repetition: Done")

        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : (self.remove_accented_chars(str(X))))
        print("remove_accented_chars: Done")        

        if process_chat_abbrevations ==True:
            df['Processed_Message'] = df['Processed_Message'].apply(lambda X : \
                                                 (self.get_actual_text_chat_abbrevations(text = str(X))))
            print("get_actual_text_chat_abbrevations: Done")
            
        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.remove_punctuations(str(X)))
        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.remove_punctuations_2(text = str(X)))
        print("remove_punctuations: Done")       
        
        
        if spelling_correction == True:        
            from textblob import TextBlob
            df['Processed_Message'] = df['Processed_Message'].apply(lambda X: str(TextBlob(X).correct()))
            print("textblob_Spelling_correction: Done")        
        
        if count_stop_words == True:
            df['count_stop_words'] = df['Processed_Message'].apply(lambda X : \
                                            self.count_stop_words(text = str(X)))
            print("count_stop_words: Done")
            
        if count_Non_stop_words == True:
            df['count_Non_stop_words'] = df['Processed_Message'].apply(lambda X : \
                                            (self.count_Non_stop_words(str(X))))
            print("count_Non_stop_words: Done")       
  
        if count_nouns ==True:
            #import spacy
            #nlp = spacy.load("en_core_web_sm")
            df['count_nouns'] = df['Processed_Message'].apply(lambda X:\
                self.count_nouns_nltk(text = X))
            print("count_nouns: Done") 
            
        if count_pronouns ==True:
            df['count_pronouns'] = df['Processed_Message'].apply(lambda X : \
            self.count_pronouns_nltk(text = X))
            print("count_pronouns: Done") 
            
        if count_verbs ==True:
            df['count_verbs'] = df['Processed_Message'].apply(lambda X : \
            self.count_verbs_nltk(text = X))
            print("count_verbs: Done")
            
        if count_adverbs ==True:
            df['count_adverbs'] = df['Processed_Message'].apply(lambda X : \
            self.count_adverbs_nltk(text = X))
            print("count_adverbs: Done")           

        if count_adjectives ==True:
            df['count_adjectives'] = df['Processed_Message'].apply(lambda X : \
            self.count_adjectives_nltk(text = X))
            
            print("count_adjectives: Done")
            
        #if count_auxliary == True:
            #df['count_auxliary'] = df['Processed_Message'].apply(lambda X : (self.count_auxliary_spacy(str(X))))
            #print("count_auxliary: Done")
            
        if count_numericals == True:
            df['count_numericals'] = df['Processed_Message'].apply(self.count_numericals)
            print("count_numericals: Done")
        if count_numericals == True:
            df['get_numericals'] = df['Processed_Message'].apply(self.get_numericals)
            print("get_numericals: Done")
            
        #from textblob import TextBlob 
        #df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.remove_text_garbage(text = str(X)))
        #print("remove_text_garbage: Done")
                    
        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.remove_stop_words(str(X)))
        print("remove_stop_words: Done")

        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.nltk_snowball_stemmer(str(X)))
        print("nltk_snowball_stemmer : Done")

        df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.textblob_lemma(text = str(X)))
        print("textblob_lemma: Done")
        
        #df['Processed_Message'] = df['Processed_Message'].apply(lambda X : self.get_root_word(str(X)))
        #print("get_root_word i.e. lemmatization: Done")

        if remove_most_repeated_rare_words == True:
            df = self.remove_most_repeated_rare_words(df, col='Processed_Message' , \
                              number_of_words_remov = number_of_words_remov)
            print("remove_most_repeated_rare_words: Done, number of Top and Bottom words remove is: ",
            number_of_words_remov)
            
        df['len_Processed_Message'] = df['Processed_Message'].apply(lambda X : len(X))
        
        print("length of Processed_Message is added to the main DataFrame : Done")
        
        print("\nText Data Preprocessing for Text Analytics is Completed!!!!!!!!!!!!!! :)")
        return df