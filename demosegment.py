import streamlit as st
import pandas as pd

# Setting up page config
st.set_page_config(
    page_title="Đề án Khoa học Dữ liệu",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded",
)
# 1. Read data
data = pd.read_csv("RFM.csv", encoding='latin-1')
# Setting up styles
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#FFFFFF, #F6F6F6);
    }
    .reportview-container .main .block-container {
        color: #333333;
        background-color: #F6F6F6; /* Thay đổi màu nền */
    }
    .btn-outline-secondary {
        color: #333333;
        background-color: #FFFFFF;
        border-color: #CCCCCC;
    }
    .css-17eq0hr {
        font-family: 'Arial';
        font-size: 16px;
    }
    .css-1q0k9al {
        font-family: 'Arial';
    }
    .header-top a {
        color: #333333;
    }
    .header-bot .main-menu > li > a {
        color: #FFFFFF;
    }
    .header-bot .main-menu > li > ul.children-menu > li > a {
        color: #FFFFFF;
    }
    .header-bot .main-menu > li > ul.children-menu > li > ul.children-menu > li > a {
        color: #FFFFFF;
    }
    .header-bot .main-menu > li > ul.children-menu > li > ul.children-menu > li > ul.children-menu > li > a {
        color: #FFFFFF;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Using menu
st.title("Đề án khoa học dữ liệu")
menu = [
    "Home",
    "Capstone Project",
    "Sử dụng các điều khiển",
    "Project 1",
    "Project 2",
    "Project 3",
]
choice = st.sidebar.selectbox("Danh mục", menu)
if choice == "Home":
    st.subheader("[Trang chủ](https://csc.edu.vn)")
elif choice == "Capstone Project":
    st.subheader(
        "[Đồ án TN Data Science]"
    )
    st.write(
        """
    - Topic 1: Sentiment Analysis
    - Topic 2: Recommendation System
    - Topic 3: RFM & Clustering
    - ..."""
    )
elif choice == "Sử dụng các điều khiển":
    pass
elif choice == "Gợi ý điều khiển project 3":
    st.write("##### 1. Some data")
    # Chọn nhập mã khách hàng hoặc nhập thông tin khách hàng vào dataframe
    st.write("##### 1. Chọn cách nhập thông tin khách hàng")
    type = st.radio(
        "Chọn cách nhập thông tin khách hàng",
        options=["Nhập mã khách hàng", "Nhập thông tin khách hàng vào dataframe"],
    )
    if type == "Nhập mã khách hàng":
        # Nếu người dùng chọn nhập mã khách hàng
        st.subheader("Nhập mã khách hàng")
        # Tạo điều khiển để người dùng nhập mã khách hàng
        customer_id = st.text_input("Nhập mã khách hàng")
        # Nếu người dùng nhập mã khách hàng, thực hiện các xử lý tiếp theo
        # Có KH này trong dữ liệu không (nếu có thì tiếp tục xử lý, nếu không thì thông báo không có KH này trong dữ liệu)
        # Đề xuất khách hàng thuộc cụm nào
        # In kết quả ra màn hình
        st.write("Mã khách hàng:", customer_id)
        st.write("Phân cụm khách hàng...")
    else:
        # Nếu người dùng chọn nhập thông tin khách hàng vào dataframe có 3 cột là Recency, Frequency, Monetary
        st.write("##### 2. Thông tin khách hàng")
        # Tạo điều khiển table để người dùng nhập thông tin khách hàng trực tiếp trên table
        st.write("Nhập thông tin khách hàng")
        # Tạo dataframe để người dùng nhập thông tin khách hàng
        df_customer = pd.DataFrame(columns=["Recency", "Frequency", "Monetary"])
        for i in range(5):
            st.write(f"Khách hàng {i+1}")
            # # Tạo các slider để nhập giá trị cho cột Recency, Frequency, Monetary
            # recency = st.slider("Recency", 1, 365, 100, key=f"recency_{i}")
            # frequency = st.slider("Frequency", 1, 50, 5, key=f"frequency_{i}")
            # monetary = st.slider("Monetary", 1, 1000, 100, key=f"monetary_{i}")
            
            
            # Nhập giá trị cho Recency, Frequency và Monetary
            recency_min, recency_max = 0, 1000748
            frequency_min, frequency_max = 1, 58920976
            monetary_min, monetary_max = 0.0, 815129756.24

            # Recency input
            recency = st.number_input("Recency", min_value=recency_min, max_value=recency_max, value=(recency_min + recency_max) // 2)

            # Frequency input
            frequency = st.number_input("Frequency", min_value=frequency_min, max_value=frequency_max, value=(frequency_min + frequency_max) // 2)

            # Monetary input
            monetary = st.number_input("Monetary", min_value=monetary_min, max_value=monetary_max, value=(monetary_min + monetary_max) / 2, format="%.2f")

            # Thêm thông tin khách hàng vừa nhập vào dataframe
            df_customer = df_customer.append(
                {
                    "Recency": recency,
                    "Frequency": frequency,
                    "Monetary": monetary,
                },
                ignore_index=True,
            )
        # Thực hiện phân cụm khách hàng dựa trên giá trị của 3 cột này
        # In kết quả ra màn hình
        st.write("##### 3. Phân cụm khách hàng")
        st.write(df_customer)
        st.write("Phân cụm khách hàng...")
        # Từ kết quả phân cụm khách hàng, người dùng có thể xem thông tin chi tiết của từng cụm khách hàng, xem biểu đồ, thống kê...
        # hoặc thực hiện các xử lý khác
