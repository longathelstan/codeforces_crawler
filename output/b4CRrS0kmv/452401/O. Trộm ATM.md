# O. Trộm ATM

## 📖 Problem

Tất cả các đường trong thành phố của Siruseri đều là một chiều. Theo luật của quốc gia này, tại mỗi giao lộ phải có một máy ATM. Điều đáng ngạc nhiên là các cửa hàng chơi điện tử cũng nằm ở các giao lộ, tuy nhiên, không phải tại giao lộ nào cũng có cửa hàng chơi điện tử. Banditji là một tên trộm nổi tiếng. Hắn quyết định làm một vụ động trời: khoắng sạch tiền trong các máy ATM trên đường đi, sau đó ghé vào một cửa hàng chơi điện tử để thư giản. Nhờ có mạng lưới thông tin rộng rãi, Banditji biết được số tiền có ở mỗi máy ATM ngày hôm đó. Xuất phát từ trung tâm, tên trộm lái xe đi dọc theo các phố, vét sạch tiền ở các ATM gặp trên đường đi. Banditji có thể đi lại nhiều lần trên một số đoạn phố, nhưng sẽ không thu gì được thêm từ các ATM đã bị khoắng trước đó. Lộ trình của Banditji phải kết thúc ở giao lộ có cửa hàng chơi điện tử. Banditji biết cách vạch lộ trình để tổng số tiền trộm được là lớn nhất.
Yêu cầu:
Hãy xác định tổng số lượng tiền bị trộm


## 🧩 Input

Input
Dòng đầu tiên chứa
$2$
số nguyên
$n$
và
$m$
,
$(1 ≤n≤ 5 * 105, 1 ≤m≤ 5 * 105)$
lần lượt là số giao lộ và số đoạn đường nối
$2$
giao lộ.
$m$
dòng tiếp theo mỗi dòng chứa
$2$
số nguyên
$u$
và
$v$
$(1 ≤u,v≤n,u≠v)$
miêu tả có cạnh nối từ
$u$
tới
$v$
.
$n$
dòng tiếp theo chứa số nguyên
$ai$
, số tiền trong ATM đặt ở giao lộ
$i$
.
Dòng thứ
$n+m+ 2$
tiếp theo chứa
$2$
số nguyên
$s$
và
$p$
, lần lượt là giao lộ trung tâm và số giao lộ có cửa hàng chơi điện tử.
Dòng cuối cùng chứa
$p$
số nguyên xác định các giao lộ có cửa hàng chơi điện tử.


## 💡 Output

Output
Một dòng duy nhất chứa một số nguyên là số tiền bị trộm


## 🧠 Example

### Input

```text
6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
4 3 5 6
```

### Output

```text
47
```



## 📝 Note

Note
Ở ví dụ nêu trên (hình vẽ minh họa ở dưới), thành phố có
$6$
giao lộ đánh số từ
$1$
đến
$6$
, số tiền trong ATM được ghi ở bên cạnh nút. Các nút hình sao chỉ giao lộ có cửa hàng chơi điện tử. Đường chấm chấm cho biết lộ trình của tên trộm. Tổng cộng, hắn đã lấy được
$47$
đồng.
![](https://espresso.codeforces.com/6e6660513fa0cfa632d6ba77cf9ca11919b56d67.png)

