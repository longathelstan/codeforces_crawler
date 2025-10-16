# I. Tìm vị trí xuất hiện đầu và cuối (7 điểm)

## 📖 Problem

Cho mảng
$a$
gồm
$n$
phần tử được sắp xếp tăng dần từ bé tới lớn và
$q$
truy vấn, mỗi truy vấn chứa số
$x$
, hãy tìm vị trí xuất hiện đầu tiên và vị trí xuất hiện cuối cùng của giá trị
$x$
trong mảng
$a$
. Nếu không có đáp án hãy in
$" - 1 - 1"$


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 106)$
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
là giá trị
$ai$
$(1 ≤ai≤ 109,ai≤ai+ 1)$
Dòng tiếp theo gồm
$q$
$(1 ≤q≤ 106)$
Tiếp theo gồm
$q$
dòng, mỗi dòng chứa số
$x$
$(1 ≤x≤ 109)$


## 💡 Output

Output
Gồm
$q$
dòng ứng với
$q$
truy vấn cần tìm, dòng thứ
$i$
chứa
$2$
số nguyên là đáp án của truy vấn thứ
$i$


## 🧠 Example

### Input

```text
6
5 7 7 8 8 10
5
5
7
8
9
10
```

### Output

```text
1 1
2 3
4 5
-1 -1
6 6
```


