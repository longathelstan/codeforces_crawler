# ZK. Chọn xu 2

## 📖 Problem

Cho
$n$
đồng xu, mỗi đồng xu có giá trị nguyên dương là
$ai$
. Hãy đếm số cách khác nhau để tạo ra tổng là
$s$
(các tập hợp có phần tử như nhau, khác thứ tự chỉ được tính một lần), sử dụng các đồng xu trong
$n$
đồng xu đã cho.
Ví dụ với tập xu
${2, 3, 5}$
, tổng cần tạo ra là
$9$
, thì có
$3$
cách:
$2 + 2 + 5$
$3 + 3 + 3$
$2 + 2 + 2 + 3$


## 🧩 Input

Input
Dòng đầu gồm 2 số nguyên
$n$
và
$s$
— Số đồng xu và tổng tiền cần tạo
$(1 ≤n≤ 100,s≤ 106)$
Dòng tiếp theo gồm
$n$
số nguyên
$ai$
(
$1 ≤ai≤ 106)$


## 💡 Output

Output
In ra số cách tạo ra tổng là
$s$
, sau khi được lấy dư với
$109+ 7$


## 🧠 Example

### Input

```text
3 9
2 3 5
```

### Output

```text
3
```


