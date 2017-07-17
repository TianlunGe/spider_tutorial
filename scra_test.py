sel = response.selector
tables = sel.xpath('.//table')
call = tables[1]
rows = call.xpath
rows = call.xpath('.//tr')
headers = rows[0]
headers.xpath('.//text()').extract()
xp = lambda row : row.xpath('.//text()').extract()
def test(rows):
    data = []
    for row in rows:
        data.append(xp(row))
    return data
from pandas as pd
from pandas import DataFrame
data = test(rows)
df = DataFrame(data)
df.to_csv('aapl_call')
%history -f scra_test
