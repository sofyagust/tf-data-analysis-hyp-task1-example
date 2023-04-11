import pandas as pd
import numpy as np


chat_id = 620363988 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p_x = x_success / x_cnt
    p_y = y_success / y_cnt
    return p_x - p_y >= 0.1
