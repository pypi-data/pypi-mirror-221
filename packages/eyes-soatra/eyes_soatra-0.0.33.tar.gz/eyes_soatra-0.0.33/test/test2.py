#!python3
from eyes_soatra import eyes
import json

a = eyes.view_page(
    url='https://www.city.kanoya.lg.jp/bouhan/atotirikatsuyouhojokin.html',
    show_header=True,
)

print(json.dumps(a, ensure_ascii=False, indent=4))