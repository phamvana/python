# Python Learning Progress

## 1. Mục đích

Tài liệu này dùng để theo dõi tiến độ học Python trong repository.

Progress không chỉ ghi nhận việc đã hoàn thành bao nhiêu TASK mà còn phản ánh:

- kiến thức đã học;
- TASK đã hoàn thành;
- TASK đang thực hiện;
- TASK bị FAIL hoặc BLOCKED;
- Mini Project;
- điểm còn yếu;
- những nội dung cần ôn tập;
- các mốc quan trọng trong quá trình học.

---

## 2. Nguyên tắc theo dõi tiến độ

Tiến độ được quản lý theo:

```text
Level
  ↓
Module
  ↓
TASK
  ↓
Mini Project
  ↓
Project
```

Không sử dụng phần trăm tổng thể để đánh giá quá trình học.

Ví dụ không sử dụng:

```text
Python: 65%
Level 1: 80%
```

Thay vào đó sử dụng trạng thái cụ thể của từng đơn vị học tập.

---

## 3. Trạng thái

Repository sử dụng các trạng thái:

```text
TODO
IN PROGRESS
BLOCKED
FAIL
PASS
```

### TODO

Đã xác định nhưng chưa bắt đầu.

### IN PROGRESS

Đang thực hiện.

### BLOCKED

Không thể tiếp tục do thiếu điều kiện cần thiết.

### FAIL

Đã kiểm tra nhưng chưa đạt yêu cầu.

### PASS

Đã hoàn thành Acceptance Criteria và review.

---

## 4. Cấu trúc tiến độ

Tiến độ được tổ chức theo các Level:

```text
Phase 0 — Learning Foundation
Level 1 — Python Basic
Level 2 — Control Flow & Function
Level 3 — String & Collections
Level 4 — Modules & Classes
Level 5 — OOP & Exception
Level 6 — File & Testing
```

Roadmap có thể được điều chỉnh khi quá trình học thực tế cho thấy cần thiết.

---

# 5. Phase 0 — Learning Foundation

**Trạng thái:** PASS

## Mục tiêu

Thiết lập nền tảng cho repository học Python:

- roadmap;
- learning rules;
- task management;
- progress tracking;
- Git workflow;
- cấu trúc thư mục học tập.

## Documents

| Document                | Trạng thái |
| ----------------------- | ---------- |
| `01-python-roadmap.md`  | PASS       |
| `02-learning-rules.md`  | PASS       |
| `03-task-management.md` | PASS       |
| `04-progress.md`        | PASS       |

## Acceptance Criteria

- [x] Hoàn thành bộ tài liệu Phase 0.
- [x] Kiểm tra cấu trúc repository.
- [x] Kiểm tra Git status.
- [x] Commit Phase 0.
- [x] Push lên GitHub.
- [x] Xác nhận repository sạch sau commit.

---

# 6. Level 1 — Python Basic

**Trạng thái:** IN PROGRESS

## Mục tiêu

Xây dựng nền tảng Python cơ bản.

## Nội dung dự kiến

- Python environment;
- `print()`;
- comments;
- variables;
- data types;
- `int`;
- `float`;
- `str`;
- `bool`;
- arithmetic operators;
- comparison operators;
- logical operators;
- input/output;
- type casting;
- expressions;
- `if`;
- `elif`;
- `else`;
- nested conditions;
- `for`;
- `while`;
- `range()`;
- accumulator;
- các bài toán cơ bản.

## Mini Project

**Python Basic Practice**

## Trạng thái TASK

| TASK | Trạng thái | Ghi chú |
|---|---|---|
| TASK-01 — Python Foundation | IN PROGRESS | Học, thực hành, Self-Test, Review và documentation hoàn thành; Git commit còn lại. |

---

# 7. Level 2 — Control Flow & Function

**Trạng thái:** TODO

## Mục tiêu

Hiểu sâu hơn về điều khiển chương trình và xây dựng hàm.

## Nội dung dự kiến

- `for`;
- `while`;
- `break`;
- `continue`;
- `pass`;
- nested loop;
- function;
- parameters;
- arguments;
- `return`;
- scope;
- default arguments;
- keyword arguments;
- docstring;
- phân rã bài toán.

## Mini Project

**Console Utility**

## Trạng thái TASK

Chưa tạo TASK.

---

# 8. Level 3 — String & Collections

**Trạng thái:** TODO

## Mục tiêu

Làm việc hiệu quả với dữ liệu dạng chuỗi và collections.

## Nội dung dự kiến

- string;
- string methods;
- indexing;
- slicing;
- list;
- tuple;
- set;
- dictionary;
- collection methods;
- nested collections;
- comprehensions;
- xử lý dữ liệu cơ bản.

## Mini Project

**Data Processing Practice**

## Trạng thái TASK

Chưa tạo TASK.

---

# 9. Level 4 — Modules & Classes

**Trạng thái:** TODO

## Mục tiêu

Biết tổ chức code thành module và bắt đầu làm việc với class/object.

## Nội dung dự kiến

- module;
- `import`;
- package;
- `__name__`;
- `__main__`;
- standard library;
- project organization;
- class;
- object;
- attribute;
- method;
- `__init__`;
- instance.

## Mini Project

**Modular Python Application**

## Trạng thái TASK

Chưa tạo TASK.

---

# 10. Level 5 — OOP & Exception

**Trạng thái:** TODO

## Mục tiêu

Hiểu và áp dụng lập trình hướng đối tượng cùng xử lý ngoại lệ.

## Nội dung dự kiến

### OOP

- encapsulation;
- inheritance;
- polymorphism;
- abstraction;
- composition;
- `classmethod`;
- `staticmethod`;
- property;
- special methods.

### Exception

- `try`;
- `except`;
- `else`;
- `finally`;
- `raise`;
- custom exceptions;
- defensive programming.

## Mini Project

**OOP Management Application**

## Trạng thái TASK

Chưa tạo TASK.

---

# 11. Level 6 — File & Testing

**Trạng thái:** TODO

## Mục tiêu

Làm việc với file và xây dựng tư duy kiểm thử.

## Nội dung dự kiến

### File

- đọc file;
- ghi file;
- text file;
- CSV;
- JSON;
- path;
- directory;
- `pathlib`.

### Testing

- testing mindset;
- test case;
- unit test;
- `unittest`;
- `pytest`;
- assertion;
- test exception;
- tổ chức test.

## Mini Project

**File-based Python Application**

## Trạng thái TASK

Chưa tạo TASK.

---

# 12. Mini Project

Mini Project được sử dụng để kiểm tra khả năng kết hợp kiến thức sau một nhóm TASK.

Danh sách Mini Project:

| Level   | Mini Project                  | Trạng thái |
| ------- | ----------------------------- | ---------- |
| Level 1 | Python Basic Practice         | TODO       |
| Level 2 | Console Utility               | TODO       |
| Level 3 | Data Processing Practice      | TODO       |
| Level 4 | Modular Python Application    | TODO       |
| Level 5 | OOP Management Application    | TODO       |
| Level 6 | File-based Python Application | TODO       |

Danh sách này có thể được điều chỉnh trong quá trình học.

---

# 13. Điểm yếu cần ôn tập

Phần này ghi nhận những kiến thức chưa vững.

| Nội dung | Mức độ | Hành động | Trạng thái |
| -------- | ------ | --------- | ---------- |
| Chưa có  | -      | -         | -          |

Khi phát hiện lỗ hổng kiến thức, bổ sung vào bảng này.

---

# 14. Lịch sử FAIL

FAIL không bị xóa khỏi quá trình học.

Mục đích là lưu lại:

- TASK nào chưa đạt;
- nguyên nhân;
- kiến thức còn thiếu;
- cách khắc phục;
- kết quả kiểm tra lại.

| TASK    | Ngày | Nguyên nhân | Hành động | Kết quả |
| ------- | ---- | ----------- | --------- | ------- |
| Chưa có | -    | -           | -         | -       |

---

# 15. Lịch sử BLOCKED

BLOCKED được ghi lại để biết những vấn đề từng ngăn cản quá trình học.

| TASK    | Ngày | Nguyên nhân | Cách xử lý | Kết quả |
| ------- | ---- | ----------- | ---------- | ------- |
| Chưa có | -    | -           | -          | -       |

---

# 16. Learning Milestones

Milestone là những mốc quan trọng trong quá trình học.

| Ngày       | Milestone                                  | Trạng thái |
| ---------- | ------------------------------------------ | ---------- |
| 2026-09-30 | Thiết lập hệ thống quản lý việc học Python | PASS       |

Các milestone có thể bao gồm:

- hoàn thành Phase 0;
- hoàn thành Level;
- hoàn thành Mini Project;
- hoàn thành Project;
- nắm vững một kỹ năng quan trọng.

---

# 17. Progress Update Log

### 2026-10-01

**Đã hoàn thành**

- Bắt đầu TASK-01 — Python Foundation.
- Hoàn thành học và thực hành biến, kiểu dữ liệu, type(), ép kiểu, cú pháp và debugging.
- Self-Test đạt cả 5 phần; AC-01 đến AC-08 đã được review trong buổi học.

**Đang thực hiện**

- Git commit cho các thay đổi của TASK-01.

**Vấn đề**

- Không có.

**Điều đã học**

- Bytecode là mã lệnh trung gian; PVM thực thi bytecode.
- Kiểu dữ liệu gắn với giá trị; type() dùng để kiểm tra kiểu.
- bool() xét giá trị truthy/falsy; chuỗi "False" không rỗng nên là True.
- Cách đọc SyntaxError, tìm lỗi cú pháp, sửa và chạy lại.

**Điều cần cải thiện**

- Tiếp tục thực hành tự viết và chạy chương trình trong repository để củng cố độ chính xác cú pháp.

**Bước tiếp theo**

- Kiểm tra diff và commit các thay đổi của TASK-01.

Mỗi mốc quan trọng có thể ghi lại một Progress Update.

Mẫu:

```markdown
### YYYY-MM-DD

**Đã hoàn thành**

- Nội dung 1
- Nội dung 2

**Đang thực hiện**

- Nội dung

**Vấn đề**

- Vấn đề gặp phải

**Điều đã học**

- Kiến thức mới

**Điều cần cải thiện**

- Nội dung cần ôn tập

**Bước tiếp theo**

- TASK tiếp theo
```

Không cần ghi Progress Update cho mọi thao tác nhỏ.

Chỉ ghi khi có thay đổi có ý nghĩa trong quá trình học.

---

# 18. Quy tắc cập nhật Progress

Progress phải được cập nhật khi:

- hoàn thành TASK;
- TASK chuyển FAIL;
- TASK chuyển BLOCKED;
- TASK chuyển PASS;
- hoàn thành Mini Project;
- hoàn thành Level;
- phát hiện lỗ hổng kiến thức quan trọng;
- thay đổi roadmap đáng kể;
- đạt một Learning Milestone.

---

# 19. Khi Roadmap thay đổi

Roadmap không phải một kế hoạch bất biến.

Có thể:

- thêm Level;
- thêm Module;
- thêm TASK;
- chia TASK;
- gộp TASK;
- thay đổi Mini Project;
- bổ sung kiến thức;
- thay đổi thứ tự học.

Khi thay đổi quan trọng, phải cập nhật documentation liên quan.

Progress phải phản ánh cấu trúc mới.

---

# 20. Tiêu chuẩn hoàn thành Level

Một Level được đánh dấu hoàn thành khi:

- các kiến thức chính đã được học;
- TASK cần thiết đã PASS;
- Self-Test đạt yêu cầu;
- người học giải thích được kiến thức;
- có khả năng áp dụng vào bài tập;
- Mini Project hoàn thành;
- các điểm yếu quan trọng đã được xác định;
- documentation được cập nhật.

Không hoàn thành Level chỉ dựa trên số lượng TASK.

---

# 21. Tiêu chuẩn hoàn thành Phase

Một Phase được xem là hoàn thành khi:

- mục tiêu Phase đã đạt;
- các tài liệu cần thiết đã hoàn thành;
- các TASK thuộc Phase đã đạt;
- Acceptance Criteria đã đạt;
- documentation được cập nhật;
- Git history phản ánh đúng quá trình;
- repository ở trạng thái sạch.

---

# 22. Nguyên tắc cuối cùng

Progress không phải bảng thành tích.

Progress là lịch sử học tập.

Mục tiêu của tài liệu này là giúp trả lời:

> Tôi đã học gì?

> Tôi đang ở đâu?

> Tôi đã thực sự hiểu chưa?

> Tôi còn yếu ở đâu?

> Bước tiếp theo là gì?

Quá trình học được ưu tiên theo:

```text
Hiểu
  ↓
Thực hành
  ↓
Kiểm tra
  ↓
Review
  ↓
PASS
  ↓
Áp dụng
  ↓
Xây dựng sản phẩm
```

Mục tiêu cuối cùng là xây dựng **năng lực sử dụng Python**, không phải chỉ tạo ra một bảng tiến độ đẹp.
