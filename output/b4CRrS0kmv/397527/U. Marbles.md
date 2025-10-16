# U. Marbles

## 📖 Problem

Tấn có
$n$
viên bi được xếp trên một đường thẳng, viên bi ở vị trí
$i$
có màu là
$ai$
. Tấn thích sắp xếp các viên bi lại sao cho các viên bi cùng màu ở cạnh nhau.
Để đạt được điều này, Tấn có thể thực hiện thao tác sau vô số lần, đổi vị trí
$2$
viên bi kề cạnh. Bạn hãy giúp Tấn tìm số truy thao tác ít nhất để sắp xếp được như ý muốn.


## 🧩 Input

Input
Dòng đầu tiên gồm
$n$
là số viên bi
$(2 ≤n≤ 4.105)$
Dòng tiếp theo gồm
$n$
số, viên bi thứ
$i$
có màu là
$ai$
$(1 ≤ai≤ 20)$


## 💡 Output

Output
In ra số lần thực hiện thao tác ít nhất để sắp xếp được như ý muốn.


## 🧠 Example

### Input

```text
7
3 4 2 3 4 2 2
```

### Output

```text
3
```



## 📝 Note

Note
Ở ví dụ
$1$
cần thực hiện
$3$
thao tác:
$[3, 4, 2, 3, 4, 2, 2]$
->
$[3, 4,$
3
$,$
2
$, 4, 2, 2]$
->
$[3,$
3
$,$
4
$, 2, 4, 2, 2]$
->
$[3, 3, 4,$
4
$,$
2
$, 2, 2]$

