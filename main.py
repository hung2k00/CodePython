'''
    Viet chuong trinh tim tat ca cac so chia het cho 7 nhung khong phai laf boi cua 5 trong doan tu lon hon bang 200 va
    nho hon bang 3200 cac so thu in thanh chuoi tren mot dong cac nhau bang dau phay
'''
import math
if __name__ == '__main__':
    j=[] #xay dung mot danh sach rong de chua ket qua
    for i in range(200,3200): #duyet cac phan tu trong doan tu 200 den 3200
        if (i%7 == 0) and (i%5!=0):#xet dieu kien theo nhu de bai yeu cau
            j.append(str(i))
    print(','.join(j))
    x = int( input( "Nhập số cần tính giai thừa:" ) )


    def fact(x):    #xay dung ham chua phan tu x
        if x == 0:
            return 1
        return x * fact( x - 1 )

    print( fact( x ) )
