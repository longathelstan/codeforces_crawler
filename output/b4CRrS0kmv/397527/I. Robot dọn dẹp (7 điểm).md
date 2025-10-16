# I. Robot dọn dẹp (7 điểm)

## 📖 Problem

Cho sàn nhà có kích thước
$H$
x
$W$
, trên đó có các ô bẩn, ô sach và một con robot sẽ phải đi dọn hết các ô bẩn đó. Tại ô
$(i,j)$
robot có thể di chuyển qua ô
$(i+ 1,j)$
,
$(i,j+ 1)$
,
$(i- 1,j)$
,
$(i,j- 1)$
.
Yêu cầu:
Xác định số nước tối thiểu để robot có thể dọn mọi ô bẩn theo bất kỳ thứ tự nào. Đưa ra số nước tối thiểu tìm được. Nếu không có cách nào để robot dọn hết hãy in ra
$- 1$


## 🧩 Input

Input
Gồm nhiều test với mỗi test:
Dòng đầu mỗi test là
$2$
số
$W$
,
$H$
$(1 ≤H,W≤ 15)$
$H$
dòng tiếp theo, mỗi dòng chứa
$W$
ký tự miêu tả các ô của hình chữ nhật.
Các ô của sàn có giá trị sau:
$'.'$
: sạch
$' * '$
: bẩn.
$'x'$
: vật cản.
$'o'$
: robot (
$1$
con)
Kết thúc test là hai số
$0$
$0$
.
Có không quá
$150$
test ở mỗi input.


## 💡 Output

Output
Đưa ra đáp án của các test theo thứ tự input, mỗi đáp án cách nhau một dòng.


## 🧠 Example

### Input

```text
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
```

### Output

```text
8
49
-1
```


