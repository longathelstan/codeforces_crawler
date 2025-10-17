# S. Trung tâm thành phố

## 📖 Problem

Ở đất nước ByteLand có n thành phố (đánh số thứ tự từ 1 đến
$n$
) được nối với nhau bằng
$m$
con đường hai chiều). Do yêu cầu về sự thịnh vượng của đất nước, cần thiết phải di chuyển thủ đô hiện thời về một thành phố nào đó trong số các thành phố nói trên. Quốc hội ByteLand muốn chọn một thành phố trung tâm nhất để di chuyển thủ đô đến đó.
Thành phố được gọi là trung tâm nếu như khi cấm các hoạt động giao thông qua thành phố này và trên các con đường nối với nó thì các thành phố còn lại tạo thành nhiều cụm thành phố nhất. Một cụm thành phố là một nhóm các thành phố mà giữa hai thành phố bất kỳ có thể đi đến được với nhau thông qua các thành phố trong cụm. Tất nhiên, nếu thêm một thành phố khác vào cụm thì tính chất trên bị phá vỡ.
Yêu cầu
: Viết chương trình tìm thành phố trung tâm cho Quốc Hội.


## 🧩 Input

Input
Dòng đầu tiên ghi hai số nguyên dương
$n$
,
$m$
$(1 ≤n≤ 3 * 105,n- 1 ≤m≤ 3 * 105)$
$m$
dòng tiếp theo, mỗi dòng ghi hai số
$ai$
,
$bi$
thể hiện có một đường đi hai chiều nối thành phố
$ai$
với thành phố
$bi$
.


## 💡 Output

Output
Ghi hai số
$Cmax$
và
$C$
thể hiện số cụm lớn nhất tạo ra khi cấm đường giao thông qua thành phố trung tâm và số hiệu của thành phố trung tâm này.
Nếu có nhiều thành phố trung tâm thì chỉ in ra thành phố có chỉ số nhỏ nhất


## 🧠 Example

### Input

```text
5 5
1 2
3 2
4 2
5 2
1 3
```

### Output

```text
3 2
```


