# Phat Hien Mu Bao Ho Bang YOLOv8

Du an nay duoc xay dung de phat hien mu bao ho trong hinh anh va video bang mo hinh YOLOv8. Chuong trinh nhan duong dan toi thu muc dau vao, thuc hien nhan dien tren toan bo tep hinh anh va video, sau do luu ket qua da duoc ve bounding box cung thong tin phat hien vao thu muc dau ra.

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/allresults.jpeg" width="1000" height="700">

## Muc Tieu Du An

Muc tieu cua du an la phat hien mu bao ho trong hinh anh va video bang thuat toan phat hien doi tuong YOLOv8. Quy trinh chinh gom viec nap mo hinh da huan luyen, thay doi kich thuoc khung hinh dau vao, chay suy luan, truc quan hoa ket qua va luu anh da gan nhan cung tep CSV chua thong tin phat hien.

```bash
python main.py <duong-dan-thu-muc-chua-hinh-anh>
```

## Cong Cu Su Dung

1. Python
2. OpenCV - xu ly hinh anh va video
3. YOLOv8 - mo hinh phat hien doi tuong
4. Supervision - truc quan hoa ket qua nhan dien va annotation
5. Ultralytics - thu vien de su dung mo hinh YOLO

## Quy Trinh Hoat Dong

1. Nap mo hinh YOLOv8 da duoc huan luyen de phat hien mu bao ho.
2. Doc hinh anh hoac video dau vao va thay doi kich thuoc khung hinh theo yeu cau.
3. Dua du lieu dau vao qua mo hinh de lay cac doi tuong duoc phat hien va toa do cua chung.
4. Su dung thu vien Supervision de ve ket qua phat hien len hinh anh.
5. Luu cac anh da duoc gan nhan vao thu muc rieng.
6. Trich xuat nhan cua cac doi tuong tu ket qua YOLOv8.
7. Danh gia ket qua va tao ma tran nham lan.
8. Tinh toan cac chi so nhu do chinh xac va loss, sau do ve bieu do.
9. Luu bieu do va tep CSV chua thong tin phat hien vao thu muc ket qua.

## Chi So Danh Gia

![Accuracy](https://github.com/meryemsakin/helmet-detection/blob/main/graph.png)

## Ma Tran Nham Lan

Ma tran nham lan giup danh gia tong quan hieu nang cua mo hinh. Hinh ben duoi la ma tran nham lan cua mo hinh phat hien mu bao ho:

![cm](https://github.com/meryemsakin/helmet-detection/blob/main/cmatrix.png)

## Han Che Va Huong Cai Thien

1. Mo hinh co the chua chinh xac trong moi tinh huong va van co kha nang xuat hien false positive hoac false negative. Co the cai thien bang cach fine-tune tren tap du lieu lon hon va da dang hon.
2. Phien ban hien tai chi phat hien mu bao ho, nhung co the mo rong de nhan dien them kinh bao ho, gang tay hoac cac trang bi an toan khac.
3. Chuong trinh hien tai chi hoat dong voi hinh anh va video, nhung co the phat trien them de ho tro luong camera truc tiep.

## Ket Luan

Du an cung cap nen tang co ban de phat hien mu bao ho trong hinh anh va video bang YOLO. Qua trinh xu ly bao gom nap mo hinh, doc du lieu dau vao, suy luan, truc quan hoa ket qua, kiem tra xem nguoi lao dong co doi mu hay khong va luu thong tin vao tep CSV. Tuy van con kha nang cai thien, du an da dap ung tot muc tieu nhan dien trang bi an toan co ban.

## Ket Qua Mau

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/hard_hat_workers42.png" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_6.jpg" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_7.jpg" width="500" height="500">
