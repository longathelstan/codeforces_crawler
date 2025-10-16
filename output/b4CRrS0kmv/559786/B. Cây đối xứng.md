# B. Cây đối xứng

## 📖 Problem

Cho một cái cây $$$n$$$ đỉnh, $$$n-1$$$ cạnh và có gốc là $$$1$$$, đỉnh thứ $$$i$$$ sẽ có ký tự ghi trên đó là $$$f_i$$$.
Bạn có $$$q$$$ truy vấn, mỗi truy vấn gồm $$$2$$$ số $$$v$$$ và $$$k$$$, bạn phải xem thử nếu sử dụng mọi ký tự của mọi đỉnh trong cây con gốc $$$v$$$ mà có khoảng cách tới đỉnh $$$1$$$ là $$$k$$$ thì có thể sắp xếp chúng lại tuỳ ý để tạo ra xâu đối xứng hay không. Biết khoảng cách từ đỉnh $$$1$$$ tới chính nó là $$$1$$$, tới các con trực tiếp của nó là $$$2$$$, ....
Yêu cầu:
Đưa "Yes" nếu có thể tạo xâu đối xứng thoả các điều kiện của truy vấn đó, ngược lại đưa "No"


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên dương $$$n$$$ và $$$q$$$ $$$(1\leq n,q\leq 5 * 10 ^5)$$$
Dòng tiếp theo gồm $$$n-1$$$ số, số thứ $$$i$$$ là giá trị $$$u_i$$$ thể hiện có cạnh hai chiều nối từ $$$u_i$$$ tới $$$i+1$$$.
Dòng tiếp theo gồm $$$n$$$ ký tự, ký tự thứ $$$i$$$ thể hiện ký tự $$$f_i$$$ của đỉnh $$$i$$$ ($$$f_i$$$ là chữ cái in thường trong tiếng anh)
$$$q$$$ dòng tiếp theo mỗi dòng gồm $$$2$$$ số $$$v_i$$$ và $$$k_i$$$ $$$(1\leq v_i, k_i\leq n)$$$


## 💡 Output

Output
Gồm $$$q$$$ dòng ứng với $$$q$$$ truy vấn cần tìm theo thứ tự đầu vào


## 🧠 Example

### Input

```text
6 51 1 1 3 3zacccd1 13 34 16 11 2
```

### Output

```text
YesNoYesYesYes
```


