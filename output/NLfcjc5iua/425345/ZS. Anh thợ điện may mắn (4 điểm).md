# ZS. Anh thợ điện may mắn (4 điểm)

## 📖 Problem

Có
$n$
thành phố được đánh số từ
$1$
đến
$n$
. Tại thành phố thứ
$i$
sẽ có
$ai$
nhà máy điện.
Mỗi nhà máy điện có thể cung cấp điện cho mọi thành phố trong một phạm vi cố định. Nói cách khác, nếu phạm vi được ký hiệu là r, thì một nhà máy điện ở thành phố i có thể cung cấp điện cho tất cả các thành phố j sao cho |i - j| <= r và 0 <= i, j <= n - 1. Sức mạnh của một thành phố là tổng số nhà máy điện mà nó đang được cung cấp điện.
Chính phủ đã cho phép xây dựng thêm k nhà máy điện, mỗi nhà máy có thể được xây dựng ở bất kỳ thành phố nào và có cùng phạm vi như những nhà máy đã có trước đó.
Cho hai số nguyên r và k, hãy tìm cách đặt sao cho sức mạnh tối thiểu của một thành phố là tối đa nếu các nhà máy điện bổ sung được xây dựng một cách tối ưu. Hãy in ra con số tối đa đó.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 106, 0 ≤r≤n- 1, 0 ≤k≤ 109)$
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
là số trạm điện đặt tại thành phố
$ai$
$(0 ≤ai≤ 105)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
5 1 2
1 2 4 5 0
```

### Output

```text
5
```



## 📝 Note

Note
Với test
$1$
: Đăt
$2$
trạm điện thêm vào vị trí số
$2$
ta được
$[1, 4, 4, 5, 0]$
Thành phố
$1$
sẽ có sức mạnh là 1 + 4 = 5
Thành phố
$2$
sẽ có sức mạnh là 1 + 4 + 4 = 9
Thành phố
$3$
sẽ có sức mạnh là 4 + 4 + 5 = 13
Thành phố
$4$
sẽ có sức mạnh là 5 + 4 = 9
Thành phố
$5$
sẽ có sức mạnh là 5 + 0 = 5
Vậy sức mạnh nhỏ nhất là
$5$
và đây cũng là cách chọn tối ưu nhất.

