# 0- Import libraries

import streamlit as st
import pandas as pd
import hashlib
import pickle
import warnings
warnings.filterwarnings('ignore')


# 1- Login functions

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
    
def isValid_Password(password):
    #returns 0 if correct 
    #returns 1 if incorrect

    res=0
    if len(password)!=0 and (len(password)<6 or len(password)>15):
        res=1
    if ('!' or '@' or '#' or '$'or '%' or'^'or'&'or'*'or'('or')'or '+'or '-' or '=' or '[' or']' or'{'or'}')in  password:
        res=1
    if ('~' or '`' or '_' or '\ 'or '|' or'/'or';'or':'or'"'or'\''or '.'or ',' or '<' or '>' or'?' )in  password:
        res=1
    return res

def isValid_Username(u):
    #returns 0 if correct 
    #returns 1 if incorrect

    res=0
    if(("@" or".com") not in u):
        res=1 
    return res


# 2- Navigate_profile

def init():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in']=False
    
    if 'log_out' not in st.session_state:
        st.session_state['log_out']=False
        #passed once through log_out
    
    if 'username' not in st.session_state:
        st.session_state['username']=""
    
    if 'fullname' not in st.session_state:
        st.session_state['fullname']=""

    if 'pass' not in st.session_state:
        st.session_state['pass']=""

    if 'company_name' not in st.session_state:
        st.session_state['company_name']=""  

    if 'e-mail' not in st.session_state:
        st.session_state['e-mail']=""

    if 'phone no. 1' not in st.session_state:
        st.session_state['phone no. 1']=""
    
    if 'phone no. 2' not in st.session_state:
        st.session_state['phone no. 2']=""

    if 'company_add' not in st.session_state:
        st.session_state['company_add']=""
        
    if 'profile_submit' not in st.session_state:
        st.session_state['profile_submit']=False  

def logout():
        st.session_state['logged_in']=False
        st.session_state['log_out']=True
        st.session_state['username']=""
        st.session_state['pass']=""
        st.session_state['fullname']=""
        st.session_state['company_name']="" 
        st.session_state['e-mail']=""
        st.session_state['phone no. 1']=""
        st.session_state['phone no. 2']=""
        st.session_state['company_add']=""

        '''TO BE IMPLEMENTED'''
        #Uncomment below line if update_profile works
        #st.session_state['profile_submit']=False

def global_var():
    global new_fullname,new_comp_name,new_comp_add,new_email,new_ph_1,new_ph_2
    new_fullname=st.session_state['fullname']
    new_comp_name=st.session_state['company_name']
    new_comp_add=st.session_state['company_add']
    new_email=st.session_state['e-mail']
    new_ph_1=st.session_state['phone no. 1']
    new_ph_2=st.session_state['phone no. 2']

def isValid_input(val1,val2,val3,val4,val5,val6):
    res=7
    if(" " not in val1):
        res=1
    elif(not val2):
        res=2
    elif(("," or "-")not in val3):
        res=3
    elif(("@" or".com") not in val4):
        res=4
    elif(len(val5)!=10 or not(val5.isdigit())):
        res=5
    elif(len(val6)!=10 or not(val6.isdigit())):
        res=6
    else:
        res=0
    return res

'''TO BE IMPLEMENTED'''
def update_profile(res): 
    #gets fullname to check for if profile filled
    #st.write("1:",st.session_state['fullname'])
    #to_do
    u_db = pd.DataFrame(res,columns =["Username","Password","company_name","company_address","fullname","email","phone_num1","phone_num2"] )
    st.dataframe(u_db)
    st.write('db rec')
    #st.session_state['fullname']=check_profile()
    #st.write("2:",st.session_state['fullname'])


# 3- Model functions (or interacting with model)

# i- Online Mode
def preprocess_predictor(data):

    # loading encoders and scalers
    with open('../Model/Model_Processing/StandardScaler', 'rb') as f:
        ss = pickle.load(f)
    with open('../Model/Model_Processing/OneHotEncoder', 'rb') as f:
        ohe = pickle.load(f)
        
    # columns
    cat_cols = [col for col in data.columns if data[col].dtype == 'object'] # categorical columns
    num_cols = [col for col in data.columns if data[col].dtype != 'object'] # numerical columns

    # predictors
    data[num_cols] = ss.transform(data[num_cols])  # standard scaler for predictor
    data_ohe = ohe.transform(data[cat_cols]) # one-hot-encoding for predictor
    col_ohe = ohe.get_feature_names_out(cat_cols)

    # data after preprocessing
    data_ohe_df = pd.DataFrame(data_ohe, columns = col_ohe, index = data.index)
    data_final = pd.concat([data.drop(columns=cat_cols), data_ohe_df], axis=1)

    # load model
    with open('../Model/Churnlytical_Model.sav', 'rb') as f:
        model = pickle.load(f)

    # predicting
    single = model.predict(data_final)
    probability = model.predict_proba(data_final)
    if single == 1:
        st.error("The customer is likely to be Churn!!")
        st.warning("Confidence = {}".format(probability[:,1] * 100) + '%')
    else:
        st.success("The customer is likely to CONTINUE !!")
        st.success("The Confidence level is about {}".format(*probability[:, 0] * 100) + '%')
        

# ii- Batch Mode
def preprocess_predictor_batch(data):
    
    # loading encoders and scalers
    with open('../Model/Model_Processing/StandardScaler', 'rb') as f:
        ss = pickle.load(f)
    with open('../Model/Model_Processing/OneHotEncoder', 'rb') as f:
        ohe = pickle.load(f)

    # separate columns into categorical and numerical
    cat_cols = [col for col in data.columns if data[col].dtype == 'object'] # categorical columns
    num_cols = [col for col in data.columns if data[col].dtype != 'object'] # numerical columns

    # predictors
    # Preprocess numerical columns
    if num_cols:  # Check if there are numerical columns
        data[num_cols] = ss.transform(data[num_cols])  # Apply standard scaling

    # Preprocess categorical columns
    if cat_cols:  # Check if there are categorical columns
        data_ohe = ohe.transform(data[cat_cols])  # Apply one-hot encoding
        col_ohe = ohe.get_feature_names_out(cat_cols)
        data_ohe_df = pd.DataFrame(data_ohe, columns=col_ohe, index=data.index)
    else:
        data_ohe_df = pd.DataFrame(index=data.index)  # Empty DataFrame if no categorical data

    # Combine preprocessed numerical and categorical data
    data_final = pd.concat([data[num_cols], data_ohe_df], axis=1)

    # load model
    with open('../Model/Churnlytical_Model.sav', 'rb') as f:
        model = pickle.load(f)

    # predicting
    single = model.predict(data_final)
    probability = model.predict_proba(data_final)
    return (single,probability)

        
# End of CHURNLYTICAL_Functions.py