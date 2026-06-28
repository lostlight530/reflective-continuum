with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_en = '<strong>ARCHIVE MEMORIAL:</strong> June 21 days single repo broke 10k, total broke 30k.'
old_zh = '<strong>封档纪念：</strong>6月21天单仓破w，6月21天总数破3w。'

new_en = '<strong>ARCHIVE MEMORIAL:</strong> June single month 21 days single repo broke 10k, total broke 30k.'
new_zh = '<strong>封档纪念：</strong>6月单月21天单仓破万，总数破3万。'

content = content.replace(old_en, new_en)
content = content.replace(old_zh, new_zh)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
