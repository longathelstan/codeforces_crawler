# L. Em see cây

## 📖 Problem

Bạn được cho một cái cây
$n$
đỉnh và
$n- 1$
cạnh.Đỉnh thứ
$i$
trên cây mang một trọng số là
$ai$
. định nghĩa,
$g(x,y)$
là ước chung lớn nhất của các đỉnh thuộc đường đi đơn từ
$x$
đến
$y$
.
$dist(x,y)$
là số lượng đỉnh thuộc đường đi từ
$x$
đến
$y$
.
$dist(x,x) = 1$
với mọi
$x$
yêu cầu:
tìm
$dist(x,y)$
lớn nhất thỏa mãn
$g(x,y) > 1$
.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên
$N$
- số đỉnh
$(1 ≤n≤ 2 * 105)$
.
Dòng thứ hai chứa
$N$
số nguyên
$a1$
,
$a2$
,
$a3$
,...,
$an$
$(1 ≤ai≤ 2 * 105)$
- trọng số của các đỉnh.
Sau đó
$n−1$
các dòng tiếp theo, mỗi dòng chứa hai số nguyên
$x$
Và
$y$
$(1 ≤x,y≤n,x≠y)$
biểu thị một cạnh kết nối đỉnh
$x$
với đỉnh
$y$
.


## 💡 Output

Output
Nếu không có cặp
$(x,y)$
nào thỏa mãn
$g(x,y) > 1$
thì in ra
$0$
ngược lại, in ra
$dist(x,y)$
lớn nhất


## 🧠 Example

### Input

```text
3
2 3 4
1 3
2 3
```

### Output

```text
2
```



## 📝 Note

Note
$dist(1, 3) = 2$
,
$g(2, 3) = 2 > 1$
trong khi đó
$dist(1, 2) = 3$
,
$gcd(1, 2) = 1$
. nên in ra
$dist(1, 3) = 2$

