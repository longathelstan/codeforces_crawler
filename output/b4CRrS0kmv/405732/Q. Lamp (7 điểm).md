# Q. Lamp (7 điểm)

## 📖 Problem

Tấn có
$n$
cái đèn, cái đèn thứ
$i$
sẽ bật sáng trong khoảng thời gian từ
$[li,ri]$
, hãy giúp Tấn đếm số cách chọn
$k$
cái đèn
$u1,u2, ...,uk$
$(u1<u2< ... <uk)$
sao cho có ít nhất một thời điểm mà
$k$
cái đèn này sáng cùng
$1$
lúc. Hãy in đáp án chia dư cho
$998244353$


## 🧩 Input

Input
Dòng đầu gồm
$2$
số
$n$
và
$k$
$(1 ≤k≤n≤ 3.105)$
$n$
dòng tiếp theo dòng thứ
$i$
gồm
$2$
số
$li$
và
$ri$
$(1 ≤li≤ri≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án chia dư cho
$998244353$


## 🧠 Example

### Input

```text
7 3
1 7
3 8
4 5
6 7
1 3
5 10
8 9
```

### Output

```text
9
```



## 📝 Note

Note
Ở test
$1$
, có
$9$
cách chọn thỏa mãn là
$(1, 2, 3)$
,
$(1, 2, 4)$
,
$(1, 2, 5)$
,
$(1, 2, 6)$
,
$(1, 3, 6)$
,
$(1, 4, 6)$
,
$(2, 3, 6)$
,
$(2, 4, 6)$
,
$(2, 6, 7)$

