# S. SEC

## 📖 Problem

Bessie định dẫn đàn bò đi trốn. Để đảm bảo bí mật, đàn bò liên lạc với nhau bằng cách tin nhắn nhị phân.
Từng là một nhân viên phản gián thông minh, John đã thu được M (1 <= M <= 50,000) tin nhắn mật, tuy nhiên với tin nhắn i John chỉ thu được b_i (1 <= b_i <= 10,000) bit đầu tiên.
John đã biên soạn ra 1 danh sách N (1 <= N <= 50,000) các từ mã hóa mà đàn bò có khả năng đang sử dụng. Thật không may, John chỉ biết được c_j (1 <= c_j <= 10,000) bit đầu tiên của từ mã hóa thứ j.
Với mỗi từ mã hóa j, John muốn biết số lượng tin nhắn mà John thu được có khả năng là từ mã hóa j này. Tức là với từ mã hóa j, có bao nhiêu tin nhắn thu được có phần đầu giống với từ mã hóa j này. Việc của bạn là phải tính số lượng này.
Tổng số lượng các bit trong dữ liệu đầu vào (tổng các b_i và c_j) không quá 500,000.


## 🧩 Input

Input
Dòng 1: 2 số nguyên: M và N
Dòng 2..M+1: Dòng i+1 mô tả tin nhắn thứ i thu được, đầu tiên là b_i sau đó là b_i bit cách nhau bởi dấu cách, các bit có giá trị 0 hoặc 1.
Dòng M+2..M+N+1: DÒng M+j+1 mô tả từ mã hóa thứ j, đầu tiên là c_j sau đó là c_j bit cách nhau bởi dấu cách.


## 💡 Output

Output
Dòng 1..M: Dòng j: Số lượng tin nhắn mà có khả năng là từ mã hóa thứ j


## 🧠 Example

### Input

```text
4 5
3 0 1 0
1 1
3 1 0 0
3 1 1 0
1 0
1 1
2 0 1
5 0 1 0 0 1
2 1 1
```

### Output

```text
1
3
1
1
2
```



## 📝 Note

Note
Có 4 tin nhắn và 5 từ mã hóa. Các tin nhắn thu được có phần đầu là 010, 1, 100 và 110. Các từ mã hóa có phần đầu là 0, 1, 01, 01001, và 11.
0 chỉ có khả năng là 010 -> 1 tin nhắn. 1 chỉ có khả năng là 1, 100, hoặc 110 -> 3 tin nhắn. 01 chỉ có thể là 010 -> 1 tin nhắn. 01001 chỉ có thể là 010 -> 1 tin nhắn. 11 chỉ có thể là 1 hoặc 110 -> 2 tin nhắn.

