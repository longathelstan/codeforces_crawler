# D. DSEQ (7 điểm)

## 📖 Problem

Cho trước một dãy số nguyên
$A=a1,a2,a3, ...,an$
. Gọi
$SUM(L,R)$
là tổng các phần tử thuộc dãy con từ chỉ số
$L$
đến
$R- 1$
.
Ví dụ: cho mảng
$A= (3,  - 4, 1, 6)$
thì:
$SUM(1, 2) = 3$
;
$SUM(1, 3) =  - 1$
.
Yêu cầu
: Tìm 3 chỉ số
$x1,x2,x3(1 ≤x1≤x2≤x3≤n+ 1)$
để chia dãy A thành các dãy con sao cho:
$RES=SUM(1,x1) -SUM(x1,x2) +SUM(x2,x3) -SUM(x3,n+ 1)$
đạt giá trị lớn nhất.


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên
$n$
$(1 ≤n≤ 105)$
;
Dòng thứ hai chứa
$n$
số nguyên
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$
.


## 💡 Output

Output
Gồm 1 dòng duy nhất chứa một số nguyên cho biết giá trị Res lớn nhất có thể.


## 🧠 Example

### Input

```text
5
2 8 -1 7 -2
```

### Output

```text
20
```


