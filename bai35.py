# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:54:37 2024

@author: Administrator
"""

def tinh_tong(n):
  """Tính tổng các số từ 1 đến n

  Args:
    n: Số nguyên dương

  Returns:
    Tổng các số từ 1 đến n
  """

  return n * (n + 1) // 2

# Ví dụ:
n = 100
ket_qua = tinh_tong(n)
print("Tổng các số từ 1 đến", n, "là:", ket_qua)