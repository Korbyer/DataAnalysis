import csv,logging
from bs4 import BeautifulSoup

def TestMap(year):
    svg = open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\seoul_edit\\sample.svg','r').read()
    senior_count = {}
    counts_only = []
    min_value = 100
    max_value = 0
    past_header = False
    soup = BeautifulSoup(svg)
    paths = soup.find_all('g')
    colors = ["#E5E3FA", "#B0ABF9", "#847DFA", "#3D2FF7", "#0C0296", "#03002C"]
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
                    senior_count[unique] += count
                except:
                    pass

        with open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\data\\TL_SCCO_EMD_2015_W.csv', 'r') as dbf:
            dbfreader = csv.reader(dbf, delimiter=',')
            for row, p in dbfreader, paths:
                if p['id']:
                    try:
                        dongName = row[1]
                        counts_only.append(senior_count[dongName])
                        count = senior_count[dongName]
                    except:
                        continue
                    if count > 1000000:
                        color_class = 5
                    elif count > 500000:
                        color_class = 4
                    elif count > 300000:
                        color_class = 3
                    elif count > 200000:
                        color_class = 2
                    elif count > 100000:
                        color_class = 1
                    else:
                        color_class = 0
                    color = colors[color_class]
                    p['fill'] = color

    except Exception as e:
        logging.exception(e)

    print(soup.prettify())
TestMap('2015')

    # tl_scco_emd_2015_w_+number

