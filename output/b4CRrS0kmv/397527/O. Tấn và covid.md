# O. Tấn và covid

## 📖 Problem

Một loại virus mới có tên là "CodeVid-23" đã lây lan giữa các lập trình viên. Tấn, là một lập trình viên, không thể tránh khỏi nó.
Có $$$n$$$ triệu chứng được đánh số từ 1 đến $$$n$$$ có thể xuất hiện khi bị nhiễm. Ban đầu, Tấn có một số triệu chứng. Anh ấy đã đến hiệu thuốc và mua $$$m$$$ loại thuốc.
Với mỗi loại thuốc, số ngày cần phải uống và tập hợp các triệu chứng mà thuốc đó loại bỏ được biết trước. Không may, các loại thuốc thường có tác dụng phụ. Do đó, với mỗi loại thuốc, tập hợp các triệu chứng xuất hiện khi uống thuốc đó cũng đã được biết.
Sau khi đọc hướng dẫn, Tấn nhận ra rằng việc uống nhiều loại thuốc cùng lúc là rất không lành mạnh.
Tấn muốn được chữa khỏi càng sớm càng tốt. Do đó, anh ấy hỏi bạn tính toán số ngày tối thiểu để loại bỏ tất cả các triệu chứng, hoặc thông báo rằng việc đó là không thể.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên duy nhất $$$t$$$ ($$$1 \le t \le 100$$$) — số lượng bài toán con.
Sau đó là mô tả của các bài toán con.
Dòng đầu tiên của mỗi bài toán con chứa hai số nguyên $$$n, m$$$ ($$$1 \le n \le 10$$$, $$$1 \le m \le 10^3$$$) — số triệu chứng và số loại thuốc, tương ứng.
Dòng thứ hai của mỗi bài toán con chứa một chuỗi độ dài $$$n$$$ bao gồm các ký tự $$$0$$$ và $$$1$$$ — mô tả triệu chứng của Tấn. Nếu ký tự thứ $$$i$$$ là $$$1$$$, Tấn có triệu chứng thứ $$$i$$$, nếu không là $$$0$$$.
Tiếp theo là $$$3 \cdot m$$$ dòng — mô tả các loại thuốc.
Mỗi mô tả thuốc bao gồm:
- Dòng đầu tiên chứa một số nguyên $$$d$$$ ($$$1 \le d \le 10^3$$$) — số ngày thuốc cần được uống.
- Hai dòng tiếp theo của mô tả thuốc chứa hai chuỗi độ dài $$$n$$$, bao gồm các ký tự $$$0$$$ và $$$1$$$ — mô tả triệu chứng thuốc loại bỏ và tác dụng phụ của thuốc.
- Dòng đầu tiên của hai dòng này mô tả triệu chứng thuốc loại bỏ: $$$1$$$ ở vị trí $$$i$$$ có nghĩa là thuốc loại bỏ triệu chứng thứ $$$i$$$, còn $$$0$$$ có nghĩa là không loại bỏ triệu chứng thứ $$$i$$$.
- Dòng thứ hai mô tả tác dụng phụ của thuốc: $$$1$$$ ở vị trí $$$i$$$ có nghĩa là triệu chứng thứ $$$i$$$ xuất hiện sau khi uống thuốc, còn $$$0$$$ có nghĩa là triệu chứng đó không xuất hiện.
Lưu ý rằng nếu một loại thuốc loại bỏ triệu chứng nào đó, triệu chứng đó sẽ không có mặt trong tác dụng phụ.
Tổng số $$$m$$$ của tất cả các bài toán con không vượt quá $$$10^3$$$.


## 💡 Output

Output
Với mỗi bài toán con, in ra một số nguyên trên một dòng riêng biệt — số ngày tối thiểu Tấn cần để loại bỏ tất cả các triệu chứng. Nếu điều này không thể thực hiện được, in ra $$$-1$$$.


## 🧠 Example

### Input

```text
45 410011310000001103001010000030101000100511010001004 1000010101101002 21121001301102 311301103100041001
```

### Output

```text
8
0
-1
6
```



## 📝 Note

Note
s Trong ví dụ đầu tiên, chúng ta có thể đầu tiên sử dụng thuốc số 4, sau đó các triệu chứng sẽ trở thành "00101". Sau đó, sử dụng thuốc số 2, tất cả các triệu chứng sẽ biến mất, và tổng số ngày là $$$5 + 3 = 8$$$. Một lựa chọn khác là áp dụng thuốc theo thứ tự $$$1, 3, 2$$$. Trong trường hợp này, tất cả triệu chứng cũng sẽ biến mất, nhưng tổng số ngày sẽ là $$$3 + 3 + 3 = 9$$$.
Trong ví dụ thứ hai, ban đầu không có triệu chứng nào, vì vậy quá trình điều trị sẽ mất 0 ngày.
Trong ví dụ thứ ba, không có lựa chọn nào để loại bỏ tất cả triệu chứng.

