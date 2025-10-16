# ZZQ. Rút tiền ngân hàng 3 (7 điểm)

## 📖 Problem

Có
$n$
người xếp hàng chờ rút tiền ở ngân hàng. Người thứ
$i$
muốn rút
$ai$
đồng, và sẽ rời đi mà không rút nếu không được phục vụ tính đến hết thời điểm
$ti$
.
Biết rằng ngân hàng có thể phục vụ bất cứ người nào theo bất cứ thứ tự nào, thời gian phục vụ người thứ
$i$
là đúng
$pi$
giây. Giờ mở cửa của ngân hàng là
$0$
và đóng cửa tại thời điểm
$T$
. Hãy giúp ngân hàng cực đại hóa tổng số tiền được rút!


## 🧩 Input

Input
Dòng đầu gồm
$n$
,
$T$
$(1 ≤n≤ 105)$
$n$
dòng tiếp theo, dòng thứ
$i$
chứa
$ai$
$ti$
,
$pi$
$(1 ≤ai≤ 105, 0 ≤  ≤ti≤T, 1 ≤pi≤ti+ 1)$


## 💡 Output

Output
Ghi tổng lượng tiền lớn nhất có thể rút khỏi ngân hàng


## 🧠 Example

### Input

```text
1 1
1 1 1
```

### Output

```text
1
```


