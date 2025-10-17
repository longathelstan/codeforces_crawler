# B. Truyền tin

## 📖 Problem

Một lớp gồm
$N$
học sinh, mỗi học sinh cho biết những bạn mà học sinh đó có thể liên lạc được (chú ý liên lạc này là liên lạc một chiều bạn
$u$
có thể gửi tin tới bạn
$v$
nhưng bạn
$v$
thì chưa chắc đã có thể gửi tin tới bạn
$u$
.
Thầy chủ nhiệm đang có một thông tin rất quan trọng cần thông báo tới tất cả các học sinh. Để tiết kiệm thời gian, thầy chỉ nhắn tin tới
$1$
số học sinh rồi sau đó nhờ các học sinh này nhắn lại cho tất cả các bạn mà các học sinh đó có thể liên lạc được, và cứ lần lượt như thế làm sao cho tất cả các học sinh trong lớp đều nhận được tin.
Hãy tìm số lượng ít nhất các học sinh mà thầy chủ nhiệm cần nhắn.


## 🧩 Input

Input
Dòng đầu gồm 2 số nguyên
$N$
,
$M$
$(1 ≤N≤ 105, 1 ≤M≤min(N* (N- 1), 105))$
$M$
dòng tiếp theo mỗi dòng gồm 2 số nguyên
$u$
và
$v$
biểu thị bạn
$u$
có thể truyền tin với bạn
$v$


## 💡 Output

Output
Gồm 1 dòng chứa số nguyên là số lượng tin nhắn tối thiểu mà thầy cần gởi đi.


## 🧠 Example

### Input

```text
12 15
1 3
3 6
6 1
6 8
8 12
12 9
9 6
2 4
4 5
5 2
4 6
7 10
10 11
11 7
10 9
```

### Output

```text
2
```


