import json

from beni import bcolor, bfunc, btask


@btask.app.command('json')
@bfunc.syncCall
async def format_json():
    '格式化 JSON （使用复制文本）'
    import pyperclip
    content = pyperclip.paste()
    try:
        data = json.loads(content)
        print(
            json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)
        )
    except:
        bcolor.printRed('无效的 JSON')
        bcolor.printRed(content)
