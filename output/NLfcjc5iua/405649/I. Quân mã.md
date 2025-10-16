# I. Quân mã

## 📖 Problem

Trong luật cờ vua, mỗi nước đi của quân mã được quy định như sau: quân mã đang ở vị trí X như hình bên dưới có thể đi đến một trong các ô mà mũi tên chỉ đến (theo đường chéo của hình chữ nhật
$2$
x
$3$
)
Yêu cầu: Cho trước bàn cờ kích thước
$n$
x
$m$
ô. Hãy đếm số nước đi ít nhất để quân mã di chuyển từ ô có tọa độ
$(x1,y1)$
đến ơ có tọa độ
$(x2,y2)$
. Trong trường hợp không đến được thì xuất ra giá trị
$- 1$
.
![](https://espresso.codeforces.com/e9a1198f8fe0ecaeff47b86b85c810ecb30d92bc.png)


## 🧩 Input

Input
Dòng
$1$
ghi
$2$
số nguyên dương
$n$
,
$m$
$(2 ≤n,m≤ 1000)$
.
Dòng
$2$
ghi
$2$
số nguyên
$x1,y1$
$(1 ≤x1≤n, 1 ≤y1≤m)$
.
Dòng
$3$
ghi
$2$
số nguyên
$x2,y2$
$(1 ≤x2≤n, 1 ≤y2≤m)$
.
Các số ghi trên cùng một dòng cách nhau ít nhất một kí tự trắng.


## 💡 Output

Output
Một số nguyên duy nhất cho biết số nước đi ít nhất để quân mã di chuyển từ ô (x1, y1) đến ô (x2, y2). Nếu không đến được thì ghi số -1.


## 🧠 Example

### Input

```text
4 6
1 1
2 4
```

### Output

```text
2
```


