# X. Chữ ký số xác nhận danh tính

## 📖 Problem

Một bài toán được đặt ra, nếu lỡ bằng cách nào đó hacker giả danh người giữ chìa khóa, và liên tục truyền các giá trị $$$x$$$ để tìm được khóa. Điều này rất nguy hiểm, chính vì thế họ lại nghĩ ra cách để xác nhận danh tính, đó là môt chìa khóa số đại diện cho số, và chỉ có người giữ chìa khóa mới có được nó. Để bảo đảm tính bảo mật nó cũng được giấu trong một tập dãy số. Dãy số ban đầu rỗng, ta có $$$q$$$ hoạt động trên mảng, mỗi hoạt động có $$$2$$$ loại sau:
Loại 1: Cập nhật hệ thống (type==1), bạn sẽ thêm một nguyên dương $$$u$$$ vào trong dãy.
Loại 2: Thử hệ thống (type==2), cụ thể ta sẽ thử tìm khóa trong dãy $$$a$$$ bởi ba con số $$$x,k,s$$$, khóa là một số nguyên dương $$$v$$$ có
xuất hiện
trong dãy số, và thỏa mãn các ràng buộc sau $$$GCD(x,v)$$$ chia hết cho $$$k$$$, $$$x+v \leq s$$$. Nếu có nhiều giá trị $$$v$$$ thỏa mãn, thì giá trị v sao cho $$$x$$$ xor $$$v$$$ là lớn nhất chính là khóa cần tìm.
Bạn hãy giải quyết bài toán trên để so với hệ thống nhá.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên $$$q$$$ $$$(1 \leq q \leq 10^5)$$$.
Mỗi dòng trong $$$q$$$ dòng, đầu tiên ta có số nguyên $$$type$$$, nếu $$$type=1$$$ thì tiếp theo là số nguyên dương $$$u$$$ $$$(1 \leq u \leq 10^5)$$$. Nếu $$$type=2$$$ thì tiếp theo là ba số nguyên dương $$$x,k,s$$$ $$$(1 \leq x,k,s \leq 10^5)$$$.


## 💡 Output

Output
Gồm $$$q$$$ dòng mỗi dòng là khóa tìm được, nếu không có khóa nào thỏa mãn thì hãy in ra -1.


## 🧠 Example

### Input

```text
5
1 1
1 2
2 1 1 3
2 1 1 2
2 1 1 1
```

### Output

```text
2
1
-1
```


