# ZZB. Bốc quà (4 điểm)

## 📖 Problem

Có
$n$
món quà ở trên trục tọa độ X. Cho trước
$a1,a2, ...,an$
với
$ai$
là vị trí của món quà
$i$
trên trục tọa độ. Có thể có nhiều món quà trên cùng một tọa độ.
Bạn được chọn
$2$
đoạn thẳng với tọa độ nguyên. Độ dài của mỗi đoạn thẳng phải chính xác là
$k$
. Bạn sẽ thu thập hết mọi món quà nằm trong ít nhất
$1$
trong
$2$
đoạn thẳng đã chọn (bao gồm cả điểm bắt đầu và kết thúc của mỗi đoạn thẳng),
$2$
đoạn thẳng có thể giao nhau.
Hãy tìm cách được nhiều món quà nhất nếu bạn chọn một cách tối ưu.


## 🧩 Input

Input
Dòng đầu gồm
$n$
và
$k$
$(1 ≤n≤ 106, 1 ≤k≤ 109)$
Dòng tiếp theo gồm
$n$
số, số thứ i là tọa độ
$ai$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm.


## 🧠 Example

### Input

```text
7 2
1 1 2 2 3 3 5
```

### Output

```text
7
```



## 📝 Note

Note
Test
$1$
:
Chọn
$2$
đoạn
$[1, 3]$
,
$[3, 5]$
, bạn sẽ thu được mọi món quà có tọa độ từ
$1$
->
$5$
tức là
$7$
món.
Test
$2$
:
Có nhiều đáp án, một trong các cách chọn tối ưu là
$[3, 3]$
,
$[4, 4]$

