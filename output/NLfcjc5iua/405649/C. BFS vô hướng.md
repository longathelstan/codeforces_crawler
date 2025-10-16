# C. BFS vô hướng

## 📖 Problem

Cho đồ thị vô hướng
$n$
đỉnh và
$m$
cạnh.
Yêu cầu:
Tìm đường đi ngắn nhất từ đỉnh
$S$
tới đỉnh
$T$
, nếu không có đường đi nào hãy in ra
$- 1$
.


## 🧩 Input

Input
Dòng đầu gồm
$4$
số
$n$
,
$m$
,
$S$
,
$T$
$(1 ≤n,m≤ 2.105, 1 ≤S≤T≤n)$
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
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
5 5 1 5
1 2
1 3
2 3
2 4
4 5
```

### Output

```text
3
```



## 📝 Note

Note
Ví dụ
$1$
![](https://espresso.codeforces.com/49e92195cbd7eb8a4072ec830d32ea1196f8176e.png)
Đường đi ngắn nhất là
$1$
->
$2$
->
$4$
->
$5$
với tổng độ dài là
$3$

