# ZY. DIVBOARD (4 điểm)

## 📖 Problem

Cho bảng hình chữ nhật kích thước m × n được chia thành lưới ô vuông đơn vị (m hàng và n cột). Trên mỗi ô
(i,j) chứa một số nguyên
$ai,j$
. Người ta cắt bảng ra thành 4 mảnh theo cách sau:
*
Cắt ngang bảng từ trái qua phải theo khe giữa hai hàng ô liên tiếp chia bảng làm 2 phần
*
Với mỗi phần chia ra tại bước trước, cắt dọc từ trên xuống dưới theo khe giữa hai cột ô liên tiếp
Sau khi cắt, mỗi phần sẽ gồm ít nhất 1 ô, tổng các số ghi trên các ô thuộc một phần gọi là trọng số của phần đó.
Tìm cách cắt bảng ra làm 4 phần theo quy tắc trên để độ chênh lệch trọng số giữa phần có trọng số lớn nhất và phần có trọng số nhỏ nhất là cực tiểu.


## 🧩 Input

Input
Dòng
$1$
chứa hai số nguyên dương
$m,n$
$(2≤m,n≤1000)$
$m$
dòng tiếp theo, dòng thứ
$i$
chứa
$n$
số nguyên không âm, số thứ j là
$ai,j≤1000$


## 💡 Output

Output
Một số nguyên duy nhất là độ chênh lệch trọng số giữa phần có trọng số lớn nhất và phần có trọng số nhỏ nhất theo phương án chia bảng tìm được


## 🧠 Example

### Input

```text
4 4
1 2 3 4
3 4 1 2
1 1 1 4
2 2 2 5
```

### Output

```text
1
```



## 📝 Note

Note
Cách chia cho test ví dụ
![](https://espresso.codeforces.com/45a9124c14e2a7618bb336019a0751413d1eec45.png)

