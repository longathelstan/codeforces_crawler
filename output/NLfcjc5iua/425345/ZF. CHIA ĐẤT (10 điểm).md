# ZF. CHIA ĐẤT (10 điểm)

## 📖 Problem

Phú hộ qua đời để lại cho
$4$
người con một mảnh đất hình vuông có kích thước
$n×n$
, trên đó có trồng một số cây gỗ quí. Theo di chúc, mảnh đất sẽ được chia thành 4 phần, mỗi phần là một hình chữ nhật. Để tiết kiệm chi phí chia đất nên chỉ có thể thực hiện cắt mảnh đất bởi một nhát cắt theo chiều ngang và một nhát cắt theo chiều dọc. Các con của phú hộ đều thích có nhiều cây gỗ quí vì vậy họ sẽ chọn phần đất có nhiều cây gỗ quí hơn. Thứ tự nhận đất sẽ từ lớn tới nhỏ, người em út sẽ nhận phần có ít cây gỗ quí nhất.
Yêu cầu: Hãy chỉ cách chia đất để chênh lệch giữa số cây gỗ quí của người anh cả và của người em út là ít nhất.


## 🧩 Input

Input
Dòng thứ nhất ghi số nguyên dương
$n$
$(2≤n≤500)$
Tiếp theo là
$n$
dòng, mỗi dòng ghi
$n$
số, số
$0$
hoặc số
$1$
. Số
$0$
thể hiện vị trí
không có cây gỗ quí, số
$1$
thể hiện vị trí có cây gỗ quí. Các số ghi trên cùng một dòng cách nhau bởi ít nhất một kí tự trắng.


## 💡 Output

Output
Một dòng ghi một số nguyên là số lượng chênh lệch cây gỗ quí ít nhất trên phần đất của người anh cả và của người em út.


## 🧠 Example

### Input

```text
6
1 0 1 0 0 1
0 1 0 0 0 1
1 0 0 0 0 0
0 1 1 0 0 1
0 1 0 0 1 0
1 0 1 0 0 0
```

### Output

```text
1
```


