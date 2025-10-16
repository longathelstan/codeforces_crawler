# Z. Chi phí chuyến bay (bản dễ)

## 📖 Problem

Một bản đồ bay được mô phỏng dưới dạng một hình chữ nhật
$n*m$
, bạn đang đứng ở ô
$(1, 1)$
và muốn tới ô
$(n,m)$
. Biết rằng, khi thực hiện một chuyến bay dài thường sẽ không có máy bay đi thằng một mạch mà phải bay qua nhiều khu trung gian, vì kinh phí của bạn có hạn nên bạn mong muốn chọn ra các ô trung gian sao cho chi phí nhỏ nhất có thể. Từ
$(a,b)$
ta bay trực tiếp (không qua trung gian) tới
$(c,d)$
nếu
$(a≤c,b≤d$
và
$(c-a) + (d-b) ≤k)$
, chi phí để bay từ ô
$(a,b)$
tới
$(c,d)$
là bằng
$Cc,d-min(Cx,y)$
với
$(a≤x≤c,b≤y≤d)$
. Tìm chi phí nhỏ nhất cần bỏ ra!


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
,
$m$
và
$k$
$(1 ≤n*m≤ 20, 1 ≤k≤n+m- 2)$
Dòng tiếp theo có
$m$
số nguyên dương
$(1 ≤Ci,j≤ 109)$
.


## 💡 Output

Output
In ra chi phí nhỏ nhất có thể


## 🧠 Example

### Input

```text
1 3 2
1 2 2
```

### Output

```text
1
```



## 📝 Note

Note
$(1, 1)$
->
$(1, 3)$

