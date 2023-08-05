import os
from pathlib import Path
from typing import Optional

import typer
from beni import bcolor, bfile, bfunc, btask
from beni.bqiniu import QiniuBucket


@btask.app.command()
@bfunc.syncCall
async def bin(
    names: str = typer.Argument(None, help="如果有多个使用,分割"),
    file: Path = typer.Option(None, help="文件形式指定参数，行为单位"),
    ak: str = typer.Option(..., help="七牛云账号AK"),
    sk: str = typer.Option(..., help="七牛云账号SK"),
    output: Optional[Path] = typer.Option(None, help="本地保存路径"),
):
    '从七牛云下载执行文件'
    bucketName = 'pytask'
    bucketUrl = 'http://qiniu-cdn.pytask.com'
    if output is None:
        output = Path(os.curdir)
    bucket = QiniuBucket(bucketName, bucketUrl, ak, sk)
    targetList: list[str] = []
    if names:
        targetList.extend(names.split(','))
    if file:
        content = await bfile.readText(Path(file))
        targetList.extend(content.split('\n'))
    targetList = [x.strip() for x in targetList]
    assert targetList, '没有指定下载内容'
    for target in targetList:
        file = output.joinpath(target).resolve()
        if file.exists():
            print(f'exists {file}')
        else:
            key = f'bin/{target}.zip'
            await bucket.downloadPrivateFileUnzip(key, output)
            bcolor.printGreen(f'added  {file}')
