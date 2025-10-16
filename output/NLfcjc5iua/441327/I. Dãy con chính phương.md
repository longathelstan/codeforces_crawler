# I. Dãy con chính phương

## 📖 Problem

Minh là một học sinh rất yêu thích lập trình, em đã tạo ra một Game X nhằm giúp người chơi phát triển tư duy toán học.
Game được mô tả như sau: cho trước
$n$
tấm thẻ hình chữ nhật được đánh số thứ từ
$1$
đến
$n$
, tấm thẻ thứ
$i$
ghi một số nguyên dương
$n$
. Mỗi lượt chơi, người chơi cần chọn số lượng tấm thẻ nhiều nhất có thể và tuân thủ các quy tắc của trò chơi như sau:
Chọn ra một số tấm thẻ xếp thành hàng ngang, sao cho thứ tự tấm thẻ tăng dần theo chỉ số từ trái sang phải.
Tấm thẻ
$i,j$
$(1 ≤i,j≤n)$
xếp cạnh nhau cần thỏa các điều kiện:
*
$0 < |i-j| ≤ 10$
*
$|aj-ai| > 0$
*
$|aj-ai|$
là bình phương của một số tự nhiên
Yêu cầu: Cho biết số lượng tấm thẻ nhiều nhất mà người chơi có thể chọn được trong mỗi lượt chơi


## 🧩 Input

Input
Dòng thứ nhất gồm
$n$
$(1 ≤n≤ 105)$
Dòng thứ
$i$
trong
$n$
dòng tiếp theo chứa số nguyên dương
$ai$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
7
2
6
2
31
22
11
26
```

### Output

```text
5
```



## 📝 Note

Note
Dãy dài nhất có
$5$
phần tử là:
$2, 6, 31, 32, 26$

