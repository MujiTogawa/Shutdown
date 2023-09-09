import os
import time

def shutdown_computer():
    hours = int(input("请输入关机时间（小时（整数））："))
    seconds = hours * 60 * 60
    os.system(f"shutdown /s /t {seconds}")
    print(f'系统将在{hours}小时后自动关机...')

shutdown_computer()
