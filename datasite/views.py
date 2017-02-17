from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import MySQLdb

def hello(request):
    return HttpResponse("Hello world")

def timeshow(request):
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)

def showdata(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    prtsln = str(offset+10)
    if offset == 517:
        prtsln = "Vyco"
    html = "<html><body>%s</body></html>" % prtsln
    return HttpResponse(html)

def search(request):
    return render_to_response('search_form.html')

def result(request):
    conn = MySQLdb.connect(host='202.112.35.231',user='root',passwd='tub20141008',db='TunnelBrokerDB')
    cur = conn.cursor()
    name = request.GET['query']
    sqlsentence = r'SELECT id,name,passwd,mac,ivi4_address,ivi_address_port,ipv6_address from raspberry_client_raspinfo where name="'+name+r'"'
    cur.execute(sqlsentence)
    res = cur.fetchall()
    prtline = '{'
    for row in res:
        prtline = prtline + r'"id":'+str(row[0])+','; 
        prtline = prtline + r'"name":"'+str(row[1])+'",'; 
        prtline = prtline + r'"passwd":"'+str(row[2])+'",'; 
        prtline = prtline + r'"mac":"'+str(row[3])+'",'; 
        prtline = prtline + r'"ivi4_address":"'+str(row[4])+'",'; 
        prtline = prtline + r'"ivi_port":'+str(row[5])+','; 
        prtline = prtline + r'"ipv6_address":"'+str(row[6])+'"'; 
    prtline = prtline + '}'
    return HttpResponse(prtline)




