# C. Mua vé

## 📖 Problem

Có
$N$
người sắp hàng mua vé dự buổi hoà nhạc. Ta đánh số họ từ
$1$
đến
$N$
theo thứ tự đứng trong hàng. Mỗi người cần mua một vé, song người bán vé được phép bán cho mỗi người tối đa hai vé. Vì thế, một số người có thể rời hàng và nhờ người đứng trước mình mua hộ vé. Biết ti là thời gian cần thiết để người i mua xong vé cho mình. Nếu người
$i+ 1$
rời khỏi hàng và nhờ người
$i$
mua hộ vé thì thời gian để người thứ
$i$
mua được vé cho cả hai người là
$ri$
.
Yêu cầu: Xác định xem những người nào cần rời khỏi hàng và nhờ người đứng trước mua hộ vé để tổng thời gian phục vụ bán vé là nhỏ nhất.


## 🧩 Input

Input
Dòng đầu tiên chứa số
$N$
$(1≤N≤105)$
.
Dòng thứ
$2$
ghi
$N$
số nguyên dương
$t1,t2, ...,tN$
.
$(1≤ti≤30000)$
Dòng thứ ba ghi
$N- 1$
số nguyên dương
$r1,r2, ...,rN- 1$
.
$(1≤ri≤30000)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
5
2 5 7 8 4
4 9 10 10
```

### Output

```text
18
```


