# C. Đoạn thẳng (5 điểm)

## 📖 Problem

Cho
$N$
đoạn thẳng, đoạn thẳng thứ
$i$
được cho bởi hai số nguyên
$ai,bi$
mà tại hai đầu mút của đoạn thẳng đó có độ dài bằng
$bi-ai$
. Hai đoạn thẳng
$i,j$
$(1 ≤i,j≤N;i≠j)$
được gọi là
giao nhau
nếu thỏa mãn một trong hai điều kiện sau:
*
$ai<aj<bi<bj$
*
$aj<ai<bj<bi$
Yêu cầu:
Tìm 2 đoạn thẳng không giao nhau có tổng độ dài hai đoạn thẳng là lớn nhất.


## 🧩 Input

Input
Dòng thứ nhất chứa số nguyên dương
$N$
$(1 ≤N≤ 5 * 105)$
.
Mỗi dòng trong
$N$
dòng tiếp theo, mỗi dòng chứa 2 số nguyên
$ai,bi$
là hai đầu mút của đoạn thẳng thứ
$i$
$(ai<bi;|ai|, |bi| ≤ 109;1 ≤i≤N)$
.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tim


## 🧠 Example

### Input

```text
3
1 3
1 4
3 6
```

### Output

```text
5
```


