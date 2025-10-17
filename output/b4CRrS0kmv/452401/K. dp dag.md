# K. dp dag

## 📖 Problem

Cho đồ thị có hướng
$G$
có
$N$
đỉnh và
$M$
cạnh. Các đỉnh được đánh số từ 1 tới
$N$
, và cạnh có hướng thứ
$i$
(
$1 ≤i≤M$
) đi từ đỉnh
$xi$
tới đỉnh
$yi$
.
Đảm bảo rằng đồ thị
$G$
không có chu trình.
Tìm độ dài đường đi có hướng dài nhất trong đồ thị
$G$
, quy ước rằng:
độ dài của một đường đi có hướng là số cạnh nằm trên đường đi đó
.


## 🧩 Input

Input
*
Dòng đầu tiên
chứa hai số nguyên
$N$
và
$M$
, lần lượt là số đỉnh và số cạnh của đồ thị đã cho (
$2 ≤N≤ 105$
,
$1 ≤M≤ 106$
).
*
Tiếp theo,
có
$M$
dòng, mỗi dòng chứa hai số nguyên
$xi$
và
$yi$
(một cặp trên mỗi dòng), biểu diễn cho cạnh thứ
$i$
của đồ thị, với hướng từ
$xi$
tới
$yi$
.
*
Yêu cầu:
Đảm bảo rằng tất cả các cạnh
$(xi,yi)$
bất kỳ đều phân biệt và đặc biệt là đồ thị
$G$
không có chu trình.


## 💡 Output

Output
Gồm một dòng duy nhất là kêt quả cần tìm


## 🧠 Example

### Input

```text
4 5
1 2
1 3
3 2
2 4
3 4
```

### Output

```text
3
```



## 📝 Note

Note
Ví dụ
$1$
:
Đường màu đỏ trong hình dưới đây là đường đi dài nhất
![](https://espresso.codeforces.com/dbe0b9ffcb113e8f5c227d5047cc33b641911bde.png)

