# V. Mã hóa thông tin

## 📖 Problem

Để bảo mật một thông tin là một xâu ký tự có dấu khoảng trắng, người ta áp dụng phương pháp sau: Việc đầu tiên ta sẽ đảo xâu lại, sau đó ta tiến hành xóa toàn bộ các khoảng trắng của xâu, sau đó nếu có ký tự nào in hoa thì chuyển hết thành in thường.
Với cách mã hóa thông tin này ta sẽ rất khó tự giải mã và thậm chí người tạo ra nó cũng không thể tìm lại được xâu ban đầu, chính vì thế người ta đã tạo ra một bảng thông tin, bên trong bảng là các cụm từ của xâu ban đầu (có thể sẽ có 1 số từ lỗi để nếu lộ bảng thì cũng gây nhiễu làm chậm quá trình giải mã). Tuy nhiên để kiểm chứng bảng có lỗi hay không, bạn được giao bảng đấy và một xâu dữ liệu yêu cầu hãy tìm một xâu ban đầu bất kỳ được tạo từ bảng và sau khi mã hóa trở thành xâu dữ liệu cho.
Ví dụ: goemtelotesolcdlohuoytonodybab
cùng bảng thông tin: do, me, Baby, close, to, you, let, go, hold, not
Ta có thể tìm ra xâu ban đầu là: Baby do not you hold me close to let me go.
Lưu ý:
Nếu có nhiều đáp án, hãy in ra một xâu bất kỳ. Một từ trong bảng thông tin có thể được dùng lại nhiều lần


## 🧩 Input

Input
Dòng đầu gồm số nguyên dương $$$n$$$ $$$(1 \leq n \leq 10^4)$$$
Một xâu có độ dài $$$n$$$ là xâu đã được mã hóa.
Dòng tiếp theo gồm một số nguyên dương $$$m$$$ $$$(1 \leq m \leq 10^5)$$$ là số lượng từ trong bảng thông tin
Gồm $$$m$$$ dòng, mỗi dòng là một từ trong bảng thông tin.


## 💡 Output

Output
In ra đáp án, nếu có nhiều đáp án, in ra đáp án bất kỳ.


## 🧠 Example

### Input

```text
30
ariksihsidlihcdnaehsetahgnisol
10
Kira
hates
is
he
losing
death
childish
L
and
Note
```

### Output

```text
Kira is childish and he hates losing
```


