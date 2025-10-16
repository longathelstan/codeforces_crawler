# Y. Thời điểm có nhiều đèn sáng nhất (4 điểm)

## 📖 Problem

Có
$n$
chiếc đèn được đánh số thứ tự từ
$1$
đến
$n$
. Chiếc đèn thứ
$i$
chỉ sáng từ giây thứ
$Si$
đến giây thứ
$Ti$
, tức là chỉ sáng ở các giây thứ
$x$
với
$Si≤x≤Ti$
Yêu cầu:
Hãy xác định thời điểm (mỗi thời điểm được xem là
$1$
giây) có nhiều đèn sáng nhất là bao nhiêu đèn? Ta gọi số đèn cùng sáng nhiều nhất này là
$X$
Tìm số giây mà tại các giây đó số đèn sáng bằng
$X$
(tức là tại các giây đó số đèn cùng sáng là nhiều nhất). Ta gọi số giây này là
$Y$


## 🧩 Input

Input
Dòng
$1$
ghi số nguyên
$n$
$(1 ≤n≤ 105)$
Dòng thứ
$i$
trong
$n$
dòng tiếp theo ghi
$2$
số nguyên
$Si$
và
$Ti$
$(1 ≤Si≤Ti≤ 106)$


## 💡 Output

Output
Dòng
$1$
ghi giá trị
$X$
Dòng
$2$
ghi giá trị
$Y$


## 🧠 Example

### Input

```text
3
1 5
3 7
7 10
```

### Output

```text
2
4
```



## 📝 Note

Note
Thời điểm có nhiều đèn sáng nhất là
$2$
đèn.
Tại giây thứ
$3, 4, 5$
có
$2$
đèn sáng (đèn
$1$
và đèn
$2$
)
Tại giây thứ
$7$
có
$2$
đèn sáng (đèn
$2$
và đèn
$3$
)

