# H. Đại đội (7 điểm)

## 📖 Problem

Có
$N$
đại đội, mỗi đại đội
$i$
có
$A[i] > 0$
binh sỹ. Các binh sỹ trong mỗi đại đội đứng thành một cột. Ta cần chọn một nhóm các đại đội liên tiếp nhau (từ đại đội
$i$
đến
$j$
) để tạo thành một
quân đoàn
.
Sức mạnh của quân đoàn này được tính bằng công thức:
$min$
(
$A[i..j]$
)
$×$
$(j-i+ 1)$
$(1 ≤i≤j≤N)$
Yêu cầu:
tìm sức mạnh quân đoàn mạnh nhất.


## 🧩 Input

Input
Dòng
$1$
: Số
$T$
là số bộ test .
$T$
nhóm dòng tiếp theo , mỗi nhóm dòng mô tả
$1$
bộ test . Nhóm dòng thứ
$i$
:
Dòng 1:
$N$
$(1 ≤N≤ 106)$
Dòng 2:
$N$
số nguyên mô tả
$N$
số
$A1$
,
$A2$
, …
$AN$
$(1 ≤Ai≤ 106)$
.
Tổng
$n$
ở các test
$≤ 106$


## 💡 Output

Output
Kết quả mỗi test ghi ra trên 1 dòng , sức mạnh quân đoàn mạnh nhất


## 🧠 Example

### Input

```text
2
4
3 4 3 1
4
1 2 1 3
```

### Output

```text
9
4
```


