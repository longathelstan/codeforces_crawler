# F. Tối ưu số cầu

## 📖 Problem

Bạn được cho 1 đồ thị vô hướng
$G= (V,E)$
có
$N$
đỉnh,
$M$
cạnh. Định nghĩa, một cạnh được gọi là cầu nếu xoá cạnh đó sẽ làm tăng số thành phần liên thông của đồ thị.
yêu cầu:
bạn được phép thêm 1 cạnh giữa 2 đỉnh bất kỳ, hãy tìm cách thêm cạnh làm cho số lượng cầu là nhỏ nhất.


## 🧩 Input

Input
Một dòng gồm 2 số nguyên
$N$
,
$M$
$(3 ≤N≤ 105,N- 1 ≤M≤ 105)$
là số đỉnh và số cạnh của đồ thị
$G$
$M$
dòng tiếp theo, mỗi dòng gồm 2 số nguyên
$u$
và
$v$
$(1 ≤u,v≤N,u≠v)$
, biểu thị cạnh nối giữa
$u$
và
$v$
Dữ liệu đảm bảo 2 đỉnh chỉ có tối đa 1 cạnh nối giữa chúng


## 💡 Output

Output
Một dòng duy nhất chứa số nguyên là số lượng cầu nhỏ nhất.


## 🧠 Example

### Input

```text
7 7
1 2
2 3
3 1
3 4
4 5
4 6
6 7
```

### Output

```text
1
```


