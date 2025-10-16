# R. CHAIN

## 📖 Problem

Chuỗi từ có độ dài n là một dãy các từ w1, w2, ..., wn sao cho với mọi 1 ≤ i < n, từ wi là tiền tố của từ wi+1.
Nhắc lại từ u có độ dài k là tiền tố của từ v có độ dài l nếu l > k và các ký tự đầu tiên của v trùng với từ u.
Cho tập hợp các từ S={s1, s2, ..., sm}. Tìm chuỗi từ dài nhất có thể xây dựng được bằng cách dùng các từ trong tập hợp S (có thể không sử dụng hết các từ).


## 🧩 Input

Input
Dòng đầu tiên chứa số nguyên m (1 ≤ m ≤ 250000). Mỗi dòng trong số m dòng sau chứa một từ trong tập S.
Biết rằng mỗi từ có độ dài không quá 250000 ký tự và tổng độ dài của các từ không vượt quá 250000 ký tự.


## 💡 Output

Output
In ra một số duy nhất là độ dài của chuỗi từ dài nhất xây dựng được từ các từ trong tập đã cho.


## 🧠 Example

### Input

```text
3
a
ab
abc
```

### Output

```text
3
```


