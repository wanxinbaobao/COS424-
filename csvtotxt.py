#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:22:45 2019

@author: wanxin
"""

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import json
import math
import re

def main():

    df = pd.read_csv("RedditNews.csv", low_memory=False, header=None)
    aEssay = df.values


    aEssay0 = np.array(aEssay[1:,2])
    string0 = ""

    for i in range(0,aEssay0.shape[0]):
        if(isinstance(aEssay0[i],float)):
            string0 += str(i) + " " + "0"+ "\n"
        else:
            temp = aEssay0[i]
            while("\r\n" in temp):
                temp = re.sub("\r\n"," ",temp)
            while("b'" in temp):
                temp = re.sub("b'"," ",temp)
            while("\'" in temp):
                temp = re.sub("\'","'",temp)
            string0 += str(i) + " " + temp + " " + "0 ""\n"



    text_file = open("reddit_text.txt", "w")
    text_file.write(string0)
    text_file.close()

if __name__ == "__main__":
  main()
