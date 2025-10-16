# Z. Thanh và kì nghỉ(6 điểm)

## 📖 Problem

Thanh là một người rất thích đi du lịch, Thanh muốn đi khắp mọi nơi từ Bắc vào Nam và đợt này Thanh sẽ đi du lịch ở một hòn đảo tại Khánh Hòa.
Kì nghỉ của Thanh gồm $$$n$$$ ngày, để phục vụ cho thú vui tao nhã của mình thì Thanh đã nghĩ ra $$$3$$$ hoạt động để làm mỗi ngày đó là:
$$$1$$$: Đi bơi. Nếu Thanh đi bơi ở ngày thứ $$$i$$$ thì độ vui mà Thanh nhận được ngày hôm đó là $$$a_i$$$.
$$$2$$$: Bắt bọ. Nếu Thanh bắt bọ ở ngày thứ $$$i$$$ thì độ vui mà Thanh nhận được ngày hôm đó là $$$b_i$$$.
$$$3$$$: Xây lâu đài cát. Nếu Thanh xây lâu đài cát ở ngày thứ $$$i$$$ thì độ vui mà Thanh nhận được ngày hôm đó là $$$c_i$$$.
Do thời gian có hạn nên mỗi ngày Thanh chỉ được làm $$$1$$$ trong $$$3$$$ hoạt động trên. Vì là một người dễ chán nên Thanh sẽ không làm lại hoạt động mà mình đã làm ngày hôm trước. Bạn hãy giúp Thanh tính độ vui lớn nhất mà Thanh có thể nhận được trong $$$n$$$ ngày nghỉ để kì nghỉ của Thanh được trọn vẹn nhé.


## 🧩 Input

Input
Dòng đầu gồm $$$n$$$ $$$(1\leq n\leq 10 ^ 5)$$$, là số ngày trong kì nghỉ của Thanh.
Dòng thứ $$$i$$$ trong $$$n$$$ dòng tiếp theo gồm $$$a_i$$$, $$$b_i$$$, $$$c_i$$$ $$$(0\leq a_i,b_i,c_i\leq 10^9)$$$, lần lượt là độ vui vẻ Thanh nhận được nếu đi bơi, bắt bọ, xây lâu đài cát trong ngày thứ $$$i$$$.


## 💡 Output

Output
Một dòng chứa độ vui lớn nhất mà Thanh có thể nhận được sau $$$n$$$ ngày nghỉ.


## 🧠 Example

### Input

```text
2
0 2 3
0 2 4
```

### Output

```text
6
```



## 📝 Note

Note
Ở test $$$1$$$:
Cách tối ưu nhất là: bắt bọ ở ngày thứ nhất, xây lâu đài cát ở ngày thứ hai. Tổng độ vui nhận được là $$$2 + 4 = 6$$$.
Thanh không thể đi xây lâu đài cát ở cả $$$2$$$ ngày vì nếu vậy sẽ không thỏa không có $$$2$$$ ngày liên tiếp làm cùng $$$1$$$ hoạt động.
Ở test $$$2$$$:
Cách tối ưu nhất là: xây lâu đài cát ở ngày thứ nhất, bắt bọ ở ngày thứ hai, xây lâu đài cát ở ngày thứ ba. Tổng độ vui nhận được là $$$70 + 50 + 90 = 210$$$.
Ở test $$$3$$$:
Cách tối ưu nhất là: xây lâu đài cát -> đi bơi -> bắt bọ -> đi bơi -> xây lâu đài cát -> bắt bọ -> đi bơi. Tổng độ vui nhận được là $$$8 + 8 + 5 + 7 + 8 + 3 + 7 = 46$$$.

