# ZR. Nhật Khôi và những đóa hoa.

## 📖 Problem

Sau bao nhiêu vất vả thể là Nhật Khôi nhà ta đã tới được trường, nhưng thật không may cậu ta đã để quên đóa hoa chuẩn bị trước của mình ở nhà, vì thế câu liền chạy tới tiệm hoa để mua. Tiệm hoa Nhật Khôi tới gồm $$$n$$$ bông hoa , bông hoa thứ $$$i$$$ có màu sắc là $$$a_i$$$ và độ thẫm mỹ là $$$b_i$$$, Nhật Khôi dự định mua $$$1$$$ dãy con gồm $$$k$$$ bông hoa trong số $$$n$$$ bông hoa đó sao cho tổng độ thẫm mỹ sau khi mua đúng dãy con gồm $$$k$$$ bông hoa đó là nhiều nhất có thể để gây ấn tượng với Nhi Thuần, nhưng cậu chợt nhớ ra Nhi Thuần chỉ thích dãy con gồm $$$k$$$ bông hoa đó nếu trong dãy không tồn tại $$$2$$$ bông hoa bất kì cạnh nhau có cùng $$$1$$$ màu. Hãy giúp Khôi mua được một dãy con gồm đúng $$$k$$$ bông hoa trong $$$n$$$ bông hoa đó mà thỏa mãn sở thích của Nhi Thuần và có tổng độ thẫm mỹ cao nhất.


## 🧩 Input

Input
.Dòng đầu gồm số nguyên dương $$$q$$$. $$$(1\leq q\leq 10)$$$
.Sau đó là $$$q$$$ nhóm test mỗi nhóm test có dạng:
+Dòng đầu gồm $$$2$$$ số nguyên dương $$$n$$$ và $$$k$$$ lần lượt là số bông hoa trong cửa hàng hoa và số lượng bông hoa Khôi định lấy.
+$$$n$$$ dòng sau dòng thứ $$$i$$$ gồm $$$2$$$ số nguyên dương $$$a_i$$$ và $$$b_i$$$ lần lượt là màu và độ thẫm mỹ của bông hoa thứ $$$i$$$.$$$(1\leq a_i,b_i\leq n)$$$


## 💡 Output

Output
Với mỗi nhóm test hãy in ra độ thẫm mỹ lớn nhất từ dãy con gồm đúng $$$k$$$ bông hoa trong $$$n$$$ bông hoa của cửa hàng hoa mà vẫn thỏa sở thích của Nhi Thuần, nếu không tồn tại cách lấy nào hãy in ra '-1'.


## 🧠 Example

### Input

```text
1
1 1
1 5
```

### Output

```text
5
```



## 📝 Note

Note
Với ví dụ 1: Nhật Khôi sẽ lấy bông hoa thứ $$$1$$$.
Với ví dụ 2:
.Ở test $$$1$$$: Nhật Khôi không thể mua các bông hoa theo thứ tự $$$(1,2,3)$$$ vì bông hoa ở vị trí $$$1$$$ và $$$2$$$ trùng màu. Nhật Khôi cũng không thể mua hoa theo thứ tự $$$(1,3,2)$$$ hay $$$(2,3,1)$$$ mặc dù nó thỏa không có $$$2$$$ bông hoa bất kì cạnh nhau có cùng $$$1$$$ màu nhưng đây không phải là một dãy con.
.Ở test $$$2$$$: Nhật Khôi sẽ lấy bông hoa thứ $$$2$$$.
.Ở test $$$3$$$: Nhật Khôi chỉ lấy được tối đa $$$1$$$ bông hoa vì nếu không bông hoa ở vị trí thứ $$$1$$$ và thứ $$$2$$$ sẽ trùng màu.
.Ở test $$$4$$$: Nhật Khôi sẽ lấy các bông hoa theo thứ tự $$$(1,2,3,4,5,8)$$$.

