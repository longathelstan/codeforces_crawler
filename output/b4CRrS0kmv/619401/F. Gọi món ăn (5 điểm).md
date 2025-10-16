# F. Gọi món ăn (5 điểm)

## 📖 Problem

Bình An đang rất đói và cô quyết định ăn trưa tại căng tin nhà trường. Căng tin có N món ăn khác nhau và thật đặc biệt: món ăn thứ i có hai giá $$$A_i$$$ và $$$B_i$$$ $$$(i=1,2,...,N)$$$ trong đó khách hàng phải trả $$$A_i$$$ nếu $$$i$$$ là món ăn đầu tiên được gọi trong bữa, các trường hợp còn lại món $$$i$$$ có giá $$$B_i$$$. Vì rất đói nên Bình An không thể quyết định là chọn những món nào để ăn. Cô ta quyết định hỏi bạn rằng nếu ăn đúng $$$k$$$ món $$$(1 \le k \le N)$$$ thì phải trả số tiền ít nhất là bao nhiêu?


## 🧩 Input

Input
*
Dòng đầu tiên ghi số nguyên dương N $$$(2 \le N \le 5*10^5)$$$ là số lượng các món ăn.
*
$$$N$$$ dòng tiếp theo, dòng thứ $$$i$$$ chứa hai số nguyên dương $$$A_i$$$ và $$$B_i$$$ $$$(1 \le A_i,B_i \le 10^9)$$$ là giá của món thứ $$$i$$$ theo mô tả ở trên.


## 💡 Output

Output
*
Ghi #N# dòng, dòng thứ #k# ghi số tiền tối thiểu phải trả khi ăn đúng #k# món ăn trong số #N# món ăn của căng tin.


## 🧠 Example

### Input

```text
3
14 5
9 3
10 5
```

### Output

```text
9
13
18
```


