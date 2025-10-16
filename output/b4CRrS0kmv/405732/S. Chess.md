# S. Chess

## 📖 Problem

Tấn có một bàn cờ
$1$
x
$n$
, tại mỗi ô, nếu ô đó có giá trị là
$0$
thì sẽ là ô trống, nếu ô đó có giá trị là
$1$
thì ô đó đang có một con chốt đứng lên. Với mỗi con chốt tại vị trí thứ
$i$
Tấn có thể di chuyển như sau:
*
Nếu ô thứ
$(i- 1)$
có một con chốt khác và ô thứ
$(i- 2)$
là một ô trống thì Tấn có thể di chuyển con chốt thứ
$i$
tới vị trí
$i- 2$
*
Nếu ô thứ
$(i+ 1)$
có một con chốt khác và ô thứ
$(i+ 2)$
là một ô trống thì Tấn có thể di chuyển con chốt thứ
$i$
tới vị trí
$i+ 2$
Hãy đếm trạng thái khác nhau của các con chốt trên bàn cờ chia dư cho
$998244353$
. Hai trạng thái được coi là khác nhau nếu có ít nhất một vị trí
$i$
khác nhau.


## 🧩 Input

Input
Dòng đầu gồm
$q$
là số lượng số test
$(1 ≤q≤ 105)$
, mỗi test có dạng.
Dòng đầu gồm
$n$
$(1 ≤n≤ 105)$
là kích thước của bàn cờ.
Dòng tiếp theo gồm
$n$
ký tự, mỗi ký tự là
$0$
hoặc
$1$
thể hiện vị trí đó có chốt đứng không.
Dữ liệu đảm bảo tổng
$n$
ở các test sẽ không vượt quá
$105$


## 💡 Output

Output
Gồm
$q$
dòng ứng với đáp án của
$q$
test.


## 🧠 Example

### Input

```text
3
4
0110
6
011011
5
01010
```

### Output

```text
3
6
1
```



## 📝 Note

Note
Ở test đầu
$3$
trạng thái là:
$1100$
$0110$
$0011$

