# ZZZC. Rồng thần (7 điểm)

## 📖 Problem

Trong một round đấu, rồng thần của Hoạt có thể khạc tối đa đạt
$N$
phát chí mạng vào team địch. Sát thương chí mạng của lần khạc thứ
$i$
gây ra là
$Ai$
. Tuy nhiên rồng thần cần có một khoảng thời gian để hồi lại mana. Vậy nên rồng thần không thể khạc
$K$
lần chí mạng liên tiếp. Bạn hãy chỉ cho Hoạt cách điều khiển sức mạnh của rồng thần sao cho tổng sát thương chí mạng gây ra của rồng thần là lớn nhất.


## 🧩 Input

Input
Dòng thứ nhất: chứa hai số nguyên
$N$
,
$K$
$(1 ≤N≤ 3 * 106;2 ≤K≤N)$
Dòng thứ hai chứa
$N$
số nguyên
$A1,A2, …,AN$
$(1 ≤Ai≤ 104)$
– sát thương chí mạng lần khạc thứ i của rồng thần.


## 💡 Output

Output
Tổng sát thương chí mạng lớn nhất mà rồng thần có thể gây ra.


## 🧠 Example

### Input

```text
7 3
1 4 2 3 6 5 9
```

### Output

```text
23
```



## 📝 Note

Note
Rồng thần sẽ khạc ở những thời điểm
$1$
,
$2$
rồi
$4$
,
$5$
sau cùng là
$7$
. Tổng sát thương sẽ là
$1 + 4 + 3 + 6 + 9 = 23$
.

