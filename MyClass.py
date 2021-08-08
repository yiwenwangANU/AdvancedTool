#!python3
# coding:utf8

from tkinter import Tk, Frame, TOP, LEFT, END, Y, Label, Entry, BOTH, Button

import os, csv


class Product:
    def __init__(self, name='', specification='', info='', num=0):
        self.name = name
        self.specification = specification
        self.info = info
        self.num = num

    def setNum(self, num):
        self.num = num


class Bland:
    def __init__(self, name='', industry='', country='', bland_num='', info=''):
        self.name = name
        self.industry = industry
        self.country = country
        self.bland_num = bland_num
        self.info = info
        self.product_list = []

    def setBland(self, name, industry, country, bland_num, info):
        self.name = name
        self.industry = industry
        self.country = country
        self.bland_num = bland_num
        self.info = info

    def addProduct(self, product):
        self.product_list.append(product)

    def combineInfoProduct(self, name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4, info4,
                           name5, spec5, info5):
        if name1 != '':
            self.addProduct(Product(name1, spec1, info1))
        if name2 != '':
            self.addProduct(Product(name2, spec2, info2))
        if name3 != '':
            self.addProduct(Product(name3, spec3, info3))
        if name4 != '':
            self.addProduct(Product(name4, spec4, info4))
        if name5 != '':
            self.addProduct(Product(name5, spec5, info5))
        return self.getInfo()

    def getBlandInfo(self):
        return '<hr /><h3>产品类型</h3>\n<p style="text-align: center;">' + self.industry + ',' + self.country + \
               '</p>\n<hr /><h3>厂家介绍</h3>\n<img src="http://info.aoyoumall.com/Mypicture/' + self.bland_num + \
               '.jpg" />\n<p>' + self.info + '</p>\n<hr /><h3>产品介绍</h3> '

    def getProductInfo(self):
        if len(self.product_list) == 0:
            return ''
        else:
            productsinfo = ''
            i = 1
            for product in self.product_list:
                product.setNum(int(self.bland_num) + i)
                i += 1
                if product.specification == '':     # 如果未填规格内容
                    html_spec = ''
                else:
                    html_spec = '<p>规格：' + product.specification + '</p>\n'   # 如果填写了规格内容
                if product.info == '':
                    html_info = ''
                else:
                    html_info = '<p>' + product.info + '</p>'

                productsinfo = productsinfo + '\n<hr /><h3>' + product.name + \
                               '</h3>\n<img src="http://info.aoyoumall.com/Mypicture/' + str(product.num) + \
                               '.jpg" />\n' + html_spec + html_info
            return productsinfo

    def getInfo(self):
        return self.getBlandInfo() + self.getProductInfo()


def change_label(name, test_output):
    test_output.delete(0, END)
    test_output.insert(0, name)
    return test_output


class ProductFrame(Frame):
    def __init__(self, bland, submitted=False):
        super().__init__()
        self.initUI()
        self.bland = bland
        self.submitted = submitted

    # 提交按键
    # 点击之后获取所有文本框内所填信息, 将商品信息加到product列表中，
    # 之后将所有文本框清空, 并将所得信息汇总并将HTML代码在输出文本框中输出
    def buttonSubmit(self, name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4, info4, name5,
                     spec5, info5, output):
        change_label(self.bland.combineInfoProduct(name1.get(), spec1.get(), info1.get(),
                                                   name2.get(), spec2.get(), info2.get(),
                                                   name3.get(), spec3.get(), info3.get(),
                                                   name4.get(), spec4.get(), info4.get(),
                                                   name5.get(), spec5.get(), info5.get()), output),
        name1.delete(0, END), spec1.delete(0, END), info1.delete(0, END),
        name2.delete(0, END), spec2.delete(0, END), info2.delete(0, END),
        name3.delete(0, END), spec3.delete(0, END), info3.delete(0, END),
        name4.delete(0, END), spec4.delete(0, END), info4.delete(0, END),
        name5.delete(0, END), spec5.delete(0, END), info5.delete(0, END)

    #
    def buttonExport(self, name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4, info4, name5,
                     spec5, info5):
        text_output = self.bland.combineInfoProduct(name1.get(), spec1.get(), info1.get(),
                                                    name2.get(), spec2.get(), info2.get(),
                                                    name3.get(), spec3.get(), info3.get(),
                                                    name4.get(), spec4.get(), info4.get(),
                                                    name5.get(), spec5.get(), info5.get())

        fieldnames = ['classid', 'title', 'ftitle', 'newstext', 'titlepic', 'category', 'subcategory', 'Tags']
        if os.path.exists('01批量上传.csv'):
            if self.submitted:
                with open('01批量上传.csv', 'r+', encoding='utf-8-sig') as csv_file:
                    reader = list(csv.reader(csv_file, skipinitialspace=True))

                with open('01批量上传.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
                    writer = csv.writer(csv_file)
                    for row in reader[:-1]:
                        writer.writerows([row])
                        print(row)

            with open('01批量上传.csv', 'a', newline='', encoding='utf-8-sig') as csv_file:

                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(
                    {'classid': 1, 'title': self.bland.name, 'ftitle': self.bland.name, 'newstext': text_output,
                     'titlepic': 'http://info.aoyoumall.com/Mypicture/' + self.bland.bland_num + '.jpg',
                     'category': self.bland.country, 'subcategory': self.bland.industry, 'Tags': ''})
        else:
            with open('01批量上传.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(
                    {'classid': 1, 'title': self.bland.name, 'ftitle': self.bland.name, 'newstext': text_output,
                     'titlepic': 'http://info.aoyoumall.com/Mypicture/' + self.bland.bland_num + '.jpg',
                     'category': self.bland.country, 'subcategory': self.bland.industry, 'Tags': ''})

        self.submitted = True

    def initUI(self):
        self.master.title("批量上传助手 2.0 version")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(side=LEFT, fill=Y)
        Label(frame1, text="产品名字1", width=8).pack(side=TOP, padx=5, pady=5)
        name1 = Entry(frame1)
        name1.pack(side=TOP, padx=5)
        Label(frame1, text="产品规格1", width=8).pack(side=TOP, padx=5, pady=5)
        spec1 = Entry(frame1)
        spec1.pack(side=TOP, padx=5)
        Label(frame1, text="产品介绍1", width=8).pack(side=TOP, padx=5, pady=5)
        info1 = Entry(frame1, width=20)
        info1.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

        frame2 = Frame(self)
        frame2.pack(side=LEFT, fill=Y)
        Label(frame2, text="产品名字2", width=8).pack(side=TOP, padx=5, pady=5)
        name2 = Entry(frame2)
        name2.pack(side=TOP, padx=5)
        Label(frame2, text="产品规格2", width=8).pack(side=TOP, padx=5, pady=5)
        spec2 = Entry(frame2)
        spec2.pack(side=TOP, padx=5)
        Label(frame2, text="产品介绍2", width=8).pack(side=TOP, padx=5, pady=5)
        info2 = Entry(frame2, width=20)
        info2.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

        frame3 = Frame(self)
        frame3.pack(side=LEFT, fill=Y)
        Label(frame3, text="产品名字3", width=8).pack(side=TOP, padx=5, pady=5)
        name3 = Entry(frame3)
        name3.pack(side=TOP, padx=5)
        Label(frame3, text="产品规格3", width=8).pack(side=TOP, padx=5, pady=5)
        spec3 = Entry(frame3)
        spec3.pack(side=TOP, padx=5)
        Label(frame3, text="产品介绍3", width=8).pack(side=TOP, padx=5, pady=5)
        info3 = Entry(frame3, width=20)
        info3.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

        frame4 = Frame(self)
        frame4.pack(side=LEFT, fill=Y)
        Label(frame4, text="产品名字4", width=8).pack(side=TOP, padx=5, pady=5)
        name4 = Entry(frame4)
        name4.pack(side=TOP, padx=5)
        Label(frame4, text="产品规格4", width=8).pack(side=TOP, padx=5, pady=5)
        spec4 = Entry(frame4)
        spec4.pack(side=TOP, padx=5)
        Label(frame4, text="产品介绍4", width=8).pack(side=TOP, padx=5, pady=5)
        info4 = Entry(frame4, width=20)
        info4.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

        frame5 = Frame(self)
        frame5.pack(side=LEFT, fill=Y)
        Label(frame5, text="产品名字5", width=8).pack(side=TOP, padx=5, pady=5)
        name5 = Entry(frame5)
        name5.pack(side=TOP, padx=5)
        Label(frame5, text="产品规格5", width=8).pack(side=TOP, padx=5, pady=5)
        spec5 = Entry(frame5)
        spec5.pack(side=TOP, padx=5)
        Label(frame5, text="产品介绍5", width=8).pack(side=TOP, padx=5, pady=5)
        info5 = Entry(frame5, width=20)
        info5.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

        frame6 = Frame(self)
        frame6.pack(side=LEFT, fill=Y)
        Label(frame6, text="Output", width=8).pack(side=TOP, padx=5, pady=5)
        output = Entry(frame6)
        output.pack(side=TOP, fill=BOTH, padx=5, expand=True)
        bt1 = Button(frame6, text='Submit', width=20, height=3,
                     command=lambda: [
                         self.buttonSubmit(name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4,
                                           info4, name5, spec5, info5, output)
                     ])
        bt1.pack(side=TOP, padx=5, pady=5)
        bt2 = Button(frame6, text='Export', width=20, height=3,
                     command=lambda: [
                         self.buttonSubmit(name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4,
                                           info4, name5, spec5, info5, output),
                         self.buttonExport(name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4,
                                           info4, name5, spec5, info5)
                     ])
        bt2.pack(side=TOP, padx=5, pady=5)


class RootFrame(Frame):

    def __init__(self, bland):
        super().__init__()
        self.initUI()
        self.bland = bland

    def createProduct(self, name, industry, country, img_start, bland_info, bland):
        bland.setBland(name, industry, country, img_start, bland_info)
        self.master.destroy()
        product = Tk()
        ProductFrame(bland)
        product.mainloop()

    def initUI(self):
        self.master.title("批量上传助手 2.0 version")
        self.pack(fill=BOTH, expand=True)

        Label(self, text='品牌').pack()
        text_name = Entry(self, width=20)
        text_name.pack()

        Label(self, text='国家').pack()
        text_country = Entry(self, width=20)
        text_country.pack()

        Label(self, text='类型').pack()
        text_industry = Entry(self, width=20)
        text_industry.pack()

        Label(self, text='厂家介绍').pack()
        text_bland_info = Entry(self, width=20)
        text_bland_info.pack()

        Label(self, text='图片开始编号').pack()
        text_img_start = Entry(self, width=20)
        text_img_start.insert(END, '0')
        text_img_start.pack()

        bt2 = Button(self, text='添加商品', width=20, height=3,
                     command=lambda: self.createProduct(text_name.get(), text_industry.get(), text_country.get(),
                                                        text_img_start.get(), text_bland_info.get(), self.bland))
        bt2.pack(padx=5, pady=10)
