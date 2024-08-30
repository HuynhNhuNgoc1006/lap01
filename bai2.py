# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:38:23 2024

@author: Administrator
"""

import math
a=float(input("Nhập số thứ nhất:"))
b=float(input("Nhập số thứ hai:"))
tong=a+b
hieu=a-b
tich=a*b
thuong=a/b
du=a%b
nguyen=a//b
print("Tổng của 2 số là:",tong)
print("Hiệu của 2 số là:",hieu)
print("Tích của 2 số là:",tich)
print(f"Thương (làm tròn 2 chữ số):{thuong:.2f}")
print(f"Thương (làm tròn 3 chữ số):{thuong:.3f}")
print("Chia lấy dư:",du)
print("Chia lấy nguyên:",nguyen)