# Python Learning Roadmap

## 1. Mục đích

Repository này được sử dụng để học Python theo một lộ trình có cấu trúc, có theo dõi tiến độ và có lưu lại quá trình thực hành.

Mục tiêu không chỉ là viết được code Python mà còn xây dựng khả năng:

- hiểu bản chất của Python;
- đọc và phân tích code;
- tự giải quyết bài toán;
- viết code rõ ràng, dễ đọc;
- kiểm tra và sửa lỗi;
- tổ chức mã nguồn;
- sử dụng Git trong quá trình học;
- xây dựng các mini-project và project thực tế.

---

## 2. Nguyên tắc xây dựng lộ trình

Lộ trình được tổ chức theo nguyên tắc:

```text
Kiến thức
    ↓
Thực hành
    ↓
Bài tập
    ↓
TASK
    ↓
Kiểm tra
    ↓
Review
    ↓
PASS
    ↓
Tổng hợp
    ↓
Mini Project / Project
```

Số lượng TASK trong mỗi Level **không cố định trước**.

TASK được tạo dựa trên:

- độ phức tạp thực tế của kiến thức;
- mức độ hiểu của người học;
- kết quả thực hành;
- các điểm còn yếu cần luyện tập;
- yêu cầu của mini-project hoặc project.

Không chạy theo số lượng TASK.

---

# 3. Cấu trúc chương trình

## Phase 0 — Learning Foundation

### Mục tiêu

Xây dựng nền tảng cho quá trình học:

- roadmap;
- quy tắc học;
- quy trình TASK;
- quản lý tiến độ;
- Git và GitHub;
- cách ghi lại quá trình học.

### Tài liệu

- `01-python-roadmap.md`
- `02-learning-rules.md`
- `03-task-management.md`
- `04-progress.md`

### Tiến độ

[→ Xem tiến độ Phase 0](./04-progress.md#5-phase-0--learning-foundation)

---

# Level 1 — Python Basic

### Mục tiêu

Nắm được nền tảng ngôn ngữ Python và có thể viết các chương trình đơn giản từ đầu.

### Nội dung chính

- Python syntax cơ bản
- `print()`
- comment
- biến
- kiểu dữ liệu cơ bản
- `int`
- `float`
- `str`
- `bool`
- toán tử số học
- toán tử so sánh
- toán tử logic
- input/output
- ép kiểu
- biểu thức
- `if`
- `elif`
- `else`
- điều kiện lồng nhau
- `for`
- `while`
- `range()`
- biến tích lũy
- các bài toán cơ bản

### Phân bổ TASK đề xuất cho Level 1

Thứ tự dưới đây dùng làm khung để chia TASK, không bắt buộc mỗi chủ đề phải có một TASK riêng. Nội dung đã được chứng minh trong Entry Assessment hoặc TASK trước có thể được kiểm tra ngắn để xác nhận, không cần học lại toàn bộ.

| Module | Trọng tâm | TASK / trạng thái |
|---|---|---|
| Module 1 — Python Foundation | Mô hình thực thi, biến, kiểu dữ liệu, cú pháp và debugging cơ bản | TASK-01 — PASS |
| Module 2 — Expressions & Operators | Biểu thức, toán tử và các khác biệt quan trọng khi chuyển từ C sang Python | TASK-02 — TODO |
| Module 3 — Conditions | Biểu thức điều kiện, if/elif/else và bài toán rẽ nhánh | Dự kiến |
| Module 4 — Loops | for, while, range, accumulator và kiểm soát vòng lặp | Dự kiến; chú ý đánh giá while |
| Module 5 — Problem Solving | Phân rã bài toán và Mini Project tổng hợp Level 1 | Dự kiến |

Input/output cơ bản được tích hợp vào các bài thực hành khi cần, thay vì mặc định tách thành một TASK riêng, vì nội dung này đã có trong Entry Assessment. Phân bổ này có thể điều chỉnh theo kết quả học và Self-Test.

### Kết quả mong đợi

Người học có thể:

- đọc hiểu chương trình Python đơn giản;
- nhận dữ liệu từ người dùng;
- xử lý dữ liệu cơ bản;
- sử dụng điều kiện;
- sử dụng vòng lặp;
- tự viết các chương trình nhỏ.

### Mini Project

**Python Basic Practice**

Một chương trình tổng hợp sử dụng:

- input;
- biến;
- kiểu dữ liệu;
- điều kiện;
- vòng lặp.

### Tiến độ

[→ Xem tiến độ Level 1](./04-progress.md#6-level-1--python-basic)

---

# Level 2 — Control Flow & Function

### Mục tiêu

Biết tổ chức chương trình thành các khối xử lý có cấu trúc và bắt đầu xây dựng các hàm có thể tái sử dụng.

### Nội dung chính

- control flow nâng cao
- `for`
- `while`
- `break`
- `continue`
- `pass`
- nested loop
- function
- parameter
- argument
- return
- local variable
- global variable
- default parameter
- keyword argument
- scope
- docstring
- tư duy chia bài toán thành hàm

### Kết quả mong đợi

Người học có thể:

- chia một bài toán thành các bước xử lý;
- viết hàm;
- truyền dữ liệu vào hàm;
- nhận kết quả từ hàm;
- tái sử dụng code;
- tránh viết một chương trình quá dài trong một khối.

### Mini Project

**Console Utility**

Một chương trình dòng lệnh gồm nhiều chức năng được tổ chức bằng function.

### Tiến độ

[→ Xem tiến độ Level 2](./04-progress.md#7-level-2--control-flow--function)

---

# Level 3 — String & Collections

### Mục tiêu

Làm chủ việc xử lý dữ liệu dạng chuỗi và các cấu trúc dữ liệu cơ bản của Python.

### Nội dung chính

### String

- indexing
- slicing
- string methods
- format string
- f-string
- xử lý chuỗi
- tìm kiếm và thay thế
- tách và ghép chuỗi

### List

- tạo list
- indexing
- slicing
- thêm/xóa phần tử
- duyệt list
- list methods
- nested list
- list comprehension

### Tuple

- tuple
- unpacking
- immutable data

### Set

- set
- unique values
- set operations

### Dictionary

- key/value
- truy cập dữ liệu
- thêm/xóa/sửa
- duyệt dictionary
- nested dictionary
- dictionary comprehension

### Kết quả mong đợi

Người học có thể lựa chọn cấu trúc dữ liệu phù hợp và xử lý dữ liệu thực tế ở mức cơ bản.

### Mini Project

**Data Processing Practice**

Xử lý danh sách và dữ liệu dạng dictionary trong một chương trình thực tế nhỏ.

### Tiến độ

[→ Xem tiến độ Level 3](./04-progress.md#8-level-3--string--collections)

---

# Level 4 — Modules & Classes

### Mục tiêu

Hiểu cách tổ chức chương trình Python thành nhiều module và bắt đầu tiếp cận class.

### Nội dung chính

- module
- import
- package
- `__name__`
- `__main__`
- thư viện chuẩn Python
- tổ chức project
- class
- object
- attribute
- method
- constructor
- `__init__`
- instance
- class cơ bản

### Kết quả mong đợi

Người học có thể:

- chia chương trình thành nhiều file;
- import và sử dụng module;
- tổ chức code có cấu trúc;
- hiểu quan hệ giữa class và object;
- tạo class đơn giản.

### Mini Project

**Modular Python Application**

Một chương trình được tổ chức thành nhiều module và class cơ bản.

### Tiến độ

[→ Xem tiến độ Level 4](./04-progress.md#9-level-4--modules--classes)

---

# Level 5 — OOP & Exception

### Mục tiêu

Hiểu sâu hơn về lập trình hướng đối tượng và xử lý lỗi trong Python.

### Nội dung chính

### OOP

- encapsulation
- inheritance
- polymorphism
- abstraction
- composition
- class method
- static method
- property
- special methods

### Exception

- exception
- `try`
- `except`
- `else`
- `finally`
- `raise`
- custom exception
- defensive programming

### Kết quả mong đợi

Người học có thể thiết kế chương trình có cấu trúc tốt hơn và xử lý các tình huống lỗi một cách chủ động.

### Mini Project

**OOP Management Application**

Một ứng dụng quản lý nhỏ sử dụng class, inheritance và exception handling.

### Tiến độ

[→ Xem tiến độ Level 5](./04-progress.md#10-level-5--oop--exception)

---

# Level 6 — File & Testing

### Mục tiêu

Biết làm việc với dữ liệu bên ngoài chương trình và xây dựng chương trình có khả năng kiểm thử.

### Nội dung chính

### File

- đọc file
- ghi file
- text file
- CSV
- JSON
- path
- directory
- `pathlib`

### Testing

- tư duy kiểm thử
- test case
- unit test
- `unittest`
- `pytest`
- assertion
- test function
- test exception
- test organization

### Kết quả mong đợi

Người học có thể:

- đọc và ghi dữ liệu;
- lưu trữ dữ liệu;
- xử lý file;
- viết test cơ bản;
- phát hiện lỗi thông qua test;
- tổ chức project có kiểm thử.

### Mini Project

**File-based Python Application**

Một ứng dụng Python lưu trữ và xử lý dữ liệu từ file, có test cơ bản.

### Tiến độ

[→ Xem tiến độ Level 6](./04-progress.md#11-level-6--file--testing)

---

# 4. Project thực hành tổng hợp

Sau khi hoàn thành các Level nền tảng, người học sẽ thực hiện các project lớn hơn.

Project được lựa chọn dựa trên:

- kiến thức đã học;
- nhu cầu thực tế;
- khả năng hiện tại;
- mục tiêu phát triển tiếp theo.

Không bắt buộc phải hoàn thành một số lượng project cố định.

---

# 5. Cách xác định hoàn thành

Một Level không được xem là hoàn thành chỉ vì đã học hết danh sách kiến thức.

Level chỉ được xem xét hoàn thành khi người học có thể:

1. Giải thích được các khái niệm chính.
2. Viết được code mà không phụ thuộc hoàn toàn vào lời giải.
3. Hoàn thành các TASK cần thiết.
4. Tự kiểm tra chương trình.
5. Sửa được các lỗi cơ bản.
6. Hoàn thành mini-project của Level.
7. Review lại những phần còn yếu.
8. Cập nhật documentation và progress.

---

# 6. Nguyên tắc điều chỉnh Roadmap

Roadmap là tài liệu định hướng, không phải danh sách cố định bất biến.

Trong quá trình học có thể:

- thêm TASK;
- chia một TASK thành nhiều TASK;
- gộp các TASK quá nhỏ;
- thêm bài luyện tập cho phần còn yếu;
- điều chỉnh mini-project;
- bổ sung kiến thức cần thiết.

Mọi thay đổi quan trọng cần được ghi nhận trong documentation và progress.

---

# 7. Trạng thái

Roadmap sử dụng các trạng thái:

- `TODO`
- `IN PROGRESS`
- `BLOCKED`
- `FAIL`
- `PASS`

Không sử dụng phần trăm hoàn thành tổng thể.

Tiến độ được đánh giá dựa trên:

```text
Level
  ↓
Module
  ↓
TASK
  ↓
Milestone
  ↓
Mini Project
```

---

# 8. Mục tiêu cuối cùng

Mục tiêu của repository không phải là hoàn thành thật nhiều bài tập.

Mục tiêu là xây dựng năng lực:

> **Hiểu → Tự làm → Kiểm tra → Sửa lỗi → Giải thích → Áp dụng**

và từng bước chuyển từ:

```text
Người học Python
        ↓
Người viết được Python
        ↓
Người giải quyết vấn đề bằng Python
        ↓
Người xây dựng ứng dụng bằng Python
```
