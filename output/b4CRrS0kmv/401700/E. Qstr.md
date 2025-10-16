# E. Qstr

## 📖 Problem

Bờm là một học sinh chuyên tin. Hôm nay Bờm được thầy dạy về thứ tự từ điển và các bài toán liên quan. Sau một hồi giảng giải và định nghĩa thứ tự từ điển là gì, thầy lấy ngay một ví dụ cho lớp. Thầy viết lên bảng 2 chuỗi kí tự dài ơi là dài, và hỏi cả lớp "Chuỗi thứ nhất có thứ tự từ điển như thế nào đối với chuỗi thứ hai: đứng trước ('<'), đứng sau ('>') hay bằng nhau ('=') ???".
Cả lớp thì đang hoang mang, vì cũng chẳng có ai hiểu được định nghĩa "Thứ tự từ điển là gì?" của thầy, nói gì đến việc giải bài tập. Nhưng Bờm thì ngược lại, do đã chuẩn bị và xem bài trước ở nhà nên đã trả lời ngay được câu hỏi của thầy sau khi thấy vừa dứt lời. Bờm ngồi chơi trong lúc mọi người đang thảo luận xôn xao, nên đã tạo thêm một số ví dụ nữa về thứ tự từ điển để có thể hiểu sâu thêm về bài học. Nhìn ngay lên bảng, Bờm phát hiện từ 2 xâu trong ví dụ của thầy, Bờm có thể tự sinh ra rất nhiều ví dụ khác. Cụ thể hơn, Bờm chọn một xâu con trong xâu thứ nhất và một xâu con trong xâu thứ hai, thế là có ngay một cặp xâu để mà so sánh. Xâu con ở đây được hiểu là một dãy các ký tự liên tiếp.
Thế là Bờm liên tục sinh ra các ví dụ và trả lời chúng. Bờm càng làm càng nhạy, và trả lời các câu hỏi về thứ tự từ điển càng nhanh. Đến nỗi trong 1 giây Bờm đã có thể trả lời đến tất cả là 10^6 câu hỏi!
Yêu cầu
Cho 2 xâu kí tự A và B (chỉ gồm các kí tự từ 'a' đến 'z') và một danh sách gồm Q câu hỏi có dạng (l, r, u, v), với ý nghĩa cần so sánh thứ tự từ điển của xâu con A[l..r] và B[u..v] (các kí tự của một xâu được đánh số từ trái qua phải, bắt đầu bằng 1; và ký hiệu A[l..r] thể hiện xâu con từ kí tự thứ l đến r của xâu A).
Bạn hãy viết một chương trình mô tả lại hoạt động trả lời các câu hỏi của Bờm.
Lưu ý
Xâu a1a2...an (ai là kí tự thứ i trong xâu a) có thứ tự từ điển nhỏ hơn xâu b1b2... bm nếu:
n < m và ai = bi với mọi i (1 ≤ i ≤ n) hoặc
với k (1 ≤ k ≤ min(m, n)) là giá trị nhỏ nhất thỏa ak ≠ bk thì ak < bk Hai xâu có thứ tự từ điển bằng nhau nếu không thể xác định được xâu nào có thứ tự từ điển nhỏ hơn.


## 🧩 Input

Input
Dòng đầu tiên gồm 2 số nguyên dương LA LB là độ dài của xâu A và xâu B.
Dòng thứ hai là xâu A.
Dòng thứ ba là xâu B.
Dòng tư là số nguyên dương Q - số câu hỏi trong danh sách
Q dòng tiếp theo, mỗi dòng gồm 4 số nguyên dương l r (1 ≤ l ≤ r ≤ LA) u v (1 ≤ u ≤ v ≤ LB) mô tả một câu hỏi cần trả lời.
LA, LB, Q ≤ 10^6.
|A| + |B| ≤ 10^6


## 💡 Output

Output
Với mỗi truy vấn, in ra 1 ký tự '=', '>' hoặc '<'. Tất cả các câu trả lời được viết trên một dòng.


## 🧠 Example

### Input

```text
13 14

bomthichdacau

bomthichdabanh

3

1 10 1 10

1 10 1 11

1 11 1 11
```

### Output

```text
=<>
```


