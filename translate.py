from tkinter import *
import requests
request = requests.session()

root = Tk()
root.geometry('600x130')
root.geometry('+550+280')

frm1 = Frame(root)
l = Label(frm1, text='输入内容:', font=('黑体', 20))
l.pack(side=LEFT)
varinput = StringVar()
varinput.set('')
e = Entry(frm1, textvariable=varinput, width=70, font=('黑体', 20))
e.pack(side=LEFT, padx='5')
frm1.pack(side=TOP)

frm2 = Frame(root)
l = Label(frm2, text='翻译结果:', font=('黑体', 20))
l.pack(side=LEFT)
varoutput = StringVar()
varoutput.set('')
e = Entry(frm2, textvariable=varoutput, width=70, font=('黑体', 20))
e.pack(side=LEFT, padx='5', pady='5')
frm2.pack(side=TOP)

def translate():
    data = {
        'kw':  varinput.get()
    }
    response = request.post('http://fanyi.baidu.com/sug', data=data)
    response = response.json()
    if not response['data']:
        varoutput.set('未找到对应的翻译')
    else:
        response = response['data'][0]['v']
        res = response.split(';')[0]
        varoutput.set(res)

Button(text='翻译', font=('黑体', 20), command=translate).pack(pady='10')
root.mainloop()