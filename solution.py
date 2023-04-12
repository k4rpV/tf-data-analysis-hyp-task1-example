import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 953761952

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    return p2 - p1 < norm.ppf(0.03, loc=0, scale=np.sqrt(p1 * (1-p1) / x_cnt + p2 * (1 - p2) / y_cnt))
