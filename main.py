import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Itetation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'

left_column, right_culumn = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

