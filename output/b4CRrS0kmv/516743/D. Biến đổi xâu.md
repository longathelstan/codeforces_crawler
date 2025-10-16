# D. Biến đổi xâu

## 📖 Problem

Cho
$q$
truy vấn, mỗi truy vấn gồm
$2$
xâu
$s$
và
$t$
có cùng độ dài, bạn có thực hiện thao tác sau vô số lần, mỗi lần chọn
$1$
xâu con liên tiếp từ
$s$
hoặc
$t$
, sau đó biến đổi xâu con liên tiếp được chọn thành cùng
$1$
ký tự bất kỳ mà bạn muốn.
Yêu cầu
: với mỗi truy vấn hãy in ra số lần biến đổi ít nhất để
$2$
xâu bằng nhau. Nếu không thể biến
$2$
xâu bằng nhau hãy in
$- 1$


## 🧩 Input

Input
Dòng đầu gồm
$q$
$(1 ≤q≤ 105)$
là số lượng truy vấn Với mỗi truy vấn sẽ gồm
$2$
dòng.
Dòng
$1$
: Xâu
$s$
Dòng
$2$
: Xâu
$t$
Tổng độ dài mọi xâu của bộ dữ liệu sẽ không vượt quá
$2.105$
, các ký tự đều sẽ thuộc chữ cái in thường và độ dài
$2$
xâu sẽ luôn bằng nhau cho mỗi truy vấn.


## 💡 Output

Output
Gồm
$q$
dòng ứng với đáp án
$q$
truy vấn cần tìm


## 🧠 Example

### Input

```text
4
abc
abc
abcelr
abaalr
aaaaa
baaaa
ab
ba
```

### Output

```text
0
1
1
2
```



## 📝 Note

Note
Test
$1$
: Không cần biến đổi
Test
$2$
: Biến
$s[3, 4]$
thành ký tự
$a$
, xâu
$s$
mới là
$abaalr$
Test
$3$
: Biến
$t[1, 1]$
thành ký tự
$a$
, xâu
$t$
mới là
$aaaaa$
Test
$4$
: Biến
$t[1, 1]$
thành ký tự a, biến
$s[2, 2]$
thành ký tự a. Xâu
$s$
và
$t$
sẽ thành
$aa$

