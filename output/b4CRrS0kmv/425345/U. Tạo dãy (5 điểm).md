# U. Tạo dãy (5 điểm)

## 📖 Problem

Cho hai dãy có cùng
$n$
số nguyên dương
$a1,a2, ...,an$
và
$b1,b2, ...,bn$
Tấn muốn tạo ra một dãy cũng có
$n$
số nguyên dương
$c1,c2, ...,cn$
thỏa mãn rằng
$ck$
$(1 ≤k≤n)$
là giá trị lớn nhất của
$ai$
x
$bj$
với mọi
$1 ≤i≤j≤k$
. Hay nói cách khác, Tấn cần tạo ra một dãy thỏa mãn rằng
$ck=max($
$ai$
x
$bj)$
với mọi
$(1 ≤i≤j≤k)$
Yêu cầu: Bạn hãy giúp Tấn tạo và in ra dãy
$c$
thỏa mãn điều kiện trên.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 106)$
Dòng tiếp theo gồm
$n$
số
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$
Dòng tiếp theo gồm
$n$
số
$b1,b2, ...,bn$
$(1 ≤bi≤ 109)$


## 💡 Output

Output
Gồm
$n$
dòng, dòng thứ
$i$
$(1 ≤i≤n)$
in ra số
$ci$
thỏa mãn điều kiện (
$i$
theo thứ tự tăng dần
$1, 2...,n$
)


## 🧠 Example

### Input

```text
3
3 2 20
1 4 1
```

### Output

```text
3
12
20
```


