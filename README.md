# Nowcasting-Web

US GDP Nowcasting data View Page.

* 영주닐슨 교수님, 라우낙 교수님 Research Assistant 프로젝트 작업. 
* 작업기한 20.03.02 ~ 20.03.19

demo page : https://nowcasting.herokuapp.com/

Django Web서버를 열기 위해서는 djangoWeb/settings.py의 SECRET_KEY 항목 데이터가 필요합니다. <br>
보안 때문에 git에는 업로드하지 않은 상태이므로, 혹시 다른 서버를 활용해 Deploy를 해야 할 경우 저에게 알려주세요.

## data Documents

* staticfile = herokuapp.com에서 사용하는 static file (html, css, javascript).
* static = local에서 서버를 돌릴 경우 사용하는 static file


### nowcasting/csv_data/Factor

  factor_block csv 데이터를 업로드할 위치. <br>
  Web에서는 이름순으로 졍렬했을 때 가장 마지막에 있는 파일을 가져와 사용하고 있습니다. <Br>
  가장 최근에 업데이트한 파일이 이름순으로 가장 마지막에 위치해 있으면 됩니다.<br>
  
  
  사용할 Column = index, factor_block column 4개. (factor_block column의 이름은 상관없습니다) <br>
  
  
  index는 '2000-01-01'을 1로 정의하고, 1개월에 1씩 증가한 값이라고 알고 있습니다.<br>
  숫자 대신 다른 string 값으로 정의하면, 그 값 그대로 BarPlot의 xlabel에 표시됩니다.
  


### nowcasting/csv_data/Historical_data

  GDP의 분기별 Nowcasting data를 업로드할 위치.<bR>
  Web에서는 이름순으로 졍렬했을 때 가장 마지막에 있는 파일을 가져와 사용하고 있습니다. <Br>
  가장 최근에 업데이트한 파일이 이름순으로 가장 마지막에 위치해 있으면 됩니다.<br>

  사용할 Column : calendar, GDP1, GDP2, GDP3, GDP4 (대소문자 포함, column명이 일치해야 합니다.)<br>

  * calendar : %Y-%m-%d 형태 datetime 형식이어야 합니다.
  * GDP1, GDP2, GDP3, GDP4 : column 순서는 바뀌어도 상관없습니다.

  * 백분율 (%) 변환은 Python 백엔드에서 작업하고 있습니다. 소수점 이하를 표시할 때, csv파일에서 원하는 소수점 자리표시 + 2를 해줘야 합니다.
  
  ex) 웹에서 소수점 이하 2번째 자리까지 표현하기 = csv 파일에서는 소수점 4번째 자리까지 표시되어야 함.


### nowcasting/views.py

  Python Backend 파일입니다. 주석으로 코드 의미를 표시해두었습니다.
  

  


