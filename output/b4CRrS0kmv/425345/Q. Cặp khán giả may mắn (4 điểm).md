# Q. Cặp khán giả may mắn (4 điểm)

## 📖 Problem

Trong giải bóng đá vòng loại World Cup 2022, khán giả khi mua vé sẽ được Ban tổ chức đánh số thứ tự
$1, 2, ...,N$
; trên vé của khán giả thứ
$i$
chứa một số ngẫu nhiên
$ai$
là mã số vé. Sau mỗi trận đấu, Ban tổ chức thực hiện trao thưởng cho cặp khán giả may mắn. Cặp khán giả ở vị trí thứ
$i$
và vị trí thứ
$j$
được gọi là may mắn nếu thỏa mãn các điều kiện sau:
*
$1 ≤i<j≤N$
*
$aj-ai≥P$
với
$P$
là số ngẫu nhiên do Ban tổ chức đưa ra
*
$j-i$
lớn nhất
Yêu cầu: Đưa ra cặp vị trí khán giả may mắn


## 🧩 Input

Input
Dòng thứ nhất chứa
$2$
số nguyên
$N$
và
$P$
$(1 ≤N≤ 106, 1 ≤P≤ 106)$
Dòng thứ hai chứa
$N$
số nguyên dương
$a1,a2, ...,an$
$(0 ≤ai≤ 109)$


## 💡 Output

Output
Gồm hai số nguyên dương là vị trí của cặp khán giả may mắn. Nếu có nhiều cặp thỏa mãn yêu cầu bài toán thì đưa ra vị trí cặp may mắn đầu tiên, nếu không có thì ghi kết quả bằng
$0$
Các số trên cùng một dòng cách một dấu cách trống.


## 🧠 Example

### Input

```text
6 3
4 3 7 2 6 4
```

### Output

```text
2 5
```


