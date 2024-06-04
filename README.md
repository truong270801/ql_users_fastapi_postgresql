# Sử dụng FastAPI, PostgreSQL và GraphQL tạo API quản lý dữ liệu người dùng  

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
* Trỏ đến branch chạy : ` git checkout GraphQL`
* Cài đặt các thư viện :` pip install -r requirements.txt`
* Chạy version database: `alembic upgrade head`
* Chạy dự án : `uvicorn main:app --reload`


### Mở trình duyệt :
* URL mặc định: `http://127.0.0.1:8000/`
* URL mở Swagger UI: `http://127.0.0.1:8000/docs/`
* URL mở Ariande GraphQL: `http://127.0.0.1:8000/graphql`

Câu lệnh truy vấn :
- Lệnh tạo thêm người dùng 

```
# Tạo dữ liệu của người dùng mới và trả về giá trị yêu cầu.
    mutation{
    createUser(user_data:{
        firstName: "tran",
        lastName: "truong",
        maidenName: "van",
        gender: "nam",
        birthDate: "2001-08-27",
        age:23 ,
        email: "truong@gmail.com",
        city: "nam dinh",
        phone: "0123456789",
        address: "nam dinh",
        university: "HAU"
    }){
        id
        firstName
        lastName
        email
        birthDate
        city
        gender
        phone
        address
        university
    }
    }

```
- Lệnh lấy tất cả người dùng :
    ```
#Lấy tất cả dữ liệu tất cả người dùng theo giá trị yêu cầu.
    query{
    allUsers{
            id
            firstName
            lastName
            email
            birthDate
            city
            gender
            phone
            address
            university
    }
    }
    ```
- Lệnh lấy thông tin 1 người dùng duy nhất:
    ```
    #Lấy dữ liệu của 1 người dùng theo trường id và trả về giá trị yêu cầu.
        query{
        user(id:1){
            firstName
            lastName
            birthDate
            age
            address
            gender
            university
        }
        }
    ```
- Lệnh sửa thông tin người dùng:

    ```
    # Sửa lại dữ liệu người dùng theo trường id và trả về kết quả theo yêu cầu.
    mutation{
    updateUser(id:5,user_data:{
                firstName: "nguyen",
                lastName: "nam",
                maidenName: "hoang",
                gender: "nam",
                birthDate: "1999-03-16",
                age:25 ,
                email: "hoangnam@gmail.com",
                city: "ha noi",
                phone: "0123456789",
                address: "ha noi",
                university: "HAU"
            }){
                id
                firstName
                lastName
                email
                birthDate
                city
                gender
                phone
                address
                university
    }
    }
```
```

 - lệnh xóa dữ liệu người dùng :

```
#Xóa toàn bộ dữ liệu người dùng và trả thông tin người dùng bị xóa theo yêu cầu .
    mutation{
    deleteUser(id:1){
                id
                lastName
     }
    }
```
