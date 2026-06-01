# Phát Hiện Mũ Bảo Hộ Bằng YOLOv8

Dự án này được xây dựng để phát hiện mũ bảo hộ trong hình ảnh và video bằng mô hình YOLOv8. Hệ thống hỗ trợ xử lý theo lô, trực quan hóa kết quả bằng bounding box và xuất báo cáo CSV để phục vụ bài toán giám sát an toàn lao động.

<img src="https://github.com/anhdungdev18/Helmet-detection-/blob/main/pic1.jpeg" width="1000" height="700">

## Mục Tiêu Dự Án

- Phát hiện mũ bảo hộ trong ảnh và video bằng mô hình YOLOv8 đã huấn luyện.
- Hỗ trợ suy luận trên thư mục ảnh hoặc tệp video đầu vào.
- Lưu ảnh và video đã annotate cùng báo cáo CSV chứa trạng thái phát hiện.
- Cung cấp notebook thử nghiệm và web demo để trình bày kết quả.

## Công Nghệ Sử Dụng

- Python
- YOLOv8 / Ultralytics
- OpenCV
- Supervision
- Gradio
- PyTorch

## Cấu Trúc Chính

- `main.py`: Chạy suy luận cho thư mục ảnh hoặc video đầu vào.
- `app.py`: Web demo bằng Gradio cho ảnh và video.
- `models/`: Chứa trọng số YOLO đã huấn luyện.
- `test_images/`: Ảnh và video mẫu để kiểm thử.
- `Result/`: Kết quả suy luận đã được lưu ra.
- `helmet-detection-yolov8.ipynb`: Notebook huấn luyện, đánh giá và suy luận.

## Cách Chạy

Chạy suy luận với thư mục ảnh:

```bash
python main.py <đường-dẫn-thư-mục-ảnh>
```

Chạy suy luận với video:

```bash
python main.py <đường-dẫn-video>
```

Chạy web demo:

```bash
python app.py
```

## Quy Trình Hoạt Động

1. Nạp mô hình YOLOv8 đã huấn luyện từ thư mục `models/`.
2. Đọc ảnh hoặc video đầu vào.
3. Chạy suy luận để phát hiện các lớp như `helmet`, `head`, `person`.
4. Vẽ bounding box và label lên ảnh hoặc khung hình video.
5. Lưu kết quả trực quan hóa vào thư mục `Result/`.
6. Xuất báo cáo CSV với trạng thái như `Helmet`, `No Helmet`, `Person Detected`.

## Đánh Giá Mô Hình

Repo hiện lưu các ảnh minh họa kết quả đánh giá:

- `graph.png`: Biểu đồ metric/loss trong quá trình huấn luyện.
- `cmatrix.png`: Ma trận nhầm lẫn của mô hình.

## Hạn Chế Và Hướng Phát Triển

- Kết quả vẫn có thể bị ảnh hưởng bởi góc chụp, che khuất hoặc chất lượng hình ảnh.
- Có thể mở rộng thêm các lớp PPE khác như kính bảo hộ, áo phản quang, găng tay.
- Có thể tích hợp thêm luồng camera thời gian thực hoặc cơ chế cảnh báo.

## Kết Quả Mẫu

<img src="https://github.com/anhdungdev18/Helmet-detection-/blob/main/Result/floor_1/images/hard_hat_workers42.png" width="500" height="500">

<img src="https://github.com/anhdungdev18/Helmet-detection-/blob/main/Result/floor_1/images/image_6.jpg" width="500" height="500">

<img src="https://github.com/anhdungdev18/Helmet-detection-/blob/main/Result/floor_1/images/image_7.jpg" width="500" height="500">
