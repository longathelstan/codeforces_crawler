# ZG. Hải tặc (5 điểm)

## 📖 Problem

Một bản đồ hải đảo gồm
$n$
hòn đảo và
$n- 1$
đường thủy hai chiều nối giữa các hòn đảo. Một tên hải tặc gần đây đang mâm me và tung hoành ngang dọc trên các hòn đảo này. Mặc dù đường thủy là
$2$
chiều những để tránh hải quân, mỗi đường thủy hắn chỉ sử dụng nhiều nhất hai lần. Giả sử đường thủy nối giữa
$2$
hòn
$ui$
và
$vi$
, nếu hắn đi từ
$ui$
sang
$vi$
thì hắn sẽ nhận được
$ci$
đồng, nếu đi từ
$vi$
đến
$ui$
thì nhận được
$di$
đồng.
Hắn thực hiện tung hoành khắp bản đồ trong
$q$
ngày, mỗi ngày xuất phát từ hòn đảo
$u$
và mong muốn đi tới hòn đảo
$v$
, bạn hãy tính thử tổng số tiền lớn nhất có thể mà tên này thu thập được vào ngày thứ
$i$
là bao nhiêu.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 2 * 105)$
.
Mỗi dòng trong
$n- 1$
dòng tiếp theo là
$4$
số nguyên dương
$u,v,c,d$
$(1 ≤u≠v≤n, 1 ≤c,d≤ 104)$
.
Tiếp theo là số nguyên
$q$
$(1 ≤q≤ 2 * 105)$
là số ngày hoạt động của hải tặc.
Sau đó là
$q$
dòng mỗi dòng gồm hai số nguyên
$u,v$
$(1 ≤u,v≤n)$
miêu tả hoạt động của cướp biển vào ngày
$i$
.


## 💡 Output

Output
In ra
$q$
dòng là đáp án của từng ngày.


## 🧠 Example

### Input

```text
5
1 2 5 10
3 5 25 3
4 2 15 12
3 2 6 7
2
1 5
4 3
```

### Output

```text
64
65
```


