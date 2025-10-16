# I. Cây hoa đua sắc

## 📖 Problem

Một năm hạnh phúc nữa lại đến, cây hoa sữa lấy thi nhau đâm hoa kết trái. Ở đầu làng có một cái cây hoa đẹp tuyệt trần, cây có
$n$
cái đỉnh và đỉnh
$1$
đặt làm gốc, theo truyền thống người dân nơi đây sẽ tổ chức một trò chơi với cái cây này.
Trò chơi thuộc thể loại câu đó, người trả lời sớm và đúng nhất sẽ thắng. Mỗi câu đố có dạng
$U$
và
$D$
, đếm xem có bao nhiêu cái đỉnh
$u$
trên cây sao cho đỉnh
$U$
nằm trên đường đi từ
$u$
đến gốc của cây và đường đi ngắn nhất từ
$u$
đến gốc có chính xác
$D$
cạnh nằm trên chúng. Bạn cần lập trình để xác định kết quả đúng cho mỗi câu đố để so sánh với người chơi.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 2 * 105)$
.
Dòng tiếp theo có
$n- 1$
số nguyên dương
$pi$
$(2 ≤i≤n)$
,
$pi$
là cha của
$i$
.
Dòng tiếp theo gồm số nguyên dương
$q$
$(1 ≤q≤ 2 * 105)$
.
Mỗi dòng trong
$q$
dòng tiếp theo, gồm
$2$
số nguyên dương
$U$
và
$D$
$(1 ≤U≤n, 0 ≤D≤n- 1)$


## 💡 Output

Output
In ra đáp án ứng với mỗi câu đố.


## 🧠 Example

### Input

```text
7
1 1 2 2 4 2
4
1 2
7 2
4 1
5 5
```

### Output

```text
3
1
0
0
```


