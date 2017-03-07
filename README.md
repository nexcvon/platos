# platos
[![build status](https://travis-ci.org/nexcvon/platos.svg?branch=master)](https://travis-ci.org/nexcvon/platos)

A really simple PLAin Text Object Serialization library.

## Getting started

### Strings

By default, the whole platos document is loaded as a single string.

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
hello, world!
more lines.
</pre></td><td><pre>
"hello, world!\nmore lines."
</pre></td></tr></table>

### Lists

Now add `***` to the head or the document:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
***
hello, world!
more lines.
</pre></td><td><pre>
["hello, world!", "more lines."]
</pre></td></tr></table>

List can hold sublists:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
***
hello, world!
more lines.
* sublist item 1
  sublist item 2
  * subsublist item 1
    subsublist item 2
  *
  sublist item 5
</pre></td><td><pre>
[
  "hello, world!",
  "more lines.",
  [
    "sublist item 1",
    "sublist item 2",
    ["subsublist item 1", "subsublist item 2"],
    [],
    "sublist item 5"
  ]
]
</pre></td></tr></table>

Note the empty list there.

List items can be multiline text:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
***
$ * hello, world!
$ more
  lines.
* $ another multiline
    text as the first item
    of a sublist.
  second sublist item.
</pre></td><td><pre>
[
  "* hello, world!",
  "more\nlines.",
  [
    "another multiline\ntext as the first item\nof a sublist.",
    "second sublist item"
  ]
]
</pre></td></tr></table>

Incase you need, here is a string starts with `***`

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
$$$
***
blablabla...
more blablabla...
</pre></td><td><pre>
"***\nblablabla...\nmore blablabla..."
</pre></td></tr></table>

And a string starts with `$$$`:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
$$$
$$$
blablabla...
more blablabla...
</pre></td><td><pre>
"$$$\nblablabla...\nmore blablabla..."
</pre></td></tr></table>

### Dictionarys

Use `%%%` to turn on dict mode:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
%%%
name = jack
age = 17
favorite food
= fish, tomatos
  and milk.
</pre></td><td><pre>
{"name": "jack", "age": 17, "favorite food": "fish, tomatos\nand milk."}
</pre></td></tr></table>

Dict as list items:

<table><tr><th>platos</th><th>json</th></tr><tr><td><pre>
% name = jack
  age = 17
% name = lucy
  age = 19
</pre></td><td><pre>
[{"name": "jack", "age": 17}, {"name": "lucy", "age": 19}]
</pre></td></tr></table>

## More extensions

### comments

like strings, but use `#`, and be dropped by parser.

### tags

To prevent some indentions.

```
$$ EOF
some text
EOF
```

same on list with `**`, and dict with `%%`.
