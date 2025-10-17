# H. Đếm cừu

## 📖 Problem

Một trang trại đang nuôi một bầy cừu với đủ loại chủng, con cừu thứ
$i$
thuộc loại
$Ai$
.
Trong một ngày nhàm chán, chủ trang trại và cậu con trai đã dắt tay nhau ra ngồi đếm cừu, nếu đoán đúng hết ông sẽ thưởng kẹo, đầu tiên ông xếp cừu vào hàng ngang và đánh số từ
$1$
đến
$n$
.
Sau đó ông có
$Q$
câu hỏi cho cậu con trai, mỗi câu hỏi là một đoạn
$L$
đến
$R$
và hỏi trong đoạn này có bao nhiêu số
$x$
sao cho số lượng cừu loại
$x$
trong đoạn cũng bằng
$x$
. Vì cậu bé là một người khá dở việc đếm nên đành nhờ bạn lập trình, hứa sẽ chia phần kẹo cho.


## 🧩 Input

Input
Dòng đầu chứa số nguyên dương
$N$
và
$Q$
$(1 ≤N,Q≤ 105)$
.
Dòng tiếp theo chứa
$N$
số nguyên dương, số thứ
$i$
là
$Ai$
$(1 ≤Ai≤ 109)$
tức là con cừu
$i$
thuộc loại
$Ai$
.
Mỗi dòng trong
$Q$
dòng tiếp theo, dòng thứ
$i$
là
$Li$
và
$Ri$
$(1 ≤Li≤Ri≤n)$
.


## 💡 Output

Output
Gồm
$Q$
dòng, dòng thứ
$i$
là đáp án của truy vấn thứ
$i$
.


## 🧠 Example

### Input

```text
7 2
3 1 2 2 3 3 7
1 7
3 4
```

### Output

```text
3
1
```


