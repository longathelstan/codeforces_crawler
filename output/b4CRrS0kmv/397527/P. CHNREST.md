# P. CHNREST

## 📖 Problem

Một nhà hàng có M món ăn khác nhau và thú vị ở chỗ là mỗi món ăn rất nhiều nên có thể đủ cho bao nhiêu người cũng được, vì thế vấn đề là gọi món nào chứ không phải mỗi món gọi bao nhiêu. Có tất cả N người đến dự tiệc sinh nhật (bao gồm cả bạn trong đó).
Bạn đã tìm hiểu được danh sách những món ăn yêu thích của từng người và bạn muốn rằng đối với mỗi người phải có
chính xác
$2$
món mà họ thích. Vì đây là tiền của bố mẹ nên cũng không nên tiêu xài quá đáng. Hãy cho biết số tiền ít nhất phải trả để gọi một thực đơn thỏa mãn các yêu cầu trên.


## 🧩 Input

Input
- Dòng đầu tiên chứa hai số
$m$
,
$n$
$(1 ≤m≤ 30, 1 ≤n≤ 10)$
- Dòng thứ hai chứa
$m$
số
$Pi$
là giá của món thứ
$i$
.
$(1 ≤Pi≤ 1000)$
- Trong
$n$
dòng cuối cùng, dòng thứ
$k$
ghi danh sách các món yêu thích của người thứ
$k$
.


## 💡 Output

Output
- Gồm một số duy nhất là kết quả của bài toán, hoặc in ra -1 nếu không có cách gọi món nào thỏa mãn.


## 🧠 Example

### Input

```text
5 3
100 150 300 425 200
1 2 4
1 3 4 5
1 4 5
```

### Output

```text
450
```



## 📝 Note

Note
Chọn món ăn
$1$
,
$2$
,
$5$
khi đó cả
$3$
vị khách đều có đúng
$2$
món ăn mà họ thích.

