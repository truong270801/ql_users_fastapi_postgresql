# Sử dụng FastAPI và PostgreSQL tạo API quản lý dữ liệu người dùng 

## Yêu cầu :
* Cài đặt [Python](https://www.python.org/downloads/)
* Cài đặt [PostgreSQL](https://www.postgresql.org/download/)
* Tùy nhu cầu dùng [Postman](https://www.postman.com/downloads/)


## Cài đặt :

* `git clone https://github.com/truong270801/ql_users_fastapi_postgresql.git`

### Cơ sở dữ liệu:
* Tạo cơ sở dữ liệu mới tên là `Users`
* Sửa đổi tên, mật khẩu, tên database, tên host trong file .env
```
DB_USER="postgres"
DB_PASS="123456"
DB_HOST="localhost:5432"
DB_NAME="Users"
```
### Mở lệnh Terminal VSCode:
* Trỏ đến thư mục chạy dự án: `cd ql_users_fastapi_postgresql`
* Cài đặt các thư viện :` pip install -r requirements.txt`
* Chạy version database: `alembic upgrade head`
* Chạy dự án : `uvicorn main:app --reload`


### Mở trình duyệt :
* URL mặc định: `http://127.0.0.1:8000/`
* URL mở Swagger UI: `http://127.0.0.1:8000/docs/`
* URL lấy dữ liệu tất cả user: `http://127.0.0.1:8000/users/`
* URL lấy dữ liệu user từ id:`http://127.0.0.1:8000/users/{id}`
