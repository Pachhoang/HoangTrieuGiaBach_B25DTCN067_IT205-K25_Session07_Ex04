quantity_input = int(input("Nhập số lượng phiếu đăng ký: "))
if quantity_input <=0:
    print("Số lượng phiếu đăng ký không hợp lệ")
    exit()
else:
    for i in range(quantity_input):
        print(f"\n=========THÔNG TIN PHIẾU ĐĂNG KÝ===========\n")
        raw_data=input("Họ tên học viên | Tên khóa học | Mã học viên | Email: ")
        parts = raw_data.split("|")
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này.")
            continue
        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_id = parts[2].strip().upper()
        email = parts[3].strip().lower()
        print(f"===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_id}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {student_id.upper()}_{course_name.upper()}")

        if "@" not in email or "." not in email:
            print("Email không hợp lệ. Vui lòng kiểm tra lại.")
            exit()
        if len(student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            exit()
            

        
# C1: Phân tích Input / Output
# - quantity_input nhận dữ liệu đầu vào từ bàn phím và được ép kiểu int.
# - raw_data là chuỗi chứa: Họ tên | Tên khóa học | Mã học viên | Email.
# - parts là list sau khi tách chuỗi bằng split("|").
# - Output là phiếu đăng ký đã chuẩn hóa hoặc thông báo lỗi tương ứng.


# C2: Đề xuất giải pháp
# - Dùng int(input()) để nhập số lượng phiếu đăng ký.
# - Dùng if quantity_input <= 0 để kiểm tra dữ liệu không hợp lệ.
# - Dùng vòng lặp for để xử lý nhiều phiếu đăng ký.
# - Dùng split("|") để tách dữ liệu thành 4 phần.
# - Dùng len(parts) != 4 để kiểm tra dữ liệu thiếu hoặc sai format.
# - Dùng strip() để xóa khoảng trắng dư thừa.
# - Dùng title() chuẩn hóa tên học viên và tên khóa học.
# - Dùng upper() chuẩn hóa mã học viên.
# - Dùng lower() chuẩn hóa email.
# - Dùng if "@" not in email hoặc "." not in email để kiểm tra email.
# - Dùng len(student_id) < 5 để kiểm tra mã học viên hợp lệ.
# - Dùng f-string để hiển thị phiếu đăng ký và mã xác nhận.


# C3: Thiết kế thuật toán / Mô tả luồng chương trình
# B1: Nhập số lượng phiếu đăng ký.
# B2: Nếu số lượng <= 0:
#       - In thông báo lỗi
#       - Dừng chương trình bằng exit()
# B3: Chạy vòng lặp theo số lượng phiếu.
# B4: Nhập chuỗi raw_data từ bàn phím.
# B5: Tách chuỗi bằng split("|").
# B6: Nếu số phần tử khác 4:
#       - Báo lỗi
#       - continue để bỏ qua phiếu hiện tại
# B7: Chuẩn hóa dữ liệu bằng strip(), title(), upper(), lower().
# B8: In phiếu đăng ký đã chuẩn hóa.
# B9: Tạo mã xác nhận bằng student_id + course_name.
# B10: Kiểm tra email hợp lệ.
# B11: Kiểm tra độ dài mã học viên.
# B12: Kết thúc khi xử lý hết tất cả phiếu đăng ký.
