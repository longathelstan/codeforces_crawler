# D. Cây phả hệ 2

## 📖 Problem

Cho cây phả hệ gồm $$$n$$$ người, người thứ $$$i$$$ sẽ có tối đa một cha là $$$p_i$$$ và có tên là $$$s_i$$$, $$$p_i=0$$$ nghĩa là người đó đứng đầu cây phả hệ, có thể có nhiều người cùng đứng đầu trong cây phả hệ.
Cha thứ $$$1$$$ của $$$x$$$ được định nghĩa là cha trực tiếp của $$$x$$$
Cha thứ $$$2$$$ của $$$x$$$ được định nghĩa là cha của cha của $$$x$$$
Cha thứ $$$3$$$ của $$$x$$$ được định nghĩa là cha của cha của cha của $$$x$$$
...
Bạn có $$$q$$$ truy vấn, truy vấn thứ $$$i$$$ gồm $$$v_i$$$ và $$$k_i$$$, bạn phải xác định có bao nhiêu người có tên phân biệt có cha thứ $$$k$$$ của mình là người thứ $$$v_i$$$.
Yêu cầu:
Với mỗi truy vấn, hãy đưa ra câu trả lời.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên dương $$$n$$$ $$$(1\leq n\leq 10 ^ 5)$$$
$$$n$$$ dòng tiếp theo, dòng thứ $$$i$$$ gồm xâu $$$s_i$$$ và cha $$$p_i$$$ của người thứ $$$i$$$ $$$(1\leq |s_i|\leq 20, 0\leq p_i\leq n)$$$. Các ký tự trong tên $$$s_i$$$ là các chữ cái in thường trong bảng chữ cái tiếng anh.
Dòng tiếp theo gồm số $$$q$$$ $$$(1\leq q\leq 10 ^ 5)$$$
$$$q$$$ dòng tiếp theo mỗi dòng gồm $$$2$$$ số $$$v_i$$$ và $$$k_i$$$ $$$(1\leq v_i, k_i\leq n)$$$


## 💡 Output

Output
Gồm $$$q$$$ dòng ứng với $$$q$$$ truy vấn cần tìm theo thứ tự đầu vào


## 🧠 Example

### Input

```text
6pasha 0gerald 1gerald 1valera 2igor 3olesya 151 11 21 33 16 1
```

### Output

```text
22010
```


