# TASK-01 — Python Foundation

## 1. Thông tin TASK

- **Tên:** Python Foundation
- **Level:** Level 1 — Python Basic
- **Module:** Module 1 — Python Foundation
- **Trạng thái:** PASS
- **Ngày bắt đầu:** 2026-10-01
- **TASK trước:** Entry Assessment
- **TASK sau:** TASK-02 — Expressions & Operators: C to Python
- **Tài liệu tham khảo chính:** W3Schools Python Tutorial

---

## 2. Bối cảnh

Entry Assessment cho thấy người học đã có nền tảng tương đối tốt về Python Basic:

- `print()`
- comments
- variables
- `int`, `float`, `str`, `bool`
- arithmetic operators
- comparison operators
- logical operators
- input/output
- type casting
- expressions ở mức cơ bản
- `if / elif / else`
- `for`
- `range()`
- accumulator

Các nội dung cần củng cố:

- mô hình thực thi Python;
- độ chính xác cú pháp khi tự viết;
- chuyển yêu cầu thành thuật toán rồi thành code;
- kiểm tra code trước khi kết luận;
- `while`;
- debugging có hệ thống.

Vì vậy TASK-01 không học lại Python từ đầu một cách máy móc, mà tập trung chuẩn hóa nền tảng và cách viết code chính xác.

---

## 3. Mục tiêu

**Củng cố mô hình thực thi Python và khả năng làm việc với biến, kiểu dữ liệu, `type()` và cú pháp Python cơ bản.**

Sau TASK-01, người học có thể:

1. Giải thích Python thực thi chương trình ở mức cơ bản.
2. Hiểu biến và assignment.
3. Nhận biết `int`, `float`, `str`, `bool`.
4. Sử dụng `type()` để kiểm tra kiểu dữ liệu.
5. Hiểu và sử dụng type casting ở mức củng cố.
6. Viết chương trình nhỏ với cú pháp chính xác.
7. Tự chạy và kiểm tra chương trình.
8. Đọc lỗi cú pháp đơn giản, xác định vị trí lỗi và sửa lỗi.
9. Giải thích được code do chính mình viết.

---

## 4. Phạm vi

### 4.1. Python execution model

Hiểu ở mức cơ bản:

```text
Python source code
       ↓
    Bytecode
       ↓
Python Virtual Machine
       ↓
    Execution
```

Có khả năng giải thích:

- Python source code là gì.
- Bytecode là gì.
- Python Virtual Machine làm gì.
- Vì sao Python có bước biên dịch sang bytecode và sau đó thực thi qua VM.

**Không đi sâu vào CPython internals.**

### 4.2. Comments

```python
# Đây là comment
```

Yêu cầu:

- biết comment bằng `#`;
- phân biệt comment với code được thực thi;
- tránh nhầm cú pháp comment của ngôn ngữ khác như `//`.

### 4.3. Variables & assignment

Ví dụ:

```python
name = "An"
age = 25
height = 1.7
is_student = True
```

Hiểu được:

- biến;
- assignment `=`;
- giá trị;
- kiểu dữ liệu;
- mối quan hệ giữa tên biến và giá trị được gán.

### 4.4. Basic data types

Tập trung vào:

```text
int
float
str
bool
```

Có khả năng xác định kiểu dữ liệu của một giá trị.

### 4.5. `type()`

Ví dụ:

```python
age = 25
print(type(age))
```

Yêu cầu:

- sử dụng được `type()`;
- đọc kết quả;
- giải thích được kết quả cho giá trị đang kiểm tra.

### 4.6. Type casting

Củng cố các hàm:

```python
int()
float()
str()
bool()
```

Mục tiêu là hiểu khi nào cần chuyển kiểu và nhận biết kết quả của việc chuyển kiểu.

Type casting không phải trọng tâm bài tập lớn của TASK-01 vì Entry Assessment cho thấy nội dung này đã có nền tảng.

### 4.7. Basic syntax

Tập trung vào các lỗi đã xuất hiện trong Entry Assessment:

- thiếu `)`;
- thiếu `:`;
- sai indentation;
- nhầm cú pháp comment;
- sai cú pháp `print()`;
- sai cú pháp f-string ở mức cơ bản.

Đây là phần thực hành quan trọng vì logic của người học tương đối tốt nhưng đôi khi code chưa chính xác về cú pháp.

---

## 5. Ngoài phạm vi TASK-01

Để tránh TASK quá lớn, chưa học sâu:

- `input()`;
- arithmetic operators;
- comparison operators;
- logical operators;
- `if`;
- `for`;
- `while`;
- collections;
- functions;
- exception handling.

Các nội dung này thuộc Module/TASK tiếp theo.

---

## 6. Tài liệu học tập

W3Schools được sử dụng như **nguồn học liệu**, không phải roadmap của dự án.

Roadmap của dự án:

```text
Roadmap
   ↓
Module
   ↓
TASK
   ↓
Tài liệu học tập
   ↓
Thực hành
   ↓
Self-Test
   ↓
Review
   ↓
PASS
```

Các chủ đề W3Schools phù hợp với TASK-01:

| TASK-01 | W3Schools |
|---|---|
| Syntax | Python Syntax |
| Comments | Python Comments |
| Variables | Python Variables |
| Data types | Python Data Types |
| `type()` | Data Types / Variables |
| Casting | Python Casting |
| `print()` | Python Output |

Phần execution model sẽ được hướng dẫn riêng vì đây không phải trọng tâm của các bài W3Schools được sử dụng cho TASK-01.

---

## 7. Acceptance Criteria

TASK-01 chỉ được **PASS** khi hoàn thành toàn bộ Acceptance Criteria.

### AC-01 — Execution model

Có thể tự giải thích:

```text
Source code
    ↓
Bytecode
    ↓
Python VM
    ↓
Execution
```

và giải thích được vai trò cơ bản của từng bước.

### AC-02 — Variables

Tự viết được chương trình khai báo ít nhất:

- một `str`;
- một `int`;
- một `float`;
- một `bool`.

### AC-03 — Data types

Tự xác định chính xác kiểu dữ liệu của các giá trị được đưa ra.

### AC-04 — `type()`

Sử dụng `type()` để kiểm tra kiểu dữ liệu và giải thích được kết quả.

### AC-05 — Comments

Sử dụng đúng comment bằng `#` và phân biệt được comment với câu lệnh Python.

### AC-06 — Syntax

Tự viết được một chương trình Python nhỏ không có lỗi cú pháp, đặc biệt tránh các lỗi đã xuất hiện trong Entry Assessment.

### AC-07 — Debugging

Được cung cấp một đoạn code có lỗi cú pháp đơn giản và thực hiện được:

1. chạy chương trình;
2. đọc lỗi;
3. xác định dòng lỗi;
4. sửa lỗi;
5. chạy lại thành công.

### AC-08 — Giải thích

Không chỉ chạy được code mà phải giải thích được code mình viết.

---

## 8. Self-Test

Sau khi học xong TASK, thực hiện một bài kiểm tra nhỏ **không xem lời giải trước**.

Cấu trúc:

```text
Phần 1 — Lý thuyết
Phần 2 — Đọc code
Phần 3 — Viết code
Phần 4 — Tìm lỗi
Phần 5 — Giải thích code
```

Self-Test là căn cứ quan trọng để quyết định PASS hay FAIL, không chỉ dựa vào việc chương trình chạy được.

---

## 9. Quy trình thực hiện

Tuân thủ quy trình phát triển/học tập của dự án:

```text
Học
 ↓
Hiểu
 ↓
Tự code
 ↓
Chạy
 ↓
Self-Test
 ↓
Debug
 ↓
Review
 ↓
Documentation
 ↓
Git
 ↓
Progress Update
 ↓
PASS
```

**Chưa đạt Acceptance Criteria → chưa PASS → không chuyển sang TASK tiếp theo.**

---

## 10. Tiến độ

| Hạng mục | Trạng thái |
|---|---|
| Xác định Level 1 gồm 5 Module | PASS |
| Chốt Module 1 — Python Foundation | PASS |
| Chốt tên TASK-01 | PASS |
| Chốt mục tiêu TASK-01 | PASS |
| Chốt phạm vi TASK-01 | PASS |
| Chốt Acceptance Criteria | PASS |
| Tạo tài liệu TASK-01 | PASS |
| Học nội dung TASK-01 | PASS |
| Thực hành | PASS |
| Self-Test | PASS |
| Review | PASS |
| Documentation cuối TASK | PASS |
| Git Commit | PASS |
| Progress Update | PASS |
| **TASK-01** | **PASS** |

---

## 11. Tổng kết học tập

### Điều đã hiểu

- Mã nguồn Python được biên dịch thành bytecode; Python Virtual Machine (PVM) thực thi bytecode. Trong CPython, trình thông dịch được triển khai bằng mã máy chạy trên hệ thống.
- Phép gán liên kết tên biến với giá trị; Python là ngôn ngữ kiểu động và `type()` cho biết kiểu của giá trị tại thời điểm kiểm tra.
- `bool()` xét giá trị truthy/falsy. Chuỗi rỗng là `False`, còn chuỗi `"False"` là `True` vì chuỗi có ký tự.
- Có thể đọc `SyntaxError`, xác định lỗi cú pháp, sửa và chạy lại chương trình.

### Nội dung muốn ôn tiếp

- Thực hành với `list`, `dict`, `tuple` trong các TASK sau.
- Tìm hiểu thêm về tham chiếu và quản lý bộ nhớ khi học các nội dung phù hợp.

### Bài tập và lỗi đáng nhớ

- `bool("False")` giúp phân biệt truthiness của chuỗi với ý nghĩa ngôn ngữ tự nhiên của nội dung chuỗi.
- Sửa lỗi thiếu dấu `)` trong `print()` giúp rèn cách đọc thông báo `SyntaxError`, kiểm tra dòng được báo và các dòng ngay trước đó.

---

## 12. Ghi chú

- Không đánh dấu TASK-01 PASS chỉ vì đã thiết kế xong tài liệu.
- Các mục PASS trong bảng tiến độ chỉ phản ánh những quyết định/chuẩn bị đã hoàn thành trước khi bắt đầu học TASK.
- `while` chưa được đánh giá trong Entry Assessment và không thuộc phạm vi TASK-01.
- Không mở rộng phạm vi sang Module 2 chỉ để làm TASK-01 lớn hơn.
- Ưu tiên **hiểu bản chất → tự viết → kiểm tra → debug → giải thích**.

---

## 13. Trạng thái cuối TASK

**PASS**

TASK-01 chỉ chuyển sang **PASS** sau khi toàn bộ Acceptance Criteria, Self-Test, Review, Documentation, Git Commit và Progress Update đã hoàn thành.
