# 导入包
from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
import tkinter as tk


# QEMU路径
root = Tk()
root.withdraw()
qemu路径 = askdirectory(title = "选择QEMU主文件夹")
qemu路径 = qemu路径.replace("/","\\")


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


# 引导设置
print("引导顺序")
print("[1]硬盘启动 [2]光盘启动")
temp = input()
引导 = int(temp)
if 引导 == 1:
    引导 = "c"
if 引导 == 2:
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


# 命名
名称 = input("启动文件名称:")


# 生成指令
指令 = (str(构架) + " -cpu " + str(型号) + " -smp " + str(核心) + " -m " + str(内存) + str(硬盘) + str(光驱) + " -boot " + str(引导) + " -vga " + str(显卡))
指令 = 指令.replace("/","\\")
with open(qemu路径 + "\\" + 名称 + ".bat","w") as f:
        f.write(指令)
print(指令)
