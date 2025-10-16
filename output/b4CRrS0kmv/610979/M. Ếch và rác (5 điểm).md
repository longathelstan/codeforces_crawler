# M. Ếch và rác (5 điểm)

## 📖 Problem

Cuộc sống an nhàn với thức ăn đầy đủ và đa dạng tại các đống rác thành phố đã sinh ra một thế hệ các chú ếch đột biến gen. Trên con đường dẫn đến bãi rác thành phố có
$n$
đống rác, đánh số bắt đầu từ
$0$
đến
$n- 1$
từ trái qua phải. Đống rác thứ
$i$
có độ dài
$hi$
. Trên mỗi đống rác hiện có một chú ếch sống. Đến tuổi trưởng thành, mỗi chú ếch đều muốn đi tìm một chỗ sống tốt đẹp hơn bằng cách nhảy sang đống rác cao hơn gần nhất bên phải. Chú ếch ở đống rác thứ
$i$
có thể thực hiện được
$Ji$
bước nhảy (
$0 <Ji≤n)$
. Bãi rác thành phố có độ cao lớn hơn mọi đống rác trên đường. Ta ký hiệu độ cao này là
$- 1$
(vì không cần và cũng không thể biết chính xác).
Ví dụ, có 8 đống rác với độ cao tương ứng từ trái qua phải là
$3, 1, 4, 5, 6, 2, 3$
và
$8$
. Số bước nhảy mỗi chú ếch có thể thực hiện là
$1, 2, 1, 3, 4, 2, 1, 2$
. Sau khi di chuyển hết khả năng của mình, chú ếch ở đống rác
$0$
sẽ tới được đống rác
$2$
với độ cao là
$4$
, còn chú ếch ở đống rác
$3$
- tới được bãi rác thành phố (độ cao
$- 1)$
.
Yêu cầu:
Hãy xác định độ cao nơi ở mới của mỗi chú ếch.


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên
$n$
$(1 ≤n≤ 2 * 106)$
.
Dòng thứ
$2$
chứa
$n$
số nguyên
$h1,h2, ...,hn$
$(1 ≤hi≤ 109)$
.
Dòng thứ
$3$
chứa
$n$
số nguyên
$J1,J2, ...,Jn$
$(1 ≤Ji≤n)$
.


## 💡 Output

Output
Một dòng chứa
$N$
số nguyên - độ cao ở mới của mỗi chú ếch


## 🧠 Example

### Input

```text
8
3 1 4 5 6 2 3 8
1 2 1 3 4 2 1 2
```

### Output

```text
4 5 5 -1 -1 8 8 -1
```


