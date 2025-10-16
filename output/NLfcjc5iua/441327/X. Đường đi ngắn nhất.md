# X. Đường đi ngắn nhất

## 📖 Problem

Cho một ma trận có kích thước
$n*n$
. hàng thứ i, cột thứ j là ô
$(i,j)$
, mỗi ô sẽ có một trọng số
$Ai,j$
, trọng số của một đường đi tổng các
$Ai,j$
nằm trên đường đi đó, trong một lần di chuyển giả sử đang đứng ở ô
$(i,j)$
bạn chỉ có thể đi tới các ô
$(i+ 1,j- 1), (i+ 1,j), (i+ 1,j+ 1)$
(các ô cần đảm bảo nằm bên trong ma trận).
Tìm đường đi có trọng số nhỏ nhất xuất phát từ một ô bất kỳ ở hàng
$1$
đến
$1$
ô bất kỳ ở hàng
$n$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 100)$
.
$n$
dòng tiếp theo, mỗi dòng gồm
$n$
số nguyên dương số thứ j là
$Ai,j$
$( - 200 ≤Ai,j≤ 200)$
.


## 💡 Output

Output
In ra trọng số nhỏ nhất tìm được.


## 🧠 Example

### Input

```text
3
2 1 3
6 5 4
7 8 9
```

### Output

```text
13
```



## 📝 Note

Note
![](https://espresso.codeforces.com/74cbc4c17921e503f2479795917a583b2a27224b.png)

