# Using Regular Expressions in Python

## Search

Using a simple search to find a string of text.<br>
See regex.py for live examples.<br>

We will search for KORD in the string:<br>

> 302351Z 27016G34KT 10SM FEW036 KORD M04/M11 A3018 RMK AO2

Compile the regular expression using a raw string.

```python
station = re.compile(r"\sKORD\s")
```

Use re.search(string, pattrn) to search for the string. This returns an objecct.

```python
ord: str = "302351Z 27016G34KT 10SM FEW036 KORD M04/M11 A3018 RMK AO2"

found_string = re.search(ord, station)
print(found_string)

<re.Match object; span=(0, 5), match='KORD '>
```

After reading a file, we can iterate through the list of strings (or any list of strings) and print<br>
those that search finds.

```python
for string in list_of_strings:
    if re.search(re_compiled_string, string):
        print(string)
```

### Resources

A usefull [web-site](https://www.regex101.com) for practicing regex.

