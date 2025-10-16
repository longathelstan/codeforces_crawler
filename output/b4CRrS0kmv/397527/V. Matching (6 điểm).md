# V. Matching (6 điểm)

## 📖 Problem

Cho
$n$
khối, các khối ở dưới dạng
$[color1|value|color2]$
, một khối có thể đảo ngược lại thành
$[color2|value|color1]$
.
Một chuỗi các khối được coi là hợp lệ nếu như điểm kết thúc của khối này là điểm bắt đầu của khối tiếp theo. Ví dụ, xét một chuỗi 3 khối
$A,B,C$
được coi là hợp lệ nếu màu bên phải của phải của khối
$A$
trùng với màu bên trái cửa khối
$B$
và màu bên phải của khối
$B$
trùng với màu bên trái của khối
$C$
.
Giá trị của một chuỗi khối là tổng
$value$
của các khối được chọn, hãy tìm chuỗi khối hợp lệ có tổng lớn nhất.


## 🧩 Input

Input
Dòng đầu gồm số nguyên
$n$
$(1 ≤n≤ 100)$
$n$
dòng tiếp theo mỗi dòng gồm
$3$
số, số thứ
$i$
mô tả
$color1$
,
$value$
,
$color2$
của khối thứ
$i$
$(1 ≤color1,color2≤ 4, 1 ≤value≤ 105)$


## 💡 Output

Output
Gồm
$1$
số duy nhất là tổng lớn nhất cần tìm.


## 🧠 Example

### Input

```text
6
2 1 4
1 2 4
3 4 4
2 8 3
3 16 3
1 32 2
```

### Output

```text
63
```



## 📝 Note

Note
Test ví dụ
$1$
, chuỗi hợp lệ có tổng lớn nhất có dạng
$[4|2|1] - [1|32|2] - [2|8|3] - [3|16|3] - [3|4|4] - [4|1|2]$
tổng giá trị là
$63$
Test ví dụ
$2$
, chuỗi hợp lệ có tổng lớn nhất có dạng
$[2|100000|1] - [1|100000|1] - [1|100000|2]$
tổng gía trị là
$300000$

