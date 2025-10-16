# I. Đất nước X

## 📖 Problem

Đất nước
$X$
bao gồm
$n$
thành phố, một số cặp trong số chúng được kết nối với những con đường một chiều. Nhìn chung, có
$n- 1$
con đường trong cả nước. Biết rằng nếu không xem xét hướng của các con đường thì có thể đi từ bất kỳ thành phố nào đến bất kỳ thành phố nào khác.
Hội đồng trưởng lão gần đây đã quyết định chọn thủ đô của
$X$
. Tất nhiên nó phải là một thành phố của đất nước này. Hội đồng phải họp ở thủ đô và thường xuyên di chuyển từ thủ đô đến các thành phố khác (ở giai đoạn này không ai nghĩ đến việc quay trở lại thủ đô từ những thành phố này). Vì lý do đó nếu thành phố
$X$
được chọn là thủ đô, thì tất cả các con đường phải được định hướng sao cho nếu chúng ta di chuyển dọc theo chúng, chúng ta có thể đi từ thành phố
$X$
đến bất kỳ thành phố nào khác. Đối với điều đó, một số con đường có thể phải được đảo ngược.
Giúp những người lớn tuổi chọn thủ đô để họ phải đảo ngược số lượng đường tối thiểu trong cả nước.


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên
$n$
$(2≤n≤2·105)$
— số thành phố trong
$X$
.
$N- 1$
dòng tiếp theo chứa mô tả về các con đường, mỗi dòng một con đường. Một con đường được mô tả bằng một cặp số nguyên
$si,ti$
$(1≤si,ti≤n;si≠ti)$
— số thành phố, được kết nối bởi con đường đó. Con đường thứ
$i$
có hướng từ thành phố
$si$
đến thành phố
$ti$
.


## 💡 Output

Output
Ở dòng đầu tiên in ra số đường ít nhất được đảo ngược nếu vốn được chọn tối ưu.
Trong dòng thứ hai in tất cả các cách có thể để chọn thủ đô — một chuỗi các chỉ số của các thành phố theo thứ tự tăng dần


## 🧠 Example

### Input

```text
3
2 1
2 3
```

### Output

```text
0
2
```


