# T. Xâu độc nhất (6 điểm)

## 📖 Problem

Cho một xâu
$s$
, bạn có thể thực hiện thao tác sau
tối đa
$1$
lần, chọn
$1$
xâu con liên tiếp
$s[l...r]$
và đảo ngược các ký tự trong xâu đó lại.
Mục tiêu của bạn là thu được xâu con
liên tiếp
dài nhất chỉ gồm các ký tự độc nhất với nhau. Một xâu được gọi xem là độc nhất nếu không có bất kỳ ký tự nào lặp lại
$2$
lần ví dụ như "vuorz" là một xâu độc nhất còn "turottinh" thì không.
Hãy tìm độ dài của xâu con
liên tiếp
độc nhất dài nhất.


## 🧩 Input

Input
Dòng đầu gồm xâu
$s$
$(1 ≤len(s) ≤ 106)$
,
$s$
chỉ chứa
$20$
ký tự in thường đầu của bảng chữ cái
$a,b, ...,t$


## 💡 Output

Output
Gồm
$1$
số duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
abacaba
```

### Output

```text
3
```



## 📝 Note

Note
Test
$1$
: không cần đảo, xâu con liên tiếp cần tìm
$cab$
.
Test
$2$
: đảo abcde
cdf
thành abcde
fdc
đoạn con cần tìm là
$abcdef$

