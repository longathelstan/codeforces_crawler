# D. Đường mới

## 📖 Problem

Trong vương quốc có
$n$
thành phố và hiện có
$m$
đường thương mại. Mỗi đường thương mại nối trực tiếp 2 thành phố và là đường một chiều.
Thương nhân mang hàng hóa đi bán ở các thành phố khác và sẽ là tốt nhất nếu anh ta mua được hàng hóa mới và trở về thành phố của mình không phải với chiếc xe ngựa rỗng. Dĩ nhiên, khi đó vì mục đích an toàn, anh ta phải quay về bằng đường thương mại.
Nếu từ
$A$
có thể tới
$B$
theo các con đường thương mại và từ
$B$
có thể trở về
$A$
cũng theo các con đường thương mại thì
$A$
và
$B$
là hai thành phố thân thiện.
Để giảm bớt nỗi cực nhọc của các thương nhân bình dân, chính phủ cho sửa sang lại các tuyến thương mại hiện có và cho xây dựng thêm một số đường thương mại mới. Tuy vậy, với ngân khố quốc gia hạn chế, nhà vua quyết định chỉ mở thêm các đường thương mại nối các thành phố thân thiện và không trùng lặp với các đường hiện có, sao cho giữa các thành phố thân thiện có đường nối trực tiếp với nhau.
Yêu cầu:
Cho
$n$
,
$m$
và mạng đường thương mại hiện có. Xác định số đường mới tối thiểu cần xây dựng thêm.


## 🧩 Input

Input
Dòng đầu tiên chứa 2 số nguyên
$n$
và
$m$
$(1 ≤n≤ 105, 0 ≤m≤ 2 * 105)$
Mỗi dòng trong m dòng tiếp theo chứa 2 số nguyên
$A$
và
$B$
xác định đường thương mại đi trực tiếp từ
$A$
đến
$B$
.
Chú ý:
Giữa 2 điểm có thể có nhiều con đường nối.


## 💡 Output

Output
Một dòng duy nhất chứa số nguyên là số đường mới tối thiểu cần xây dựng thêm.


## 🧠 Example

### Input

```text
3 3
1 2
2 3
3 1
```

### Output

```text
3
```


