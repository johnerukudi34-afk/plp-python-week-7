# PLP Python Week 7 - Lists

This assignment practices Python lists, indexing, loops, conditions, and list methods.

### Files

* `list_warmup.py` - Demonstrates list indexing, append, remove, and len.
* `shopping_list.py` - Provides an interactive shopping list manager using a loop and list methods.
* `list_report.py` - Prints a numbered list, counts item names with more than 4 letters, and finds the longest item.
* `screenshots/` - Contains screenshots showing the programs running.

### Why check `in` before `.remove()`?

Checking `in` before using `.remove()` makes the program safer because `.remove()` causes an error if the item does not exist in the list. Using `in` first allows the program to display a helpful message instead of crashing.
