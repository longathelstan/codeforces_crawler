# ZZZZ. Trồng cây

## 📖 Problem

Ông
$X$
đang lên kế hoạch trồng cây trong khu vườn của mình. Có
$n$
loại cây mà ông cân nhắc muốn trồng. Cụ thể, nếu ông mua
$s$
cây loại thứ
$i$
thì ông cần bỏ ra
$s×ci$
đồng và hiệu quả kinh tế của s cây loại đó đem lại là
$vi+ (vi−wi) + ⋯ + (vi−(s−1)×wi)$
. Ông
$X$
dự định sẽ bỏ ra tất cả
$T$
đồng và muốn tìm phương án mua để tổng hiệu quả kinh tế là lớn nhất.
Yêu cầu: Cho
$n$
loại cây, cây thứ
$i$
$(i= 1, 2, ...,n)$
có các thông tin là
$ci,vi,wi$
và
$m$
câu hỏi
$T1,T2, ...,Tm$
. Với mỗi câu hỏi
$Tk(k= 1, 2, ...,m)$
, hãy tìm phương án giúp ông
$X$
dùng không quá
$Tk$
đồng để mua những loại cây nào và số lượng tương ứng là bao nhiêu để tổng hiệu quả kinh tế là lớn nhất.


## 🧩 Input

Input
Dòng đầu chứa hai số nguyên dương
$n$
,
$m$
$(n≤ 105,m≤10)$
;
Tiếp theo là n dòng, mỗi dòng chứa ba số nguyên dương
$ci,vi,wi(ci,vi,wi≤1000)$
;
Cuối cùng là một dòng chứa
$m$
số nguyên dương
$T1,T2, ...,Tm(Tk≤1000)$
.


## 💡 Output

Output
Gồm một dòng chứa
$m$
số nguyên là tổng hiệu quả kinh tế lớn nhất mà ông
$X$
có thể đạt được tương ứng với
$m$
câu hỏi trong dữ liệu vào.


## 🧠 Example

### Input

```text
3 1
5 10 5
4 7 2
1 1 1
10
```

### Output

```text
18
```


