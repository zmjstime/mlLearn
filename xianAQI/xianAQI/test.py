item = {}
item['city'] = 'xian'
item['date'] = tds[0].string
item['aqi'] = tds[1].string
item['ranges'] = tds[2].string
item['level'] = tds[3].string
item['pm25'] = tds[4].string
item['pm10'] = tds[5].string
item['so2'] = tds[6].string
item['co'] = tds[7].string
item['no2'] = tds[8].string
item['o3'] = tds[9].string
item['rank'] = tds[10].string

sql = '''insert into environment VALUES('%s','%s',%d,'%s','%s',%f,%f,%f,%f,%f,%f,%d)''' %\
    (item['city'], item['date'], item['aqi'], item['ranges'], item['level'], item[
     'pm25'], item['pm10'], item['so2'], item['co'], item['no2'], item['o3'], item['rank'])
