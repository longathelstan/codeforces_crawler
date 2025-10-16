# M. Toà nhà 2

## 📖 Problem

Hưng có
$N$
tòa nhà có chiều cao lần lượt là
$h1,h2,h3, ...,hn$
, Hưng muốn làm sao để mọi tòa nhà có chiều cao bằng nhau. Điều này có thể thực hiện bằng cách lấy đi gạch từ một tòa nhà hoặc thêm một số gạch vào một tòa nhà. Việc lấy đi một viên gạch hoặc thêm một viên gạch tại toà
$i$
được thực hiện với chi phí
$ci$
.
Yêu cầu:
Với mỗi
$i$
từ
$1$
tới
$n$
, hãy tìm chi phí tối thiểu để Hưng có thể làm cho
$i$
tòa nhà đầu
trở nên đẹp mắt bằng cách tái cấu trúc các tòa nhà sao cho
$i$
tòa nhà đầu thỏa mãn điều kiện:
$h1=h2=h3= ... =hi=k$
(với
$k$
có thể là bất kỳ số nào).
Để thuận tiện, tất cả các tòa nhà được coi là những chồng gạch thẳng đứng, và các viên gạch có kích thước giống nhau.


## 🧩 Input

Input
Dòng đầu gồm
$N$
$(1 ≤N≤ 2 * 105)$
Dòng tiếp theo gồm
$N$
số, số thứ
$i$
là giá trị của
$hi$
$(1 ≤hi≤ 109)$
Dòng tiếp theo gồm
$N$
số, số thứ
$i$
là giá trị của
$ci$
$(1 ≤ci≤ 109)$
Test
$32$
không sai


## 💡 Output

Output
Gồm một dòng chứa
$n$
số cần tìm cách nhau bởi dấu cách


## 🧠 Example

### Input

```text
3
1 5 100
1 10 100
```

### Output

```text
0 4 1049
```


