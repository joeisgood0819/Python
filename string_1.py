# \n 換行符號
# \t Tab字元
# \\ 正常的反斜線字元
# \ 普通的雙引號字元

x = "\t這個字元的開頭是\"tab\"字元"
y = "這個字串包含反斜線(\\)字元"

x = "Hello, 'World" #可以直接放'在裡面
x = 'Hello, "World' #可以直接放"在裡面

x = """blablabla""" #三引號字串可建立跨行字串

#Python獨有一行80字上限
if a == b:
    long_string = """Lorem ipsum dolor sit amet, consectetur adip.""" #缺點: 包含換行字元、破壞視覺架構

long_string = "Lorem ipesfkasfaffff" \
            = "akfdj;lfkja;lj;sff;a;s" \
            = "fjas;lfdjk;lfja;jfafsd"
#python將視為以上為一行

long_string = (
    "Lorem ipesfkasfaffff"
    "akfdj;lfkja;lj;sff;a;s"
    "fjas;lfdjk;lfja;jfafsd"
)
#同樣視為一行







