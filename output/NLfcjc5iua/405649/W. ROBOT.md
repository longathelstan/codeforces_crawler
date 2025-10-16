# W. ROBOT

## 📖 Problem

Trên một lưới ô vuông
$N$
hàng,
$M$
cột. Các dòng được đánh số từ
$1$
đến
$N$
theo thứ tự từ trên xuống dưới, các cột được đánh số từ
$1$
đến
$M$
theo thứ tự từ trái qua phải. Tại ô
$(1, 1)$
người ta đặt một robot dò đường đi. Robot này có đặc điểm là chỉ có thể di chuyển theo
$2$
hướng: đi thẳng hoặc rẽ trái, mỗi lần đi một ô. Trên lưới ô vuông có một vài vị trí có vật cản mà robot không được đi vào những vị trí này.
![](https://espresso.codeforces.com/c2c3a8e216c81ea671f01937dba2f7acf3806b39.png)
Cho vị trí
$(yd,xd)$
của một ô đích cần di chuyển đến. Biết rằng trong lần di chuyển đầu tiên, từ ô
$(1, 1)$
robot có thể di chuyển đến ô
$(2, 1)$
hoặc
$(1, 2)$
đều được. Hãy in ra đường đi ngắn nhất của con robot đó.


## 🧩 Input

Input
- Dòng thứ nhất là hai số nguyên
$N$
,
$M$
cách nhau một khoảng trắng
$(1≤N,M≤100)$
- Trong
$N$
dòng tiếp theo, mỗi dòng gồm
$M$
số nguyên
$0$
hoặc
$1$
cách nhau một khoảng trắng. Các dòng này xác định tình trạng của lưới, số
$0$
nghĩa là ô lưới không có vật cản, số 1 là ô lưới có vật cản.
- Dòng thứ
$3$
là hai số
$yd$
, xd cách nhau một khoảng trắng
$(1≤yd≤N, 1≤xd≤M)$
.
(Dữ liệu cho đảm bảo tại ô
$(1, 1)$
và ô
$(yd,xd)$
không có vật cản, ô
$(yd,xd)$
khác với ô xuất phát)


## 💡 Output

Output
Một số duy nhất là đường đi ngắn nhất của con robot đó.


## 🧠 Example

### Input

```text
4 5
0 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 0 0 1 0
2 4
```

### Output

```text
7
```


