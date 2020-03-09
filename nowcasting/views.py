from django.shortcuts import render
import pandas as pd
import glob2
import os
import numpy as np
from itertools import chain
# csv_file = glob2.glob(os.path.join(data_path, 'Factor',"*.csv"))
# Create your views here.
def index(request):
    data_path = os.path.join(os.getcwd(),'nowcasting', 'csv_data')
    # Stacked_bar Chart data. 가장 마지막으로 업데이트된 csv파일을 불러온다.
    factor_file = glob2.glob(os.path.join(data_path, 'Factor',"*.csv"))[-1]
    # print(csv_file)
    factor = pd.read_csv(factor_file, index_col = 0)
    # 최근 두 달 치의 factor_block 데이터를 가져온다.
    factor_list = [list(factor[i].values[-8:]) for i in factor.columns]
    factor_xlabel = list(factor.index[-8:])


    # Line Chart for GDP 1 ~ 4
    gdp_file = glob2.glob(os.path.join(data_path, 'Historical_data',"*.csv"))[-1]
    gdp = pd.read_csv(gdp_file, index_col = 'calender')
    gdp.index = pd.to_datetime(gdp.index)
    gdp = gdp[['GDP1', 'GDP2', 'GDP3','GDP4']]
    
    # 매주 일요일 데이터만 추출, 14개 데이터 (14주 전 ~ 이번 주까지)
    gdp_data = gdp.loc[gdp.index.weekday == 6][-14:]
    
    gdp_list = [list(gdp_data[i] * 100) for i in gdp_data.columns]
    gdp_xlabel = list(gdp_data.index.strftime("%Y-%m-%d"))
    gdp_min, gdp_max = min(chain(*gdp_list)), max(chain(*gdp_list))
    print(gdp_min, gdp_max)
    data1 = [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100]
    return render(request, 'dashboard.html', 
        context = {
            'linePlot_data' : {
                'data': gdp_list,
                'xlabel': gdp_xlabel,
                'tick_min': gdp_min,
                'tick_max': gdp_max + (gdp_max) * 1/10,
        }, 
            'barPlot_data': {
                "data": factor_list, 
                'xlabel' : factor_xlabel 
            }, 
        })