# Q. Đường đi k cạnh

## 📖 Problem

Bạn được cho một đồ thị có hướng gồm đỉnh
$n$
và
$m$
cạnh, các đỉnh được đánh số từ
$1$
tới
$n$
. Hãy đếm số đường đi có
$k$
bước (cạnh) và in ra kết quả theo modulo
$109+ 7$
. Một đường đi có thể có ghé thăm các đỉnh và cạnh nhiều lần


## 🧩 Input

Input
Dòng đầu là
$3$
số nguyên
$n,m,k$
$(1 ≤n≤ 100, 0 ≤m≤n* (n- 1), 1 ≤k≤ 1018)$
lần lượt là số đỉnh, số cạnh và số bước của đường
Dòng tiếp theo mô tả các cạnh của đồ thị. Dòng thứ
$i$
gồm
$2$
số nguyên
$ai,bi$
$(1 ≤ai,bi,ai≠bi)$
thể hiện đường đi từ đỉnh tới đỉnh. Đồ thị đã cho đảm bảo không có khuyên và mỗi cạnh không xuất hiện quá một lần


## 💡 Output

Output
In ra một dòng chứa số đường đi thoả mãn yêu cầu input theo modulo
$109+ 7$


## 🧠 Example

### Input

```text
3 4 2
1 2
2 3
3 1
2 1
```

### Output

```text
5
```



## 📝 Note

Note
Ở ví dụ này, ta được cho đồ thị chứa
$3$
đỉnh và
$4$
cạnh như sau:
![](https://espresso.codeforces.com/ddbf8ef68fbf3a0c5d3f1b5ba1be241108299045.png)
Có
$5$
đường đi với số bước
$k= 2$
:
*
$1$
->
$2$
->
$1$
*
$1$
->
$2$
->
$3$
*
$2$
->
$1$
->
$2$
*
$2$
->
$3$
->
$1$
*
$3$
->
$1$
->
$2$

