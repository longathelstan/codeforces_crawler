# ZC. CTAIN

## 📖 Problem

Cho n bình chứa nước (1 <= n <= 4). Ban đầu, mỗi bình đều chứa đầy nước. Bình i có dung lượng là oi, với 1 <= oi <= 49.
Bạn có thể thực hiện 1 trong 3 thao tác sau:
Đổ tất cả nước ở trong bình A sang bình B. Thao tác này chỉ được thực hiện nếu bình B có đủ chỗ trống.
Lấy 1 lượng nước ở bình A và đổ đầy hoàn toàn bình B.
Đổ tất cả nước mà 1 bình đang chứa.


## 🧩 Input

Input
Cho 1 dãy wi. Hỏi có tồn tại 1 dãy thao tác đổ nước để từ trạng thái ban đầu (mỗi bình chứa đầy nước), ta đến được trạng thái mà bình i chứa wi nước.
Nếu tồn tại dãy thao tác đổ nước, tìm số lượng thao tác ít nhất.


## 💡 Output

Output
Dòng đầu: số lượng test T (T <= 20).
Mỗi test gồm:
*
1 dòng chứa số nguyên dương n (n <= 4).
*
1 dòng chứa n số oi, với 1 <= oi <= 49.
*
1 dòng chứa n số wi, với 1 <= wi <= oi.


## 🧠 Example

### Input

```text
2
3
3 5 5
0 0 4
2
20 25
10 16
```

### Output

```text
6
NO
```


