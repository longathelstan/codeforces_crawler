# A. Biểu diễn cạnh 1

## 📖 Problem

Cho đồ thị vô hướng
$n$
đỉnh và
$m$
cạnh.
Yêu cầu:
Hãy biểu diễn đồ thị dưới dạng ma trận
$a$
có kích thước
$n$
x
$n$
,
$ai,j= 1$
nếu có cạnh nối từ đỉnh
$i$
tới
$j$
,
$ai,j= 0$
nếu không có cạnh nối từ đỉnh
$i$
tới
$j$
.


## 🧩 Input

Input
Dòng đầu gồm
$2$
số
$n$
,
$m$
$(1 ≤n,m≤ 2000)$
Sau đó gồm
$m$
dòng, dòng thứ
$i$
gồm
$2$
số
$x$
,
$y$
$(1 ≤x,y≤n)$
thể hiện có cạnh vô hướng nối giữa
$2$
đỉnh
$x$
và
$y$
.


## 💡 Output

Output
Đưa ra ma trận cần tìm


## 🧠 Example

### Input

```text
5 5
1 2
1 3
2 3
2 4
4 5
```

### Output

```text
0 1 1 0 0 
1 0 1 1 0 
1 1 0 0 0 
0 1 0 0 1 
0 0 0 1 0
```



## 📝 Note

Note
Đồ thị cho ví dụ
$1$
![](https://espresso.codeforces.com/49e92195cbd7eb8a4072ec830d32ea1196f8176e.png)

