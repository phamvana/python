# TASK-02 — Expressions & Operators: C to Python

## 1. Thông tin TASK

- **Tên:** Expressions & Operators — C to Python
- **Level:** Level 1 — Python Basic
- **Module:** Module 2 — Expressions & Operators
- **Trạng thái:** IN PROGRESS
- **Ngày bắt đầu:** 2026-10-01
- **TASK trước:** TASK-01 — Python Foundation
- **TASK sau:** Dự kiến TASK-03 — Conditions
- **Tài liệu tham khảo chính:** Python expressions and operators

---

## 2. Bối cảnh

Người học đã có bằng kỹ sư Công nghệ thông tin và từng học Lập trình căn bản bằng C. Entry Assessment cho thấy đã có nền tảng về toán tử số học, so sánh, logic và biểu thức.

TASK-01 đã củng cố biến, kiểu dữ liệu, phép gán, type(), ép kiểu cơ bản và cú pháp Python. Vì vậy TASK-02 không dạy lại toán tử từ đầu. TASK tập trung vào cách áp dụng kiến thức đã có và những khác biệt dễ nhầm khi chuyển từ C sang Python.

---

## 3. Mục tiêu

Viết, đọc và kiểm tra biểu thức Python chính xác; giải thích được các điểm khác biệt quan trọng giữa cách viết biểu thức trong C và Python.

Sau TASK-02, người học có thể:

1. Tính và dự đoán kiểu kết quả của biểu thức số học Python.
2. Phân biệt /, //, %, **.
3. Chuyển biểu thức dùng toán tử logic từ C sang Python.
4. Hiểu phép so sánh liên hoàn trong Python.
5. Dùng ngoặc để thể hiện rõ thứ tự thực hiện.
6. Tự kiểm tra biểu thức bằng các giá trị thường gặp và trường hợp biên.

---

## 4. Kiến thức cần có

- Hoàn thành TASK-01 — Python Foundation.
- Biết biến, kiểu int, float, bool và phép gán.
- Đã học toán tử căn bản trong C.

---

## 5. Phạm vi

### 5.1. In scope

- Toán tử số học: +, -, *, /, //, %, **.
- Thứ tự ưu tiên và cách dùng ngoặc trong biểu thức.
- Toán tử so sánh: ==, !=, <, <=, >, >=.
- So sánh liên hoàn, ví dụ 0 <= score <= 100.
- Toán tử logic and, or, not và short-circuit ở mức cơ bản.
- Phép gán kết hợp thường dùng như += và -=.
- Khác biệt giữa biểu thức Python và cách viết tương ứng trong C.
- Tự dự đoán kết quả, sau đó chạy code để kiểm tra.

### 5.2. Khác biệt C–Python cần nắm

| Ý định | C | Python | Điểm cần chú ý |
|---|---|---|---|
| Chia | / | / | Chia / trong Python trả về kết quả dạng số thực, kể cả khi hai toán hạng là int. |
| Chia lấy phần nguyên | Tùy kiểu toán hạng với / | // | // làm tròn xuống; ví dụ -7 // 2 == -4. |
| Phần dư với số âm | Phần dư theo phép chia lấy phần nguyên của C | % | Quy tắc số âm khác nhau; trong Python -7 % 2 == 1, còn trong C -7 % 2 == -1. |
| Lũy thừa | pow() hoặc thư viện | ** | ^ trong Python là XOR theo bit, không phải lũy thừa. |
| Logic AND/OR/NOT | &&, \|\|, ! | and, or, not | Python dùng từ khóa; && và \|\| không phải cú pháp toán tử logic Python. |
| Tăng một đơn vị | ++ | += 1 | Python không có toán tử ++/--. |
| So sánh khoảng | Ghép hai phép so sánh bằng && | low <= value <= high | Python hỗ trợ so sánh liên hoàn. |

Không cần học lại cú pháp C; bảng chỉ dùng để đối chiếu các điểm chuyển ngữ.

### 5.3. Out of scope

- Câu lệnh if, elif, else và điều kiện lồng nhau.
- for, while, break, continue.
- input() và xử lý dữ liệu người dùng.
- Toán tử bitwise và biểu diễn nhị phân.
- Thứ tự ưu tiên đầy đủ của mọi toán tử Python.
- Boolean operator trả về toán hạng và các cách dùng nâng cao.

---

## 6. Bài tập

1. **Dự đoán trước khi chạy:** xác định giá trị và kiểu của các biểu thức có /, //, %, **.
2. **Chuyển từ C sang Python:** viết lại các biểu thức có &&, ||, !, ++ và phép lũy thừa; giải thích từng thay đổi.
3. **So sánh liên hoàn:** viết biểu thức kiểm tra một giá trị nằm trong khoảng, không dùng if.
4. **Thứ tự thực hiện:** dự đoán kết quả của một biểu thức, rồi thêm ngoặc để làm rõ ý định.
5. **Trường hợp biên:** kiểm tra số âm, chia hết/không chia hết, và biểu thức so sánh ở đúng ranh giới.

Người học tự viết và chạy từng đoạn nhỏ; không dùng lời giải có sẵn trước khi tự dự đoán kết quả.

---

## 7. Acceptance Criteria

TASK-02 chỉ được **PASS** khi đạt tất cả tiêu chí:

### AC-01 — Toán tử và kiểu kết quả

Giải thích và dự đoán đúng giá trị, kiểu kết quả của các biểu thức dùng +, -, *, /, //, %, ** ở các ví dụ phù hợp.

### AC-02 — Chia và số âm

Phân biệt đúng / với //; giải thích được kết quả -7 // 2 và kiểm tra phép % tương ứng bằng chương trình.

### AC-03 — Chuyển từ C sang Python

Chuyển đúng các biểu thức mẫu dùng &&, ||, !, ++ và toán tử lũy thừa; giải thích được vì sao ^ không dùng để lũy thừa trong Python.

### AC-04 — So sánh và logic

Viết biểu thức dùng toán tử so sánh và and/or/not, bao gồm một phép so sánh liên hoàn.

### AC-05 — Thứ tự ưu tiên

Dự đoán kết quả biểu thức và dùng ngoặc khi cần để code thể hiện rõ thứ tự tính toán mong muốn.

### AC-06 — Tự kiểm tra

Chạy các ví dụ do mình viết, kiểm tra giá trị lẫn kiểu kết quả và thử ít nhất một trường hợp biên.

### AC-07 — Giải thích

Giải thích được các biểu thức mình viết và lý do chọn toán tử Python tương ứng.

---

## 8. Self-Test

Thực hiện không xem lời giải trước, gồm:

1. Giải thích sự khác nhau giữa /, // và **.
2. Đọc biểu thức và dự đoán giá trị cùng kiểu kết quả.
3. Chuyển một nhóm biểu thức C sang Python.
4. Viết phép so sánh liên hoàn và biểu thức logic tương ứng.
5. Tìm và sửa các phép chuyển ngữ sai như dùng ^ để lũy thừa hoặc && làm AND.
6. Nêu kết quả kiểm tra cho ít nhất một trường hợp có số âm.

---

## 9. Tổng kết học tập

### Nội dung đã nắm

- Với số nguyên trong Python 3, phép chia / cho kết quả float; // làm tròn xuống.
- Với số âm, quy tắc // và % của Python khác phép chia số nguyên và phép dư của C. Cắt về 0 trong phép chia int của C; Python dùng floor division.
- Dùng ** để lũy thừa; ^ là XOR theo bit. Python dùng and, or, not thay cho &&, ||, !; không có ++.
- Python hỗ trợ phép so sánh liên hoàn. Ngoặc đơn nhóm biểu thức để điều khiển phần được tính trước.
- Phép gán kết hợp như += và -= cập nhật giá trị biến; and/or có thể bỏ qua vế phải do short-circuit.
- Cần diễn đạt phép chia số nguyên C chính xác: -5 / 2 cho -2 trực tiếp, không tạo -2.5 ở bước trung gian.

### Kết quả Acceptance Criteria

| Tiêu chí | Kết quả |
|---|---|
| AC-01 — Toán tử và kiểu kết quả | PASS |
| AC-02 — Chia và số âm | PASS |
| AC-03 — Chuyển từ C sang Python | PASS |
| AC-04 — So sánh và logic | PASS |
| AC-05 — Thứ tự ưu tiên | PASS |
| AC-06 — Tự kiểm tra | PASS |
| AC-07 — Giải thích | PASS |

### Self-Test và mã thực hành

- Self-Test đạt đủ các phần dự đoán kết quả/kiểu, chuyển biểu thức C sang Python, phép gán kết hợp, short-circuit, so sánh liên hoàn và giải thích khác biệt chia số âm.
- File thực hành: practice/level-1/module-02-expressions-operators/task_02_expressions.py.
- Các biểu thức thực hành và output đã được chạy, review trong môi trường Python 3.

---

## 10. Tiến độ

| Hạng mục | Trạng thái |
|---|---|
| Xác định mục tiêu và phạm vi | PASS |
| Đối chiếu nền tảng C và Entry Assessment | PASS |
| Học nội dung TASK-02 | PASS |
| Thực hành | PASS |
| Self-Test | PASS |
| Review | PASS |
| Documentation cuối TASK | PASS |
| Git Commit | TODO |
| Progress Update | PASS |
| **TASK-02** | **IN PROGRESS** |

---

## 11. Kết quả

**IN PROGRESS**

Chỉ chuyển sang **PASS** sau khi hoàn thành Acceptance Criteria, Self-Test, Review, documentation, Git và Progress Update.
