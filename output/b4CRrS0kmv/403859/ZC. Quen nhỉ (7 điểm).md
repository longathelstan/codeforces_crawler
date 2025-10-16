# ZC. Quen nhỉ (7 điểm)

## 📖 Problem

Cho
$2$
mảng
$a$
và
$b$
gồm
$n$
phần tử và số nguyên
$k$
, bạn phải chọn dãy con đúng
$k$
phần tử, giả sử
$k$
vị trí bạn chọn là
$i1,i2, ...,ik$
điểm của bạn sẽ là
$(a[i1] +a[i1] + ... +a[ik]) *min(b[i1],b[i2], ...,b[ik])$
Hãy in ra số điểm lớn nhất có thể đạt được.


## 🧩 Input

Input
Dòng đầu gồm
$2$
số
$n$
và
$k$
$(1 ≤n≤ 5 * 105, 1 ≤k≤n)$
Dòng
$2$
gồm
$n$
số, số thứ
$i$
là giá trị
$ai$
$(1 ≤ai≤ 105)$
Dòng
$3$
gồm
$n$
số, số thứ
$i$
là giá trị
$bi$
$(1 ≤bi≤ 105)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4 3
1 3 3 2
2 1 3 4
```

### Output

```text
12
```



## 📝 Note

Note
Test
$1$
chọn dãy (
$1$
,
$3$
,
$4$
) điểm là (1 + 3 + 2) * min(2,3,4) = 6 * 2 = 12
Test
$2$
chọn dãy
$(3)$
điểm là 3 * 10 = 30

