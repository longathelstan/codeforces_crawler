# ZZU. Cột điện

## 📖 Problem

Công ty điện lực XYZ có nhiệm vụ cung cấp điện cho thành phố Nha Trang. Để cung cấp điện cho thành phố công ty đã cho lắp hệ thống gồm
$n$
cột điện được đánh số theo thứ tự từ
$1$
đến
$n$
, cột điện thứ
$i$
có chiều cao là một số nguyên dương
$hi$
, các dây điện được nối giữa các cột điện liền kề, tức là nối từ cột
$1$
đến cột
$2$
, từ cột
$2$
đến cột
$3$
, ..., từ cột
$n- 1$
đến cột
$n$
.
Vì mỹ quan đô thị, thành phố Nha Trang đã đưa ra quy định sẽ thu của công ty XYZ một khoản chi phí cho hai cột điện liền kề
$i$
và
$i+ 1$
là tổng
$c$
x
$|hi$
-
$hi- 1|$
(
$i$
=
$2$
..
$n$
). Để giảm thiểu chi phí, lãnh đạo công ty đã quyết định chọn giải pháp cho lắp đặt nâng chiều cao một số cột điện. Tuy nhiên, nếu cột điện
$i$
nâng chiều cao thêm
$x$
đơn vị thì công ty phải mất một khoản chi phí là
$x2$
Yêu cầu: Cho biết
$n$
và
$c$
và các chiều cao
$hi$
, bạn hãy giúp công ty XYZ tính chi phí thấp nhất khi công ty thực hiện theo giải pháp của lãnh đạo công ty.


## 🧩 Input

Input
Dòng đầu gồm
$n$
,
$c$
$(1 ≤n≤ 104, 1 ≤c≤ 106)$
Mỗi dòng trong
$n$
dòng sau chứa một số nguyên
$hi$
$(1 ≤hi≤ 1000)$


## 💡 Output

Output
Một số nguyên là chi phí thấp nhất mà công ty XYZ phải trả


## 🧠 Example

### Input

```text
5 2
2
3
5
1
4
```

### Output

```text
15
```



## 📝 Note

Note
Test
$1$
:
Nâng cột
$1$
thêm
$1$
, nâng cột
$4$
thêm
$2$
. Khi đó chiều cao các cột lần lượt là:
$3, 3, 5, 3, 4$
. Tổng chi phí là
$2$
x
$(0 + 2 + 2 + 1)$
+
$12$
+
$22$
= 15

