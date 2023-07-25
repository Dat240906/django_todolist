<span style="color:red">


                    ▓█████▄  ▄▄▄     ▄▄▄█████▓
                    ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒
                    ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░
                    ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ 
                    ░▒████▓  ▓█   ▓██▒ ▒██▒ ░ 
                    ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   
                    ░ ▒  ▒   ▒   ▒▒ ░   ░    
                    ░ ░  ░   ░   ▒    ░      
                    ░          ░  ░        
                    ░                        

</span>


# TO-DO LIST Project
Mô tả ngắn về dự án của bạn ở đây.

## Cách sử dụng API

Dưới đây là các hướng dẫn cơ bản về cách sử dụng API trong dự án này.

#########################_API_USER_######################################

**Kết quả trả về (CHUNG):**
-success
{
    "status":True,
    "data": your_data
}
-error
{
    "status":False,
    "message": message_error
}




**Endpoint:** /api/user/
-------------------------------------------------
**Phương thức:** POST

**Mô tả:** Lấy các dịch vụ (việc làm) của user

**Tham số:**

{
    "type":'get_service',
    "username":"your_username",
    "password":"your_password"
}

------------------------------------------------
**Phương thức:** POST

**Mô tả:** Tạo tài khoản User

**Tham số:**

{
    "type":'create_acc',
    "username":"your_username",
    "password":"your_password"
}
#######################_API_SERVICE_###########################################


**Endpoint:** /api/service/
-------------------------------------------------------
**Phương thức:** POST

**Mô tả:** Thêm service

**Tham số:**

{
    "type":"add_service",
    "username":"your_username",
    "password":"your_password",
    "title": "title_want_add",
    "time": "2023-07-25T08:31:15Z"
}

Note: Lưy ý về trường time: (bên trên là ví dụ, bạn có thể thay đổi)
    "2023": Năm.
    "07": Tháng (tháng 7).
    "25": Ngày trong tháng.
    "08": Giờ (24 giờ).
    "31": Phút.
    "15": Giây.
    "Z": Đại diện cho múi giờ UTC (Coordinated Universal Time).
---------------------------------------------------
**Phương thức:** POST

**Mô tả:** Xóa Service

**Tham số:**

{
    "type":"del_service",
    "username":"your_username",
    "password":"your_password",
    "title": "title_want_delete",
}

## Liên hệ

Đây chỉ là dự án học tập, Nếu bạn có bất kỳ vấn đề hoặc câu hỏi, hãy liên hệ với tôi qua phungthanhdat001@gmail.com
