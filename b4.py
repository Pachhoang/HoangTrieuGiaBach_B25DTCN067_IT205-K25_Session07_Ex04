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
            

        

