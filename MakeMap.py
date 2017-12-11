import csv,logging
from bs4 import BeautifulSoup
from lxml import etree as ET

def TestMap(year):
    svg = open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\seoul_edit\\sample.svg', 'r').read()
    senior_count = {}
    counts_only = []
    dongName_list=[]
    # tree = ET.parse('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\seoul_edit\\sample.svg')
    # root = tree.getroot()
    # for child in root:
    #     if 'path' in child.tag and child.attrib['id'] not in ["seperator", "State_Lines"]:
    #         child.attrib['style'] = g_style+'color'
    past_header = False
    soup = BeautifulSoup(svg)
    paths = soup.find_all('g')
    colors = ["#E5E3FA", "#B0ABF9", "#847DFA", "#3D2FF7", "#0C0296", "#03002C"]
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

        with open('C:\\Users\\admin\\PycharmProjects\\DataAnalysis\\data\\TL_SCCO_EMD_2015_W.csv', 'r') as dbf:
            next(dbf)
            dbfreader = csv.reader(dbf, delimiter=',')
            for row in dbfreader:
                dongName = row[1]
                dongName_list.append(dongName)
            for p in paths:
                i = 0
                # if p['id']:
                try:
                    counts_only.append(senior_count[dongName_list[i]])
                    count = senior_count[dongName_list[i]]
                    i += 1
                except:
                    continue
                if count > 100000000:
                    color_class = 5
                elif count > 5000000:
                    color_class = 4
                elif count > 3000000:
                    color_class = 3
                elif count > 2000000:
                    color_class = 2
                elif count > 1000000:
                    color_class = 1
                else:
                    color_class = 0
                color = colors[color_class]
                p['style'] = g_style + color

    except Exception as e:
        logging.exception(e)

    # print(soup.prettify())
TestMap('2015')

    # tl_scco_emd_2015_w_+number

