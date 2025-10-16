# Z. OPPOSITE

## 📖 Problem

Cho mảng
$a$
gồm
$n$
phần tử. Ở mỗi lượt, bạn có thể đi từ vị trí
$i$
tới vị trí
$i-ai$
(nếu
$1 ≤i-ai$
) hoặc tới vị trí
$i+ai$
(nếu
$i+ai≤n$
).
Với mỗi vị trí
$i$
từ
$1$
tới
$n$
hãy in ra số lượt ít nhất để tới vị trí
$j$
bất kỳ sao cho
$(aj+ai)%2 = 1$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số
$n$
$(1 ≤n≤ 2.105)$
là số lượng phần tử
Dòng sau gồm
$n$
số nguyên dương
$a1,a2, ...,an$
$(1 ≤ai≤n)$
, số thứ
$i$
là giá trị của
$ai$
.


## 💡 Output

Output
Gồm
$n$
số
$d1,d2, ...,dn$
, trong đó
$di$
là đáp án của vị trí thứ
$i$
, in ra
$- 1$
nếu không thể đi tới ô thỏa đề bài.


## 🧠 Example

### Input

```text
10
4 5 7 6 7 5 4 4 6 4
```

### Output

```text
1 1 1 2 -1 1 1 3 1 1
```


