# Chatbot-ChatGPT-Python
Tạo chatbot với ChatGPT bằng Python
# Cách cài đặt
Bước 1: Các bạn clone repo này về bằng lệnh: 
`git clone https://github.com/ellyx13/Chatbot-ChatGPT-Python.git`

Bước 2: Cài đặt các thư viện python cần thiết: 
`pip install -r requirements.txt`

# Cách sử dụng
Bước 1: Đăng ký tài khoản ChatGPT. Các bạn có thể xem hướng dẫn đăng ký [tại đây](https://anonyviet.com/cach-tao-tai-khoan-chatgpt-o-viet-nam/)

Bước 2: Hỏi AI bất cứ thứ gì.

Bước 3: Bật F12 và vào tab Application > Storage > Cookies > Chọn mục đầu tiên và tìm token có tên là "__Secure-next-auth.session-token". Sau đó copy mã token trong cột Value.

Bước 4: Dán mã token đó vào biến session_token trong file pyChatbotGPT.py

Bước 5: Chạy file bằng lệnh 
`python pyChatbotGPT.py`

Vậy là xong rồi đó. 

Ngoài ra các bạn cũng có thể đưa con bot này ra internet để bạn bè sử dụng bằng ngrok nhé.
