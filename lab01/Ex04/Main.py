from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):
    print("**CHUONG TRINH QUAN LY SINH VIEN**")
    print("**************MENU**************")
    print("** 1. Thêm sinh viên.")
    print("** 2. Cập nhật thông tin sinh viên bởi ID.")
    print("** 3. Xóa sinh viên bởi ID.")
    print("** 4. Tìm kiếm sinh viên theo tên.")
    print("** 5. Sắp xếp inh viên theo DTB.")
    print("** 6. Sắp xếp inh viên theo tên chuyên ngành.")
    print("** 7. Hiển thị danh sách sinh viên.")
    print("** 0. Thoát.")
    print("*******************************")

    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSV()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSV() > 0):
            print("\n2. Cap nhat thong tin sinh vien.")
            print("\nNhap ID:")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 3):
        if (qlsv.soLuongS() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID:")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co ID = ", ID, ", da bi xoa.")
            else:
                print("\nSinh vien co ID = ", ID, ", khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 4):
        if (qlsv.soLuongSV() > 0):
            print("\n4. Tìm kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 5):
        if (qlsv.soLuongSV() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 6):
        if (qlsv.soLuongSV() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 7):
        if (qlsv.soLuongSV() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")