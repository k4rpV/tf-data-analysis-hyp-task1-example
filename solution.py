from statsmodels.stats.proportion import proportions_ztest

chat_id = 953761952

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    return proportions_ztest(count=[x_success, y_success], nobs=[x_cnt, y_cnt], alternative='smaller')[1] > 0.03
