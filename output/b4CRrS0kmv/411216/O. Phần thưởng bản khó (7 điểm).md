# O. Phần thưởng bản khó (7 điểm)

## 📖 Problem

Trên phố có
$n$
gian hàng nằm trên một đường thẳng, được đánh số từ 1 đến
$n$
. Mỗi gian hàng bán các món đồ chơi với những mức giá khác nhau – gian hàng thứ
$i$
bán đồ chơi với giá
$ai$
đồng.
Có
$k$
bạn nhỏ trên phố, bạn nhỏ thứ
$i$
sẽ đi qua các gian hàng đồ chơi từ gian hàng
$li$
đến gian hàng
$ri$
. Bạn sẽ dừng lại ở một số gian hàng, và ở mỗi gian hàng dừng lại, bạn sẽ mua đúng một món đồ chơi.
Yêu cầu
: Biết rằng, bạn nhỏ thứ sẽ đi qua các gian hàng
$li$
,
$li$
$+$
$1$
, … ,
$ri$
và mang theo
$ti$
đồng. Xác định số lượng món đồ chơi tối đa mỗi bạn có thể mua được nếu chọn dừng lại ở những gian hàng tối ưu.


## 🧩 Input

Input
Dòng đầu tiên gồm hai số nguyên dương
$n$
và
$k$
$(1 ≤n,k≤ 105)$
Dòng tiếp theo gồm
$n$
số nguyên dương
$a1,a2, ...,ai$
$(1 ≤ai≤ 105)$
.
$k$
dòng tiếp theo, mỗi dòng gồm ba số nguyên dương
$li,ri,ti$
$(1 ≤li≤ri≤n, 1 ≤ti≤ 1010)$


## 💡 Output

Output
Gồm
$k$
dòng, dòng thứ là số món đồ chơi tối đa bạn thứ mua được nếu dừng lại ở các gian hàng tối ưu.


## 🧠 Example

### Input

```text
5 3
2 3 4 5 6
1 2 4
2 4 13
3 3 1
```

### Output

```text
1
3
0
```



## 📝 Note

Note
Với ví dụ
$1$
Bạn nhỏ thứ nhất đi từ gian hàng
$1$
đến gian hàng
$2$
và mang theo
$4$
đồng. Bạn có thể mua đồ chơi ở một trong hai gian hàng nhưng không thể mua đồ chơi ở cả hai gian.
Bạn nhỏ thứ hai đi từ gian hàng
$2$
đến gian hàng
$4$
, mang theo
$13$
đồng và có thể mua đồ chơi ở cả ba gian hàng
$3$
$+$
$4$
$+$
$5$
$=$
$12$
.
Bạn nhỏ thứ ba chỉ đi đến gian hàng
$3$
và không thể mua đồ chơi ở gian hàng này do chỉ có
$1$
đồng
Ở ví dụ
$2$
Bạn nhỏ đầu tiên có đủ tiền để mua hai món đồ chơi ở gian hàng
$1$
và
$3$
Bạn nhỏ thứ hai có đủ tiền để mua hai món đồ chơi ở gian hàng
$2$
và
$3$

