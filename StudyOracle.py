import pprint
import operator
import cx_Oracle
import datetime

#http://www.oracle.com/technetwork/articles/dsl/python-091105.html
#cx_Oracle.connect('FUT_MTS','FUT_MTS','MTS')

con = cx_Oracle.connect('MSK_BUDGET_DATA/MSK_BUDGET_DATA@NSSER_HARD')
print("cx_Oracle version",cx_Oracle.version)
print("Oracle RDBMS version",con.version)

cur = con.cursor()
cur.arraysize = 100

s_sql = "select grbs,id_org,id_serv_work,n_value " \
        "from Q_DATA_REPORT_2_EMBED t " \
        "where id_col=32 and " \
        "id_calendar=1052017 and " \
        "id_rep_type=1 and " \
        "id_serv_work!='1p' and " \
        "grbs not in ('075')"

t_begin = datetime.datetime.now()
cur.execute(s_sql)
t_end = datetime.datetime.now()
delta = t_end - t_begin
print("Query execution time is: ",delta.total_seconds()," seconds")
t_begin = datetime.datetime.now()

#list of tuples, each row in a dataset is a tuple
rows = cur.fetchall()
print("Dataset row count: ",len(rows))

l_grbs = [] # list of lists [grbs, count]

for r in rows:
    ds_grbs = r[0] #first elemt of tuple(row) is grbs
    if ds_grbs not in [item[0] for item in l_grbs]:
        l_grbs.append([ds_grbs,1])
    else:
        l_grbs[[item[0] for item in l_grbs].index(ds_grbs)][1] += 1

sorted_x = sorted(l_grbs, key=operator.itemgetter(1), reverse=True)
pprint.pprint(sorted_x)

t_end = datetime.datetime.now()
delta = t_end - t_begin
print("Dataset proccess time is: ",delta.total_seconds()," seconds")

cur.close()
con.close()