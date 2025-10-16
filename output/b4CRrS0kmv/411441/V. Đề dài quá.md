# V. Đề dài quá

## 📖 Problem

yenthanh132 vừa trúng vé số, anh ta định mua một hòn đảo để xây nhà nghỉ mát. Thế là anh ta để ý ngay đến vương quốc đảo dừa trù phú của Pirate vĩ đại. Sau cuộc nội chiến dừa và vụ "tam phân thiên hạ" lộn xộn vừa rồi thì hiện vương quốc dừa đã được bình yên với sự cai trị của vị vua mới - Pirakute (Xem bài VMAOCE để biết thêm chi tiết). Do rất yêu quê hương đảo nước của mình nên Pirakute đã một mực không chịu bán bất cứ hòn đảo nào cho yenthanh132, tuy nhiên nhờ sự đàm phán lâu dài cùng với mức giá kết xù của yenthanh132 đưa ra để mua đảo nên Pirakute sau khi suy nghĩ một thời gian đã đưa ra quyết định. Pirakute sẽ đồng ý bán cho yenthanh132 một hòn đảo với điều kiện anh ta phải tính được số hòn đảo hiện có trong vương quốc dừa.
Do sau một thời gian dài nội chiến nhiều thông tin đã bị mất, không ai thống kê lại xem hiện thời vương quốc dừa có tổng cộng bao nhiêu đảo. Thay vào đó chỉ còn lại một tài liệu cổ nói về lịch sử của vương quốc dừa từ thuở khai thiên lập địa. Tài liệu nói rằng từ thời xa xưa, cụ tổ Pirate đã xây dựng từng hòn đảo bằng cách chở dừa đến và chất thành đống ở giữa biển, các trái dừa này sẽ mọc ra những cây dừa và thế là một hòn đảo dừa được tạo ra. Lịch sử nói rằng K năm đầu tiên là thời kì khó khăn nhất của vương quốc dừa. Do có một số hòn đảo chất lượng không tốt nên bị mất đi và việc Pirate kiên trì tạo thêm các hòn đảo mới nên số lượng các hòn đảo qua K năm đầu tiên lên xuống thất thường nhưng luôn có ít nhất một đảo. Số lượng hòn đảo trong K năm đầu được lịch sử ghi lại trong dãy số a[1], a[2],... , a[K]. Sau K năm đó, tức là kể từ năm K+1, các cây dừa trên hòn đảo đã trưởng thành và cho trái, các trái dừa rớt xuống biển và tự động tạo nên các hòn đảo dừa mới một cách tự nhiên. Số lượng đảo dừa từ đó tăng một cách chống mặt và vương quốc dừa trở thành một đại cường quốc. Lịch sử cũng nói lại rằng số lượng đảo dừa trong năm thứ i sẽ bằng tích số lượng đảo dừa của K năm trước. Tức là số lượng đảo dừa của vương quốc trong năm i bằng a[i] = a[i-1] * a[i-2] * ... * a[i-K]. Mặc dù vương quốc đã trải qua nhiều thăng trầm, chiến tranh liên miên nhưng số lượng đảo dừa qua từng năm vẫn tăng đều theo công thức đó.
Thế là có đủ thông tin để yenthanh132 có thể tính được số lượng đảo dừa của vương quốc dừa. Nhưng tính tới thời điểm hiện tại đã là năm tồn tại thứ N của vương quốc và N là một số rất lớn nên không ai có thể tính được. yenthanh132 định dùng siêu máy tính mà anh ta đã mua hôm nọ (TNHTEST) nhưng khổ nỗi vương quốc dừa dùng điện năng lượng mặt trời nên không có đủ điện để chạy siêu máy tính được. Thế là giờ chỉ còn mỗi cái Laptop Pentium 3 800Mhz là có thể dùng được. Bạn là một nhà lập trình viên siêu hạng, hãy giúp yenthanh132 và chứng tỏ rằng Laptop cùi tới mấy mà biết sử dụng thì cũng có thể làm nên chuyện :)
- Cho số N, K và dãy số a[1], a[2],... , a[K] - số đảo dừa trong vương quốc qua K năm đầu
- Với i>K ta có a[i] = a[i-1] * a[i-2] * a[i-3] * ... * a[i-K];
- Tính a[N], do số lượng hòn đảo rất lớn nên yenthanh132 chỉ yêu cầu bạn tính phần dư của kết quả khi chia cho số 1000000007 ( = 10^9 + 7). Tức là tính a[N]
Lưu ý: Những đường dẫn đến bài tập bên ngoài chỉ mang tính chất tham khảo cho vui, không liên quan đến bài này.


## 🧩 Input

Input
Dòng đầu tiên gồm hai số nguyên dương N, K
$(1 ≤N≤ 109, 1 ≤K≤ 50,K<N)$
.
Dòng thứ hai ghi
$K$
số nguyên dương, số thứ
$i$
của dãy số là
$ai$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Ghi ra kết quả theo modulo 1000000007 (10^9 + 7).


## 🧠 Example

### Input

```text
7 3
1 2 3
```

### Output

```text
139968
```


