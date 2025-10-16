# G. Tô màu 5

## 📖 Problem

Lớp Hồng đang chơi trò tô màu trên bảng số. Các bạn kẻ một bảng số hình chữ nhật gồm
$N$
dòng và
$M$
cột. Các hàng được đánh số từ 1 đến
$N$
, từ trên xuống dưới; các cột được đánh số từ 1 đến
$M$
, từ trái sang phải. Ô ở hàng thứ
$i$
và cột thứ
$j$
được gọi là ô
$(i,j)$
và được điền giá trị là
$i*j$
. Có
2
bạn tham gia chơi trò chơi, bạn chọn một hình chữ nhật trên bảng số và tô bằng một màu mà bạn thích (các hình chữ nhật của các bạn có thể đè lên nhau – tô đè lên).
Yêu cầu:
Cho
$N,M$
là kích thước bảng số và một hình chữ nhật được mô tả bằng ô trái trên và ô phải dưới. Hãy tỉnh tổng những ô
chưa được tô màu
trên bảng số.


## 🧩 Input

Input
Dòng đầu chứa ba số nguyên
$N$
,
$M$
$(1 ≤N,M≤ 109)$
Gồm hai dòng chứa bốn số nguyên
$x,y,u,v$
mô tả ô trái trên
$(x,y)$
và ô phải dưới
$(u,v)$
của một hình chữ nhật. Các ô thoả mãn mô tả một hình chữ nhật nằm trong bảng số.


## 💡 Output

Output
Kết quả:
Ghi ra thiết bị ra chuẩn một số nguyên duy nhất là phần dư của phép chia của tổng các ô chưa được tô màu trên bảng số cho
$109+ 7$
.


## 🧠 Example

### Input

```text
3 3
1 2 3 3
3 1 3 3
```

### Output

```text
3
```



## 📝 Note

Note
![](https://espresso.codeforces.com/3b15107c1bb8b7f607a6ce4745af4f6f3a93d28b.png)

