# L. Password 2

## 📖 Problem

Một phần mềm quản lý tại công ty B-SOFT được một nhân viên phát hiện ra lỗi bảo mật rất thú vị. Phần mềm này phục vụ cho N nhân viên trong công ty, mỗi nhân viên có một tài khoản đi kèm với một mật khẩu để đăng nhập vào hệ thống nhưng trong một số trường hợp, nhân viên này có thể dùng mật khẩu của mình để đăng nhập vào tài khoản của nhân viên khác nếu chuỗi ký tự mật khẩu của nhân viên này chứa chuỗi con (các ký tự liên tiếp nhau) là mật khẩu của nhân viên kia. Giám đốc công ty muốn biết mật khẩu mỗi người có thể dùng để truy cập được bao nhiêu tài khoản của người khác.
Yêu cầu
: Bạn hãy giúp Giám đốc công ty B-SOFT giải quyết bài toán trên.


## 🧩 Input

Input
Dòng đầu ghi số nguyên dương
$N$
$(1≤N≤105)$
.
Dòng thứ
$i$
$(i= 1...N)$
trong
$N$
dòng tiếp theo, mỗi dòng ghi một xâu ký tự gồm các chữ cái thường trong bảng chữ cái tiếng Anh.
Dữ liệu đảm bảo tổng số lượng ký tự của
$N$
xâu sẽ không vượt quá
$105$


## 💡 Output

Output
Gồm
$N$
dòng, với dòng thứ
$i$
$(i= 1...N)$
là số lượng tài khoản (không kể tài khoản của mình) mà người thứ
$i$
có thể đăng nhập được vào hệ thống bằng mật khẩu của mình.


## 🧠 Example

### Input

```text
3
a
a
ab
```

### Output

```text
1
1
2
```


