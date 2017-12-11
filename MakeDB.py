import psycopg2,logging



# 미리 postgresql Admin 을 이용해 DB를 만들어 놓는다 => Food_Date_연도

def connectDB(year):
    conn_string="host='localhost' dbname ='Food_Date_"+year+"' user='postgres' password='gydufdl135'"
    try:
        conn = psycopg2.connect(conn_string)
    except Exception as e:
        logging.exception(e)
    return conn


def makeDB(year):
    conn = connectDB(year)
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users_data(
                disYear text,
                disMonth text,
                disDate text,
                disDay text,
                cityCode text,
                citySidoName text,
                citySggName text,
                aptCode text,
                aptName text,
                disQuantity text,
                disQuantityRate text,
                disCount text,
                disCountRate text,
                dongName text,
                isHoliday text
            )
            """)
        conn.commit()
        conn.close()

    except Exception as e:
        logging.exception(e)




def copyCSV(year):
    conn = connectDB(year)
    try:

        cur = conn.cursor()

        with open('/Users/admin/IdeaProjects/JavaCrawler/data/Food_Date_' + year + '.csv', 'r') as f:


            # Notice that we don't need the `csv` module.
            next(f)  # Skip the header row.
            cur.copy_from(f, 'users_data', sep=',')

        conn.commit()

        f.close()
        conn.commit()
        conn.close()

    except Exception as e:
        logging.exception(e)

# makeDB('2015')
copyCSV('2015')
