# ZZF. Xâu đối xứng

## 📖 Problem

Cho xâu S gồm n kí tự in thường. Cho Q truy vấn có dạng $$$L_i, R_i$$$ với $$$(1 \le i \le Q)$$$, yêu cần kiểm tra xem xâu con $$$S[L...R]$$$ có phải xâu đối xứng hay không?


## 🧩 Input

Input
Dòng đầu tiên cho số nguyên dương n,Q $$$(n \le 2000, Q \le 10^5)$$$.
Dòng thứ hai là xâu S gồm các kí tự in thường.
Q dòng tiếp theo gồm 2 số nguyên $$$L_i, R_i$$$ $$$(1 \le L_i \le R_i \le n)$$$


## 💡 Output

Output
Gồm Q dòng chứa kết quả của từng truy vấn, in ra "YES" nếu là xâu đối xứng và "NO" không phải xâu đối xứng.


## 🧠 Example

### Input

```text
6 4
abbbba
1 3
2 3
2 4
1 6
```

### Output

```text
NO
YES
YES
YES
```


