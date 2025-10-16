# O. Chia dãy tạo tổng lớn nhất

## 📖 Problem

Cho một dãy
$A$
có
$n$
phần tử và một số nguyên dương
$k$
. Tìm cách chia dãy
$A$
thành các dãy con (các phần tử trong cùng một dãy con phải nằm liên tiếp nhau trong dãy
$A$
) và số lượng phần tử của một dãy con không vượt quá
$k$
. Sau khi chia xong với mỗi phần tử trong một dãy con ta thay thế nó thành số lớn nhất trong
dãy con đó
.
Tìm cách chia sao cho tổng các phần tử sau khi chia và thay thế là lớn nhất !


## 🧩 Input

Input
Dòng đầu tiên gồm
$2$
số nguyên dương
$n,k$
$(1 ≤k≤n≤ 500)$
.
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
là
$Ai$
$(1 ≤Ai≤ 109)$
.


## 💡 Output

Output
In ra đáp án.


## 🧠 Example

### Input

```text
7 3
1 15 7 9 2 5 10
```

### Output

```text
84
```



## 📝 Note

Note
Ta chia thành các dãy [1,3], [4,4], [5,7], số lớn nhất từng dãy là
$15, 9, 10$
, hình thành nên dãy là
$[15, 15, 15, 9, 10, 10, 10]$
. Tổng là
$84$
.

