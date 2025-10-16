# P. Đếm dãy con

## 📖 Problem

Cho mảng
$a$
gồm
$n$
phần tử, hãy đếm số cách chọn ra dãy con không cần liên tiếp gồm đúng
$m$
phần tử từ mảng
$a$
sao cho hiệu giữa phần tử lớn nhất và phần tử nhỏ nhất trong dãy được chọn không vượt quá
$k$
.


## 🧩 Input

Input
Dòng đầu gồm
$3$
số
$n$
,
$m$
,
$k$
$(1 ≤n≤ 2 * 105, 1 ≤m≤n, 1 ≤k≤n)$
Dòng tiếp theo gồm
$n$
số
$a1,a2, ...,an$
$(1 ≤ai≤n)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm chia dư cho
$109+ 7$


## 🧠 Example

### Input

```text
4 3 2
1 2 4 3
```

### Output

```text
2
```



## 📝 Note

Note
Với ví dụ
$1$
, ta có thể chọn dãy
$(a1,a2,a4)$
hoặc
$(a2,a3,a4)$
cả
$2$
dãy đều gồm đúng
$3$
phần tử và hiệu giữa phần tử lớn nhất và phần tử nhỏ nhất không vượt quá
$2$
.

