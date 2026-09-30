# Python Task Management

## 1. Mục đích

Tài liệu này quy định cách tạo, thực hiện, kiểm tra và quản lý TASK trong quá trình học Python.

Mục tiêu của TASK là chia quá trình học thành những đơn vị nhỏ, rõ ràng và có thể kiểm tra được.

Mỗi TASK phải giúp người học trả lời được:

- Tôi đang học gì?
- Tôi cần làm gì?
- Khi nào được xem là hoàn thành?
- Tôi đã hiểu nội dung chưa?
- Tôi cần cải thiện điều gì?

---

## 2. TASK là gì?

TASK là một đơn vị học tập có:

- mục tiêu rõ ràng;
- phạm vi xác định;
- kiến thức cần sử dụng;
- yêu cầu thực hiện;
- Acceptance Criteria;
- trạng thái;
- kết quả review.

Một TASK không nhất thiết tương ứng với một bài học.

Một TASK có thể bao gồm:

- một khái niệm;
- một nhóm khái niệm liên quan;
- một nhóm bài tập;
- một kỹ năng;
- một phần nhỏ của Mini Project.

---

## 3. Nguyên tắc thiết kế TASK

### 3.1. Một TASK có mục tiêu chính

Mỗi TASK nên tập trung vào một mục tiêu học tập chính.

Ví dụ:

```text
TASK-01
Mục tiêu:
Hiểu và sử dụng biến trong Python.
```

Không nên đưa quá nhiều kiến thức mới không liên quan vào cùng một TASK.

---

### 3.2. TASK phải có phạm vi rõ ràng

Mỗi TASK phải xác định:

- làm gì;
- không làm gì;
- kiến thức nào thuộc phạm vi;
- kiến thức nào chưa thuộc phạm vi.

Điều này giúp tránh scope creep.

---

### 3.3. TASK phải có tiêu chí hoàn thành

Mỗi TASK phải có Acceptance Criteria.

Acceptance Criteria phải có khả năng kiểm tra được.

Ví dụ:

```text
Acceptance Criteria:

- Giải thích được biến là gì.
- Tạo và sử dụng được biến.
- Sử dụng được biến trong biểu thức.
- Viết được bài tập nhỏ sử dụng biến.
- Tự kiểm tra chương trình.
```

Không sử dụng các tiêu chí quá chung như:

```text
- Hiểu Python.
- Biết lập trình.
- Thành thạo biến.
```

---

## 4. Cấu trúc một TASK

Một TASK nên có cấu trúc:

```text
# TASK-XX — Tên TASK

## 1. Thông tin TASK

- Tên
- Level
- Module
- Trạng thái
- Ngày bắt đầu
- Ngày hoàn thành
- TASK trước
- TASK sau

## 2. Mục tiêu

TASK này nhằm đạt được điều gì?

## 3. Phạm vi

### In Scope

Những nội dung thuộc TASK.

### Out of Scope

Những nội dung chưa thuộc TASK.

## 4. Kiến thức cần có

Prerequisite cần thiết trước khi thực hiện.

## 5. Nội dung thực hiện

Các nội dung cần học và thực hành.

## 6. Bài tập

Danh sách bài tập.

## 7. Acceptance Criteria

Tiêu chí để PASS.

## 8. Self-Test

Cách tự kiểm tra.

## 9. Review

Kết quả review.

## 10. Documentation

Tài liệu cần cập nhật.

## 11. Git

Commit liên quan.

## 12. Progress Update

Cập nhật tiến độ.

## 13. Kết quả

PASS / FAIL / BLOCKED
```

Không bắt buộc mọi TASK phải có đầy đủ mọi mục nếu nội dung TASK không cần.

Tuy nhiên, các mục quan trọng như **Mục tiêu, Phạm vi, Acceptance Criteria và Kết quả** nên luôn có.

---

## 5. Trạng thái TASK

Repository sử dụng 5 trạng thái chính:

```text
TODO
IN PROGRESS
BLOCKED
FAIL
PASS
```

### TODO

TASK đã được xác định nhưng chưa bắt đầu.

### IN PROGRESS

TASK đang được thực hiện.

### BLOCKED

TASK không thể tiếp tục do thiếu điều kiện cần thiết.

Phải ghi rõ nguyên nhân và hướng xử lý.

### FAIL

TASK đã được kiểm tra nhưng chưa đạt Acceptance Criteria.

FAIL không phải là thất bại của quá trình học.

FAIL là trạng thái phản ánh kết quả kiểm tra tại thời điểm đó.

### PASS

TASK đã hoàn thành Acceptance Criteria và vượt qua review.

---

## 6. Quy trình thực hiện TASK

Mỗi TASK thực hiện theo quy trình:

```text
TODO
  ↓
IN PROGRESS
  ↓
Requirement
  ↓
Understand
  ↓
Plan
  ↓
Implement
  ↓
Self-Test
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

Nếu không đạt:

```text
Review
  ↓
FAIL
  ↓
Phân tích nguyên nhân
  ↓
Sửa / học lại / bổ sung bài tập
  ↓
Self-Test
  ↓
Review
  ↓
PASS
```

Nếu không thể tiếp tục:

```text
IN PROGRESS
  ↓
BLOCKED
  ↓
Xử lý nguyên nhân
  ↓
IN PROGRESS
```

---

## 7. Acceptance Criteria

Acceptance Criteria là điều kiện bắt buộc để TASK được PASS.

Một TASK không được PASS chỉ vì:

- code chạy;
- không có syntax error;
- AI nói code đúng;
- đã dành nhiều thời gian;
- đã hoàn thành tất cả bài tập nhưng chưa hiểu.

Acceptance Criteria phải đánh giá cả:

### Knowledge

Người học có hiểu kiến thức không?

### Practice

Người học có tự thực hành được không?

### Code

Code có đáp ứng yêu cầu không?

### Test

Code đã được kiểm tra phù hợp chưa?

### Explanation

Người học có giải thích được cách hoạt động không?

---

## 8. Self-Test

Mỗi TASK phải có hình thức tự kiểm tra phù hợp.

Ví dụ:

### Với kiến thức

- tự giải thích bằng lời;
- trả lời câu hỏi;
- viết lại khái niệm.

### Với code

- chạy chương trình;
- thử nhiều input;
- thử trường hợp biên;
- kiểm tra output.

### Với bài toán

- giải lại bài;
- thay đổi input;
- kiểm tra trường hợp đặc biệt.

Mục tiêu của Self-Test là xác nhận rằng người học thực sự hiểu nội dung.

---

## 9. Review

Review được thực hiện sau Self-Test.

Review có thể kiểm tra:

- yêu cầu đã hoàn thành chưa;
- code có đúng không;
- code có dễ đọc không;
- logic có hợp lý không;
- người học có hiểu code không;
- có kiến thức nào chưa vững không;
- có scope creep không.

Review có thể do:

- người học tự review;
- AI/Mentor review;
- kết hợp cả hai.

AI/Mentor không thay thế Acceptance Criteria.

---

## 10. TASK FAIL

Khi TASK FAIL phải ghi nhận:

- nguyên nhân;
- tiêu chí chưa đạt;
- lỗi gặp phải;
- kiến thức chưa vững;
- hành động khắc phục.

Ví dụ:

```text
Status: FAIL

Reason:
Chưa hiểu rõ cách sử dụng vòng lặp while.

Missing Criteria:
Chưa xử lý được điều kiện kết thúc vòng lặp.

Action:
Học lại while và thực hiện thêm bài tập.
```

Sau khi khắc phục, TASK được kiểm tra lại.

Không xóa lịch sử FAIL.

---

## 11. TASK BLOCKED

BLOCKED được sử dụng khi TASK không thể tiếp tục vì lý do chưa thể xử lý ngay.

Ví dụ:

```text
Status: BLOCKED

Reason:
Môi trường Python chưa được cài đặt đúng.

Required Action:
Kiểm tra Python installation và PATH.
```

BLOCKED phải có hành động tiếp theo.

Không sử dụng BLOCKED thay cho việc chưa làm TASK.

---

## 12. TASK PASS

TASK chỉ được PASS khi:

- mục tiêu đã đạt;
- phạm vi đã hoàn thành;
- Acceptance Criteria đã đạt;
- Self-Test đã thực hiện;
- Review đã hoàn thành;
- documentation cần thiết đã cập nhật;
- Git đã được xử lý theo quy trình;
- Progress Update đã được cập nhật.

PASS là kết quả của quá trình kiểm tra, không phải chỉ là trạng thái do người học tự đặt.

---

## 13. TASK phụ

Có thể tạo TASK phụ khi:

- kiến thức của TASK chính chưa đủ;
- xuất hiện lỗ hổng kiến thức;
- cần luyện tập thêm;
- một phần nội dung lớn hơn dự kiến.

Ví dụ:

```text
TASK-05
    ├── TASK-05.1
    ├── TASK-05.2
    └── TASK-05.3
```

TASK phụ phải có mục tiêu và phạm vi rõ ràng.

Không tạo TASK phụ chỉ để tăng số lượng TASK.

---

## 14. Khi TASK quá lớn

Nếu một TASK trở nên quá lớn:

```text
TASK lớn
    ↓
Phân tích
    ↓
Chia thành các TASK nhỏ
```

Dấu hiệu TASK quá lớn:

- có quá nhiều mục tiêu;
- Acceptance Criteria quá dài;
- thời gian thực hiện vượt quá dự kiến;
- xuất hiện nhiều kiến thức mới không liên quan;
- khó xác định trạng thái hoàn thành.

---

## 15. Khi TASK quá nhỏ

Không cần tạo TASK riêng cho mọi thao tác rất nhỏ.

Ví dụ không nhất thiết tạo:

```text
TASK — print()
TASK — input()
TASK — int()
```

nếu các nội dung này có thể học hợp lý trong cùng một TASK về Input/Output.

TASK phải phản ánh **đơn vị học tập có ý nghĩa**, không phải số lượng thao tác.

---

## 16. TASK và Level

Quan hệ:

```text
Level
  ↓
Module
  ↓
TASK
  ↓
Bài tập
  ↓
Self-Test
  ↓
Review
```

TASK là đơn vị thực thi chính.

Level là đơn vị quản lý kiến thức lớn hơn.

Module là nhóm các kiến thức liên quan.

---

## 17. TASK và Mini Project

Mini Project được thực hiện sau khi đã hoàn thành các TASK cần thiết.

Quan hệ:

```text
Kiến thức
  ↓
TASK
  ↓
TASK
  ↓
TASK
  ↓
Mini Project
```

Mini Project dùng để kiểm tra khả năng kết hợp kiến thức.

Không dùng Mini Project để thay thế toàn bộ TASK nền tảng.

---

## 18. Điều chỉnh TASK

Trong quá trình học có thể:

- thêm TASK;
- chia TASK;
- gộp TASK;
- thay đổi Acceptance Criteria;
- thêm bài tập;
- điều chỉnh phạm vi.

Mọi thay đổi quan trọng phải phản ánh trong documentation.

Không giữ TASK cứng nhắc nếu thực tế học tập cho thấy cần điều chỉnh.

---

## 19. Quy tắc đặt tên TASK

Tên TASK phải ngắn gọn và mô tả đúng nội dung.

Ví dụ:

```text
TASK-01 — Python Environment
TASK-02 — Variables
TASK-03 — Data Types
TASK-04 — Input and Output
TASK-05 — Operators
```

Tên TASK không nên chứa những thông tin không cần thiết.

---

## 20. Quy tắc đánh số TASK

TASK được đánh số theo Level/Module hoặc theo hệ thống được thống nhất trong roadmap.

Không thay đổi số TASK đã hoàn thành chỉ để sắp xếp lại đẹp hơn.

Nếu cần thay đổi cấu trúc, phải giữ lại lịch sử thay đổi trong documentation/Git.

---

## 21. Không sử dụng tiến độ phần trăm

Không sử dụng:

```text
Python Level 1: 70%
```

để đánh giá tiến độ học tập.

Thay vào đó theo dõi:

```text
Level
  ↓
Module
  ↓
TASK
  ↓
Mini Project
```

và trạng thái:

```text
TODO
IN PROGRESS
BLOCKED
FAIL
PASS
```

Điều này phản ánh tiến độ thực tế rõ hơn phần trăm.

---

## 22. Tiêu chuẩn TASK tốt

Một TASK tốt phải:

- có mục tiêu rõ;
- có phạm vi rõ;
- có Acceptance Criteria;
- có cách Self-Test;
- có thể review;
- phù hợp trình độ hiện tại;
- không quá lớn;
- không quá nhỏ;
- có giá trị học tập;
- có thể ghi nhận kết quả.

---

## 23. Mẫu TASK tối thiểu

Khi tạo TASK mới, có thể sử dụng mẫu:

```markdown
# TASK-XX — Tên TASK

## 1. Thông tin TASK

- **Level:** Level X
- **Module:** Tên Module
- **Trạng thái:** TODO
- **Ngày bắt đầu:** YYYY-MM-DD
- **Ngày hoàn thành:** -
- **TASK trước:** -
- **TASK sau:** -

## 2. Mục tiêu

Mục tiêu chính của TASK.

## 3. Phạm vi

### In Scope

- Nội dung 1
- Nội dung 2

### Out of Scope

- Nội dung chưa học

## 4. Kiến thức cần có

- Prerequisite 1
- Prerequisite 2

## 5. Nội dung thực hiện

- Nội dung 1
- Nội dung 2

## 6. Bài tập

- Bài tập 1
- Bài tập 2

## 7. Acceptance Criteria

- [ ] Tiêu chí 1
- [ ] Tiêu chí 2
- [ ] Tiêu chí 3

## 8. Self-Test

Mô tả cách tự kiểm tra.

## 9. Review

Kết quả review.

## 10. Documentation

Tài liệu cần cập nhật.

## 11. Git

Commit liên quan.

## 12. Progress Update

Cập nhật tiến độ.

## 13. Kết quả

**PASS / FAIL / BLOCKED**
```

---

## 24. Nguyên tắc cuối cùng

TASK không phải là danh sách việc cần làm để hoàn thành cho nhanh.

TASK là đơn vị giúp biến:

```text
Kiến thức
   ↓
Thực hành
   ↓
Kiểm tra
   ↓
Review
   ↓
Năng lực
```

Mục tiêu cuối cùng là **học được và sử dụng được Python**, không phải hoàn thành thật nhiều TASK.
