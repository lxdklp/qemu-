# 导入包
import os
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
import tkinter as tk


# 检测操作系统类型
系统 = os.name
if 系统 == "nt":
    后辍 = ".bat"
if 系统 == "posix":
    后辍 = ".sh"


# QEMU路径
root = Tk()
root.withdraw()
qemu路径 = askdirectory(title = "选择QEMU主文件夹")
qemu路径 = qemu路径.replace("/","\\")
qemu路径 = ('"' + qemu路径 + '"')
print(qemu路径)


while 1:
    print("[0]关于 [1]生成虚拟硬盘 [2]生成启动文件 [3]退出")
    temp = input()
    选择 = int(temp)


    # 关于
    if 选择 == 0:
        print("~~遇到问题请自己Google~~")
        print("如发现BUG,欢迎bilibili私信我或者在gayhub上传你的修改版")
        print("bilibili@楼下的苦力怕")
        print("gayhun:https://github.com/lxdklp     bilibili:https://space.bilibili.com/489752882")
        print("项目地址:https://github.com/lxdklp/qemu-cmd-generator")


    # 生成虚拟硬盘
    if 选择 == 1:
        # 格式设定
        print("[1]raw(原始的磁盘镜像格式) [2]qcow2(QEMU目前推荐的QEMU镜像格式) [3]qcow(较旧的QEMU镜像格式) [4]cow(用户模式LinuxCopy-On-Write的镜像文件格式) [5]vdi(兼容VirtualBox1.1的镜像文件格式) [6]vmdk(兼容VMware 4以上的镜像文件格式) [7]vpc(兼容Virtual PC的镜像文件格式)")
        temp = input()
        格式 = int(temp)
        if 格式 == 1:
            格式 = "raw"
        if 格式 == 2:
            格式 = "qcow2"
        if 格式 == 3:
            格式 = "qcow"
        if 格式 == 4:
            格式 = "cow"
        if 格式 == 5:
            格式 = "vdi"
        if 格式 == 6:
            格式 = "vmdk"
        if 格式 == 7:
            格式 = "vpc"

        # 容量设定
        print("硬盘容量(GB)")
        容量 = input()

        # 保存
        生成 = input("虚拟硬盘名称:")
        生成路径 = askdirectory(title = "选择保存位置")
        生成路径 = 生成路径.replace("/","\\")
        生成路径 = ('"' + 生成路径 + '"')
        print(生成路径)

        # 执行指令
        指令 = (qemu路径 + "qemu-img create -f " + 格式 + 容量 + "G" + 生成路径)
        os.system(指令)


    # 生成启动文件
    if 选择 == 2:
        # 模式选择
        print("模式")
        print("[1]普通 [2]高级")
        temp = input()
        模式 = int(temp)


        # CPU设置
        print("CPU构架")
        print("[1]x86 [2]arm")
        temp = input()
        构架 = int(temp)
        if 构架 == 1:
            构架 = "qemu-system-x86_64"
            print("CPU型号")
            print("[1]core2duo [2]qemu64 [3]qemu32")
            temp = input()
            型号 = int(temp)
            if 型号 == 1:
                型号 = "core2duo"
            if 型号 == 2:
                型号 = "qemu64"
            if 型号 == 3:
                型号 = "qemu32"
        if 构架 == 2:
            构架 = "qemu-system-aarch64"
            print("CPU型号")
            print("[1]cortex-a15 [2]cortex-a57 [3]arm1176")
            temp = input()
            型号 = int(temp)
            if 型号 == 1:
                型号 = "cortex-a15"
            if 型号 == 2:
                型号 = "cortex-a57"
            if 型号 == 3:
                型号 = "arm1176"

        print("CPU核心数")
        temp = input()
        核心 = int(temp)


        # 内存设置
        print("内存大小(M)\n注：如果设置内存小于256M可能无法正常运行！")
        temp = input()
        内存 = int(temp)

        # 硬盘设置
        print("[1]有硬盘 [2]无硬盘")
        temp = input()
        硬盘 = int(temp)
        if 硬盘 == 1:
            硬盘路径 = askopenfilename(title = "选择虚拟硬盘")
            硬盘 = (" -hda " + 硬盘路径)
        if 硬盘 == 2:
            硬盘 = ("")


        # 光驱设置
        print("[1]有光驱 [2]无光驱")
        temp = input()
        光驱 = int(temp)
        if 光驱 == 1:
            光盘路径 = askopenfilename(title = "选择虚拟光盘")
            光驱 = (" -cdrom " + 光盘路径)
        if 光驱 == 2:
            光驱 = ("")


        # 软驱设置
        print("[1]有软驱 [2]无软驱")
        temp = input()
        软驱 = int(temp)
        if 软驱 == 1:
            软驱路径 = askopenfilename(title = "选择虚拟光盘")
            软驱 = (" -cdrom " + 软驱路径)
        if 软驱 == 2:
            软驱 = ("")


        # 引导设置
        print("引导顺序")
        print("[1]软盘启动 [2]硬盘启动 [3]光盘启动")
        temp = input()
        引导 = int(temp)
        if 引导 == 1:
            引导 = "a"
        if 引导 == 2:
            引导 = "c"
        if 引导 == 3:
            引导 = "d"


        # 显卡设置
        print("显卡选择")
        print("[1]cirrus [2]std [3]vmware [4]qxl")
        temp = input()
        显卡 = int(temp)
        if 显卡 == 1:
            显卡 = "cirrus"
        if 显卡 == 2:
            显卡 = "std"
        if 显卡 == 3:
            显卡 = "vmware"
        if 显卡 == 4:
            显卡 = "qxl"


        # 高级模式选项
        if 模式 == 2:
            检测 = 0

            # 模拟设备
            print("是否要设定设备")
            print("[1]是 [2]否")
            temp = input()
            设备 = int(temp)
            if 设备 == 1:
                print("模拟的设备名称\n如树莓派“raspi3、raspi2” 普通x86“pc”")
                设备 = input()
                设备 = ("-M " + 设备)
                检测 = 1
            if 设备 == 2:
                设备 = ""

            # 内核设置
            print("是否要设定设备树引导文件(.dtb)")
            print("[1]是 [2]否")
            temp = input()
            设备树 = int(temp)
            if 设备树 == 1:
                设备树 = askopenfilename(title = "选择设备树引导文件文件")
                设备树 = ("-dtb  " + 设备树)
                检测 = 1
            if 设备树 == 2:
                设备树 = ""

            # 内核设置
            print("是否要设定内核")
            print("[1]是 [2]否")
            temp = input()
            内核 = int(temp)
            if 内核 == 1:
                内核 = askopenfilename(title = "选择内核文件")
                内核 = ("-kernel " + 内核)
                检测 = 1
            if 设备 == 2:
                内核 = ""
            if 检测 == 0:
                print("你这和普通模式有区别嘛")


        # 普通模式选项
        if 模式 == 1:
            设备 = ""
            设备树 = ""
            内核 = ""


        # 生成指令
        名称 = input("启动文件名称:")
        生成 = askdirectory(title = "选择保存位置")
        生成 = 生成.replace("/","\\")
        指令 = (qemu路径 + "\\" + str(构架) + " -cpu " + str(型号) + str(设备) + " -smp " + str(核心) + " -m " + str(内存) + str(硬盘) + str(光驱) + str(软驱) + " -boot " + str(引导) + " -vga " + str(显卡) + str(设备树) + str(内核))
        指令 = 指令.replace("/","\\")


        # 保存
        with open(生成 + 名称 + 后辍,"w") as a:
                a.write(指令)

        运行 = tkinter.messagebox.askquestion(title = "是否运行生成的文件" , message = "是否运行生成的文件")
        if 运行 == "yes":
            os.system(生成 + "\\" + 名称 + 后辍)


    # 退出
    if 选择 == 3:
        break