# Q. XOR (5 điểm)

## 📖 Problem

Hôm nay Tấn và Tân mới được học phép tính mới trong hệ nhị phân là phép XOR. Nhắc lại, kết quả phép xor giữa
$2$
bit giống nhau sẽ là
$0$
và khác nhau sẽ ra
$1$
. Cụ thể hơn
$0$
XOR
$0$
=
$0$
,
$1$
XOR
$1$
=
$0$
, còn lại ra
$1$
.
Tấn và Tân đã sáng tạo ra một trò chơi mới dựa trên phép xor, đầu tiên Tấn ghi
$n$
số nguyên
$ai$
. Sau đó Tân ghi
$m$
số nguyên
$bi$
. Nhiệm vụ của Tân là với mỗi số nguyên
$bi$
tân phải in ra
$aj$
là kết quả làm cho
$bi$
XOR
$aj$
lớn nhất. Các bạn hãy giúp Tân.


## 🧩 Input

Input
Dòng đầu gồm số nguyên
$n$
$(1 ≤n≤ 105)$
Dòng tiếp theo gồm
$n$
số
$ai$
$(0 ≤ai≤ 109)$
Dòng tiếp gồm số nguyên
$m$
$(1 ≤m≤ 105)$
Dòng tiếp theo gồm
$n$
số
$bi$
$(0 ≤bi≤ 109)$
Dữ liệu đảm bảo các giá trị của
$ai$
riêng biệt


## 💡 Output

Output
Gồm một dòng chứa
$m$
số cần tìm


## 🧠 Example

### Input

```text
2
0 1
2
2 3
```

### Output

```text
1 0
```



## 📝 Note

Note
Với test ví dụ
$1$
$2$
xor
$1$
>
$2$
xor
$0$
$3$
xor
$0$
>
$3$
xor
$1$

