# I. Vị trí xâu con

## 📖 Problem

Cho
$n$
xâu, xâu thứ
$i$
được biểu diễn bởi
$si$
.
Một xâu
$X$
là xâu con của một xâu con của
$Y$
nếu
$X$
là một chuỗi các ký tự liên tiếp của
$Y$
Yêu cầu:
Đưa ra các vị trí
$i$
tăng dần sao cho
$si$
là xâu con của một xâu khác trong
$n- 1$
xâu còn lại.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 100)$
$n$
dòng tiếp theo, dòng thứ
$i$
gồm xâu
$si$
Mọi xâu đều có độ dài không vượt quá
$100$
, các ký tự trong xâu là các chữ cái in thường từ '
$a$
' tới '
$z$
'.


## 💡 Output

Output
Gồm một dòng duy nhất chứa các số cần tìm, các số cách nhau bởi dấu cách.


## 🧠 Example

### Input

```text
4
tan
toilatan
la
ton
```

### Output

```text
1 3
```



## 📝 Note

Note
Ví dụ
$1$
,
$s1$
và
$s3$
là xâu con của
$s2$

