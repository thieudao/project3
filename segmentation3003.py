import streamlit as st
import pandas as pd
import csv

# Thiết lập tiêu đề trang và các cài đặt khác
st.set_page_config(
    page_title="Đồ án Khoa học Dữ liệu",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Thiết lập các kiểu dáng cho giao diện
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

# Tiêu đề chính của ứng dụng
st.title("Đồ án khoa học dữ liệu")

# Danh sách các mục menu
menu = [
    "Giới thiệu đồ án",
    "Đồ án phân tích tình cảm",
    "Đồ án đề xuất sản phẩm",
    "Đồ án Phân khúc thị trường",
]

# Lựa chọn của người dùng
choice = st.sidebar.selectbox("Danh mục", menu)

# Hiển thị nội dung tương ứng với lựa chọn của người dùng
if choice == "Giới thiệu đồ án":
    st.write(
        """ Đồ án này gồm 3 phần: (1) Phân tích tình cảm; (2) Đề xuất sản phẩm và (3) Phân khúc khách hàng 
        **(Minh họa thêm)**
        """
    )

elif choice == "Đồ án phân tích tình cảm":
    st.write("<span style='color:green; font-size:24px;'>Bạn Vi sẽ trình bày</span>", unsafe_allow_html=True)

elif choice == "Đồ án đề xuất sản phẩm":
    st.markdown('<a style="color:purple; font-size:24px;">Bạn Phúc sẽ trình bày tại <a href="https://recommendersystem-htphuc.streamlit.app">link này</a></a>', unsafe_allow_html=True)

elif choice == "Đồ án Phân khúc thị trường":
    st.write("##### <span style='color:blue'>Đồ án này sẽ giúp xác định nhóm khách hàng để có chiến lược chăm sóc khách hàng phù hợp nhằm tăng doanh thu</span>", unsafe_allow_html=True)

    
    # Hàm đọc file CSV
    def read_csv_file(file_path):
        try:
            data = pd.read_csv(file_path, encoding='latin-1')
            return data
        except FileNotFoundError:
            st.error(f"Không tìm thấy tệp {file_path}")

    # Hàm phân khúc khách hàng
    def segment_customer(rfm_score):
        if rfm_score >= 13:
            return "VIP"
        elif 11 <= rfm_score < 13:
            return "Thân thiết"
        elif 9 <= rfm_score < 11:
            return "Tiềm năng"
        elif 7 <= rfm_score < 9:
            return "Quan tâm"
        else:
            return "Bàng quan"

    # Đường dẫn tới tệp CSV
    file_path = "RFMnew.csv"

    # Đọc dữ liệu từ tệp CSV
    data = read_csv_file(file_path)

    # Thêm cột "Customer_Segment" vào DataFrame
    data['Customer_Segment'] = data['RFMscore'].apply(segment_customer)

    # Hiển thị DataFrame
    st.write(data)

    # Lựa chọn nhập thông tin từ người dùng
    input_option = st.radio(
        "Chọn cách nhập thông tin khách hàng:",
        ["Nhập mã khách hàng", "Nhập thông tin RFM"]
    )
    if input_option == "Nhập mã khách hàng":
        st.subheader("Nhập mã khách hàng")
        # Lấy mã khách hàng từ người dùng
        customer_id = st.text_input("Nhập mã khách hàng (CustomerID): ")

        # Kiểm tra xem mã khách hàng có tồn tại trong dữ liệu không
        if customer_id:
            try:
                customer_id = int(customer_id)
                if customer_id not in data['CustomerID'].values:
                    st.write(f"Mã khách hàng {customer_id} không tồn tại trong dữ liệu.")
                else:
                    # Lấy nhóm khách hàng cho mã khách hàng được cung cấp
                    customer_rfm_score = data[data['CustomerID'] == customer_id]['RFMscore'].values[0]
                    customer_segment = segment_customer(customer_rfm_score)
                    st.write(f"Mã khách hàng {customer_id} thuộc nhóm {customer_segment}.")
            except ValueError:
                st.write("Vui lòng nhập một số nguyên cho mã khách hàng.")
        
    # Phân 5 nhóm khách hàng (dựa vào tính thường xuyên và giá trị của giao dịch)
    # 1. Khách hàng VIP	13-15	Mua gần đây, thường xuyên, giá trị cao
    # 2. Khách hàng thân thiết	11-13	Mua gần đây, thường xuyên, giá trị trung bình
    # 3. Khách hàng tiềm năng	9-11	Mua cách đây vừa phải, thường xuyên, giá trị trung bình
    # 4. Khách hàng cần quan tâm 7-9	Mua cách đây lâu, không thường xuyên, giá trị trung bình
    # 5. Khách hàng bàng quan	5-7	Mua cách đây lâu, không thường xuyên
            # Hiển thị tất cả các cột khi in ra DataFrame
        pd.set_option('display.max_columns', None)
        # Mô tả RFMscore
        print(data['RFMscore'].describe().round(0))
        data['Customer_Segment'] = data['RFMscore'].apply(segment_customer)
    else:
        st.subheader("Nhập thông tin RFM")
        # Định nghĩa các giá trị tối thiểu và tối đa cho RFM
        recency_min, recency_max = 0, 1000748
        frequency_min, frequency_max = 1, 58920976
        monetary_min, monetary_max = 0.0, 815129756.24

        # Nhập giá trị Recency
        recency = st.number_input("Nhập giá trị Recency (Recency): ", min_value=recency_min, max_value=recency_max, value=(recency_min + recency_max) // 2)

        # Nhập giá trị Frequency
        frequency = st.number_input("Nhập giá trị Frequency (Frequency): ", min_value=frequency_min, max_value=frequency_max, value=(frequency_min + frequency_max) // 2)

        # Nhập giá trị Monetary
        monetary = st.number_input("Nhập giá trị Monetary (Monetary): ", min_value=monetary_min, max_value=monetary_max, value=(monetary_min + monetary_max) / 2, format="%.2f")

        # Xử lý các giá trị RFM để xác định nhóm khách hàng sử dụng mô hình
        # (Thay thế phần này bằng logic phân khúc RFM thực tế của bạn sử dụng mô hình)
        input_data = [[recency, frequency, monetary]]
        # customer_segment = model.predict(input_data)[0]

        # st.write(f"Khách hàng thuộc nhóm: {customer_segment}")
#Done`
