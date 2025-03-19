# DisLinesNumber
>**DisLinesNumber**是一个PDF行号去除器。

例如在审稿时，大多数论文的pdf存在行号。如果使用翻译软件阅读或者pdf文档翻译，经常存在翻译引擎误认为行号是名词的数量，将行号也参与翻译。[PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate/issues/641)，优秀的pdf翻译项目，暂时也没有很好的解决方法。

`DisLinesNumber`是一个`python`脚本，其原理是在`pdf`行号的地方应用标注覆盖，从而达到删除行号的目的

---
# 使用方法

## 环境安装
要求：
- [Python 3.X](https://www.python.org/downloads/)

安装好`python`以后安装库：
````bash
pip install argparse PyMuPDF
````

## 使用方法1（最简单）
双击`run.bat`，脚本会自动识别当前目录所有pdf文件并遮盖行号。

## 使用方法2（自定义参数）
以下两种情况，你可以自定义参数运行：
- 遮盖区域不适用你的pdf，你可以自定义遮盖区域（默认0-50）
- 你不想将文件复制到当前目录，你可以自定义输入文件路径（默认处理当前目录所有pdf文件）

在当前目录打开终端，输入命令:
```python
python DisLinesNumber.py --width <your_width> --file <your_filename>
```

将上面的`<your_width>`和`<your_filename>`分别替换为你要遮盖的宽度，和要处理的`pdf`文件路径。
如果你是`Linux`或`MacOS`系统，可能需要将命令中的`python`替换为`python3`。
