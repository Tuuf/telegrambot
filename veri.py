import httpx
url="https://finans.truncgil.com/today.json"
response=httpx.get(url)
veri=response.json()


x = veri['ABD DOLARI']
amerika = x['Alış']

x=veri['İNGİLİZ STERLİNİ']
sterlin = x['Alış']

x=veri['İSVİÇRE FRANGI']
frank = x['Alış']
#
x=veri['KANADA DOLARI']
kanada = x['Alış']
#
x=veri['KUVEYT DİNARI']
kuveytdinar = x['Alış']
#
x=veri['NORVEÇ KRONU']
norveckron = x['Alış']

x=veri['SUUDİ ARABİSTAN RİYALİ']
sudiriyal = x['Alış']
#
x=veri['JAPON YENİ']
japyen= x['Alış']
#
x=veri['BULGAR LEVASI']
bulgarleva = x['Alış']
#
x=veri['RUMEN LEYİ']
romenleyi= x['Alış']

x=veri['RUS RUBLESİ']
ruble= x['Alış']

x=veri['İRAN RİYALİ']
riyaliran= x['Alış']

x=veri['ÇİN YUANI']
yuan= x['Alış']

x = veri['PAKİSTAN RUPİSİ']
pakistanrubi = x['Alış']

x = veri['KATAR RİYALİ']
katarriyali = x['Alış']




