import cv2
import time

# Mở camera
cap = cv2.VideoCapture(0)  # 0 là số thứ tự của camera, có thể thay đổi tùy vào thiết bị

# Thiết lập thời gian giữa các video (đơn vị: giây)
video_interval = 0.5

# Thiết lập thư mục chứa video
output_folder = r'd:\Downloads\frames'
if not cv2.os.path.exists(output_folder):
    cv2.os.makedirs(output_folder)

# Lấy thông số của frame để cấu hình VideoWriter
width = int(cap.get(3))  # Chiều rộng frame
height = int(cap.get(4))  # Chiều cao frame

# Tạo đối tượng VideoWriter (dạng video)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Hoặc sử dụng 'MJPG' nếu không có XVID

# Lấy thời điểm bắt đầu
start_time = time.time()

# Đếm số video đã lưu
video_count = 1

# Biến để xác định khi nào bắt đầu thu frame
start_recording = False

while True:
    # Tính thời gian kết thúc dựa trên thời gian bắt đầu và khoảng thời gian giữa các video
    end_time = start_time + video_interval

    # Tạo tên file video dựa trên số thứ tự
    video_name = f"{output_folder}/frame_{video_count}.avi"

    # Tạo đối tượng VideoWriter cho video mới
    out = cv2.VideoWriter(video_name, fourcc, 30, (width, height))

    while time.time() < end_time:
        # Đọc frame từ camera
        ret, frame = cap.read()
        
        # Phản chiếu hình ảnh theo chiều ngang
        frame = cv2.flip(frame, 1)

        # Hiển thị frame
        cv2.imshow('Camera', frame)

        # Ghi frame vào video
        out.write(frame)

        # Thoát khỏi vòng lặp khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Đóng VideoWriter của video vừa kết thúc
    out.release()

    # Tăng số thứ tự của video
    video_count += 1

    # Cập nhật thời điểm bắt đầu cho video tiếp theo
    start_time = time.time()

    # Thoát khỏi vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Đóng camera và cửa sổ
cap.release()
cv2.destroyAllWindows()
