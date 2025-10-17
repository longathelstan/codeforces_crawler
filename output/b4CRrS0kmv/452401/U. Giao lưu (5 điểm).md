# U. Giao lưu (5 điểm)

## 📖 Problem

Có
$N$
thành phố ở đất nước ABC, được đánh số từ
$0$
tới
$N- 1$
. Ngoài ra, còn có
$M$
con đường hai chiều, được đánh số từ
$0$
tới
$M- 1$
. Mỗi con đường nối hai thành phố khác nhau. Con đường thứ
$i$
kết nối thành phố thứ
$Ui$
với thành phố thứ
$Vi$
và tiêu thụ
$Wi$
đơn vị xăng khi đi qua bằng ô tô. Các thành phố được kết nối với nhau đảm bảo có thể đi lại giữa bất kỳ cặp thành phố nào thông qua các con đường này.
Đối với mỗi ngày trong
$Q$
ngày tiếp theo, một cặp thành phố muốn thiết lập quan hệ chính trị. Cụ thể, vào ngày thứ
$j$
, thành phố thứ
$Xj$
muốn thiết lập mối quan hệ với thành phố thứ
$Yj$
.
Để thực hiện điều này, thành phố thứ
$Xj$
sẽ
đi đến thành phố
thứ
$Yj$
bằng ô tô. Tương tự, thành phố Y_j cũng sẽ
đi đến thành phố
thứ X_j bằng ô tô. Tuy nhiên, có một số nguyên sau được đưa ra:
- Để tránh ùn tắc, Cả hai ô tô sẽ
không
ở trong cùng một thành phố vào cùng một thời điểm.
- Cả hai ô tô cũng không nên đi cùng
một con đường
theo hướng ngược nhau cùng một thời điểm.
- Khi ô tô đi trên một con đường thì phải
đi hết
con đường và đi đến thành phố đích (nói cách khác, ô tô không được phép quay đầu xe ở giữa đường).
-Ô tô được phép đến cùng một thành phố hay đi một con đường
nhiều
hơn một lần. Ngoài ra, ô tô cũng có thể
chờ
ở bất kì thành phố nào vào bất kỳ thời điểm nào.
Vì ô tô có dung tích bình nhiên liệu lớn sẽ đắt tiền nên cả hai thành phố muốn chọn tuyến đường cho cả hai ô tô sao cho dung tích bình nhiên liệu lớn nhất của hai ô tô là nhỏ nhất.
Ở mỗi thành phố đều có các trạm xăng với nguồn cung cấp vô hạn, do đó, dung tiếp bình nhiên liệu mà ô tô cần là mức tiêu thụ xăng lớn nhất trong tất cả các con đường mà ô tô đi qua.


## 🧩 Input

Input
Dòng đầu tiên là hai số nguyên dương
$N,M$
$(2 ≤N≤ 105,N- 1 ≤M≤ 2 * 105)$
là số thành phố và số các con đường;
Dòng thứ
$i$
$(1 ≤i≤M)$
trong số
$M$
dòng tiêp theo gồm ba số
$U(i- 1),V(i- 1),W(i- 1)$
$(0 ≤U(i- 1)<V(i- 1)<N, 1 ≤W(i- 1)≤ 109)$
mô tả một con đường hai chiều.
Dữ liệu đảm bảo rằng có nhiều nhất một con đường nối giữa mỗi cặp thành phố và có thể đi lại giữa bất kỳ cặp thành phố nào thông qua các con đường;
Dòng tiếp theo là một số
$Q$
$(1 ≤Q≤ 5)$
là số ngày xảy ra sự kiện.
$Q$
dòng tiếp theo, mỗi dòng gồm
$2$
số nguyên
$Xi,Yi$
$(1 ≤Xi≠Yi≤N)$
.


## 💡 Output

Output
Gồm
$Q$
dòng, dòng thứ
$i$
là số nguyên biểu diễn giá trị nhỏ nhất của dung tích bình nhiên liệu lớn nhất của cả hai ô tô mà một người đại diện từ thành phố X có thể đến được thành phố thứ Y và ngược lại thỏa mãn quy tắc trong đề, hoặc in ra -1 nếu không tồn tại cách thực hiện.


## 🧠 Example

### Input

```text
5 4
0 1 2
1 2 3
2 3 1
3 4 4
2
0 4
0 3
```

### Output

```text
-1
-1
```



## 📝 Note

Note
Test số
$2$
:
Ở sự kiện thứ nhất, đầu tiên, ô tô từ thành phố thứ nhất có thể đến thành phố thứ ba. Tiếp theo, ô tô từ thành phố thứ hai có thể đi đến thành phố thứ nhất và ô tô từ thành phố thứ ba có thể đến thành phố thứ hai. Do đó, bình nhiên liệu tối da của hai ô tô là 3 đơn vị xăng.
Ở sự kiện thứ hai, bất kỳ ô tô nào đi đến hoặc đi từ thành phố thứ tư đều phải cần 10 đơn vị xăng.
![](https://espresso.codeforces.com/d556f32ec87102d6723c41d3fa468a4d89cb90a1.png)

