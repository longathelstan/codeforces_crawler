# N. Toà nhà 3

## 📖 Problem

Hưng có
$N$
tòa nhà có chiều cao lần lượt là
$h1,h2,h3, ...,hn$
, Hưng muốn làm sao để mọi tòa nhà có chiều cao bằng nhau. Điều này có thể thực hiện bằng cách lấy đi gạch từ một tòa nhà hoặc thêm một viên gạch vào một tòa nhà hoặc lấy một viên gạch từ toà nhà này sang toà nhà khác.
Việc thêm một viên gạch vào một toà sẽ có chi phí là
$a$
.
Việc lấy đi một viên gạch từ một toà sẽ có chi phí là
$b$
Việc lấy một viên gạch từ một toà nhà này sang một toà nhà khác là
$c$
Yêu cầu:
hãy tìm chi phí tối thiểu để Hưng có thể làm cho
$i$
tòa nhà đầu
trở nên đẹp mắt bằng cách tái cấu trúc các tòa nhà sao cho
$n$
tòa nhà đầu thỏa mãn điều kiện:
$h1=h2=h3= ... =hn=k$
(với
$k$
có thể là bất kỳ số nào).
Để thuận tiện, tất cả các tòa nhà được coi là những chồng gạch thẳng đứng, và các viên gạch có kích thước giống nhau.


## 🧩 Input

Input
Dòng đầu gồm
$4$
số
$N$
,
$a$
,
$b$
,
$c$
$(1 ≤N≤ 2 * 105, 1 ≤a,b,c≤ 104)$
Dòng tiếp theo gồm
$N$
số, số thứ
$i$
là giá trị của
$hi$
$(1 ≤hi≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
3 1 5 100
1 10 100
```

### Output

```text
189
```


