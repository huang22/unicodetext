# unicodetext
对unicode文本进行处理

## 主要功能
1. 提供unicode blocks，可以通过IDE自动补全功能，快速获取block里面的所有字符
```python
import unicodetext
print (unicodetext.UnicodeBlocks.Emoticons)
```
2. 提供unicode categories，可以通过IDE自动补全功能，快速获取分类中的所有字符
```python
import unicodetext
print (unicodetext.UnicodeCategories.Punctuation)
```
3. 提供字符提取功能
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.extract_emoticon(text))
```
也可以通过提供blocks或者是categories进行自定义的提取
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.extract_chr(text, chrs=unicodetext.UnicodeCategories.Symbol))
```

4. 提供字符清除功能
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_punctuation(text))
```
可以通过指定`replace_str`，将清除字符用对应字符标识
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_punctuation(text, replace_str = '[del]'))
```

也可以通过提供blocks或者是categories进行自定义的清除
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_chr(text, chrs=unicodetext.UnicodeCategories.Symbol))
```

## 安装
直接通过`pip`安装
```shell
pip install -U unicodetext
```
或者是直接拉取代码进行安装
```shell
git clone https://github.com/huang22/unicodetext.git
cd unicodetext
pip install .
```