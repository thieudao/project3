import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using menu
st.title("Trung Tâm Tin Học")
menu = ["Home", "Capstone Project", "Sử dụng các điều khiển", "Gợi ý điều khiển project 1", "Gợi ý điều khiển project 2", "Gợi ý điều khiển project 3"]
choice = st.sidebar.selectbox('Danh mục', menu)
if choice == 'Home':    
    st.subheader("[Trang chủ](https://csc.edu.vn)")  
elif choice == 'Capstone Project':    
    st.subheader("[Đồ án TN Data Science](https://csc.edu.vn/data-science-machine-learning/Do-An-Tot-Nghiep-Data-Science---Machine-Learning_229)")
    st.write("""### Có 3 chủ đề trong khóa học:
    - Topic 1: Sentiment Analysis
    - Topic 2: Recommendation System
    - Topic 3: RFM & Clustering
    - ...""")
elif choice == 'Sử dụng các điều khiển':
elif choice=='Gợi ý điều khiển project 3':
    st.write("##### 1. Some data")
    # Chọn nhập mã khách hàng hoặc nhập thông tin khách hàng vào dataframe
    st.write("##### 1. Chọn cách nhập thông tin khách hàng")
    type = st.radio("Chọn cách nhập thông tin khách hàng", options=["Nhập mã khách hàng", 
                                                                    "Nhập thông tin khách hàng vào dataframe"])
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
            # Tạo các slider để nhập giá trị cho cột Recency, Frequency, Monetary
            recency = st.slider("Recency", 1, 365, 100, key=f"recency_{i}")
            frequency = st.slider("Frequency", 1, 50, 5, key=f"frequency_{i}")
            monetary = st.slider("Monetary", 1, 1000, 100, key=f"monetary_{i}")
            # Cũng có thể thay bằng các điều khiển khác như number_input...
            # Thêm thông tin khách hàng vừa nhập vào dataframe
            df_customer = df_customer.append({"Recency": recency, "Frequency": frequency, "Monetary": monetary}, ignore_index=True)            
        # Thực hiện phân cụm khách hàng dựa trên giá trị của 3 cột này
        # In kết quả ra màn hình
        st.write("##### 3. Phân cụm khách hàng")
        st.write(df_customer)
        st.write("Phân cụm khách hàng...")
        # Từ kết quả phân cụm khách hàng, người dùng có thể xem thông tin chi tiết của từng cụm khách hàng, xem biểu đồ, thống kê...
        # hoặc thực hiện các xử lý khác
# Done
    
    
    
        

        
        

    



