import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

# st.write('Interactiv Widgets')

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

# text = st.text_input('あなたの趣味を教えてください。')
# cond = st.slider('あなたの調子を教えてください。', 0, 10, 2)
# 'あなたの趣味は', text, 'です。'
# '調子：', cond

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'

# cond = st.slider('あなたの調子を教えてください。', 0, 10, 2)
# '調子：', cond



# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('./zou.png')
#     st.image(img, caption='momokanozou', use_column_width=True)



# df = pd.DataFrame({
#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40],
# })

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.write(df)
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

