集成了一些常用的小工具：

* diff
* rename

## 使用

一、rename

```
from wlc_tools.rename import rename_md5

rename_md5( $(your_image_path) )

```

二、diff

```
from wlc_tools.diff import diff

delimiter = '-'

diff($(your_fold1_path), $(your_fold2_path), $(fold1_tag), $(flod2_tag), $(your_result_path), $(delimiter))
```




## build
    
```bash
python setup.py sdist bdist_wheel
```

## 上传到pipy

```
pip3 install twine
python3 -m twine upload dist/*
```

## 安装

```
pip install wlc-tools
```