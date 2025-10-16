# ZQ.  ĐTQG An Giang 2025 - Bài 4 - (7 điểm)

## 📖 Problem

Các nhà khoa học đang tiến hành một cuộc khảo sát $$$m$$$ mẫu vật trong phòng thí nghiệm. Mỗi mẫu vật được mô tả bởi $$$n$$$ thuộc tính khác nhau. Để thuận tiện cho việc ghi chép, người ta biểu diễn một mẫu vật bằng một xâu gồm $$$n$$$ ký tự, trong đó:
*
ký hiệu (+): thể hiện mẫu vật có thuộc tính tại vị trí tương ứng.
*
ký hiệu (-): thể hiện mẫu vật không có thuộc tính đó.
Như vậy, toàn bộ dữ liệu nghiên cứu gồm $$$m$$$ xâu ký tự, mỗi xâu gồm $$$n$$$ ký tự (+) hoặc (-).
Các nhà khoa học quan tâm đến việc so sánh hai mẫu vật với nhau dựa trên tập thuộc tính. Với hai mẫu vật $$$v_i$$$ và $$$v_j$$$, họ định nghĩa: $$$v_i$$$ bao hàm $$$v_j$$$ nếu thỏa mãn cả hai điều kiện sau:
Với mọi vị trí $$$k = 1, \ldots, n$$$: nếu $$$v_j$$$ có thuộc tính tại vị trí $$$k$$$ thì $$$v_i$$$ cũng có thuộc tính tại vị trí đó.
Tồn tại ít nhất một vị trí $$$k$$$ mà $$$v_i$$$ có thuộc tính và $$$v_j$$$ không có.
Ví dụ:
*
$$$u$$$:
++++-
, $$$v$$$:
++---
$$$\Rightarrow$$$ $$$u$$$ bao hàm $$$v$$$.
*
$$$u$$$:
+-+-+
, $$$v$$$:
----+
$$$\Rightarrow$$$ $$$u$$$ bao hàm $$$v$$$.
*
$$$u$$$:
+-+-+
, $$$v$$$:
++++-
$$$\Rightarrow$$$ $$$u$$$ không bao hàm $$$v$$$.
*
$$$u$$$:
++++-
, $$$v$$$:
----+
$$$\Rightarrow$$$ $$$u$$$ không bao hàm $$$v$$$, đồng thời $$$v$$$ cũng không bao hàm $$$u$$$.
Để đánh giá mức độ đa dạng của tập mẫu vật, các nhà khoa học muốn tính một giá trị nghiên cứu, được xác định bằng: số cặp $$$(i, j)$$$ $$$(1 \le i, j \le m)$$$ sao cho $$$v_i$$$ bao hàm $$$v_j$$$.


## 🧩 Input

Input
Đọc từ file
TEXT.INP
có cấu trúc như sau:
*
Dòng đầu tiên có hai số nguyên $$$m$$$ và $$$n$$$ $$$(1 \le m \le 2 \cdot 10^5;\ 1 \le n \le 20)$$$.
*
$$$m$$$ dòng tiếp theo, dòng thứ $$$i$$$ có $$$n$$$ ký hiệu (+) hoặc (-) mô tả thuộc tính của mẫu vật thứ $$$i$$$.


## 💡 Output

Output
Ghi ra file
TEXT.OUT
một số nguyên duy nhất – giá trị nghiên cứu tìm được.


## 🧠 Example

### Input

```text
5 5
----+
+-+-+
++---
---+-
++++-
```

### Output

```text
3
```


