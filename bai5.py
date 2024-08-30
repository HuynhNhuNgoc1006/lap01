# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:43:55 2024

@author: Administrator
"""

import math
gio,phut,giay=map(int,input("Nhập giờ, phút và giây:").split())
tong_giay=gio*3600+phut*60+giay
print(f"{tong_giay}giay")