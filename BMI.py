import streamlit as st
st.write('我們的組名是猛祺')
w = st.number_input('請輸入體重(KG)？')
h = st.number_input('請輸入身高(M)？')
confirm_input=st.button('輸入確認')

if confirm_input:
      bmi = w/(h*h)
      st.write('BMI為', bmi)
      if (bmi < 18):
           st.write('體重過輕')
      elif (bmi < 24):
           st.write('體重正常')
      elif (bmi < 27):
           st.write('體重過重')
      else:
           st.write('體重肥胖')
