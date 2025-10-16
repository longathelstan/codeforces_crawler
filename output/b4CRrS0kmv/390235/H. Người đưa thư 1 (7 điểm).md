# H. Người đưa thư 1 (7 điểm)

## 📖 Problem

Vì tạch VOI nên Hưng quyết định đổi nghề sang làm người đưa thư.
Thành phố Hưng làm việc là thành phố gồm
$n$
ngôi nhà liên thông với nhau, có
$n- 1$
con đường hai chiều có độ dài khác nhau nối giữa các ngôi nhà, hằng ngày Hưng có thể xuất phát tại bất cứ ngôi nhà nào (vì cậu vô gia cư nên ngủ ở đâu cũng được) và phải đi giao thư tới
$n$
ngôi nhà này.
Yêu cầu:
Hưng muốn nhờ bạn giúp Hưng đưa ra độ dài đường đi ngắn nhất để giao thư hết
$n$
ngôi nhà này khi có thể xuất phát ở bất kỳ đâu và không cần trở về điểm xuất phát, mỗi ngôi nhà có thể đi qua nhiều lần.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên dương
$n$
$(1 ≤n≤ 105)$
$n- 1$
dòng tiếp theo, mỗi dòng chứa
$3$
số nguyên
$u$
,
$v$
,
$w$
biểu diễn cạnh nối giữa
$2$
đỉnh
$u,v$
với trọng số là
$w$
.
$(1 ≤u,v≤n,u≠v, 1 ≤w≤ 109)$
.


## 💡 Output

Output
Gồm một dòng duy nhất chứa đáp án cần tìm


## 🧠 Example

### Input

```text
7
1 2 1
2 3 1
1 4 1
4 5 1
1 6 1
6 7 1
```

### Output

```text
8
```


