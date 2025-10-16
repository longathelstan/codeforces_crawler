# N. Hình vuông con (7 điểm)

## 📖 Problem

Em được BTC kỳ thi Duyên Hải Đồng Bằng Bắc Bộ năm 2022 trao một phần thưởng do có thành tích làm bài tốt.
Để nhận thưởng, BTC đưa ra một bảng hình chữ nhật được chia thành lưới ô vuông đơn vị kích thước
$m*n$
. Các hàng của bảng được đánh số từ
$1$
dến
$m$
, từ trên xuống dưới. Các cột của bảng được đánh số từ
$1$
đến
$n$
, từ trái qua phải. Ô nằm trên hàng
$i$
, cột
$j$
của bẳng được gọi là ô
$(i,j)$
và có ghi giá trị
$ai$
$j$
(
$1 ≤i≤m, 1 ≤j≤n$
). Một hình vuông con của bảng là hình vuông chiếm chọn một số ô của bảng.
Yêu cầu:
với số nguyên dương
$k$
cho trước, em hãy chọn ra một hình vuông con kích thước
$k*k$
sao cho giá trị của số nhỏ nhất trong hình vuông con là lớn nhất. Đó chính là giá trị của phần thưởng em nhận được!


## 🧩 Input

Input
Dòng thứ nhất chứa ba số nguyên dương
$m,n,k(1 ≤n≤ 1000;1 ≤m≤ 1000;k≤n;k≤m)$
. Trong
$m$
dòng tiếp theo, mỗi dòng chứa n số nguyên dương
$ai$
$j$
là số ghi trên ô ở dòng thứ
$i$
và cột thứ
$j$
(
$ai$
$j$
$≤ 106$
;
$1 ≤i≤m, 1 ≤j≤n)$


## 💡 Output

Output
Gồm 1 số dòng duy nhất chứa một số nguyên là giá trị của số nhỏ nhất trong hình vuông thỏa mãn điều kiện.


## 🧠 Example

### Input

```text
5 5 2
1 11 2 3 3
9 9 2 3 3
2 2 2 2 2
1 2 2 5 6
4 10 2 7 8
```

### Output

```text
5
```



## 📝 Note

Note
Hình vuông con kích thước 2 x 2 là:
5 6
7 8
có giá trị của số nhỏ nhất là 5 thỏa mãn điều kiện

