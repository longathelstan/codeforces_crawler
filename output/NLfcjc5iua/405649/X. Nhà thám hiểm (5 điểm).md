# X. Nhà thám hiểm (5 điểm)

## 📖 Problem

Một nhà thám hiểm bắt đầu từ phòng
$(1, 1)$
muốn di chuyển đến phòng
$(N,M)$
tuân thủ qui tắc sau:
Trên sàn của mỗi phòng có viết một số huyền bí là số nguyên trong khoảng từ 1 đến 1000. Khi nhà thám hiểm có thể lựa chọn một trong tám hướng di chuyển (song song với các bức tường hoặc theo các đường chéo) lập tức anh ta được di chuyển theo hướng đó đi một số lượng phòng đúng bằng số viết trên sàn nhà theo hướng đã chọn. Nếu như điều đó không thực hiện được (khi số lượng phòng theo hướng lựa chọn là nhỏ hơn số viết trên sàn) thì nhà thám hiểm vẫn ở nguyên vị trí và buộc phải lựa chọn hướng dịch chuyển khác. Không được di chuyển hai lần trong cùng một phương theo cùng một hướng.
Yêu cầu: Tìm cách di chuyển từ ô
$(1, 1)$
đến ô
$(N,M)$
sau ít lần dịch chuyển nhất.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên
$N$
,
$M$
, tương ứng là số phòng theo chiều ngang và theo chiều đứng của sơ đồ toà lâu đài
$(1≤N,M≤1000)$
.
Dòng thứ
$i$
trong số
$M$
dòng tiếp theo chứa dãy
$N$
số nguyên là các số viết trên dãy phòng ở dòng thứ
$i$
của toà lâu đài.
Các số trên cùng dòng được viết cách nhau bởi dấu cách.


## 💡 Output

Output
Ghi ra số bước dịch chuyển ít nhất. Ghi
$- 1$
nếu không có cách di chuyển đến ô
$(N,M)$
.


## 🧠 Example

### Input

```text
5 4
3 3 6 7 11
3 2 1 1 3
3 2 2 1 1
2 1 2 2 1
```

### Output

```text
4
```



## 📝 Note

Note
Nếu nhà thám hiểm đang đứng ở phòng (3, 3) trong lâu đài thì anh ta có thể di chuyển đến các phòng (1;1), (3;1), (1;3), (5;1), và (5;3). Để di chuyển từ phòng (3, 2) đến phòng (5,4) sử dụng hai lần dịch chuyển, nhà thám hiểm không được di chuyển đến ô (4,3) rồi từ (4,3) đến (5,4), bởi vì như vậy đã di chuyển trong cùng một phương theo cùng một hướng, mà cần di chuyển đến ô (2,1) và từ đó đến (5,4).

