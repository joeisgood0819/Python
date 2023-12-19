# 在 Python 中，轉義字元（Escape characters）用於表示特殊的字符。以下是一些基本的轉義字元：

# \n - 換行符號（Newline）： 用於在字符串中插入換行。
message = "Hello,\nWorld!"
print(message)

#讓\n不會重複換行
# Default behavior (end='\n')
print("Hello")
print("World")
# Customizing the end parameter
print("Hello", end=' ')
print("World")


# \t - 制表符（Tab）： 用於在字符串中插入水平制表符。
indented_message = "This is an indented line.\tIndented!"
print(indented_message)

# \r - 回車符（Carriage Return）： 用於在字符串中插入回車。
carriage_return_message = "This line will be\rreplaced!"
print(carriage_return_message)

# \' - 單引號： 用於在字符串中插入單引號。
single_quote_message = 'This is a single-quote: \'Hello!\''
print(single_quote_message)

# \" - 雙引號： 用於在字符串中插入雙引號。
double_quote_message = "This is a double-quote: \"Hello!\""
print(double_quote_message)

# \a - 喚醒聲（Alert）： 通常用於發出嗶聲或其他提示聲。
alert_message = "This is an \aalert!"
print(alert_message)

# \b - 退格符號（Backspace）： 在字符串中插入退格。
backspace_message = "Backspace\bExample"
print(backspace_message)

# \f - 換頁符號（Form Feed）： 通常用於控制打印機或顯示器以換頁。
form_feed_message = "This is a line with\fform feed."
print(form_feed_message)

# \n - 換行符號（Newline）： 用於在字符串中插入換行。
newline_message = "This is a line with\nnewline."
print(newline_message)

# \r - 回車符號（Carriage Return）： 用於在字符串中插入回車。
carriage_return_message = "This line will be\rreplaced!"
print(carriage_return_message)

# \v - 垂直制表符號（Vertical Tab）： 通常用於垂直制表。
vertical_tab_message = "Vertical\vTab"
print(vertical_tab_message)