# U. Meet (6 điểm)

## 📖 Problem

Có
$N$
thành phố và
$M$
con đường một chiều kết nối giữa
$2$
thành phố. Có
$K$
nhóm, nhóm thứ
$i$
đang ở thành phố
$Xi$
và muốn đến thành phố
$Yi$
. Mỗi nhóm có thể đi trên một hành trình bất kỳ từ thành phố xuất phát đến thành phố đích. Hãy tìm các thành phố mà tại đó tất cả
$K$
nhóm trên hành trình của mình có thể dừng tại đó để gặp gỡ nhau.
Lưu ý:
Vì các nhóm
$i$
muốn đi thăm quan các thành phố nhiều lần trừ
$Xi$
trước khi đi đến
$Yi$
, thế nên trong lộ trình đi của nhóm có thể có nhiều thành phố lặp lại tuy nhiên
$Yi,Xi$
tức thành phố đích đến không được lặp lại trong lộ trình.


## 🧩 Input

Input
Dòng đầu ghi
$3$
số tự nhiên
$N$
,
$M$
và
$K$
số lượng thành phố, số lượng con đường và số lượng các nhóm.
Mỗi dòng trong
$M$
dòng tiếp theo ghi
$2$
số nguyên
$A$
và
$B$
biểu thị con đường một chiều từ thành phố
$A$
đến thành phố
$B$
.
Mỗi dòng trong
$K$
dòng cuối cùng ghi
$2$
số
$Xi$
và
$Yi$
là thành phố xuất phát và đích đến của nhóm
$i$
.
Đảm bảo có một tuyến đường từ
$Xi$
đến
$Yi$
.


## 💡 Output

Output
Dòng đầu tiên in ra số lượng thành phố thỏa mãn
$S$
.
Dòng tiếp theo in ra
$S$
số được sắp xếp theo thứ tự tăng dần - số thứ tự những thành phố thỏa mãn


## 🧠 Example

### Input

```text
9 15 2
1 4
4 5
1 7
6 7
5 6
6 8
3 8
3 5
6 3
1 6
8 9
3 2
2 9
7 9
8 7
3 7
1 2
```

### Output

```text
3
3 5 6
```



## 📝 Note

Note
![](https://espresso.codeforces.com/fee4743aac405449f648e0a23a760c1355b3a95d.png)

