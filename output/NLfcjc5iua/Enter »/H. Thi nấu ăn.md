# H. Thi nấu ăn

## 📖 Problem

Có
$n$
bạn sinh viên đang tham gia dự thi nấu ăn nhân dịp năm mới và được đánh số báo danh từ
$1$
đến
$n$
, bạn sinh viên thứ
$i$
tham dự với số lượng là
$ai$
món ăn.
Ban tổ chức sẽ đánh số các món ăn dự thi như sau: các món ăn của thí sinh thứ nhất đánh số từ
$1$
đến
$a1$
, các món ăn của thí sinh thứ hai đánh số từ
$a1+ 1$
đến
$a1+a2$
.... và tương tự như vậy cho đến món cuối cùng. Sau khi chấm thi, Ban tổ chức chọn trao giải cho m món ăn với các số hiệu là
$p1,p2, ...,pm$
. Hãy cho biết các món ăn đạt giải đó thuộc về các bạn sinh viên nào?


## 🧩 Input

Input
Dòng thứ nhất là số nguyên
$n$
$(1≤n≤105)$
là số thí sinh tham gia dự thi.
Dòng thứ hai là
$n$
số nguyên
$a1,a2, ...,an$
$(1≤ai≤104)$
là số lượng món ăn của từng thí sinh, mỗi số cách nhau một khoảng trắng.
Dòng thứ ba là số nguyên
$m$
$(1≤m≤105)$
là số lượng món ăn đạt giải.
Dòng thứ tư là
$m$
số nguyên
$p1,p2, ...,pm$
$(1 ≤pi≤ 109)$
là số hiệu của m món ăn đạt giải, mỗi số cách nhau một khoảng trắng.


## 💡 Output

Output
Là
$m$
số nguyên
$s1,s2, ...,sm$
cho biết số báo danh thí sinh của từng món ăn đạt giải (món ăn
$pi$
là của thí sinh số báo danh
$si$
), mỗi số cách nhau một khoảng trắng.
Nếu món ăn đó không thuộc về thí sinh nào hãy in
$- 1$


## 🧠 Example

### Input

```text
5
5 4 1 2 3
4
5 6 12 100
```

### Output

```text
1 2 4 -1
```


