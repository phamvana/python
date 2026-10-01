# TASK-02 — Expressions & Operators: C to Python
# Dự đoán kết quả và kiểu dữ liệu trước khi chạy.
# Sau đó viết print() để kiểm tra từng biểu thức.

# TODO 1: / với hai số nguyên (Dự đoán: 3.5, float)
res1 = 7 / 2
print("TODO 1 (7 / 2)  :", res1, "| Kiểu:", type(res1))

# TODO 2: // với hai số nguyên dương (Dự đoán: 3, int)
res2 = 7 // 2
print("TODO 2 (7 // 2) :", res2, "| Kiểu:", type(res2))

# TODO 3: // với một số âm (Dự đoán: -4, int - làm tròn xuống phía -\infty)
res3 = -7 // 2
print("TODO 3 (-7 // 2):", res3, "| Kiểu:", type(res3))

# TODO 4: % với một số âm (Dự đoán: 1, int - theo công thức: a - (a // b) * b)
res4 = -7 % 2
print("TODO 4 (-7 % 2) :", res4, "| Kiểu:", type(res4))

# TODO 5: ** để tính lũy thừa (Dự đoán: 8, int - 2 mũ 3)
res5 = 2 ** 3
print("TODO 5 (2 ** 3) :", res5, "| Kiểu:", type(res5))

# TODO 6: ^ để so sánh với phép lũy thừa (Dự đoán: 1, int - đây là phép Bitwise XOR, không phải lũy thừa)
res6 = 2 ^ 3
print("TODO 6 (2 ^ 3)  :", res6, "| Kiểu:", type(res6))

# ==============================================================================
# TOÁN TỬ SO SÁNH VÀ LOGIC (C to Python)
# ==============================================================================

# Biểu thức 1: Kiểm tra score nằm trong khoảng [0, 100] (score = 100)
score = 100
check_score = 0 <= score <= 100  # Hoặc: score >= 0 and score <= 100
print("Logic 1 (0 <= score <= 100)           :", check_score, "| Kiểu:", type(check_score))

# Biểu thức 2: Chuyển age >= 18 && has_permission sang Python (age = 17, has_permission = True)
age = 17
has_permission = True
check_permission = age >= 18 and has_permission
print("Logic 2 (age >= 18 and has_permission):", check_permission, "| Kiểu:", type(check_permission))

# Biểu thức 3: Chuyển !(is_admin || is_blocked) sang Python (is_admin = False, is_blocked = False)
is_admin = False
is_blocked = False
check_access = not (is_admin or is_blocked)
print("Logic 3 (not (is_admin or is_blocked)):", check_access, "| Kiểu:", type(check_access))

# ==============================================================================
# ĐỘ ƯU TIÊN CỦA TOÁN TỬ VÀ DẤU NGOẶC (Operator Precedence)
# ==============================================================================

# Biểu thức A: Không dùng ngoặc (Dự đoán: 14, int)
result_a = 2 + 3 * 4
print("Precedence A (2 + 3 * 4)  :", result_a, "| Kiểu:", type(result_a))

# Biểu thức B: Dùng ngoặc ép ưu tiên (Dự đoán: 20, int)
result_b = (2 + 3) * 4
print("Precedence B ((2 + 3) * 4):", result_b, "| Kiểu:", type(result_b))

# ==============================================================================
# PHÉP GÁN KẾT HỢP (Augmented Assignment Operators)
# ==============================================================================

total = 10
total += 3 * 2  # Tương đương: total = total + (3 * 2) -> total = 10 + 6 = 16
total -= 4      # Tương đương: total = total - 4 -> total = 16 - 4 = 12

print("Augmented Assignment (total):", total, "| Kiểu:", type(total))

# ==============================================================================
# SHORT-CIRCUIT EVALUATION (Đánh giá ngắn mạch)
# ==============================================================================

# Dùng print() để quan sát xem vế phải có được đánh giá hay không.
# Biểu thức 1: False and ... (Dự đoán: False, vế phải BỊ BỎ QUA)
res_sc1 = False and print("--> Vế phải của and đang được đánh giá!")
print("Short-circuit 1 (False and ...):", res_sc1)

# Biểu thức 2: True or ... (Dự đoán: True, vế phải BỊ BỎ QUA)
res_sc2 = True or print("--> Vế phải của or đang được đánh giá!")
print("Short-circuit 2 (True or ...) :", res_sc2)

count = 4
count += 1  # Tương đương với count++ trong C
count += 3  # Tương đương với count = count + 3
print("count:", count, "| Kiểu:", type(count))

# Self-Test Task-02 Verification Script

print("=== 1. Giá trị và kiểu ===")
print("5 / 2  :", 5 / 2, type(5 / 2))
print("-5 // 2:", -5 // 2, type(-5 // 2))
print("-5 % 2 :", -5 % 2, type(-5 % 2))
print("2 ** 3 :", 2 ** 3, type(2 ** 3))
print("2 ^ 3  :", 2 ^ 3, type(2 ^ 3))

print("\n=== 2. C sang Python ===")
x, is_admin, is_blocked, count = 50, False, False, 10
print("Chain logic     :", 0 <= x <= 100)
print("Not Or logic    :", not (is_admin or is_blocked))
count += 1
print("Count increment :", count)

print("\n=== 3. Phép gán kết hợp ===")
total = 8
total += 2 * 3
total -= 5
print("Total value     :", total, type(total))

print("\n=== 4. Short-circuit ===")
print("False and print('A') -> Kết quả:", False and print("A"))
print("True or print('B')   -> Kết quả:", True or print("B"))

print("\n=== 5. So sánh liên hoàn ===")
for score in [0, 100, 101]:
    print(f"score = {score:3d} -> 0 <= score <= 100 là {0 <= score <= 100}")