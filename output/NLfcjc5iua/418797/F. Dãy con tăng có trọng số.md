# F. Dãy con tăng có trọng số

## 📖 Problem

Xét dãy số nguyên dương
$a1,a2, ...,an$
. Một dãy chỉ số
$1 ≤i1<i2< ⋯ <ik≤n$
mà
$ai1<ai2< ⋯ <aik$
thì dãy
$ai1<ai2< ⋯ <aik$
được gọi là một dãy con tăng của dãy
$a1,a2, ...,an$
và tổng
$ai1+ai2+ ⋯ +aik$
được gọi là trọng số của dãy con tăng.
Yêu cầu
: Cho dãy số nguyên dương
$a1,a2, ...,an$
và số nguyên dương
$W$
, hãy tìm dãy con tăng của dãy
$a1,a2, ...,an$
có độ dài lớn nhất và trọng số không vượt quá
$W$
.


## 🧩 Input

Input
Dòng đầu gồm
$2$
số nguyên
$n$
và
$W$
$(1 ≤n≤ 20, 1 ≤W≤ 400)$
Dòng thứ hai gồm
$n$
số nguyên dương
$a1,a2, ...,an(1 ≤ai≤n)$


## 💡 Output

Output
Gồm một dòng chứa một số là độ dài dãy con tăng lớn nhất tìm được thỏa mãn.


## 🧠 Example

### Input

```text
5 10
4 2 3 1 5
```

### Output

```text
3
```



## 📝 Note

Note
Ở ví dụ
$1$
: một trong các cách chọn cho độ dài tối đa là
$3$
là chọn dãy
$a2,a3,a5$
đây là dãy tăng dần và tổng của
$a2+a3+a5≤ 10$

