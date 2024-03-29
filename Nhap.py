import streamlit as st
import pandas as pd
import pickle

# Setting up page config
st.set_page_config(
    page_title="Đề án Khoa học Dữ liệu",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Read data
data = pd.read_csv("RFM.csv", encoding='latin-1')

# GUI
st.title("Đồ án khoa học dữ liệu")
st.write("## Segmentation")

# GUI
menu = ["Mô tả đề án", "Phân khúc khách hàng"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Mô tả đề án':    
    st.subheader("Mô tả đề án")
    st.write("""
    **Mục tiêu đề án** : Phân nhóm khách hàng dựa vào RFM (Recency, Frequency, Monetary) xử lý trên bộ dữ liệu khách hàng của một cửa hàng bán lẻ online có trụ sở tại Anh chứa các giao dịch từ 12/01/2010 đến 12/09/2011.
    """)  
elif choice == 'Phân khúc khách hàng':
    model = pickle.load(open('model.pkl','rb'))
    
    # Sidebar for user interaction
    choice = st.sidebar.selectbox("Chọn cách nhập", ("1 - ID khách hàng", "2 - R F M"))

    if choice == "1 - ID khách hàng":
        ######  1. Chọn sản phẩm  theo ID Khách hàng  ############
        #Tạo điều khiển để cửa hàng chọn thông tin
        unique_products = data['sub_category'].unique().copy()
        st.write("Phần này đang được cập nhật...")
        
    elif choice == "2 - R F M":
        #################################################
        ######  2. Chọn sản phẩm theo R F M  ###########
        #################################################
        st.write("Phần này đang được cập nhật...")