import json
# import hashlib
from pathlib import Path

main_path = Path(__file__).parent.parent  # 项目根目录

exclude_file = ['LICENSE', 'README.md']  # 排除的文件列表
exclude_dir = ['index']  # 排除的文件夹列表


json_file = {}

for dir in main_path.iterdir():
    if dir.is_file() or dir.name.startswith('.') or dir.name in exclude_dir:
        # 不是文件夹、或文件夹名以.开头、或在排除列表中的文件夹跳过
        continue
    else:
        json_file[dir.name] = {}
        for file in dir.rglob('*'):
            if not file.is_file() or any(p in exclude_dir or p.name.startswith('.') for p in file.parents):
                # 不是文件，或者父目录中有以.开头或在排除列表的中文件夹跳过
                continue
            # hash值，暂不用
            # json_file[dir.name][file.stem] = {
            #     'path': str(file).replace(str(dir.parent), '').replace('\\', '/'),
            #     'hash': hashlib.md5(file.read_bytes()).hexdigest()
            # }
            json_file[dir.name][file.stem] = str(file).replace(str(dir.parent), '').replace('\\', '/')

# 保存文件
with open(main_path / 'path.json', 'w', encoding='utf-8') as f:
    json.dump(json_file, f, ensure_ascii=False, indent=2)