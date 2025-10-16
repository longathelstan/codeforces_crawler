# O. Ếch săn mồi (5 điểm)

## 📖 Problem

Có
$M$
bậc thang đánh số từ
$1$
đến
$m$
từ trên xuống. Mỗi bậc thang được chia đều làm
$n$
ô, đánh số từ
$1$
tới
$n$
từ trái qua phải. Ô thứ
$j$
trên bậc thang
$i$
được gọi là ô
$(i,j)$
và trên đó có một lượng thức ăn là
$ai,j$
.
Một con ếch muốn đi săn mồi trên những bậc thang. Ếch được xuất phát từ một ô tùy ý trên bậc thang
$1$
và nhảy dần xuống bậc thang
$m$
. Khi nhảy tới ô nào thì ếch sẽ ăn hết số thức ăn trong ô đó. Tuy nhiên có một hạn chế từ ô
$(x,y)$
, chú ếch chỉ đươc phép nhảy sang ô
$(x',y')$
nếu, thỏa mãn
$x' =x+ 1$
và
$|y' -y| ≤k$
Yêu cầu:
Tìm một cách đi kiếm ăn cho chú ếch sao cho tổng lượng thức ăn kiếm được là nhiều nhất


## 🧩 Input

Input
Dòng
$1$
chứa ba số nguyên dương
$n,m,k$
$(1 ≤n,m,k≤ 2 * 103)$
.
$m$
dòng tiếp theo, dòng thứ
$i$
chứa
$n$
số nguyên dương
$ai,j≤ 109$
.


## 💡 Output

Output
In ra đáp án là tổng lượng thức ăn lớn nhất có thể ăn


## 🧠 Example

### Input

```text
3 5 2
4 3 2 1 1
4 3 5 4 9
1 2 3 7 5
```

### Output

```text
18
```


