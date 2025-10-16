# B. Truy vết dãy wavio

## 📖 Problem

Dãy số nguyên
$a1,a2,a3, …,ak$
được gọi là dãy số WAVIO nếu tồn tại số tự nhiên
$1 ≤m≤k$
sao cho:
*
$a1≤a2≤ ... ≤am$
*
$ak≤ak−1≤ ... ≤am$
Ví dụ dãy số
$1, 2, 3, 4, 5, 2, 1$
là
$1$
dãy WAVIO độ dài
$7$
. Cho dãy
$a$
gồm
$n$
số nguyên. Hãy tìm dãy WAVIO dài nhất
Yêu cầu
: Dòng đầu là độ dài dãy WAVIO lớn nhất tìm được, dòng tiếp theo là chỉ số của các phần tử được lấy của dãy WAVIO dài nhất bất kỳ tìm được theo thứ tự tăng dần.


## 🧩 Input

Input
Dòng
$1$
: số nguyên dương
$N$
$(N≤ 103)$
, độ dài dãy số.
Dòng
$2$
:
$N$
số nguyên dương
$ai$
$(ai≤109)$
.


## 💡 Output

Output
Gồm hai dòng ứng với kết quả của bài toán như mô tả


## 🧠 Example

### Input

```text
10
1 2 3 4 5 4 3 2 1 10
```

### Output

```text
9
1 2 3 4 5 6 7 8 9
```


