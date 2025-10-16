# C. Vị trí tốt (7 điểm)

## 📖 Problem

Cho dãy số nguyên
$a1,a2, ...,an$
. Dãy số này được viết trên một vòng tròn. Nghĩa là, khi cắt vòng tròn tại vị trí
$j$
, ta thu được:
$aj,aj+ 1, ...,an,a1,a2, ...,aj- 1$
Vị trí
$j$
được gọi là
vị trí tốt
, nếu các điều kiện sau đây được thỏa mãn:
$aj> 0$
$aj+aj+ 1> 0$
$aj+aj+ 1+aj+ 2> 0$
...
$aj+aj+ 1+ ... +an+a1+ ... +aj- 1> 0$
Yêu cầu: Hãy đếm số
vị trí tốt
.


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên
$n$
.
$(1 ≤n≤ 3 * 106)$
Dòng thứ
$2$
chứa dãy số
$a1,a2, ...,an$
.
$( - 109≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
5
0 1 -2 10 3
```

### Output

```text
2
```



## 📝 Note

Note
Các vị trí tốt là vị trí
$4$
và
$5$

