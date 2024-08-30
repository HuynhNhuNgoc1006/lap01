# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:48:35 2024

@author: Administrator
"""

can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))

bmi = can_nang / (chieu_cao * chieu_cao)

print("Chỉ số BMI của bạn là:", bmi)