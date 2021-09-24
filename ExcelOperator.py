#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from UI.noname import plc
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np
import pandas as pd
from scipy.fftpack import fft
from math import pi

import wx
import wx.xrc
import locale

fbase = 50
hhh = 401

''' 函数：返回变量是否被定义过 '''


# def resource_path(relative_path):
#     if getattr(sys, 'frozen', False):  # 是否Bundle Resource
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)


def isset(v):
    try:
        type(eval(v))
    except:
        return 0
    else:
        return 1


class MyFrame(plc):
    locale.getlocale()
    ''' 创建输出路径  '''

    def __init__(self, parent):
        plc.__init__(self, parent)

        wx.Frame.SetBackgroundColour(self, 'Write')  # ???
        font1 = wx.Font(22, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.m_comboBox1.AppendItems('MDO4054C')
        # self.m_staticText15.SetFont(font1)
        # self.m_button.SetFont(font1)
        # self.m_button2.SetFont(font1)
        # self.m_staticText16.SetFont(font1)

    def OnButtonClick(self, event):

        print("OnButtonClick")
        fbase = float(self.m_textCtrl1.GetValue())  # hhh
        hhh = float(self.m_textCtrl2.GetValue())  # hhh

        x_name = 'name'
        dic = {'CH1': 0.3333, 'CH2': 0.3333, 'CH3': 0.3333, 'CH4': 0.3333}

        # 读取gain
        G1 = float(self.m_textCtrl10.GetValue())
        G2 = float(self.m_textCtrl11.GetValue())
        G3 = float(self.m_textCtrl12.GetValue())
        G4 = float(self.m_textCtrl13.GetValue())

        dic['CH1'] = G1
        dic['CH2'] = G2
        dic['CH3'] = G3
        dic['CH4'] = G4

        print('增益')
        print(dic)

        # 过滤表
        # 查看勾选项
        checkedItemsl = list(checkedItems)
        print(checkedItemsl)
        f_csv3 = f_csv2[checkedItemsl]
        f_csv3['TIME'] = f_csv2['TIME']

        # 过滤根据时间范围
        T0 = float(self.m_T0.GetValue())
        Tend = float(self.m_Tend.GetValue())
        f_csv3 = f_csv3[f_csv3['TIME'] <= Tend]
        f_csv3 = f_csv3[f_csv3['TIME'] >= T0]
        f_csv3 = f_csv3.replace([np.inf, -np.inf], 0)
        # 过滤表加权
        for item in checkedItemsl:
            f_csv3[item] = f_csv3[item] * dic[item]

        f_csv3['FFT'] = f_csv3.apply(lambda x: x.sum(), axis=1)

        print(f_csv3.head())
        print(f_csv3.tail())

        # 参考
        plt.close('all')

        fig1 = plt.figure(1)  # 波形图##########################
        ax1 = fig1.add_subplot(1, 1, 1)
        # fig = plt.figure(figsize=(960/72,360/72))
        ax1.plot(f_csv3['TIME'].values, f_csv3['FFT'].values, color="red", linewidth=1.5, linestyle="-")
        ax1.grid(linestyle='-.', linewidth=0.3, alpha=0.9)
        ax1.set_title('Data - Time Domain')
        ax1.set_xlabel('Time')
        print('f_sample2 = %s' % f_sample2)

        # plt.figure(2)#幅值图##########################
        from FFTtest import myfft
        [F1, P1, Fs__len] = myfft(f_csv3['TIME'].values, f_csv3['FFT'].values, f_sample2)
        print('Fs__len = %s' % Fs__len)

        temp_ind = int(np.round(50 / Fs__len))
        f_base_peak = abs(P1[temp_ind])
        P1_base = P1 / f_base_peak

        thd = 0
        for i in P1_base:
            thd = thd + (i * i)
        print('thd = %f' % thd)
        print('================================')
        thd = thd / 1 - 1  # 由于包含了基波的1，平方和在平方前乘了100
        thd = np.sqrt(thd) * 100
        print('thd = %f' % thd)

        def Show(y):
            # 参数为一个list

            len_y = len(y)
            x = F1
            print('F1')
            print(F1)
            _y = [y[-1]] * len_y

            # fig = plt.figure(figsize=(960 / 72, 360 / 72))
            fig2 = plt.figure(2)
            ax2 = fig2.add_subplot(1, 1, 1)

            ax2.grid(linestyle='-.', linewidth=0.3, alpha=0.9)
            ax2.set_title('Data - Frequency Domain /THD = %.2f %%' % thd)
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Mag(Phase Peak)')

            ax2.plot(x, y, color='blue')
            # line_x = ax2.plot(x, _y, color='skyblue')[0]
            line_y = ax2.axvline(x=len_y - 1, color='skyblue')
            ax2.set_xlim(-fbase, fbase * hhh)

            # 标签
            text0 = ax2.text(0, 0, ' ', fontsize=10)

            def scroll(event):
                try:
                    axtemp = event.inaxes
                    x_min, x_max = axtemp.get_xlim()
                    fanwei_x = (x_max - x_min) / 10
                    if event.button == 'up':
                        axtemp.set(xlim=(x_min + fanwei_x, x_max - fanwei_x))
                    elif event.button == 'down':
                        axtemp.set(xlim=(x_min - fanwei_x, x_max + fanwei_x))
                    fig2.canvas.draw_idle()
                except:
                    pass

            # 这个函数实时更新图片的显示内容
            def motion(event):
                try:
                    # 调试
                    temp = y[int(np.round(event.xdata / Fs__len))]
                    temp_x = F1[int(np.round(event.xdata / Fs__len))]
                    for i in range(len_y):
                        _y[i] = temp
                    # line_x.set_ydata(_y)
                    # line_y.set_xdata(event.xdata)
                    line_y.set_xdata(temp_x)

                    # text0.set_position((event.xdata , temp * 1.015))
                    text0.set_position((temp_x, temp * 1.015))
                    text0.set_text(("%.1f" % temp) + '\n' + ("%.1fHz" % temp_x))

                    fig2.canvas.draw_idle()  # 绘图动作实时反映在图像上
                except:
                    pass

            def on_button_release(event):
                try:
                    pass
                except:
                    pass

            def on_key_press(event):
                global text1
                try:
                    if event.key == '=':
                        temp = y[int(np.round(event.xdata / Fs__len))]
                        temp_x = F1[int(np.round(event.xdata / Fs__len))]
                        # text1 = ax2.text(1, 1, ' ', fontsize=10, bbox=dict(facecolor='red', alpha=0.5))
                        text1 = ax2.text(1, 1, ' ', fontsize=10)
                        text1.set_position((temp_x, temp * 1.015 + 0.1))
                        text1.set_text(("%.1f" % temp) + '\n' + ("%.1fHz" % temp_x))

                    if event.key == '-':
                        print('-')
                        for txt in ax2.texts:
                            print('+1')
                            txt.remove()

                        fig2.canvas.draw_idle()
                except:
                    pass

            fig2.canvas.mpl_connect('key_press_event', on_key_press)
            # fig2.canvas.mpl_connect('button_release_event', on_button_release)
            fig2.canvas.mpl_connect('scroll_event', scroll)
            fig2.canvas.mpl_connect('motion_notify_event', motion)

        # plt.plot(F1, P1,color="red", linewidth=1.5, linestyle="-")
        Show(P1)

        #
        plt.tight_layout()
        # # plt.savefig(x_name + ".png", dpi=500)
        plt.show()
        #######################

        # fh = open("FFT.txt", mode='w', encoding='utf-8')
        # cm = '\n'
        # for i in range(hhh):
        #     cm += ("\t%.2f\tHz:\t " % (i * fbase))
        #     cm += '%.2f' % he_list[i]
        #     cm += "\t\t % \t"
        #     cm += 'RMS = %.2f' % (abs(Y1[int(fbase * i / (f_sample / len))]) / len * 1.414)
        #     cm += "\n"
        # cm += 'end\n'
        # fh.write(cm)
        # fh.close()

    def OnFileChanged(self, event):
        global f_sample1, len_t, t
        self.m_checkList3.Clear()
        print("OnFileChanged")
        locale.setlocale(locale.LC_ALL, 'English_United States')
        # 获取文件路径
        CSV_Path = self.m_filePicker1.GetPath()
        print(type(CSV_Path))
        print((CSV_Path))
        # 打开文件，查询前25行
        f = open(CSV_Path)
        f_csv = pd.read_csv(f, engine='python', nrows=25, header=2)
        # f_csv = f_csv.fillna(-1)
        f_csv.head(15)

        # 分析前25行#####################################################################################
        model = ''
        dt = float(0)
        rlen = float(0)
        for i in range(0, 15):
            if f_csv.iloc[i, 0] == 'Sample Interval':
                dt = float(f_csv.iloc[i, 1])
        for i in range(0, 15):
            if f_csv.iloc[i, 0] == 'Record Length':
                rlen = float(f_csv.iloc[i, 1])

        if dt == float(0) or rlen == float(0):
            print("读取错误，程序结束")

        f_sample1 = 1 / dt
        t_all = dt * rlen

        self.m_dt.Value = ("%.4f MHz" % (f_sample1 / 1000000))
        self.m_len.Value = ("%.2f E3条" % (rlen / 1000))
        print('dt = %.2f' % dt)
        t = np.arange(0, t_all, dt)
        len_t = np.size(t)  # 5e6
        print('n = %.2f' % len_t)

        # TIME的位置#####
        for i in range(0, 22):
            if f_csv.iloc[i, 0] == 'TIME':
                savei = i
        print('i = %f' % i)
        ###############################################################
        global freqDataF, f_sample2
        freqDataF = int(1)
        if f_sample1 > 250E3:
            freqDataF = int(f_sample1 / 250E3)
            f_sample2 = f_sample1 / freqDataF
        else:
            f_sample2 = f_sample1

        # 分析整表####################################################################
        f = open(CSV_Path)
        global f_csv2
        # 19 20
        f_csv2 = pd.read_csv(f, engine='python', header=19)

        if f_csv2.iloc[0, 0] == 'TIME':
            f = open(CSV_Path)
            f_csv2 = pd.read_csv(f, engine='python', header=20)
        f_csv2 = f_csv2.fillna(-1)

        # 间隔读取####################################################################
        f_csv2 = f_csv2[f_csv2.index % freqDataF == 0]
        print(f_csv2.head(3))
        print(f_csv2.iloc[0, 0])
        print('end')

        # ################### 更新勾选项 ####################
        temp = f_csv2.columns.values

        ind = ["CH1", "CH2", "CH3", "CH4"]
        global channalName  # 表中包含的通道名
        channalName = []
        for i in ind:
            if i in temp:
                channalName.append(i)
                self.m_checkList3.AppendItems(i)

        self.m_checkList3.Update()
        print('file end')

        # global Tu
        # plt.figure()
        # Tu = plt.subplot(1, 1, 1)  # 功率图

    def BoxToggled(self, event):
        plt.close('all')
        plt.clf()
        font = {'family': 'SimHei',
                'weight': 'bold',
                'size': '10'}
        plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
        plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
        # plt.subplots()  #

        print("BoxToggled")
        inx = self.m_checkList3.GetCheckedItems()
        print(inx)
        print(type(inx))

        global checkedItems
        checkedItems = self.m_checkList3.GetCheckedStrings()
        print(checkedItems)

        # Tu.grid(linestyle='-.', which='major')
        # Tu.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)
        for item in checkedItems:
            plt.plot(f_csv2['TIME'], f_csv2[item], label=item)

        # liney = np.linspace(0, 200, 200)
        # linex0 = np.ones(200) * 0
        # linex1 = np.ones(200) * 1
        # plt.plot(linex0, liney, color="green", linewidth=1.5, linestyle="-.", label="T0")
        # plt.plot(linex1, liney, color="green", linewidth=1.5, linestyle="-.", label="T1")

        plt.legend(loc='upper right')
        plt.xlabel('Time')

        # ax = plt.gca()
        # cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=False, color='grey')
        # plt.ylabel()
        plt.title('CSV File Record Data')
        plt.style.use('seaborn-paper')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def mOnMenuSelection2(self, event):
        dlg = wx.MessageDialog(None,
                               "1.csv文件中的±inf（超出Y轴范围部分）将被0代替。\n2.当采样频率超过500Kps为节约运算时间会做降频处理。\n3.分析与图形显示与计算机性能有关。\n4.FFT窗口可以用键盘‘=’‘-’添加删除标签。",
                               u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

    def mOnMenuSelection1(self, event):
        dlg = wx.MessageDialog(None, u"上海电气风电集团 电气COE\n版本:V210909", u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()


def save_all():
    pass


'''end of file'''
