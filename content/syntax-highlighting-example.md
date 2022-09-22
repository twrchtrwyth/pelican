Title: How to Format Code Blocks
Date: 17-08-2022 18:10
Category: examples
Tags: pelican, python, programming, javascript
Slug: syntax-highlighting
Status: hidden

This post contains some examples of code blocks, and demonstrates how syntax highlighting works.

First, some python without line numbers:

```python
for i in range(5):
	print(i)
```

And now with line numbers (note: this doesn't render properly as things stand--I don't know why the numbers don't line up, even after editing the pre-code padding in `main.css`):

	#!python
	# This doesn't line up.
	print("And it is agonising to try to fix.")

Here's a longer example of some Python:

	:::python
	import antigravity
	
	print("This is the first line.")
	print("And this is the second.")
	
	# Here's an example of looping over a list.
	my_list = [1, 2, 3]
	for number in my_list:
	    print(number)


	class Test:
		def __init__(self, monty):
			self.monty = "python"

		def function(argument):
			print("This is a function.")

		def another_one(spam):
			"""
			I am trying to use as many lines as possible.
			"""
			return spam + "eggs"

If we want to highlight specific lines (this just obscures the text!):

	:::python hl_lines="1 3"
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

