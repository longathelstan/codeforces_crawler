# I. STRkARY

## 📖 Problem

Xâu
$x$
được gọi là chuyển dịch của xâu y, nếu tồn tại hai xâu
$u,v$
(
$u$
,
$v$
có thể là xâu rỗng) sao cho
$x=uv$
và
$y=vu$
. Ở đây
$uv$
ký hiệu phép toán ghép
$v$
nối tiếp vào sau xâu
$u$
.
Ví dụ: Xâu
$x= «abba»$
là chuyển dịch của xâu
$y= «baab»$
, bởi vì với
$u= «ab»,v= «ba»$
ta có
$x=uv$
và
$y=vu$
.
Cho xâu ký tự
$s$
độ dài
$n$
. Xâu
$s$
được gọi là có tính chất
$k$
-phân, nếu ta có thể chia xâu
$s$
thành
$k$
xâu con liên tiếp có độ dài bằng nhau, sao cho mỗi xâu con trong chúng đều là chuyển dịch của mọi xâu con khác trong số
$k−1$
xâu con còn lại. Ta quy ước rằng tất cả các xâu
$s$
đều có tính chất
$1$
-phân.
Yêu cầu: Hãy liệt kê tất cả giá trị
$k$
sao cho xâu
$s$
đã cho có tính chất
$k$
-phân.


## 🧩 Input

Input
Một dòng duy nhất chứa xâu
$s$
$(1≤|s|≤2 * 105)$
gồm các ký tự latin thường.


## 💡 Output

Output
Dòng thứ nhất ghi ra số m là số lượng các giá trị k sao cho xâu s có tính chất k-phân.
Dòng thứ hai ghi ra m giá trị
$ki$
nêu trên theo thứ tự tăng dần. Hai giá trị liên tiếp được ghi cách nhau bởi dấu cách.


## 🧠 Example

### Input

```text
abbabaab
```

### Output

```text
3
1 2 4
```



## 📝 Note

Note
Trong ví dụ thứ nhất chúng ta có thể giữ nguyên xâu
$(k= 1)$
; hoặc chia thành
$k= 2$
xâu con
$«abba»$
và
$«baab»$
; hoặc chia thành
$k= 4$
xâu con
$«ab», «ba», «ba»$
và
$«ab»$
..

