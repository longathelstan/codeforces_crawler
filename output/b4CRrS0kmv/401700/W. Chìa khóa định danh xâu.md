# W. Chìa khóa định danh xâu

## 📖 Problem

Vậy vấn đề mã hóa xâu coi như xong một phần, tuy nhiên vấn đề là bảng thông tin và xâu mã hóa có thể cho ra đời tương đối xâu đầu vào có thể có, vậy bài toán đặt ra làm cách nào để biết đâu là thông tin chính xác họ muốn truyền tải. Để làm điều đó bằng cách đơn giản nhất, họ tạo ra các xâu đầu vào, sắp xếp theo thứ tự từ điển và đánh số thứ tự từng xâu, và họ lưu số thứ tự của thông tin lại. Bây giờ số đó nó giống như một chiếc chìa khóa giúp xác định đâu là thông tin cần truyền tải.
Thế nếu chìa khóa bị lộ thì cũng như không nên họ xây dựng một bài toán mã hóa để giữ bí mật cho số thứ tự. Họ tạo ra một dãy số có $$$n$$$ số nguyên dương, giá trị MEX của dãy này chính là chiếc chìa khóa được ẩn giấu. Tuy nhiên nếu vậy vẫn còn khá đơn giản, họ có một quy trình sau cho phép người dùng có thể đổi chìa khóa tuy nhiên vẫn có thể xác định được số thứ tự, đó là họ chọn một nguyên dương $$$x$$$, sau đó thực hiện xor tất cả số nguyên dương trong dãy cho $$$x$$$ và bùm họ đã thay đổi được giá trị MEX tuy nhiên với bảng thông tin giá trị x họ vẫn tìm được chìa thôi. Và giờ bạn được giao nhiêm vụ test hệ thống tốc độ xử lý, cho $$$q$$$ ngày, mỗi ngày là họ đưa một số nguyên dương $$$x$$$ bạn được yêu cầu tìm MEX sau khi tất cả phần tử của dãy xor với $$$x$$$.
lưu ý:
từ ngày thứ $$$i$$$ trở đi, tất cả các giá trị $$$A_j$$$ đều được gán là $$$A_j=A_j$$$ ^ $$$(x_i)$$$
Mex của một dãy là số nguyên không âm nhỏ nhất không xuất hiện trong dãy.


## 🧩 Input

Input
Cho số nguyên dương $$$n$$$ và $$$q$$$ $$$(1 \leq n,q \leq 3*10^5)$$$.
Một dãy số gồm $$$n$$$ số nguyên dương $$$A_i$$$ $$$(1 \leq A_i \leq 3*10^5)$$$.
Gồm $$$q$$$ dòng, mỗi dòng là một số nguyên dương $$$x$$$.


## 💡 Output

Output
Gồm $$$q$$$ dòng, số thứ $$$i$$$ là $$$Mex$$$ sau i ngày.


## 🧠 Example

### Input

```text
5 4
0 1 5 6 7
1
1
4
5
```

### Output

```text
2
2
0
2
```


