# Y. Đường đi lớn nhất

## 📖 Problem

Cho một bảng
$A$
kích thước
$m$
x
$n$
, trên đó ghi các số nguyên aij. Một người xuất phát tại ô nào đó của cột
$1$
, cần sang cột
$n$
(tại ô nào cũng được).
Quy tắc đi: Từ ô
$(i,j)$
chỉ được quyền sang một trong
$3$
ô
$(i,j+ 1)$
;
$(i- 1,j+ 1)$
;
$(i+ 1,j+ 1)$


## 🧩 Input

Input
Dòng
$1$
: Ghi hai số
$m$
,
$n$
là số hàng và số cột của bảng.
$(1 <  =m,n<  = 500)$
$M$
dòng tiếp theo, dòng thứ
$i$
ghi đủ
$n$
số trên hàng
$i$
của bảng theo đúng thứ tự từ trái qua phải
$( - 1000 ≤ai,j≤ 1000)$


## 💡 Output

Output
Gồm 1 dòng duy nhất ghi tổng lớn nhất tìm được


## 🧠 Example

### Input

```text
5 7
9 -2 6 2 1 3 4
0 -1 6 7 1 3 3
8 -2 8 2 5 3 2
1 -1 6 2 1 6 1
7 -2 6 2 1 3 7
```

### Output

```text
41
```


