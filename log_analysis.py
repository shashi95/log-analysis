import datetime
import psycopg2


def most_popular_article():
    """What are the most popular three articles of all time"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """select a.title, count(*) as num from articles a join log
    l on '/article/' || a.slug = l.path group by a.author,
    a.title order by num desc limit 3"""
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print("Most popular three articles of all time")
    for row in rows:
        print(row[0], row[1])


def popular_author():
    """Who are the most popular article authors of all time."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """select ath.name,  count(*) as num from authors ath join
    articles ar on ath.id=ar.author join log l on
    '/article/' || ar.slug = l.path group by ath.name,ar.title
    order by num desc limit 3;"""
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print("Most popular article authors of all time")
    for row in rows:
        print(row[0], row[1])


def error_day():
    """On which days did more than 1% of requests lead to errors"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("create view all_calls as select DATE(time) as date, " +
              "count(*) as all_count from log group by DATE(time)")
    c.execute("create view error_calls as select DATE(time) as date, " +
              "count(*) as error_count from log where " +
              "status ='404 NOT FOUND' group by DATE(time), status")
    c.execute("select t1.date, error_count*100/all_count as " +
              "percentage from all_calls t1 join error_calls t2 " +
              "on t1.date=t2.date where error_count*100/all_count>1;")
    rows = c.fetchall()
    db.close()
    print("Days when more than 1 percent of requests lead to errors")
    for row in rows:
        print(row[0].strftime('%b %d, %Y'), str(row[1]) + "% errors")


most_popular_article()
popular_author()
error_day()
