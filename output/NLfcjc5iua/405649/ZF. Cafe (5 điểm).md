# ZF. Cafe (5 điểm)

## 📖 Problem

Tấn và Phước đang thực hiện một chuyến đi đến Thành phố DakLak, nơi nổi tiếng với những quán cà phê cappuccino và expresso ngon nhất. Tuy nhiên, khi đi dạo quanh thành phố, họ đã lạc mất nhau.
Thành phố bao gồm
$n*m$
ô, mỗi ô
$(x,y)$
sẽ là số:
*
$0$
nếu nó không phải quán cà phê
*
$1$
nếu nó là quán cà phê chỉ phục vụ cappuccino
*
$2$
nếu nó là quán cà phê chỉ phục vụ expresso
*
$3$
nếu nó là quán cà phê phục vụ cả cappuccino và expresso
Tấn đang ở ô
$(1, 1)$
trong khi Phước đang ở
$(n,m)$
. Mỗi người trong số họ có thể di chuyển theo bốn hướng hoặc đứng yên tại ô của mình. Vì đã là mùa hè và thời tiết cực kỳ khủng khiếp nên đi bộ rất mệt và mỗi bước tốn 1 thể lực.
Tuy nhiên, có một thứ có thể tiết kiệm sức mạnh ý chí cho họ... Tấn thích expresso, còn Phước thích cà phê cappuccino. Nếu họ hiện đang ở trong một ô có quán cà phê phục vụ đồ uống ưa thích của họ, họ có thể uống và di chuyển đến bất kỳ ô lân cận nào mà không tốn sức lực.
Yêu cầu:
Xác định tổng sức lực tối thiểu mà cả hai phải bỏ ra để họ có thể gặp nhau ở bất kỳ ô nào.


## 🧩 Input

Input
Dòng đầu tiên nhập vào gồm một số nguyên
$T$
$(1 ≤T≤ 104)$
- Số lượng số test
Dòng đầu tiên của mỗi test gồm
$2$
số nguyên
$n,m$
$(1 ≤n,m≤ 106,n*m≤ 106)$
Dòng thứ
$i$
trong
$n$
dòng tiếp theo bao gồm
$m$
số nguyên
$ai, 1,ai, 2, ...,ai,m$
$(0 ≤ai,j≤ 3)$
mô tả ô
$(i,j)$
Dữ liệu đảm bảo
$n*m$
trên tất cả các trường hợp thử nghiệm sẽ không vượt quá
$106$


## 💡 Output

Output
Gồm
$T$
dòng ứng với
$T$
đáp án cần tìm


## 🧠 Example

### Input

```text
4
4 6
2 2 0 0 0 0
0 2 0 0 0 0
0 0 0 0 1 0
0 0 0 0 1 1
10 2
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
3 3
3 3 3
3 3 3
3 3 3
1 1
0
```

### Output

```text
2
10
0
0
```



## 📝 Note

Note
Với ví dụ
$1$
chọn địa điểm gặp là ô
$(3, 3)$
Tấn sẽ di chuyển
$(1, 1)$
->
$(1, 2)$
->
$(2, 2)$
->
$(2, 3)$
->
$(3, 3)$
với tổng chi phí là
$1$
Phước sẽ di chuyển
$(4, 6)$
->
$(4, 5)$
->
$(3, 5)$
->
$(3, 4)$
->
$(3, 3)$
với tổng chi phí là
$1$
Vậy tổng chi phí tối ưu nhất của
$2$
người là
$2$
.

