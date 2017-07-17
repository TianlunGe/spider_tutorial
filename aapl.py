sel = response.selector
tables = sel.xpath
tables = sel.xpath('.//tables')
tables
tables = sel.xpath('.//table')
tables
sel.css('.Bdsp(0)')
tables
bal = tables[1]
rows = bal.xpath('.//tr')
rows
xp = lambda row : row.xpath('.//text()').extract()
def _unpack(rows):
    res = []
    for row in rows:
        res.append(xp(row))
    return res
data = _unpack(rows)
data
from pandas import DataFrame
df = DataFrame(data)
df.to_csv('aapl_balance')
%history -f 'aapl.py'
