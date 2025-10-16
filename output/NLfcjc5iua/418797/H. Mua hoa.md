# H. Mua hoa

## 📖 Problem

Hôm nay là ngày 20-10 nên Tấn đi mua hoa để tặng bạn gái. Tiệm hoa Tấn tới gồm
$n$
bông hoa , bông hoa thứ
$i$
có màu sắc là
$ai$
và độ thẫm mỹ là
$bi$
, Tấn dự định mua
$1$
dãy con gồm
$k$
bông hoa trong số
$n$
bông hoa đó sao cho tổng độ thẫm mỹ sau khi mua đúng dãy con gồm
$k$
bông hoa đó là nhiều nhất có thể để gây ấn tượng với bạn gái, nhưng cậu chợt nhớ ra bạn gái mình chỉ thích dãy con gồm
$k$
bông hoa đó nếu trong dãy không tồn tại
$2$
bông hoa bất kì cạnh nhau có cùng
$1$
màu. Hãy giúp Tấn mua được một dãy con gồm đúng
$k$
bông hoa trong
$n$
bông hoa đó mà thỏa mãn sở thích của bạn gái và có tổng độ thẫm mỹ cao nhất.


## 🧩 Input

Input
Dòng đầu gồm
$2$
số nguyên dương
$n$
và
$k$
lần lượt là số bông hoa trong cửa hàng hoa và số lượng bông hoa Khôi định lấy.
$(1 ≤k≤n≤ 20)$
$n$
dòng sau dòng thứ
$i$
gồm
$2$
số nguyên dương
$ai$
và
$bi$
lần lượt là màu và độ thẫm mỹ của bông hoa thứ
$i$
.
$(1 ≤ai,bi≤n)$


## 💡 Output

Output
Hãy in ra độ thẫm mỹ lớn nhất từ dãy con gồm đúng
$k$
bông hoa trong
$n$
bông hoa của cửa hàng hoa mà vẫn thỏa sở thích của bạn gái Tấn, nếu không tồn tại cách lấy nào hãy in ra '-1'.


## 🧠 Example

### Input

```text
3 3
2 1
2 2
3 3
```

### Output

```text
-1
```



## 📝 Note

Note
Với ví dụ 1: Tấn không thể mua các bông hoa theo thứ tự
$(1, 2, 3)$
vì bông hoa ở vị trí
$1$
và
$2$
trùng màu. Tấn cũng không thể mua hoa theo thứ tự
$(1, 3, 2)$
hay
$(2, 3, 1)$
mặc dù nó thỏa không có
$2$
bông hoa bất kì cạnh nhau có cùng
$1$
màu nhưng đây không phải là một dãy con.

