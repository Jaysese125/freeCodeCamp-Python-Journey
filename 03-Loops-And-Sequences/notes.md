\# 🔄 Study Notes: Loops and Sequences



\## 1. Core Mechanics of Python Lists

\* \*\*Definition:\*\* An ordered, mutable sequence of element types enclosed in square brackets `\[]`.

\* \*\*Zero-Based Indexing:\*\* The first item sits at index `0`. Negative indices read backward from the right margin, starting with `-1`.







\## 2. Advanced Operations

\* \*\*Mutations \& Removal:\*\* Direct item reassignment via index (`list\[0] = 'New'`) or destruction using the `del list\[i]` keyword. Out-of-bounds access triggers an `IndexError`.

\* \*\*Unpacking:\*\* Extracting values straight into distinct variables. Use `\*rest` to catch any remaining overflows into a secondary array sequence:

&#x20; ```python

&#x20; name, \*remaining\_items = \['Alice', 34, 'Developer']

\* \*\*Slicing Syntax:\*\* list\[start:end:step] pulls custom index ranges up to, but excluding, the final limit index parameter.

