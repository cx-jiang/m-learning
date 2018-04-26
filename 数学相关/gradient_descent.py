#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:56:14 2018

@author: gjiang
"""

import numpy as np

A = np.array([[1,0],[0,2]])
b = np.array([0,0])
x = np.array([2,1])
epsilon=1e-5

grad=2*(np.dot(A,x) + b)
iter=0
while(np.linalg.norm(grad) > epsilon):
    iter += 1
    t = np.linalg.norm(grad)**2 / np.dot(np.dot(2*grad.T,A),grad)
    x = x - t*grad
    grad=2*(np.dot(A,x) + b)
    fun_val=np.dot(np.dot(x.T,A),x) + 2*np.dot(b.T,x)
    print('iter_number = {num} norm_grad = {norm_grad:2.6f} fun_val = {val:2.6f} \n'\
          .format(num=iter,norm_grad=np.linalg.norm(grad),val=fun_val)) 