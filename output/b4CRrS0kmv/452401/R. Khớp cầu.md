# R. Khớp cầu

## 📖 Problem

Xét đơn đồ thị vô hướng
$G= (V,E)$
, có
$N$
đỉnh và
$M$
cạnh. Người ta định nghĩa một đỉnh gọi là khớp nếu như xoá đỉnh đó sẽ làm tăng số thành phần liên thông của đồ thị. Tương tự như vậy, một cạnh được gọi là cầu nếu xoá cạnh đó sẽ làm tăng số thành phần liên thông của đồ thị.
Vấn đề đặt ra là cần phải đếm tất cả các khớp và cầu của đồ thị
$G$
. .


## 🧩 Input

Input
Một dòng gồm 2 số nguyên
$N$
và
$M$
$(1 ≤N≤ 105, 1 ≤M≤ 105)$
$M$
dòng tiếp theo, mỗi dòng chứa 2 số nguyên
$u$
và
$v$
$(1 ≤u,v≤N,u≠v)$


## 💡 Output

Output
Một dòng duy nhất ghi hai số, số thứ nhất là số khớp, số thứ hai là số cầu của
$G$


## 🧠 Example

### Input

```text
10 12
1 10
10 2
10 3
2 4
4 5
5 2
3 6
6 7
7 3
7 8
8 9
9 7
```

### Output

```text
4 3
```


