# N. Tính đồng nhất

## 📖 Problem

Giải mã không bao giờ là một công việc đơn giản. Mỗi quốc gia đều có có thư viện riêng lưu trữ hồ sơ các mật mã: Cách mã hóa và giải mã, Ai đã sử dụng nó và khi nào, . . . Với một thông tin được mã hóa, việc đầu tiên người ta phải xác định một số đặc trưng để làm khóa tra cứu, tìm kiếm trong thư viện.
Bài tập cho các học viên hôm nay là cho thông tin được mã hóa thành dãy số nguyên
$a1$
,
$a2$
, . . .,
$an$
. Giả thiết
$a1$
gặp trong dãy số
$k1$
lần,
$a2$
– gặp
$k2$
lần, . . .Tính đồng nhất của dãy là số nguyên nhỏ nhất
$c≥ 1$
và
$c≠ki$
với mọi
$i$
. Yêu cầu xử lý
$q$
truy vấn, mỗi truy vấn thuộc một trong 2 dạng:
$1$
$lf$
$rt$
– Tìm tính đồng nhất dãy đã cho trong đoạn từ vị trí
$lf$
đến vị trí
$rt$
(kể cả
$rt$
),
$1≤lf≤rt≤n$
.
$2$
$p$
$x$
– thay
$ap$
bằng
$x$
.


## 🧩 Input

Input
Dòng đầu tiên chứa
$2$
số nguyên
$n$
và
$q$
$(1≤n,q≤105)$
Dòng thứ
$2$
chứa
$n$
số nguyên
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$
Mỗi dòng trong
$q$
dòng sau chứa
$3$
số nguyên xác định một truy vấn.


## 🧠 Example

### Input

```text
10 4
1 2 3 1 1 2 2 2 9 9
1 1 1
1 2 8
2 7 1
1 2 8
```

### Output

```text
2
3
2
```


