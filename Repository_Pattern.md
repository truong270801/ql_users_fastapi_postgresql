# Tìm hiểu Repository Pattern 

## Repository Pattern là gì?
### Khái niệm.
  Repository Pattern là lớp trung gian giữa tầng Business Logic và Data Access , giúp cho việc truy cập dữ liệu chặt chẽ và bảo mật hơn. Repository đóng vai trò là một lớp kết nối giữa tầng Business và Model của ứng dụng.

![](https://images.viblo.asia/fd4b10a0-f1b1-4ed1-9bd1-578c871820ae.png)
### Tác dụng của Repository Pattern
* Tách biệt Business Logic và Data Access: Repository Pattern giúp tách biệt Business Logic của ứng dụng từ chi tiết về cách dữ liệu được lưu trữ và truy xuất. Điều này làm cho mã nguồn dễ bảo trì hơn, vì nó cho phép thay đổi cách lưu trữ dữ liệu mà không cần sửa đổi nhiều mã trong Business Logic.
* Tăng khả năng kiểm thử: Bằng cách sử dụng Repository Pattern, có thể dễ dàng thay thế các đối tượng Repository bằng các đối tượng giả định (mock objects) trong quá trình kiểm thử. Điều này giúp việc kiểm thử trở nên dễ dàng hơn và đảm bảo tính đáng tin cậy của ứng dụng.
* Tăng tính tái sử dụng mã: Repository Pattern tạo điều kiện cho việc tái sử dụng mã, vì nó cho phép các phương thức truy xuất dữ liệu được tái sử dụng trong nhiều phần của ứng dụng mà không cần viết lại hoặc sao chép mã.
* Giảm sự phụ thuộc giữa các thành phần của ứng dụng: Bằng cách sử dụng Repository Pattern, các lớp khác nhau của ứng dụng chỉ cần phụ thuộc vào các giao diện của Repository mà không cần biết chi tiết về cách dữ liệu được lưu trữ hoặc truy xuất. Điều này giúp giảm sự phụ thuộc giữa các thành phần và làm cho mã nguồn dễ bảo trì hơn.

## Triển khai Repository Pattern 
Triển khai Repository Pattern bằng ngôn ngữ Javascript:
1. Đối tượng Dữ liệu (Data Object): Đây là các đối tượng đại diện cho dữ liệu trong ứng dụng . Ví dụ, trong một ứng dụng quản lý người dùng, có một đối tượng `User` để lưu trữ thông tin về người dùng.

```
class User {
    constructor(id, name, email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
}
```

2. Repository Interface: Định nghĩa các phương thức cần thiết để thao tác với đối tượng dữ liệu. Interface này định nghĩa các phương thức như `getById`, `getAll`, `create`, `update`, `delete`.

```
class UserRepository {
    getById(id) {}
    getAll() {}
    create(user) {}
    update(user) {}
    delete(id) {}
}
```

3. Triển khai Repository: Triển khai các phương thức đã được định nghĩa trong Repository Interface. Trong triển khai này,  thực hiện các thao tác thực tế với cơ sở dữ liệu hoặc nguồn dữ liệu khác.

```
class UserMemoryRepository extends UserRepository {
    constructor() {
        super();
        this.users = [];
    }

    getById(id) {
        return this.users.find(user => user.id === id);
    }

    getAll() {
        return this.users;
    }

    create(user) {
        this.users.push(user);
    }

    update(user) {
        const index = this.users.findIndex(u => u.id === user.id);
        if (index !== -1) {
            this.users[index] = user;
        }
    }

    delete(id) {
        this.users = this.users.filter(user => user.id !== id);
    }
}
```

4. Sử dụng Repository: Trong ứng dụng thực tế, sử dụng các đối tượng Repository để thao tác với dữ liệu.

```
const userRepository = new UserMemoryRepository();

const user1 = new User(1, 'Truong', 'truong@example.com');
userRepository.create(user1);

const user2 = userRepository.getById(1);
console.log(user2);

user2.name = 'Truong';
userRepository.update(user2);

const allUsers = userRepository.getAll();
console.log(allUsers);

userRepository.delete(1);
```




