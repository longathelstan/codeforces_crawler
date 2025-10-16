# O. Tay đua tài ba

## 📖 Problem

Nhâm Tấn là tay đua tài ba đến từ đất biển và giờ đây anh ta sẽ bước vào một kỳ thi danh cho những ông trùm đua xe từ mọi miền đất nước hội tụ. Nhân dịp trước khi đua anh Tấn được tham quan trường đua, nơi đây có
$n$
địa điểm đặc biệt, địa điểm thứ
$i$
có độ cao là
$Hi$
so với mặt đất. Ngoài ra sẽ có một số đường đi nối giữa
$2$
địa điểm, theo luật của đường đua nếu ta đi từ địa điểm
$i$
đến
$j$
mà
$Hi$
bé hơn
$Hj$
sẽ mất đi
$Hj$
-
$Hi$
đơn vị xăng, tuy nhiên nếu lớn hơn bạn sẽ được btc cấp
$Hi$
-
$Hj$
đơn vị xăng.
Giờ đây Nhâm Tấn suy xét
$Q$
trường hợp, mỗi trường hợp giả sử anh đang đứng ở
$a$
và đích nằm ở
$b$
, hiện tại anh chỉ còn
$c$
xăng, anh muốn biết mình có thể đi đến
$b$
được không. Vì anh không thể vào đua thử mà chỉ có thể cung cấp cho bạn thông tin, bạn hãy lập trình để thông báo kết quả của mỗi thử nghiệm cho anh ấy nhé!


## 🧩 Input

Input
Dòng đầu chứa
$2$
số nguyên
$n$
và
$m$
$(2 ≤n≤ 2 * 105, 1 ≤m≤ 2 * 105)$
là số địa điểm đặc biệt và số lượng đường nối giữa 2 địa điểm.
Dòng tiếp theo chứa
$n$
số nguyên, số
$i$
là
$Hi$
$(1 ≤Hi≤ 109)$
là độ cao của đường đua.
$m$
dòng tiếp theo, mỗi dòng gồm
$2$
số nguyên
$u$
và
$v$
biểu thị có cạnh nối giữa 2 địa điểm
$u$
và
$v$
.
Dòng tiếp theo chứa số nguyên
$Q$
$(1 ≤Q≤ 2 * 105)$
.
$Q$
dòng tiếp theo mỗi dòng gồm
$3$
số nguyên
$a$
,
$b$
,
$c$
$(1 ≤a,b≤n, 0 ≤c≤ 109)$
lần lượt là địa điểm đang đứng hiện tại, đích đến và lượng xăng hiện tại của xe anh.


## 💡 Output

Output
$Q$
dòng, mỗi dòng là
$YES$
nếu như anh có thể về đích ngược lại in ra
$NO$
nếu điều đó là không thể.


## 🧠 Example

### Input

```text
7 7
1 5 3 4 2 4 1
1 4
4 3
3 6
3 2
2 5
5 6
5 7
5
1 1 3
6 2 0
4 7 0
1 7 4
1 7 2
```

### Output

```text
YES
NO
YES
YES
NO
```


