# Q. Nối mạng

## 📖 Problem

Các học sinh khi đến thực tập trong phòng máy tính thường hay chơi trò chơi điện tử trên mạng. Để ngăn ngừa, người trực phòng máy đã ngắt tất cả các máy tính ra khỏi mạng và xếp chúng thành một dãy trên một cái bàn dài và gắn chặt máy xuống mặt bàn rồi đánh số thứ tự các máy từ
$1$
đến
$N$
theo chiều từ trái sang phải.
Các học sinh tinh nghịch không chịu thua, họ đã quyết định tìm cách nối các máy trên bàn bởi các đoạn dây nối sao cho mỗi máy được nối với ít nhất một máy khác. Để tiến hành công việc này, họ đã đo khoảng cách giữa hai máy liên tiếp. Bạn hãy giúp các học sinh này tìm cách nối mạng thoả mãn yêu cầu đặt ra sao cho tổng độ dài cáp nối phải sử dụng là ít nhất.


## 🧩 Input

Input
Dòng đầu tiên chứa số lượng máy
$N$
$(2≤N≤105)$
.
Dòng thứ
$i$
trong số
$N- 1$
dòng tiếp theo chứa các khoảng cách từ máy
$i$
đến máy
$i+ 1$
$(i= 1, 2, ...,N- 1)$
. Giả thiết rằng khoảng cách từ máy
$1$
đến máy
$N$
không vượt quá
$106$
.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
6
2
2
3
2
2
```

### Output

```text
7
```



## 📝 Note

Note
Nối máy
$1$
->
$2$
,
$3$
->
$4$
,
$5$
->
$6$
Tổng là
$2$
+
$3$
+
$2$
=
$7$

