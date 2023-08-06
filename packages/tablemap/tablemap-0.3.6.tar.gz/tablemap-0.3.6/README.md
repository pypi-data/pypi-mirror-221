# About

Tablemap is a useful Python data wrangling tool for situations where Pandas or SQL may feel cumbersome when dealing with tasks that go beyond their typical routine.

Instead of going the long way around with Pandas, where a table is simply a list of dictionaries, Tablemap offers a more efficient alternative. It allows you to effortlessly chain together processes on tables without the need to excessively rely on stackoverflow.com for complex Pandas operations.

In addition, this tool is designed for those who want a simpler solution that minimizes memory concerns.

# Installation

Requires only built-in Python libraries, without any external dependencies.

```python
pip install tablemap
```

# Tutorial

## Saving tables in the database

Let's create a table `t1` in `sample.db`. 

```python
from tablemap import Conn, Rows

t1 = [
    {'col1': 'a', 'col2': 4},
    {'col1': 'a', 'col2': 5},
    {'col1': 'b', 'col2': 1},
]

conn = Conn('sample.db')
conn['t1'] = t1
```

The right-hand side of the assignment can consist of a list of dictionaries, an iterator that yields dictionaries, or an object fetched from the connection (referred to as the Rows object, which will be introduced shortly). For example, you can use `conn['t1']` and then chain table-manipulating methods such as `map`, `update`, `by` and more.

In this context, each dictionary represents a row in a table. For instance, `{'col1': 'a', 'col2': 4}` represents a row with two columns, `col1` and `col2`.

The process of opening and closing the database is handled safely in the background.

To browse tables in the database,

```python
rs = conn['t1']
print(rs)

# to convert it into a familiar data structure,
print(rs.list())

# to display only a portion of it
rs1 = rs[1:]
print(rs1)

# rs[1:] creates a new object, while rs remains unmodified.
print(rs.size(), rs1.size())
# This is equivalent to
print(len(rs), len(rs1))
```

If you prefer a graphical user interface (GUI), you can open the `sample.db` file using software such as [SQLiteStudio](https://sqlitestudio.pl/) or [DB Browser for SQLite](https://sqlitebrowser.org/). 

Once you have cleaned up the table, you may choose to proceed with the analysis using Pandas.

```python
import pandas as pd

df = pd.DataFrame(conn['t1'].list())
conn['t1_copy'] = df.to_dict('records')
```

## Rows objects

The `conn['t1']` expression returns a `Rows` object, which represents a list of dictionaries. There are two ways to create Rows objects:

1. By passing a table name to the Conn object, such as `conn['t1']`.
2. By directly passing a list of dictionaries or a dictionary-yielding iterator to the Rows class, for example, `Rows(t1)`.

When you pass a column name to a Rows object, it returns a list of elements for that column. For example, `Rows(t1)['col1']` would result in `['a', 'a', 'b']`.

Rows objects provide methods that can be chained together to transform a table.

*** 

## Methods for table manipulation


<!-- + #### A few to brag about. 

    Some of the properties of this module that make data-wrangling easier 
        
    1. All the methods in this section create a new `Rows` object.  

        ```python
        rs = conn['t1']
        rs1 = rs.chain(t1)
        ```

        `rs` and `rs1` are different objects, so `rs` is not `chain`ed.

        ```python
        t1 = Rows(t1)
        t1_listed = t1.list() 
        t1_listed[0]['col1'] = 'x'
        # Create a new list from t1, and it's a fresh one.
        t1.list()[0]['col1'] != 'x' 
        ```

    2. `rs` (or `rs1`) does not contain any data in the table, yet. It simply holds instructions and is executed when it's needed. (when you want it to be saved in the database, to be printed out, to be listed up, or simply to get the size of it)

        So you can easily combine all the methods safely and freely, for example, (`filter` is not covered yet, hopefully, it's self-evident.)

        ```python
        rs = conn['t1']
        high = rs.filter(lambda r: r['col2'] > 4)
        low = rs.filter(lambda r: r['col2'] < 2)
        rs2 = high.chain(low)
        ```

        Since `rs2` simply holds instructions without actually performing operations, the above code requires very little computing power unless you want to save it in the database or see the result for yourself.  

    3. Memory requirement is minimal. 

        ```python
        conn['t1_1'] = rs2
        ```

        Now it actually works because you are trying to save the rows `rs2` generates in the table `t1_1`. Still, `tablemap` does not load up all of `rs2` on memory. It loads and saves one-by-one. 

    4. Opens and closes the database automatically and safely. Users don't have to worry about it. Even the keyboard interrupts (like ctrl-c) during the table insertion do not corrupt the database.
 -->
 

+ ### `filter` and `update`

Each row is simply a dictionary with column names as keys, so you can access a column value by passing a column name to the row (dictionary). To create new columns or update the existing ones,

```python
# \ for line-continuation
conn['t1_1'] = conn['t1']\
    .filter(lambda r: r['col2'] > 2)\
    .update(
        col2=lambda r: r['col2'] + 1,
        col3=lambda r: r['col1'] + str(r['col2'])
    )
```

A lambda expression is a nameless function. In the expression `lambda r: r['col2'] > 2`, the parameter `r` represents a single dictionary and the whole expression returns an evaluated value of `r['col2'] > 2` for each iteration.

Columns are updated sequentially, so `col3` has `a5` and `a6`, not `a4` and `a5`.


+ ### `by` and `fold`

To sum up `col2` grouped by `col1`,

```python
conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .fold(
        col2_sum=lambda rs: sum(rs['col2']),
        col2_min=lambda rs: min(rs['col2']),
        col2_max=lambda rs: max(rs['col2']),
    )
```

`by` takes fields as an argument (list of field names or comma-separated field names) for grouping, and the next process (`fold` in this case) takes on each group (a `Rows` object).

In the expression `lambda rs: sum(rs['col2'])`, the parameter `rs` represents a `Rows` object. So `rs['col2']` returns a list of elements in the column `col2`. And of course, for that reason, you may chain up all the methods in this section.

While `update` works on a dictionary, `fold` does on a `Rows` object. (`fold` folds n rows to one row. So the lambda expression in `fold` must return a single value, like a string or a number.)

`fold` must be preceded by grouping methods such as `by` or `windowed` which shows up soon. `filter` may or may not be preceded by grouping methods. 

+ ### `rename`

To replace old column names with new ones,

```python
conn['t1_1'].rename(
    c2min='col2_min',
    c2max='col2_max'
)
```

+ ### `join`

To merge tables,

```python
conn['t2'] = [
    {'col1': 'b', 'col3': -1},
    {'col1': 'c', 'col3': 3},
    {'col1': 'b', 'col3': ''},
]

conn['t1_col3'] = conn['t1'].by('col1')\
    .join(conn['t2'].by('col1'), 'full')
```

There are 4 join types, 'inner', 'left', 'right', and 'full'. The default is 'inner'. You may want to check [this tutorial](https://www.w3schools.com/sql/sql_join.asp) if you are not familiar with these terms.

Tables must be grouped to be joined.

If the table `t1` and `t2` have columns with the same name, `t1` columns will be updated with `t2` columns.

Empty strings represent missing values.

+ ### `distinct`

To group the table `t1` by `col1` and to leave only the first row in each group (removing duplicates),

```python
conn['t1_1'] = conn['t1'].distinct('col1')
```
You can pass multiple columns to `distinct` as in `by`

+ ### `select` and `deselect` 

You can pass columns to `select` or `deselect` to pick up or delete specific columns in a table

```python
conn['t1_1'] = conn['t1'].update(col3=lambda r: r['col2'] + 1)\
    .deselect('col1, col2')
```

+ ### slicing 

To take the first 2 rows from table `t1`,

```python
print(conn['t1'][:2])
```

Negative values are not supported. Of course, you can chain up other methods after slicing. 

Like the other methods, slicing does not execute the operation. `conn['t1'][:2]` holds the instruction to take the first two rows, not the rows themselves. However, the `print` function enforces taking the first two rows to print out on the screen. So it works as expected.

Grouping methods like `by` or `windowed` may come right before slicing, and the rows will be flattened. 

`conn['t1']['col1']` is not slicing; it returns a list of column values, not a `Rows` object. 

+ ### `takewhile` and `dropwhile`

`takewhile` and `dropwhile` take a predicate (a function that returns a value to be considered `True` or `False`, already seen it in `filter`) as an argument to do what these names suggest. Refer to [itertools.takewhile](https://docs.python.org/3/library/itertools.html#itertools.takewhile) and [itertools.dropwhile](https://docs.python.org/3/library/itertools.html#itertools.dropwhile)

Grouping methods may be preceded right before these methods.

+ ### `map`

When `update` or `fold` is not powerful enough, you can deal with a row or `Rows` in a more sophisticated way.

```python
# Some of you may feel uncomfortable with the naming.
# This is just a lambda function for the 'map' method.
# It can be challenging to justify spending time on naming a function that is used nowhere else.
def fn4t1(rs):
    # `rs` is a `Rows` object. 
    # Now you can apply all the methods in this section to manipulate the table.
    # And once again, since these methods create a new `Rows` object instead of modifying the original,
    # you can safely build any combinations of methods as you want.
    tot = sum(rs['col2'])
    # You don't always have to pass a function to the `update` method. The same applies to the `fold` method.
    return rs[:1].update(col2_sum=tot)

conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .map(fn4t1)\
    .deselect('col2')
```

The argument for `map` is a function that returns a `Rows` object or a single dictionary or None. It takes a single dictionary as an argument or a `Rows` object in case the previous process is `by` (`group`) or `windowed`.

+ ### `zip` and `zip_longest`

Like `chain`, `zip` takes a list of dictionaries or an iterator that yields dictionaries or a `Rows` object as an argument. The argument updates the `Rows` object row by row until either one is depleted. 

With `zip`, the above `fn4t1` can be rewritten as

```python
def fn4t1(rs):
    rs2 = [{'col2_sum': sum(rs['col2'])}]
    return rs.zip(rs2)
```

Another example,

```python
conn['t1_1'] = conn['t1'].zip({'idx': i} for i in range(100))
```

`zip_longest` creates empty columns when either one is depleted.

+ ### `merge` 

The same interface as `join`. While `join` combines cross-producted rows from two tables,
`merge` simply `zip_longest` them. For example, when `join` combines 2 rows against 3 rows in each group,
6 rows are generated while `merge` produces only 3 rows.


+ ### `index`

To add an index column,

 ```python
conn['t1'].index('index_column', start=1, step=2)
conn['t1'].by('col1').index('group_index_column')
 ```

+ ### `windowed`

When you need to group a chunk of consecutive rows,

```python
conn['t1_1'] = conn['t1'].windowed(4, 2).fold(
    sum=lambda rs: sum(rs['col2'])
)

# It works with `by`, for example.
conn['t1'].by('col1').windowed(3).index('cnt')
```

`fold` takes the first 4 consecutive rows (of course a `Rows` object) and the next 4 starting from the 3rd (skipping 2 rows) and so on. When rows less than or equal to 4 are left, it will be the last. 

Grouped rows can also be windowed.

```python
print(conn['t1'].by('col1').windowed(3).index('group_no'))
```

+ ### `order` and `group`

Actually, `by` is a combination of `order` and `group`. You can control more precisely by separating these processes, 

```python
conn['t1_col2sum_groupby_col1'] = conn['t1']\
    .order('col1, col2 desc').group('col1')\
    .map(fn4t1)
```

Now, `map` takes a `Rows` object where `col2` is sorted in descending order.

The keyword `desc` can be either uppercased, lowercased, or mixed. 

The ascending order is the default.
 
Regarding the `group` method, if no argument is provided, it will group all the preceding rows.

+ ### `split`
 ```python
# `xs` is a list of `Rows`.
xs = conn['t1'].by('col1').split()
 ```


 + ### `insert`
 To concatenate the `t1` table with itself,

 ```python
 conn['t1'].insert(conn['t1'])
 conn['t1'].insert(t1)
 ```
 
`insert` is special in that this is the only method that returns None.

<!-- + ### `chain`

To concatenate the `t1` table with itself and create a new table called `t1_double` in the database, you can use the `chain` method provided by the `Rows` object. Here are a couple of examples:

```python
conn['t1_double'] = conn['t1'].chain(conn['t1'])
```

This code will create a new table called `t1_double` in the database and populate it with the concatenated result of `t1` with itself.

Alternatively, if you already have a list of dictionaries or an iterator that yields dictionaries named `t1`, you can pass it as an argument to the `chain` method:

```python
conn['t1_double'] = conn['t1'].chain(t1)
```

Make sure that the tables being concatenated (`t1` and `t1` in this case) have the same columns. The order of the columns does not matter for concatenation to work correctly.
 -->


## Some remarks 

- cross-join example

    ```python
    # table2 = conn['t1'].list() is not effective.
    # You should convert it to a list.
    # Otherwise, 'map' attempts to fetch
    # the table 't2' from the database
    # for every group by 'col1'.
    table2 = conn['t2'].list()

    def fn4t1(rs):
        ...do some work using table3
        return something 

    conn['some_table'] = conn['t1'].by('col1').map(fn4t1)
    ```

- `Rows` methods do not update objects directly. They create a new object every time a `Rows` method is invoked.

    So the following code works as expected.
    ```python
    rs = conn['t1']
    rs.by('col1').fold(col2_tot=sum(rs['col2']))
    ```
    In expression `sum(rs['col2'])`, `rs` represents a `Rows` object when the statement `rs = conn['t1']` is evaluated. Methods like `by` or `fold` in the statement do not affect `rs` in `sum(rs('col2'))`.

    Take a close look at the next.

    ```python
    def fn4t1(rs):
        # The original `rs` is not updated.
        # Only `newrs` holds the instruction to update the column 'col2'.
        # The update instruction will not be executed in the next statement.
        # `newrs` simply keeps the instruction here until it's really needed,
        # for example, during database insertion or content print-out.
        newrs = rs.update(col2=lambda r: r['col2'] + 1)
        return newrs.order('col2').zip(rs.order('col2 desc').rename(col2_1='col2'))

    conn['t1_1'] = conn['t1'].by('col1').map(fn4t1)

    ``` 

- Since column names are dictionary keys, they are case-sensitive. However, column names in SQLite3 (on which `tablemap` is powered) are case-insensitive by default. To avoid confusion, it is strongly recommended that you keep them lower-cased, and spaces stripped. 

    `tablemap` does not automatically convert uppercase column names. Making any excessive assumptions on users' intentions might add more confusions. 

## [API Documentation](https://tablemap.readthedocs.io/en/latest/tablemap.html#module-tablemap.tablemap)