![](https://www.bitdegree.org/storage/course-image/python-for-beginners.jpg)

## Giới thiệu Python

**Python** là một ngôn ngữ lập trình trên nhiều nền tảng như _Windows_, _Linux_
_macOS_. **Python** là mã nguồn mở và miễn phí khi sử dụng.

Hiện tại trên nền tảng _Linux_, _macOS_ có cài đặt sẵn **Python** nhưng
phiên bản thấp vì vậy trước khi sử dụng vài ứng dụng hoặc lập trình phát
triển với một vài thứ chúng ta cần nâng cấp phiên bản lên để tương thích
với yêu cầu của chúng ta.

**Python** là một ngôn ngữ thực thi khá nhanh trong quá trình máy tính xử
lý và độ thông dụng của nó rất lớn và nhiều, hiện nay có rất nhiều công
cụ hoặc ứng dụng được sử dụng **Python** để thực thi nó

## Cài đặt Python

Để cài đặt **Python** chúng ta vào một trong những địa chỉ sau

- Tải cho [Windows](https://www.python.org/downloads/windows/)
- Tải cho [maxOS](https://www.python.org/downloads/mac-osx/)
- Tải cho [Linux](https://www.python.org/downloads/source/)

Chọn tập tin tương thích với máy tính của chúng ta **(32-bit)** hoặc **(64-bit)**
để thuận tiện và sử dụng cơ bản thì chúng ta chọn phiên bản **Python 3.7**

Với nền tảng là _Windows_ khi cài đặt chúng ta chú ý chọn mục **Add Python
to environment variables** mục này sẽ đưa **Python** vào hệ thống biến của
hệ thống khi đó chúng ta có thể gọi **Python** bất kỳ ở thư mục nào để thực
thi mã nguồn của chúng ta.

Dưới đây là một hình ảnh minh hoạ khi chúng ta chọn trong khi cài đặt **Python**

![](https://cdn.programiz.com/sites/tutorial2program/files/python-install_0.jpg)

Sau khi hoàn tất quá trình cài đặt chúng ta có thể chạy **Python**

## Chạy Python trực tiếp

Sau khi cài đặt xong chúng ta mở `cmd` trong _Windows_, `terminal` trong
_Linux_ hoặc _macOS_ gõ vào lệnh `python` chúng ta sẽ được màn hình như sau

![](https://cdn.programiz.com/sites/tutorial2program/files/python-run-command-mode.jpg)

Chúng ta gõ thử vào `1 + 1` và nhấn `Enter`. màn hình sẽ hiển thị ra kết 
quả `2` như vậy là chúng ta đã hoàn thành cài đặt **Python** lên máy tính
của chúng ta.

Để thoát **Python** trên màn hình thực thi chúng ta gõ vào `quit()` và nhấn
`Enter` **Python** sẽ thoát ra.

## Cài đặt trình soạn thảo mã Python

Hiện nay có nhiều trình soạnn thảo mã để có thể soạn thảo mã **Python**
Nếu chúng ta sử dụng _Windows_ chúng ta có thể chon **[Nodepad++](https://notepad-plus-plus.org/downloads/)**
hoặc **[Visual Studio Code](https://code.visualstudio.com/download)** lưu
ý chúng ta chọn đúng với hệ thống máy tính của chúng ta **(32-bit)** hoặc **(64-bit)**
và cài đặt chúng

Để cài đặt **Nodepad++** chúng ta tham khảo [tài liệu tại đây](https://npp-user-manual.org/docs/getting-started/)
và cài đặt **Visual Studio Code** chúng ta tham khảo [tài liệu tại đây](https://code.visualstudio.com/docs/setup/setup-overview)
đây là trên quan điểm của tác giả để có thể có một trình soạn thảo mã nguồn
**Python** nhỏ và nhẹ nhất để tiến hành học **Python**


## Làm quen với vài ví dụ Python cơ bản

Hãy mở trình soạn thảo văn bản của chúng ta và nhập đoạn mã sau lưu với
tên tập tin là `hello.py`. lưu ý đuôi là `.py`

    print("hello, world!")

Tiến hành chạy tập tin `hello.py` bằng câu lệnh sau

    python hello.py

> Lưu ý hãy chuyển tới thư mục lưu trữ tập tin `hello.py` trước khi thực
thi câu lệnh trên nhé.

Khi đó kết quả sẽ như sau

    hello, world!

Nếu kết quả trên màn hình của chúng ta có kết quả như vậy thì chúng ta đã
hoàn tất một ví dụ nhỏ về **Python**

## Các từ khóa của Python

Trong **Python** sẽ có các từ khóa cơ bản để chúng ta làm việc cụ thể nó
sẽ bao gồm như sau

- Nhập xuất: `print`, `input`
- Rẽ nhánh: `if`, `else`, `elif`
- Vòng lặp: `for`, `while`
- Thoát và tiếp tục vòng lặp: `break`, `continue`
- Định nghĩa hàm: `def`
- Nạp thư viện: `from`, `import`

### Từ khóa `print`

`print` là một từ khóa hệ thống dành cho việc xuất ra màn hình với những
thứ mình cần xem.

Để xuất ra câu thông báo ta viết mã như sau

    print("Nội dung thông báo")

Khi thực thi thì trên màn hình sẽ xuất ra dòng chữ như sau

    Nội dung thông báo

> Từ khóa `print` cũng có thể xuất ra vài đối tượng nếu như nó được định
nghĩa kiểu chuối trả về có nghĩa là hàm `__str__` trong đối tượng được định
nghĩa

### Từ khóa `input`

`input` là từ khóa dùng cho mục đích nhận dữ liệu từ bàn phím của người dùng

> Lưu ý từ khóa `input` giá trị mạc định là string, nếu ta muốn nhập một số
nguyên a thì ta sẽ ép kiểu đầu vào như sau: `a = int(input())`

Để yêu cầu người dùng nhập vào bất kỳ ký từ nào từ bàn phím ta viết mã
như sau

    print('Nhập vào tên bạn: ')
    x = input()
    print("Chào, {}".format(x))

Trong đoạn mã trên sẽ xuất ra câu thông báo _Nhập vào tên bạn:_ và có màn
hình chờ cho bạn nhập thông tin vào, sau khi nhập xong nhấn phím `Enter`
thì sẽ xuất ra như sau

    Nhập vào tên bạn: Bob
    Chào, Bob

## Từ khóa `if`, `else`, `elif`

Từ khóa `if`, `else`, `elif` dùng để rẽ nhánh trong quá trình chúng ta
kiểm tra một cái gì đó

Cú pháp:

    if điều kiện:
        Khối lệnh xử lý if
    elif điều kiện:
        Khối lệnh xử lý elif
    else:
        Khối lệnh xử lý else

Ví dụ với mã sau

    print("Nhập vào một số từ 1 đến 3: ")
    val = input()
    if val == "1":
        print("Một")
    elif val == "2":
        print("Hai")
    elif val == "3":
        print("Ba")
    else:
        print("Số bạn nhập không hợp lệ !")


Khi thực thi với đầu vào là `1` thì sẽ có kết quả như sau

    Nhập vào một số từ 1 đến 3: 1
    Một

Khi thực thi với đầu vào là `2` thì sẽ có kết quả như sau

    Nhập vào một số từ 1 đến 3: 2
    Hai

Khi thực thi với đầu vào là `3` thì sẽ có kết quả như sau

    Nhập vào một số từ 1 đến 3: 3
    Ba

Khi thực thi với đầu vào là `4` thì sẽ có kết quả như sau

    Nhập vào một số từ 1 đến 3: 4
    Số bạn nhập không hợp lệ !


## Soạn thảo mã Python

Sau khi hoàn tất quá trình cài đặt **Python** và trình soạn thảo cho lựa
chọn của chúng ta, tiếp đây sẽ tiến hành soạn thảo mã **Python**

Để bắt đầu chúng ta cần lưu ý như sau

Để khai báo một hàm trong **Python** chúng ta bắt đầu với từ khoá `def`
nó là viết tắt của từ `define` có nghĩa là khai báo sau đó tới tên hàm cần
định nghĩa ví dụ: định nghĩa hàm `chao_python` chúng ta sẽ soạn thảo mã
như sau


    def chao_python():
        print("Chào Python")

Vì python không sử dụng dấu `{` và `}` để ngăn cách nên chúng ta cần phải
chú ý dấu cách cho hợp lệ để mã **Python** được đúng nên sử dụng 2 dấu cách
trở lên hoặc là một `tab` để phân biệt.

