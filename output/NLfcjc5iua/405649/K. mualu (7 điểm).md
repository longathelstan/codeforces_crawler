# K. mualu (7 điểm)

## 📖 Problem

Tỉnh Alpha có $$$n$$$ ngôi làng khác nhau, các ngôi làng được đánh số thứ tự từ 1 đến $$$n$$$, giữa các ngôi làng được xây dựng hệ thống đường đi sao cho giữa hai ngôi làng bất kỳ luôn có đường đi và không có hai ngôi làng nào có nhiều hơn một con đường nối trực tiếp.
Mưa lũ thường xuyên xảy ra tại tỉnh Alpha làm cho giao thông giữa các ngôi làng có nguy cơ bị chia cắt, do vậy trong nhiều năm qua người dân đã cố gắng khắc phục bằng nhiều biện pháp như xây đê bao quanh các ngôi làng, nâng cao các tuyến đường... Tuy nhiên mọi biện pháp chỉ để đề phòng chứ không thể đảm bảo việc đi lại giữa các ngôi làng trong mùa mưa lũ.
Khi mùa lũ về, nếu mực nước dâng cao lên $$$x$$$ đơn vị (đo độ dài) thì những tuyến đường có độ cao nhỏ hơn x sẽ bị ngập trong nước, tỉnh Alpha có thể bị chia cắt thành nhiều vùng và người dân trong mỗi vùng sẽ bị cô lập không thể đi đến các vùng khác.
Yêu cầu: Hiện nay độ cao của mực nước tại tỉnh Alpha vừa đo được là $$$x$$$ đơn vị, bạn hãy tính xem tỉnh này đang bị chia cắt thành bao nhiêu vùng. Biết rằng một vùng bao gồm các làng có đường đi lại với nhau nhưng không có đường đi đến các làng ở vùng khác. Một làng không có đường đi đến tất cả các làng khác cũng được xem là một vùng.


## 🧩 Input

Input
- Dòng đầu tiên gồm ba số nguyên dương $$$n$$$, $$$m$$$, $$$x$$$ lần lượt là số làng, số tuyến đường và độ cao của nước $$$(1 ≤ n ≤ 10^5 ; 1 ≤ m ≤ 2.10^5; 1 ≤ x ≤ 10^9)$$$
- Trong $$$m$$$ dòng tiếp theo, mỗi dòng ghi 3 số nguyên $$$u$$$, $$$v$$$, $$$c$$$ trong đó $$$c$$$ là độ cao của tuyến đường nối $$$2$$$ làng $$$u$$$ và $$$v$$$ $$$(1 \leq u, v \leq n ; 1 \leq c \leq 10^9)$$$.
Giữa các số trên cùng một dòng được ghi cách nhau một dấu cách.


## 💡 Output

Output
Một số nguyên duy nhất là kết quả của bài toán


## 🧠 Example

### Input

```text
5 7 5
1 2 2
1 3 5
1 4 4
1 5 1
2 3 6
3 4 3
4 5 5
```

### Output

```text
2
```



## 📝 Note

Note
Các tuyến đường $$$(1, 2); (1, 4); (1, 5); (3, 4)$$$ bị ngập do vậy còn $$$2$$$ vùng $$$(4, 5)$$$ và $$$(1, 2, 3)$$$

