# J. Xâu lặp k lần

## 📖 Problem

Cho hai xâu
$s$
và
$t$
, xâu
$t$
được gọi là lặp lại
$k$
lần nếu lấy
$t$
nối
$k$
lần với nhau thì xâu kết quả là một xâu con của
$s$
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
Đưa ra giá
$k$
lớn nhất để xâu
$t$
được gọi là lặp lại
$k$
lần.


## 🧩 Input

Input
Dòng đầu gồm xâu
$t$
có độ dài không vượt quá
$100$
Dòng hai gồm xâu
$s$
có độ dài không vượt quá
$10000$
Các ký tự trong xâu là các chữ cái in thường từ '
$a$
' tới '
$z$
'


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm. Nếu không có
$k$
nào thoả mãn để xâu kết quả là xâu con của
$t$
hãy đưa ra
$0$


## 🧠 Example

### Input

```text
tan
tontontantan
```

### Output

```text
2
```



## 📝 Note

Note
Ví dụ
$1$
, giá trị
$k$
cần tìm là
$2$
vì lúc xâu
$t$
lập lại
$2$
lần thì xâu kết quả là "
$tantan$
" là một xâu con của
![](https://espresso.codeforces.com/1e209f9a46e57cd066fbd4ba2bcf95c079094f94.png)
Ví dụ
$2$
, giá trị
$k$
cần tìm là
$2$
vì lúc xâu
$t$
lập lại
$2$
lần thì xâu kết quả là "
$ntanta$
" là một xâu con của
![](https://espresso.codeforces.com/ed743662ba5eda4acf1047f05dd777b2bfda1212.png)
$n$
Ví dụ
$3$
, giá trị
$k$
cần tìm là
$1$
vì lúc xâu
$t$
lập lại
$2$
lần thì xâu kết quả là "
$t$
" là một xâu con của
![](https://espresso.codeforces.com/644d266e01cc777d911a63237dcc4eb60f579601.png)
$ontontantan$

