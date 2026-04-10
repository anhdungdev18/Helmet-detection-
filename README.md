# Phát Hiện Mũ Bảo Hộ Bằng YOLOv8

Dự án này được xây dựng để phát hiện mũ bảo hộ trong hình ảnh và video bằng mô hình YOLOv8. Chương trình nhận đường dẫn tới thư mục đầu vào, thực hiện nhận diện trên toàn bộ tệp hình ảnh và video, sau đó lưu kết quả đã được vẽ bounding box cùng thông tin phát hiện vào thư mục đầu ra.

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/allresults.jpeg" width="1000" height="700">

## Mục Tiêu Dự Án

Mục tiêu của dự án là phát hiện mũ bảo hộ trong hình ảnh và video bằng thuật toán phát hiện đối tượng YOLOv8. Quy trình chính gồm việc nạp mô hình đã huấn luyện, thay đổi kích thước khung hình đầu vào, chạy suy luận, trực quan hóa kết quả và lưu ảnh đã gán nhãn cùng tệp CSV chứa thông tin phát hiện.

```bash
python main.py <đường-dẫn-thư-mục-chứa-hình-ảnh>
```

## Công Cụ Sử Dụng

1. Python
2. OpenCV - xử lý hình ảnh và video
3. YOLOv8 - mô hình phát hiện đối tượng
4. Supervision - trực quan hóa kết quả nhận diện và annotation
5. Ultralytics - thư viện để sử dụng mô hình YOLO

## Quy Trình Hoạt Động

1. Nạp mô hình YOLOv8 đã được huấn luyện để phát hiện mũ bảo hộ.
2. Đọc hình ảnh hoặc video đầu vào và thay đổi kích thước khung hình theo yêu cầu.
3. Đưa dữ liệu đầu vào qua mô hình để lấy các đối tượng được phát hiện và tọa độ của chúng.
4. Sử dụng thư viện Supervision để vẽ kết quả phát hiện lên hình ảnh.
5. Lưu các ảnh đã được gán nhãn vào thư mục riêng.
6. Trích xuất nhãn của các đối tượng từ kết quả YOLOv8.
7. Đánh giá kết quả và tạo ma trận nhầm lẫn.
8. Tính toán các chỉ số như độ chính xác và loss, sau đó vẽ biểu đồ.
9. Lưu biểu đồ và tệp CSV chứa thông tin phát hiện vào thư mục kết quả.

## Chỉ Số Đánh Giá

![Accuracy](https://github.com/meryemsakin/helmet-detection/blob/main/graph.png)

## Ma Trận Nhầm Lẫn

Ma trận nhầm lẫn giúp đánh giá tổng quan hiệu năng của mô hình. Hình bên dưới là ma trận nhầm lẫn của mô hình phát hiện mũ bảo hộ:

![cm](https://github.com/meryemsakin/helmet-detection/blob/main/cmatrix.png)

## Hạn Chế Và Hướng Cải Thiện

1. Mô hình có thể chưa chính xác trong mọi tình huống và vẫn có khả năng xuất hiện false positive hoặc false negative. Có thể cải thiện bằng cách fine-tune trên tập dữ liệu lớn hơn và đa dạng hơn.
2. Phiên bản hiện tại chỉ phát hiện mũ bảo hộ, nhưng có thể mở rộng để nhận diện thêm kính bảo hộ, găng tay hoặc các trang bị an toàn khác.
3. Chương trình hiện tại chỉ hoạt động với hình ảnh và video, nhưng có thể phát triển thêm để hỗ trợ luồng camera trực tiếp.

## Kết Luận

Dự án cung cấp nền tảng cơ bản để phát hiện mũ bảo hộ trong hình ảnh và video bằng YOLO. Quá trình xử lý bao gồm nạp mô hình, đọc dữ liệu đầu vào, suy luận, trực quan hóa kết quả, kiểm tra xem người lao động có đội mũ hay không và lưu thông tin vào tệp CSV. Tuy vẫn còn khả năng cải thiện, dự án đã đáp ứng tốt mục tiêu nhận diện trang bị an toàn cơ bản.

## Kết Quả Mẫu

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/hard_hat_workers42.png" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_6.jpg" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_7.jpg" width="500" height="500">
