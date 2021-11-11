import streamlit as st

move_top='<p style="color:Red; font-size: 20px;"><a href="#stock-market-prediction-using-transfer-learning-exploratory-data-analysis">Move to top<a></p>'
st.sidebar.markdown(move_top,unsafe_allow_html=True)

sidebar_used_modules = '<p style="color:Red; font-size: 20px;"><b>Used Modules<b></p>'
st.sidebar.markdown(sidebar_used_modules,unsafe_allow_html=True)




st.sidebar.markdown('1. talib as tb\n  2. pandas as pd\n'+
    '3. yfinance as yf\n 4. numpy as np\n 5. streamlit as st\n 6. seaborn as sns\n'+
    '7. tensorflow as tf \n 8. keras_tuner as kt\n 9. matplotlib.pyplot as plt')

sidebar_other_imports = '<p style="color:Red; font-size: 20px;"><b>Other Imports<b></p>'
st.sidebar.markdown(sidebar_other_imports,unsafe_allow_html=True)

st.sidebar.markdown('from **sklearn.model_selection**- train_test_split\n\n   '+
'from **sklearn.ensemble**- AdaBoostRegressor\n\n'+
'from **keras.wrappers.scikit_learn**- KerasRegressor\n\n'+
'from **sklearn.metrics**- mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error\n\n'+
'from **sklearn.preprocessing**- MinMaxScaler\n\n'+
'from **sklearn.model_selection**- GridSearchCV\n\n'+
'from **math**- sqrt\n\n'+
'from **tensorflow.keras.models**- Sequential\n\n'+
'from **tensorflow.keras.layers**- GRU,LSTM,Dense,Bidirectional')



st.title('Stock market prediction using Transfer Learning- Exploratory Data Analysis')

st.subheader("Index")

data_collection = '<p style="color:Red; font-size: 20px;"><a href="#data-collection">Data Collection<a></p>'
eda_source = '<p style="color:Red; font-size: 20px;"><a href="#exploratory-data-analysis-on-source-stock-infosys">Exploratory Data Analysis of Source Stock<a></p>'
eda_target = '<p style="color:Red; font-size: 20px;"><a href="#exploratory-data-analysis-on-target-stock-new-gen-software-technologies-limited">Exploratory Data Analysis of Target Stock<a></p>'
prediction = '<p style="color:Red; font-size: 20px;"><a href="#prediction-of-stock-market">Prediction<a></p>'
home = '<p style="color:Red; font-size: 20px;"><a href="#stock-market-prediction-using-transfer-learning-exploratory-data-analysis">Home<a></p>'
downloads = '<p style="color:Red; font-size: 20px;"><a href="#downloads">Downloads<a></p>'
st.markdown(data_collection,unsafe_allow_html=True)
st.markdown(eda_source,unsafe_allow_html=True)
st.markdown(eda_target,unsafe_allow_html=True)
st.markdown(prediction,unsafe_allow_html=True)
st.markdown(downloads,unsafe_allow_html=True)
    
st.header("Data Collection")
st.markdown("The data is downloaded from [Yahoo Finance](https://finance.yahoo.com/) using the yfinance API.")
st.markdown("The following stocks are used along the implementation.")
st.write("**Infosys** stock- Source stock 1- INFY.NS")
st.write("**TCS** stock- Source stock 1- TCS.NS")
st.write("**New gen Software Technologies Limited** stock- Target stock- NEWGEN.NS")

note1 = '<p style="color:Red; font-size: 15px;"><b>Note:<b></p>'
st.markdown(note1,unsafe_allow_html=True)
st.write("-As the data formats are the same, the Exploratory Data Analysis is carried out on only Source Stock 1- Infosys.")
st.write("-The final features are selected from both the source datasets and used in Prediction Model.")
st.write("-Target Dataset is the same in EDA and prediction model i.e. NEWGEN.NS")
st.write("-Hence, the Infosys stock is referred to as Source stock in the EDA.")

#Options for Box plots of source and target stocks------------------
st.header("SMA of Source and Target Stocks ")
option=st.selectbox("Select to see SMA plot",['Choose Option','Simple Moving Average of Source Stock',
    'Simple Moving Average of Target Stock'])

if option=="Simple Moving Average of Source Stock":
    st.subheader("Box plot of SMA_Source_Stock")
    st.image("sma_source_stock.png")
    if st.checkbox("View Code"):
        st.code("sma_source_stock = tb.SMA(source_stock_data['Adj Close'], timeperiod=30)",'python')
elif option=="Simple Moving Average of Target Stock":
    st.subheader("Box plot of SMA_Target_Stock")
    st.image('sma_target_stock.png')
    if st.checkbox("View Code"):
        st.code("sma_target_stock = tb.SMA(target_stock_data['Adj Close'], timeperiod=30)",'python')
	

#Plots of EDA of Source------------------
st.header("Exploratory Data Analysis on Source Stock-- Infosys")

st.subheader("Analysis of Source Features")
op_eda_source=st.selectbox("Different plots of source features",['Choose a plot','Time Vs EMA Values','Stochastic K Vs Time',
    'Stochastic D Vs Time','Relative Strength Indicator Vs Time','Common channel Index vs Time',
    'Time Vs Averaged Closing Price',"Momentum Vs Time",'Price Vs Time','Correlation'])

if op_eda_source=='Time Vs EMA Values':
    st.subheader("Plot of Time Vs EDA Values")
    st.image('time_ema_source.png')

elif op_eda_source=='Stochastic K Vs Time':
    st.subheader("Plot Stochastic K Vs Time")
    st.image('stochastic_k_source.png')

elif op_eda_source=='Stochastic D Vs Time':
    st.subheader('Plot of Stochastic D Vs Time')
    st.image('stochastic_d_source.png')

elif op_eda_source=="Relative Strength Indicator Vs Time":
    st.subheader('Plot Relative Strength Indicator Vs Time')
    st.image('rsi_source.png')

elif op_eda_source=='Common channel Index vs Time':
    st.subheader('Plot of Common channel Index vs Time')
    st.image('cci_source.png')

elif op_eda_source=='Time Vs Averaged Closing Price':
    st.subheader('Plot of Time Vs Averaged Closing Price')
    st.image('average_source.png')

elif op_eda_source=='Momentum Vs Time':
    st.subheader("Plot of Momentum Vs Time")
    st.image('momentum_source.png')

elif op_eda_source=="Price Vs Time":
    st.subheader("Plot of Price Vs Time")
    st.image('price_time_source.png')

elif op_eda_source=="Correlation":
    st.subheader("Plot for Correlation")
    st.image('correlation_source.png')


#Plots of EDA of Source------------------
st.header("Exploratory Data Analysis on Target Stock-- New gen Software Technologies Limited")

st.subheader("Analysis of Target Features")
op_eda_target=st.selectbox("Different plots of target features",['Choose a plot','Time Vs EMA Values','Stochastic K Vs Time',
    'Stochastic D Vs Time','Relative Strength Indicator Vs Time','Common channel Index vs Time',
    'Time Vs Averaged Closing Price',"Momentum Vs Time",'Price Vs Time','Correlation'])

if op_eda_target=='Time Vs EMA Values':
    st.subheader("Plot of Time Vs EDA Values")
    st.image('time_ema_target.png')

elif op_eda_target=='Stochastic K Vs Time':
    st.subheader("Plot Stochastic K Vs Time")
    st.image('stochastic_k_target.png')

elif op_eda_target=='Stochastic D Vs Time':
    st.subheader('Plot of Stochastic D Vs Time')
    st.image('stochastic_d_target.png')

elif op_eda_target=="Relative Strength Indicator Vs Time":
    st.subheader('Plot Relative Strength Indicator Vs Time')
    st.image('rsi_target.png')

elif op_eda_target=='Common channel Index vs Time':
    st.subheader('Plot of Common channel Index vs Time')
    st.image('cci_target.png')

elif op_eda_target=='Time Vs Averaged Closing Price':
    st.subheader('Plot of Time Vs Averaged Closing Price')
    st.image('average_target.png')

elif op_eda_target=='Momentum Vs Time':
    st.subheader("Plot of Momentum Vs Time")
    st.image('momentum_target.png')

elif op_eda_target=="Price Vs Time":
    st.subheader("Plot of Price Vs Time")
    st.image('price_time_target.png')

elif op_eda_target=="Correlation":
    st.subheader("Plot for Correlation")
    st.image('correlation_target.png')


#Training and Prediction of Data
st.header("Prediction of Stock Market")

st.subheader("Prediction of first source stock- Infosys")
st.image('prediction_source1.png')

st.subheader("Prediction of second source stock- TCS")
st.image('prediction_source2.png')

st.subheader("Prediction of target stock- New gen Software Technologies Limited")
st.text('Case: Before Hyperparameter Tuning')
st.image('prediction_transfer_learning.png')

st.subheader("Prediction of target stock- New gen Software Technologies Limited")
st.text('Case: After Hyperparameter Tuning')

st.subheader("Downloads")
download=st.selectbox("Select the file to be downloaded",['Choose the dataset','Source Features Dataset 1- Infosys','Source Features Dataset 2- TCS',
    'Target Features Dataset- New gen Software Technologies Limited','Exploratory Data Analysis ipynb file','Final Model ipynb file'])

if download=="Source Features Dataset 1- Infosys":
    st.download_button(label="Download Source Feature Dataset 1",data="https://github.com/sudo-tharun/pda_project/blob/5469d47dcceb12d1524a276fa3bbdedc6f6efe82/final-data/features_source_infy.csv",file_name="features_source.csv")

elif download=="Source Features Dataset 2- TCS":
    st.download_button(label="Download Source Feature Dataset 2",data="https://github.com/sudo-tharun/pda_project/blob/5469d47dcceb12d1524a276fa3bbdedc6f6efe82/final-data/features_source_tcs.csv",file_name="features_source2.csv")

elif download=="Target Features Dataset- New gen Software Technologies Limited":
    st.download_button(label="Download Target Feature Dataset",data="https://github.com/sudo-tharun/pda_project/blob/5469d47dcceb12d1524a276fa3bbdedc6f6efe82/final-data/target_stocks.csv",file_name="target_stocks.csv")

elif download=="Exploratory Data Analysis ipynb file":
    st.download_button(label="Download Exploratory Data Analysis file",data='https://github.com/sudo-tharun/pda_project/blob/f98c6502b46c1e4bdc33c523048d15e03c91cad1/multi_source_transfer_learning_using_XAI_for_stock_prediction.ipynb',file_name="final_model.ipynb")
elif  download=="Final Model ipynb file":
    st.download_button(label="Download Final Model ipynb file",data='https://github.com/sudo-tharun/pda_project/blob/f98c6502b46c1e4bdc33c523048d15e03c91cad1/exploratory-data-analysis.ipynb',file_name="eda.ipynb")
