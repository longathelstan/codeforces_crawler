# E. DANKIEN2

## 📖 Problem

Có
$n$
con kiến đang đứng trên 1 đường thẳng, con kiến thứ
$i$
đứng tại vị trí
$ai$
. Hãy tìm tổng khoảng của
$n$
con kiến so với từng vị trí
$ai$
theo thứ tự input.


## 🧩 Input

Input
Dòng đầu tiền gồm
$n$
$(1 ≤n≤ 106, 1 ≤x≤ 109)$
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
là tọa độ
$ai$
của con kiến thứ
$i$
$(1 ≤ai≤ 109)$
$(1 ≤a1<a2< ... <an≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất chứa
$n$
số ứng với
$n$
đáp án cần tìm.


## 🧠 Example

### Input

```text
5
1 2 3 4 5
```

### Output

```text
10 7 6 7 10
```



## 📝 Note

Note
Giải thích:
Khoảng cách của từng con kiến so với vị trí
$a1= 1$
lần lượt là: 0 1 2 3 4, nên đáp án là
$0 + 1 + 2 + 3 + 4 = 10$
Khoảng cách của từng con kiến so với vị trí
$a2= 2$
lần lượt là: 1 0 1 2 3, nên đáp án là
$1 + 0 + 1 + 2 + 3 = 7$
Khoảng cách của từng con kiến so với vị trí
$a3= 3$
lần lượt là: 2 1 0 1 2, nên đáp án là
$2 + 1 + 0 + 1 + 2 = 6$

