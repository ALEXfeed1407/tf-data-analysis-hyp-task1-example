import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    from scipy.stats import norm
    a1 = x_success /  x_cnt
    a2 = y_success /y_cnt
    diff = np.sqrt((a1 * (1 - a1) / x_cnt) + (a2 * (1-a2) / y_cnt))
    z_ = (a2 - a1) / diff
    z_crit = norm.ppf(1-0.02)
    decision = z_ > z_crit
  
    return decision
