# C. Chi và bức tranh(7 điểm)

## 📖 Problem

Chi là một người có khiếu nghệ thuật cao, Chi luôn nhìn mọi vật theo nhiều chiều hướng khác nhau. Hôm nay, Chi có dịp ghé vào viện bảo tàng nổi tiếng nhất Việt Nam để ngắm những bức tranh. Trong những bức tranh muôn màu, muôn vẻ ở viện bảo tàng thì đã có một bức tranh lọt vào tầm mắt xanh của Chi.
Bức tranh đó là hình $$$1$$$ cái cây gồm $$$n$$$ đỉnh, $$$n - 1$$$ cạnh hai chiều, liên thông với nhau. $$$n$$$ đỉnh này đều chưa có màu, Chi muốn tô màu từng đỉnh của bức tranh này bằng một trong $$$2$$$ màu $$$đen$$$ và $$$trắng$$$, nhưng theo Chi nếu $$$2$$$ đỉnh được nối với nhau thì không được có chung màu $$$đen$$$ vì như vậy là biểu hiện của điềm xui.
Chi muốn nhờ bạn tính xem có bao nhiêu cách tô hết $$$n$$$ đỉnh mà không có biểu hiện của điềm xui. Vì số cách có thể rất lớn nên hãy in đáp án chia dư cho $$$10^9+7$$$.


## 🧩 Input

Input
Dòng đầu gồm $$$n$$$ $$$(1\leq n \leq 10^5)$$$, là số đỉnh của cây.
Dòng thứ $$$i$$$ trong $$$n$$$ dòng tiếp theo gồm $$$u_i$$$ và $$$v_i$$$ $$$(1 \leq u_i<v_i \leq n)$$$, thể hiện có cạnh nối đỉnh $$$u_i$$$ tới $$$v_i$$$.


## 💡 Output

Output
Gồm một dòng duy nhất gồm số cách tô, chia dư cho $$$10^9 + 7$$$.


## 🧠 Example

### Input

```text
3
1 2
2 3
```

### Output

```text
5
```



## 📝 Note

Note
Ở test $$$1$$$: Có $$$5$$$ cách tô như trong hình.
![](https://espresso.codeforces.com/9c0a8a95871546aed2898c119d7ae800e48410f0.png)
Ở test $$$2$$$: Có $$$9$$$ cách tô như trong hình.
![](https://espresso.codeforces.com/273b961141de4f685a33890ee13ca6c896581018.png)

