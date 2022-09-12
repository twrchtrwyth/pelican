Title: How to Format Code Blocks
Date: 17-08-2022 18:10
Category: examples
Tags: pelican, python, programming, javascript
Slug: syntax-highlighting
Status: hidden

This post contains some examples of code blocks, and demonstrates how syntax highlighting works. Notably, the Future Imperfect theme has completely knackered this--there are no colours, and the line numbers example has a block within the block, which looks awful.

First, some python without line numbers:

```python
for i in range(5):
	print(i)
```

And now with line numbers:

	#!python
	print("This is the first line.")
	print("And this is the second.")
	# Here's an example of looping over a list.
	my_list = [1, 2, 3]
	for number in my_list:
	    print(number)

If we want to highlight specific lines:

	:::!python hl lines="1 3"
	print("This line is important.")
	print("But this one isn't.")
	important_list = [1, 2, 3]

What about some JavaScript?

```javascript
// This function is pretty pointless.
function test(number){
  return 1 + number
}
```

