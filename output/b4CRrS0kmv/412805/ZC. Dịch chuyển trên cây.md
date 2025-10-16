# ZC. Dịch chuyển trên cây

## 📖 Problem

Cho đồ thị cây vô hướng liên thông gốc là
$1$
gồm
$n$
đỉnh và
$n- 1$
cạnh, việc di chuyển giữa
$2$
đỉnh sẽ phải đi qua cạnh nối giữa
$2$
đỉnh đó với thời gian là
$1$
, sẽ có
$1$
ký tự tiếng anh in thường được ghi trên mỗi đỉnh, khi đứng tại
$1$
đỉnh có ký tự bất kỳ ta có thể di chuyển tới bất kỳ đỉnh nào có cùng ký tự với đỉnh đang đứng với thời gian là
$1$
.
Yêu cầu
: Cho
$q$
truy vấn, mỗi truy vấn gồm
$2$
đỉnh
$u$
và
$v$
, hãy in ra thời gian ngắn nhất để đi từ
$u$
tới
$v$


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 2 * 105)$
là số lượng đỉnh
Dòng tiếp theo gồm
$n$
ký tự dính liền nhau, ký tự thứ
$i$
được ghi trên đỉnh thứ
$i$
. Các ký tự chỉ gồm các chữ cái in thường trong tiếng anh
$n- 1$
dòng tiếp theo, mỗi dòng gồm
$2$
đỉnh
$u$
và
$v$
$(1 ≤u,v≤n$
) thể hiện có đường đi từ đỉnh
$u$
tới
$v$
với thời gian là
$1$
Dòng tiếp theo gồm
$q$
$(1 ≤q≤ 2 * 105)$
là số lượng truy vấn
Tiếp theo là
$q$
dòng, mỗi dòng gồm
$2$
số
$u$
và
$v$
$(1 ≤u,v≤n)$
bạn hãy in ra thời gian ngắn nhất để đi từ
$u$
tới
$v$
Dữ liệu đảm bảo đồ thị liên thông


## 💡 Output

Output
Gồm
$q$
dòng ứng với
$q$
đáp án cần tìm theo dữ liệu đầu vào


## 🧠 Example

### Input

```text
11
acecdbadzbc
1 2
2 3
3 4
4 5
5 6
6 7
2 8
8 9
9 10
1 11
4
1 1
11 5
1 9
1 10
```

### Output

```text
0
2
3
3
```



## 📝 Note

Note
![](https://espresso.codeforces.com/d05ab1ba8443e2fabe044c0a5c2613f6d2149327.png)
Với truy vấn
$1$
, thời gian dịch chuyển ngắn nhất là
$0$
.
Với truy vấn
$2$
,
$11$
->
$4$
->
$5$
, thời gian dịch chuyển ngắn nhất là
$2$
Với truy vấn
$3$
,
$1$
->
$2$
->
$8$
->
$9$
, thời gian dịch chuyển ngắn nhất là
$3$
Với truy vấn
$4$
,
$1$
->
$7$
->
$6$
->
$10$
, thời gian dịch chuyển ngắn nhất là
$3$

