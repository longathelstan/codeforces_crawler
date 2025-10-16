# K. Cây may mắn

## 📖 Problem

Nhâm Tấn là 1 người yêu thích các số may mắn. Số may mắn là một số mà các chữ số của nó chỉ chứa
$4$
hoặc
$7$
, Ví dụ: các số
$47$
,
$744$
,
$4$
,
$7$
,
$4474777$
là may mắn còn
$5$
,
$17$
,
$467$
thì không.
Một ngày nọ, Nhâm Tấn bắt gặp một cái cây có
$n$
đỉnh. Bên cạnh đó, cây đã được tính trọng số, tức là mỗi cạnh của cây đều có trọng số (là một số nguyên dương). Một cạnh là may mắn nếu trọng số của nó là một con số may mắn.
Nhâm Tấn tự hỏi có bao nhiêu bộ ba đỉnh
$(i,j,k)$
tồn tại trên đường đi từ
$i$
đến
$j$
và trên đường đi từ
$i$
đến
$k$
phải có ít nhất một cạnh may mắn (cả ba đỉnh trong một bộ khác nhau từng đôi một).
lưu ý:
Thứ tự bộ ba quan trọng, tức là (1,2,3), (1,3,2), (2,3,1) được tính là 3 bộ ba khác nhau. Một cây có
$n$
đỉnh là một đồ thị liên thông vô hướng có đúng
$n- 1$
cạnh.
yêu cầu:
Tìm xem có bao nhiêu bộ ba đỉnh như vậy tồn tại.


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên
$n$
$(1 ≤n≤105)$
— số đỉnh của cây.
$N- 1$
dòng tiếp theo mỗi dòng chứa ba số nguyên:
$ui,vi,wi$
$(1 ≤ui,vi≤n, 1 ≤wi≤ 109,ui≠vi)$
— cặp đỉnh được nối với nhau bởi cạnh và trọng số của cạnh.


## 💡 Output

Output
Một dòng duy nhất chứa số nguyên là đáp án của bài


## 🧠 Example

### Input

```text
4
1 2 4
3 1 2
1 4 7
```

### Output

```text
16
```



## 📝 Note

Note
16 bộ ba đỉnh từ mẫu đầu tiên là:
$(1, 2, 4), (1, 4, 2), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)$
.

