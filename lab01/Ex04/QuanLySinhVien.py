from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if (self.soLuongSV() > 0):
            maxID = self.listSinhVien[0]._id
            for sv  in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID = maxID + 1
        return maxID
    
    def soLuongSV(self):
        return self.listSinhVien.__len__()
    
    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập diểm của sinh viên: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSV(self, ID):
        sv:SinhVien = self.findbyID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = int(input("Nhập chuyên ngành của sinh viên: "))
            diemTB = float(input("Nhập diểm của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại. ".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name , reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB , reverse=False)

    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSV() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSV() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted - False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted =True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocluc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<30} {:<8} {:<30}{:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Điểm TB", "Học lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<30} {:<8} {:<30}{:<8} {:<8}"
                    .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien