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

## 字符集
### unicodetext.UnicodeBlocks
- Unicode 15.1定义的[328 blocks](https://en.wikipedia.org/wiki/Unicode_block#List_of_blocks)。为了能作为变量，在代码中自动补全，把所有block名字的空格与横线去除。
### unicodetext.UnicodeCategories
- Letter = Lu | Ll | Lt | Lm | Lo
- Mark = Mn | Mc | Me
- Number = Nd | Nl | No
- Punctuation = Pc | Pd | Ps | Pe | Pi | Pf | Po
- Symbol = Sm | Sc | Sk | So
- Separator = Zs | Zl | Zp
- Other = Cc | Cf | Cs | Co | Cn
- Cased_Letter = Lu | Ll | Lt

| Abbr | Long                  | Description                                                         |
|:---- |:--------------------- |:--------------------------------------------------------------------|
| Lu   | Uppercase_Letter      | an uppercase letter                                                 |
| Ll   | Lowercase_Letter      | a lowercase letter                                                  |
| Lt   | Titlecase_Letter      | a digraph encoded as a single character, with first part uppercase  |
| Lm   | Modifier_Letter       | a modifier letter                                                   |
| Lo   | Other_Letter          | other letters, including syllables and ideographs                   |
| Mn   | Nonspacing_Mark       | a nonspacing combining mark (zero advance width)                    |
| Mc   | Spacing_Mark          | a spacing combining mark (positive advance width)                   |
| Me   | Enclosing_Mark        | an enclosing combining mark                                         |
| Nd   | Decimal_Number        | a decimal digit                                                     |
| Nl   | Letter_Number         | a letterlike numeric character                                      |
| No   | Other_Number          | a numeric character of other type                                   |
| Pc   | Connector_Punctuation | a connecting punctuation mark, like a tie                           |
| Pd   | Dash_Punctuation      | a dash or hyphen punctuation mark                                   |
| Ps   | Open_Punctuation      | an opening punctuation mark (of a pair)                             |
| Pe   | Close_Punctuation     | a closing punctuation mark (of a pair)                              |
| Pi   | Initial_Punctuation   | an initial quotation mark                                           |
| Pf   | Final_Punctuation     | a final quotation mark                                              |
| Po   | Other_Punctuation     | a punctuation mark of other type                                    |
| Sm   | Math_Symbol           | a symbol of mathematical use                                        |
| Sc   | Currency_Symbol       | a currency sign                                                     |
| Sk   | Modifier_Symbol       | a non-letterlike modifier symbol                                    |
| So   | Other_Symbol          | a symbol of other type                                              |
| Zs   | Space_Separator       | a space character (of various non-zero widths)                      |
| Zl   | Line_Separator        | U+2028 LINE SEPARATOR only                                          |
| Zp   | Paragraph_Separator   | U+2029 PARAGRAPH SEPARATOR only                                     |
| Cc   | Control               | a C0 or C1 control code                                             |
| Cf   | Format                | a format control character                                          |
| Cs   | Surrogate             | a surrogate code point                                              |
| Co   | Private_Use           | a private-use character                                             |
| Cn   | Unassigned            | a reserved unassigned code point or a noncharacter                  |


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
