from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from datetime import datetime
import dateutil.parser
from pytz import timezone
import json

def dt_df(js_dt):
  date1 = ''
  tz1 = ''
  date2 = ''
  tz2 = ''
  data_dt = json.loads(js_dt)
  for k, value in data_dt.items():
    if(k == 'date1'):
      date1 = value;
    if(k == 'date2'):
      date2 = value
    if(k == 'tz1'):
      tz1 = value;
    if(k == 'tz2'):
      tz2 = value
  dt_1= timezone(tz1).localize(dateutil.parser.parse(date1))
  dt_2= timezone(tz2).localize(dateutil.parser.parse(date2))
  dt_gmt_1 = dt_1.astimezone(timezone('GMT'))
  dt_gmt_2 = dt_2.astimezone(timezone('GMT'))
  return (dt_gmt_1-dt_gmt_2).total_seconds()

def crt_dt(js_data , tz_snd):
  date_fst = ''
  tz_fst = ''
  data_dt = json.loads(js_data)
  for k, value in data_dt.items():
    if(k == 'date'):
      date_fst = value
    if(k == 'tz'):
      tz_fst = value
  fmt = '%m.%d.%Y %H:%M:%S'
  dt_fst = timezone(tz_fst).localize(datetime.strptime(date_fst,fmt))
  dt_snd = dt_fst.astimezone(timezone(tz_snd))
  return dt_snd.strftime(fmt)

def g_cur(time):
    tzT = timezone(time)
    dt = datetime.now().astimezone(tzT)

    fmt = '%m.%d.%Y %H:%M:%S %Z'
    return ' Time at the moment '+time+' is: '+dt.strftime(fmt)

#Web Application Method
def app(environ, start_response):

    env_get = parse_qs(environ['QUERY_STRING'])
    dt_current = g_cur('Etc/GMT')

    set_tz = env_get.get('tz', [''])[0]

    if(set_tz != ''):
      dt_current = g_cur(set_tz)
    try:
        sz_reqBD = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        sz_reqBD = 0
    reqBD = environ['wsgi.input'].read(sz_reqBD)
    post_env = parse_qs(reqBD.decode())
    post_dt = post_env.get('dt_sel', [''])[0]
    tz_snd_post = post_env.get('tz_snd', [''])[0]
    if(post_dt != ""):
      time_res = crt_dt(post_dt , tz_snd_post)
    else:
      time_res = ''

    post_ddf =post_env.get('post_ddf', [''])[0]
    if(post_ddf != ""):
      res_df = dt_df(post_ddf)
    else:
      res_df = ''

    resBD = "Time:"+time_res + dt_current + res_df;

    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(resBD)))
    ]

    start_response(status, headers )
    return [resBD.encode('cp866')]

with make_server('', 8080, app) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()
    httpd.handle_request()
