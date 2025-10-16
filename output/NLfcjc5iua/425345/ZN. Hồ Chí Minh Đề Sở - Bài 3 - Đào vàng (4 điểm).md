# ZN. Hồ Chí Minh Đề Sở - Bài 3 - Đào vàng (4 điểm)

## 📖 Problem

Đào vàng là trò chơi khá phổ biến và có nhiều phiên bản. Hãy cùng xét một phiên bản của trò chơi này. Có
$N$
thỏi vàng được cố định ở các vị trí
$X1,X2,X3, ...,Xn$
trên một trục nằm ngang. Nếu người chơi đào ở vị trí
$X$
với máy khoan có lực đập
$R$
thì có thể lấy được các thỏi vàng cách vị trí
$X$
tối đa
$R$
đơn vị chiều dài hay các thỏi vàng có vị trí nằm trong khoảng
$[X-R;X+R]$
. Người chơi được đào tối đa
$K$
lần và lực đập
$R$
là giống nhau ở các lần đào. Nếu người chơi chọn lực đập
$R$
càng nhỏ thì số điểm đạt được càng cao và ngược lại. Người chơi được thực hiện tối đa
$K$
lần đào, hãy giúp người chơi chọn lực đập
$R$
nhỏ nhất để có thể đào hết
$N$
thỏi vàng.
Yêu cầu:
Cho trước vị trí của
$N$
thỏi hàng, hãy viết chương trình tìm giá trị nguyên
$R$
bé nhất sao cho người chơi có thể lấy được
$N$
thỏi vàng sau tối đa
$K$
lần đào.


## 🧩 Input

Input
Dòng đầu chứa 2 số nguyên
$N$
và
$K$
lần lượt cho biết số lượng thỏi vàng và số lần đào tối đa. Dòng thứ
$i$
trong
$N$
dòng tiếp theo cho biết vị trí
$Xi(0 ≤Xi≤ 109)$
của thỏi vàng thứ
$i$
.


## 💡 Output

Output
Một số nguyên là giá trị lực đập
$R$
bé nhất để lấy được
$N$
thỏi vàng tối đa sau
$K$
lần đào.


## 🧠 Example

### Input

```text
6 1
2
20
6
5
4
17
```

### Output

```text
9
```



## 📝 Note

Note
Giải thích ví dụ
$1$
:
Với lực đập
$R= 9$
, người chơi có thể đào
$1$
lần ở vị trí
$X1= 11$
Với lực đập
$R= 2$
, người chơi có thể đào
$2$
lần ở vị trí
$X1= 4$
và
$X2= 18$

