# G. Nhật Khôi và màn tỏ tình.

## 📖 Problem

Thế là đã mọi thứ đã sẵn sàng, giờ Nhật Khôi chỉ cần tỏ tình nữa thui. Trước sự mặt dày của Khôi, Nhi Thuần đã xiu lòng nhưng vì không muốn bị gọi dễ dãi nên Nhi Thuần đã đố Nhật Khôi $$$1$$$ bài toán mà nếu Nhật Khôi giải được thi Nhi Thuần mới đồng ý. Nhi Thuần cho Nhật Khôi $$$1$$$ dãy gồm $$$n$$$ phần tử, phần tử thứ $$$i$$$ có giá trị là $$$a_i$$$, Khôi phải trả lời $$$q$$$ truy vấn, mỗi truy vấn có dạng $$$[l,r]$$$ Nhật Khôi phải trả về khoảng cách xa nhất giữa hai phần tử giống nhau trong đoạn $$$[l ,r]$$$. Hãy giúp Nhật Khôi cưa đỗ Nhi Thuần nhé.


## 🧩 Input

Input
Dòng đầu gồm số $$$n$$$ là số phần tử của mảng.
$$$n$$$ dòng sau dòng thứ $$$i$$$ chứa $$$1$$$ số nguyên dương $$$a_i$$$ là giá trị của phần tử thứ $$$i$$$.$$$(1\leq a_i \leq n)$$$
Dòng tiếp theo gồm số $$$q$$$ là số truy vấn.
$$$q$$$ dòng sau dòng thứ $$$i$$$ chứa $$$2$$$ số nguyên dương $$$l_i$$$ và $$$r_i$$$.$$$(1\leq l_i\leq r_i\leq n)$$$


## 💡 Output

Output
Gồm $$$q$$$ dòng mỗi dòng gồm một số duy nhất là đáp án của $$$q$$$ truy vấn tương ứng theo thứ tự nhập vào.


## 🧠 Example

### Input

```text
5
1
2
2
2
1
5
1 5
1 4
1 3
1 2
1 1
```

### Output

```text
4
2
1
0
0
```



## 📝 Note

Note
. Mảng đã cho gồm $$$5$$$ phần tử theo thứ tự như sau: $$$[1,2,2,2,1]$$$.
. Ở truy vấn $$$1$$$:
+Số $$$1$$$ gần nhất ở vị trí số $$$1$$$ và xa nhất ở vị trí số $$$5$$$. Khoảng cách giữa chúng là $$$5 - 1 = 4$$$.
+Số $$$2$$$ gần nhất ở vị trí số $$$2$$$ và xa nhất ở vị trí số $$$4$$$. Khoảng cách giữa chúng là $$$4 - 2 = 2$$$.
Vì $$$4$$$ lớn nhất nên đáp án là $$$4$$$.
. Ở truy vấn $$$2$$$:
+Số $$$1$$$ gần nhất ở vị trí số $$$1$$$ và xa nhất ở vị trí số $$$1$$$. Khoảng cách giữa chúng là $$$1 - 1 = 4$$$.
+Số $$$2$$$ gần nhất ở vị trí số $$$2$$$ và xa nhất ở vị trí số $$$4$$$. Khoảng cách giữa chúng là $$$4 - 2 = 2$$$.
Vì $$$2$$$ lớn nhất nên đáp án là $$$2$$$.
. Ở truy vấn $$$4$$$:
+Số $$$1$$$ gần nhất ở vị trí số $$$1$$$ và xa nhất ở vị trí số $$$1$$$. Khoảng cách giữa chúng là $$$1 - 1 = 0$$$.
+Số $$$2$$$ gần nhất ở vị trí số $$$2$$$ và xa nhất ở vị trí số $$$2$$$. Khoảng cách giữa chúng là $$$2 - 2 = 0$$$.
Vì $$$0$$$ lớn nhất nên đáp án là $$$0$$$.

