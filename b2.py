print(" --- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ")
weight = float(input("Nhậpp cân nặng bệnh nhân: "))

print ("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân: ", name_patient)
print("Cân nặng đã nhập: ", weight)

print("CẢNH BÁO - Kiểu dữ liệu đang lưu là: ", type(weight))

# Giải thích đặc điểm của hàm input() trong Python
#       Hàm input luôn trả về chuỗi giá trị 
#           nên khi muốn lưu giá trị kiểu số thì cần phải ép kiểu dữ liệu
#           luồng thực thi của trương trình:
#                    + Nhập thông tin bệnh nhân
#                       + in ra thông tin bệnh nhân