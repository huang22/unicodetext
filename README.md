# unicodetext
Processing Unicode Text

🌍 [中文](README_cn.md)

## How To Use
1. Unicode's blocks (`unicodetext.UnicodeBlocks`), which can be quickly accessed through the IDE's auto-completion feature to obtain all the characters within the block.
```python
import unicodetext
print (unicodetext.UnicodeBlocks.Emoticons)
```
2. Unicode's categories (`unicodetext.UnicodeCategories`), which can be quickly accessed through the IDE's auto-completion feature to obtain all the characters within the category.
```python
import unicodetext
print (unicodetext.UnicodeCategories.Punctuation)
```
3. Character extraction.
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.extract_emoticon(text))
```
Custom extraction can also be performed by providing specific Unicode blocks or categories:
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.extract_chr(text, chrs=unicodetext.UnicodeCategories.Symbol))
```

4. Character removal
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_punctuation(text))
```
The removed characters can be replaced with specified characters by `replace_str`:
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_punctuation(text, replace_str = '[del]'))
```

Custom removal can also be performed by providing specific Unicode blocks or categories:
```python
import unicodetext
text =  "i am here 237 .! 3 *。、！ +-23689068 发斯蒂芬改 23579 😄"
print (unicodetext.remove_chr(text, chrs=unicodetext.UnicodeCategories.Symbol))
```

## Install
Install the library with:
```shell
pip install -U unicodetext
```
You can also clone this repository and install:
```shell
git clone https://github.com/huang22/unicodetext.git
cd unicodetext
pip install .
```