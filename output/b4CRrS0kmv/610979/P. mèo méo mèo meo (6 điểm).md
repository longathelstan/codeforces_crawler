# P. mèo méo mèo meo (6 điểm)

## 📖 Problem

Tấn là một người thích các tranh về mèo. Mạng xã hội Tấn xài có
$n$
ảnh
liên tiếp
về mèo, nhưng có những bức ảnh sẽ đẹp hơn các bức ảnh còn lại, bức ảnh thứ
$i$
sẽ có độ đẹp là
$ai$
.
Tấn muốn đăng lại
chính xác
$x$
bức ảnh về mèo mà thỏa các điều kiện sau:
*
Cứ
$k$
bức ảnh
liên tiếp
bất kỳ thì phải có
$1$
ảnh được đăng lại bởi Tấn
*
Tổng độ đẹp của
$x$
bức ảnh Tấn đăng là lớn nhất có thể
Ví dụ, nếu
$k= 1$
Tấn phải đăng lại mọi bức ảnh trên mạng xã hội.
$k= 2$
thì Tấn có thể không đăng lại một số bức ảnh, nhưng giữa
$2$
bức ảnh liên tiếp thì phải có
$1$
bức ảnh được dăng.
Hãy giúp Tấn tìm tổng độ đẹp lớn nhất có thể thỏa mãn các điều kiện trên.


## 🧩 Input

Input
Dòng đầu gồm
$3$
số nguyên dương
$n$
,
$k$
và
$x$
$(1 ≤k,x≤n≤ 5000)$
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
là độ đẹp
$ai$
của bức ảnh thứ
$i$
$(1 ≤ai≤ 109)$
.


## 💡 Output

Output
In
$- 1$
nếu không có cách nào chọn thỏa mãn
Nếu có thì hãy in ra tổng độ đẹp lớn nhất có thể thỏa mãn các điều kiện trên.


## 🧠 Example

### Input

```text
5 2 3
5 1 3 10 1
```

### Output

```text
18
```


