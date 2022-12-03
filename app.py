import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Load the model
model = pd.read_pickle('irlandia_grid_knn.pkl')

# Load the dataset
df = pd.read_csv('Deploy.csv')
#st.write(df.sample(5))

# Sidebar Prediction
#st.sidebar.subheader('Churn Prediction')
#if st.sidebar.checkbox('Show Prediction'):
# Input
st.header('Churn Prediction Presented by Team Irlandia')
st.write('Aplikasi ini memprediksi kemungkinan seseorang akan churn berdasarkan beberapa fitur yang telah dibuat')
st.write(df.sample(5))
#divider
divider = st.container()
divider.markdown('---')

st.subheader('Prediction Input')
selisih_tanggal = st.number_input('Selisih Tanggal Pembelian Akhir - Pembelian Awal',0)
promo_code = st.selectbox('Masukan Code Promo',('NOPROMO','AZ2022','BUYMORE','WEEKENDSERU','XX2022','LIBURDONG','WEEKENDMANTAP','SC2022','STARTUP'))
#st.write('Promo Code :', promo_code)
purchase_year = st.number_input('Masukan Tahun Pembelian',0)
#st.write('Tahun Pembelian :', purchase_year)
tenure = st.number_input('Masukan Tenure',0)
rfm_score = st.number_input('Masukan RFM Score',0)
total_promo = st.number_input('Masukan Total Promo',0)
monetary = st.number_input('Masukan Monetary',0)
frequency = st.number_input('Masukan Frequency',0)
recency = st.number_input('Masukan Recency',0)
ongkir = st.number_input('Masukan Ongkir',0)
monthly_spending = st.number_input('Masukan Monthly Spending',0)
payment_method = st.selectbox('Masukan Metode Pembayaran',('Credit Card', 'Gopay', 'OVO', 'Debit Card', 'LinkAja'))

# Masukan Data ke dalam df
data = [[selisih_tanggal, promo_code, purchase_year, tenure, rfm_score, total_promo, monetary, frequency, recency, ongkir, monthly_spending, payment_method]]
df = pd.DataFrame(data, columns = ['selisih_tanggal', 'promo_code', 'purchase_year', 'tenure', 'rfm_score', 'total_promo', 'monetary', 'frequency', 'recency', 'ongkir', 'monthly_spending', 'payment_method'])
# One Hot Encoding
#df = pd.get_dummies(df, columns=['promo_code', 'payment_method'])
#st.write(df)

# Feature Yang Tidak Di Select pada Select Box akan Di Isi 0
if promo_code == 'NOPROMO':
    df['promo_code_NOPROMO'] = 1
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'AZ2022':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 1
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'BUYMORE':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 1
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'WEEKENDSERU':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 1
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'XX2022':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 1
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'LIBURDONG':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 1
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'WEEKENDMANTAP':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 1
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 0
elif promo_code == 'SC2022':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 1
    df['promo_code_STARTUP'] = 0
elif promo_code == 'STARTUP':
    df['promo_code_NOPROMO'] = 0
    df['promo_code_AZ2022'] = 0
    df['promo_code_BUYMORE'] = 0
    df['promo_code_WEEKENDSERU'] = 0
    df['promo_code_XX2022'] = 0
    df['promo_code_LIBURDONG'] = 0
    df['promo_code_WEEKENDMANTAP'] = 0
    df['promo_code_SC2022'] = 0
    df['promo_code_STARTUP'] = 1

if payment_method == 'Credit Card':
    df['payment_method_Credit Card'] = 1
    df['payment_method_Gopay'] = 0
    df['payment_method_OVO'] = 0
    df['payment_method_Debit Card'] = 0
    df['payment_method_LinkAja'] = 0
elif payment_method == 'Gopay':
    df['payment_method_Credit Card'] = 0
    df['payment_method_Gopay'] = 1
    df['payment_method_OVO'] = 0
    df['payment_method_Debit Card'] = 0
    df['payment_method_LinkAja'] = 0
elif payment_method == 'OVO':
    df['payment_method_Credit Card'] = 0
    df['payment_method_Gopay'] = 0
    df['payment_method_OVO'] = 1
    df['payment_method_Debit Card'] = 0
    df['payment_method_LinkAja'] = 0
elif payment_method == 'Debit Card':
    df['payment_method_Credit Card'] = 0
    df['payment_method_Gopay'] = 0
    df['payment_method_OVO'] = 0
    df['payment_method_Debit Card'] = 1
    df['payment_method_LinkAja'] = 0
elif payment_method == 'LinkAja':
    df['payment_method_Credit Card'] = 0
    df['payment_method_Gopay'] = 0
    df['payment_method_OVO'] = 0
    df['payment_method_Debit Card'] = 0
    df['payment_method_LinkAja'] = 1

# drop promo_code and payment_method
df = df.drop(['promo_code', 'payment_method'], axis=1)
st.write(df)
# Scaling
scaler = MinMaxScaler()
data_scaled = scaler.fit(df)
data_scaled = scaler.transform(df)

# Button
predict = st.button('Predict')
# Prediction
prediction = model.predict(data_scaled)
#st.write(prediction)
if predict:
    if prediction == 1:
        st.write('Customer Not Churn')
    else:
        st.write('Customer Churn')