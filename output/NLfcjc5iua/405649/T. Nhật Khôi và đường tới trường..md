# T. Nhật Khôi và đường tới trường.

## 📖 Problem

Mặt trời đã mọc, gà đã gáy, và Nhật Khôi nhà ta đã thức giấc sau một giấc ngủ say, cậu đã chuẩn bị tắm rửa và sửa soạn đây đủ để đi tới trường và thực hiện kế hoạch của mình. Quãng đường từ nhà Khôi tới trường có thể biểu diễn dưới dạng 1 ma trận $$$n x n$$$. Nhà Khôi ở ô $$$(1 , 1)$$$ được kí hiệu là 'K', trường Khôi ở ô $$$(n , n)$$$ được kí kiệu là 'S'. Các ô còn lại của ma trận mỗi ô có thể là 1 trong 2 kí hiệu sau: '.' nếu ô đó là ô đất trống, '*' nếu ô đó có xe đậu.
Khôi xuất phát từ nhà mình và muốn tới trường càng sớm càng tốt để có nhiều thời gian chuẩn bị. Từ $$$1$$$ ô cậu có thể đi tới $$$4$$$ ô kề cạnh nếu ô kề cạnh không nằm ngoài bảng $$$n x n$$$ và ô đó không có xe đậu. Vì tối hôm qua cậu ngủ đủ giấc nên sáng nay Nhật Khôi rất năng động cậu có thể thực hiện $$$k$$$ lần nhảy qua $$$1$$$ chiếc xe đang đậu. Cậu chỉ có thể thực hiện lượt nhảy của mình nếu trước mặt cậu chỉ có duy nhất $$$1$$$ chiếc xe và sau khi nhảy qua chiếc xe đó cậu sẽ đáp ở $$$1$$$ ô đất trống nằm trong bảng $$$n x n$$$. Mỗi lần cậu bước qua một ô kề cạnh hoặc thực khiện bước nhảy của mình đều tốn $$$1$$$ đơn vị thời gian. Hãy xác định thời gian sớm nhất mà Nhật Khôi có thể tới trường nếu tuân thủ theo các qui tắt trên.


## 🧩 Input

Input
.Dòng đầu gồm số nguyên dương $$$q$$$ là số lượng số test. $$$(1\leq q\leq 10)$$$
.Sau đó là $$$q$$$ nhóm test mỗi nhóm test có dạng:
+Dòng đầu gồm số $$$2$$$ số $$$n$$$ và k thể hiện kích thước ma trận $$$nxn$$$ và số lần Khôi có thể thực hiện bước nhảy của mình.$$$(1\leq n\leq 500)$$$
+$$$n$$$ dòng sau mỗi dòng gồm $$$n$$$ kí tự dính liền nhau thể hiện ma trận $$$n x n$$$.


## 💡 Output

Output
Với mỗi nhóm truy vấn trong mỗi nhóm test in ra $$$1$$$ số duy nhất là thời gian ngắn nhất để Nhật Khôi tới được trường.


## 🧠 Example

### Input

```text
1
2 0
K*
*S
```

### Output

```text
-1
```



## 📝 Note

Note
Với ví dụ 1: Nhật Khôi sẽ bị kẹt tại ô $$$(1,1)$$$.
Với ví dụ 2:
.Ở test $$$1$$$: Đây là $$$1$$$ trong các cách đi hợp lệ $$$(1,1)$$$ -> $$$(1,2)$$$ -> $$$(1,3)$$$ -> $$$(2,3)$$$ ->$$$(3,3)$$$.
.Ở test $$$2$$$: Đây là $$$1$$$ trong các cách đi hợp lệ $$$(1,1)$$$ -> $$$(3,1)$$$ -> $$$(3,2)$$$ -> $$$(3,3)$$$.
.Ở test $$$3$$$: Nhật Khôi sẽ bị kẹt tại ô $$$(1,1)$$$.
.Ở test $$$4$$$: Đây là $$$1$$$ trong các cách đi hợp lệ $$$(1,1)$$$ -> $$$(3,1)$$$ -> $$$(3,2)$$$ -> $$$(3,3)$$$.
.Ở test $$$5$$$: Nhật Khôi cần ít nhất $$$2$$$ lần nhảy để tới đích.
.Ở test $$$6$$$: Nhật Khôi không thể nhảy $$$1$$$ lần qua $$$2$$$ xe.
.Ở test $$$7$$$: Nhật Khôi không nhất thiết phải dùng lượt nhảy của mình mà vẫn tới trường nhanh nhất.
.Các test $$$2,4,5,6,7$$$ sẽ không xuất hiện trong $$$50\%$$$ số test có $$$k = 0$$$.

