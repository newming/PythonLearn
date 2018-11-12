import tkinter
from tkinter import messagebox

def closeWindow():
    messagebox.showinfo(title='警告', message='在考虑考虑')
    return

def closenolove():
    noLove()

def noLove():
    # TopLevel 是一个独立的顶级窗口
    no_love = tkinter.Toplevel(window)
    no_love.title('再考虑考虑呗')
    no_love.geometry('300x100+630+300')
    label = tkinter.Label(no_love, text='再考虑考虑呗', font=('微软雅黑', 25))
    # 包定位
    label.pack()
    # 点击关闭当前窗口
    btn = tkinter.Button(no_love, text='好的', width=10, height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol('WM_DELETE_WINDOW', closenolove)

def Love():
    love = tkinter.Toplevel(window)
    love.title('好巧，我也是')
    love.geometry('300x100+630+300')
    label = tkinter.Label(love, text='好巧，我也是', font=('微软雅黑', 25))
    label.pack()
    btn = tkinter.Button(love, text='好的', width=10, height=2, command=closeLove)
    btn.pack()
    love.protocol('WM_DELETE_WINDOW', closeLoveToplevel)

def closeLove():
    window.destroy()

def closeLoveToplevel():
    pass

# 创建窗口
window = tkinter.Tk()
# 窗口的标题
window.title('你喜欢我吗？')
# 设置窗口的大小 注意是小写的 x 分隔的是窗口大小，+号跟的是窗口的位置
window.geometry('476x520+540+250')
# 设置窗口的位置
# window.geometry('+540+250')

# 用户点击关闭触发的方法
window.protocol('WM_DELETE_WINDOW', closeWindow)

# 标签控件
label = tkinter.Label(window, text='hello world', font=('微软雅黑', 15), fg='red')
# 定位 网格式布局  pack包  place位置
label.grid()

label1 = tkinter.Label(window, text='喜欢我吗？', font='微软雅黑')
# sticky 对齐方式 NSWE 上下左右 默认 row 第0行，column第0列，sticky 为W
label1.grid(row=1, column=1, sticky=tkinter.E)

# 设置图片 这里使用 jpg 有点问题 https://stackoverflow.com/questions/47357090/tkinter-error-couldnt-recognize-data-in-image-file?rq=1
photo = tkinter.PhotoImage(file='license.png')
imgLabel = tkinter.Label(window, image=photo)
# columnspan 合并单元格
imgLabel.grid(row=2, columnspan=2)

# 点击按钮
btn1 = tkinter.Button(window, text='喜欢', width=15, height=2, command=Love)
btn1.grid(row=3, column=0, sticky=tkinter.W)

btn2 = tkinter.Button(window, text='不喜欢', width=5, height=1, command=noLove)
btn2.grid(row=3, column=1, sticky=tkinter.E)

# 显示窗口 消息循环
window.mainloop()

"""
打包成 app

1. 安装 pip install pyinstaller
2. 找到程序位置执行
pyinstaller -F xxx.py
想去掉黑窗口
pyinstaller -F -w xxx.py
修改图标
pyinstaller -F -w -i xxx.ico xxx.py
http://www.bitbug.net 图标生成地址
"""