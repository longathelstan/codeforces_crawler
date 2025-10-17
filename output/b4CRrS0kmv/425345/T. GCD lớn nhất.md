# T. GCD lớn nhất

## 📖 Problem

Xét mảng
$a$
gồm
$n$
phần tử. Tấn được thực hiện thao tác xóa một đoạn thẳng liên tiếp của mảng
$a$
có độ dài
$k$
đúng một lần.
Yêu cầu: Hãy giúp Tấn tìm cách xóa sao cho ước chung lớn nhất của
$n-k$
số còn lại trong mảng
$a$
là lớn nhất có thể


## 🧩 Input

Input
Dòng đầu chứa
$2$
số
$n$
và
$k$
$(1 ≤K<N≤ 105)$
là độ dài mảng
$a$
và hằng số
$K$
.
Dòng thứ
$2$
chứa
$n$
số, số thứ
$i$
là giá trị của
$ai$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là giá trị ước chung lớn nhất của
$n-k$
số còn lại trong mảng
$A$
sau khi thực hiện thao tác trên đúng một lần.


## 🧠 Example

### Input

```text
5 2
2 4 3 5 6
```

### Output

```text
2
```



## 📝 Note

Note
Xóa đoạn con liên tiếp
$[3, 5]$
còn lại
$[2, 4, 6]$
,
$GCD(2, 4, 6) = 2$
, đây cũng là giá trị ước chung lớn nhất có thể tìm được.

