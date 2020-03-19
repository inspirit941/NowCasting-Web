from django.shortcuts import render
import pandas as pd
import glob2
import os
import numpy as np
from itertools import chain

def index(request):
    data_path = os.path.join(os.getcwd(),'nowcasting', 'csv_data')
    
    # Stacked_bar Chart data. 
    # 디렉토리의 가장 마지막에 있는 파일을 불러온다.
    factor_file = glob2.glob(os.path.join(data_path, 'Factor',"*.csv"))[-1]
    factor = pd.read_csv(factor_file, index_col = 0)
    factor.index = pd.to_datetime(factor.index)
    # 뒤에서부터 8개의 row만 가져온다.
    factor_list = [list(factor[i].values[-8:]) for i in factor.columns]
    factor_xlabel = list(factor.index.strftime("%Y-%m-%d")[-8:])
    factor_tick_min = [min(factor_list[i]) for i in range(len(factor_list))]
    factor_tick_max = [max(factor_list[i]) for i in range(len(factor_list))]
    factor_columns = list(factor.columns)
    print(factor_tick_min, factor_tick_max)

    # Line Chart for GDP 1 ~ 4
    gdp_file = glob2.glob(os.path.join(data_path, 'Historical_data',"*.csv"))[-1]
    
    # calender column을 index로 한 csv 파일을 불러온다.
    gdp = pd.read_csv(gdp_file, index_col = 'calender')
    
    # datetime 형태로 변환 / GDP1, GDP2, GDP3, GDP4 column만 추출한다.
    gdp.index = pd.to_datetime(gdp.index)
    gdp = gdp[['GDP1', 'GDP2', 'GDP3','GDP4']]
    
    # weekday == 6은 sunday라는 뜻. 일요일 row만 추출한 뒤 뒤에서부터 14개 row만 가져온다. 
    # = 14주치 데이터.
    gdp_data = gdp.loc[gdp.index.weekday == 6][-14:]
    
    gdp_list = [list(gdp_data[i] * 100) for i in gdp_data.columns]
    gdp_xlabel = list(gdp_data.index.strftime("%Y-%m-%d"))
    
    # linePlot x축과 y축 범위 설정을 위한 값
    gdp_min, gdp_max = min(chain(*gdp_list)), max(chain(*gdp_list))
    
    # html에 json 형태로 데이터를 전송. html의 script에서 인자로 받아 실행한다.
    return render(request, 'dashboard.html', 
        context = {
            'linePlot_data' : {
                'data': gdp_list,
                'xlabel': gdp_xlabel,
                'tick_min': gdp_min,
                'tick_max': gdp_max + (gdp_max) * 1/10,
        }, 
            'Factor_data': {
                "data": factor_list, 
                'xlabel' : factor_xlabel,
                'tick_min' : factor_tick_min,
                'tick_max' : factor_tick_max,
                'value_name' : factor_columns
            }, 
        })
