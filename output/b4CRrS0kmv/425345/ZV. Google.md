# ZV. Google

## 📖 Problem

Ở Google văn phòng được xếp
$m$
dãy bàn theo hàng ngang, mỗi hàng có
$n$
bàn làm việc. Khoảng cách mỗi bàn là 1. Trong
$k$
bàn làm việc bộ phận IT sẽ lắp bộ phát Wifi, wifi ở mỗi bàn không giống nhau, wifi thứ
$i$
sẽ cho phép người dùng có thể truy cập trong phạm vi bán kính
$ri$
với tốc độ đường truyền là
$bi$
.
Laptop của nhân viên Google có trang bị một thiết bị đặc biệt có khả năng kết hợp tốc độ đường truyền của các wifi khác nhau để nhận được đường truyền có tốc độ băng tổng tốc độ của các đường truyền wifi mà máy tính có thể tiếp cận.
Hãy xác định tốc độ đường truyền tối đa mà một nhân viên ngồi tại bàn làm việc có thể nhận được và đếm số lượng vị trí như thế.


## 🧩 Input

Input
Dòng đầu ghi số nguyên
$m$
$(1 ≤m≤ 30000)$
là số dãy bàn.
Dòng thứ hai ghi số nguyên
$n$
$(1 ≤n≤ 1000)$
là số bàn trên
$1$
dãy.
Dòng thứ ba ghỉ số nguyên
$k$
$(1 ≤k≤ 1000)$
là bộ phát wifi.
K dòng tiếp theo mỗi dòng chứa thông tin về các bộ phát wifi gồm
$4$
số nguyên:
$x$
,
$y$
,
$r$
,
$b$
. Với
$x$
là số thứ tự bàn trong dãy từ trái sang phải nơi có bộ phát wifi,
$y$
là số thứ tự của dãy bàn,
$r$
,
$b$
lần lượt là bán kính phủ sóng và tốc độ của bộ phát wifi đó.
$(1 ≤x≤n, 1 ≤y≤m, 1 ≤r≤ 30000, 1 ≤B≤ 10000)$


## 💡 Output

Output
Gồm
$2$
số là tốc độ đường truyền tối đa mà một nhân viên ngồi tại bàn làm việc có thể nhận được và số lượng vị trí như thế.


## 🧠 Example

### Input

```text
3
5
3
1 3 2 5
3 1 2 7
5 1 1 5
```

### Output

```text
12
5
```



## 📝 Note

Note
![](https://espresso.codeforces.com/32317b96ff02c06e35a4329c131a208a325282c1.png)

