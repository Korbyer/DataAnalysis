import csv,logging
from bs4 import BeautifulSoup

# 서울시 행정구역 읍면동 위치정보 (좌표계: ITRF2000)
# http://data.seoul.go.kr/openinf/mapview.jsp?infId=OA-13222

# 서울시 법정구역 읍면동 공간정보 (좌표계: ITRF2000)
# http://data.seoul.go.kr/openinf/mapview.jsp?infId=OA-13220

def TestMap(year):
    svg = open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\seoul_edit\\sample_law.svg', 'r').read()
    senior_count = {}
    dongName_list=[]
    soup = BeautifulSoup(svg, 'lxml')
    paths = soup.find_all('g')
    colors = ["#E5E3FA", "#C7C2F9", "#A097F4", "#7B70E0", "#4739CC", "#180C8C", "#FF0000"]
    g_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    try:
        with open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\data\\Food_Date_'+year+'.csv', 'r') as f:
            next(f)
            spamreader = csv.reader(f, delimiter=',')
            for row in spamreader:
                # if not past_header:
                #     past_header = True
                try:
                    unique = row[13]
                    count = float(row[9].strip())
                    if not unique in senior_count:
                        senior_count[unique] = count
                    else:
                        senior_count[unique] += count
                except:
                    pass

        with open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\data\\TC_SPBE17_2015.csv', 'r') as dbf:
            next(dbf)
            i = 1
            dbfreader = csv.reader(dbf, delimiter=',')
            for row in dbfreader:
                dongName = row[1]
                dongName_list.append(dongName)
            for p in paths:
                check_tag = "tc_spbe17_2015_" + str(i)
                if p.has_attr('fill'):
                    pass

                elif p.has_attr('qgisviewbox'):
                    pass

                elif p.has_attr('stroke'):
                    pass

                elif p['id'] in [check_tag]:
                    try:
                        count = senior_count[dongName_list[i-1]]
                        i += 1
                    except:
                        count = -1
                        i += 1

                    if count == -1:
                        color_class = 6
                    elif count > 1000000000:
                        color_class = 5
                    elif count > 500000000:
                        color_class = 4
                    elif count > 300000000:
                        color_class = 3
                    elif count > 200000000:
                        color_class = 2
                    elif count > 100000000:
                        color_class = 1
                    else:
                        color_class = 0
                    color = colors[color_class]
                    p['style'] = g_style + color

                else:
                    continue
    except Exception as e:
        logging.exception(e)

    with open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\sample_'+year+'.svg', 'w') as file:
        # 해당 BeautifulSoup 을 이용해서 저장할 경우,
        # Body, html 태그가 svg 파일 안에 붙어서 나오는데
        # 이 경우 svg 형태로 제대로 표현되지 않기 때문에, 해당 두 가지 태그들을 지워줘야 한다.
        for match in soup.find_all(['body', 'html']):
            match.unwrap()
        file.write(str(soup))

    print(year+"년도 서울지도 추출 성공...")
    print(senior_count)
#
# def Public_Holiday_Map():
#
# def Special_Holiday_Map():


TestMap('2015')
TestMap('2016')
TestMap('2017')

