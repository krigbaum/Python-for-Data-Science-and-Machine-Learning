print()
print(" =============================================================================================")
print()
print("                                 *** Section 5:  Pandas ***")
print()
print(" =============================================================================================")
print()
print(" Pandas Series:")
print()
print(" import numpy as np")
import numpy as np
print(" import pandas as pd")
import pandas as pd
print()

print(" labels = ['a', 'b', 'c']")
labels = ['a', 'b', 'c']
print(" Data = [10, 20, 30]")
Data = [10, 20, 30]
print(" npArr = np.array(Data)")
npArr = np.array(Data)
print(" pyDict = {'d::15, 'e':25, 'f':35}")
pyDict = {'d':15, 'e':25, 'f':35}
print(" arr = pd.Series(data = Data)")
arr = pd.Series(data = Data)
print()
print(" arr:")
print(arr)
print()
print()
print(" arr = pd.Series(data = Data, index = labels)")
arr = pd.Series(data = Data, index = labels)
print()
print(" arr:")
print(arr)
print()
print()
print(" As long as order is maintained correctly, the labels 'data' and labels can be omitted.")
print(" 'arr = pd.Series(data = Data, index = labels)' is identical to 'arr = pd.Series(Data, labels)'")
print()
print(" A Pandas series may also me constructed from a Numpy array.")
print()
print(" arr = pd.Series(npArr)")
arr = pd.Series(npArr)
print("arr:")
print(arr)
print()
print()
print(" Labels may also be passed in with the Numpy array.")
print(" arr = pd.Series(npArr, labels)")
arr = pd.Series(npArr, labels)
print("arr:")
print(arr)
print()
print()
print(" A Pandas series may also me constructed from a Python dictionary.")
print(" arr = pd.Series(pyDict)")
arr = pd.Series(pyDict)
print("arr:")
print(arr)
print()
print()
print(" arr2 = pd.Series([1, 2, 3, 4], ['USA', 'Britain', 'Germany', 'Japan'])")
arr2 = pd.Series([1, 2, 3, 4], ['USA', 'Britain', 'Germany', 'Japan'])
print()
print("arr2:")
print(arr2)
print()
print()
print(" arr3 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])")
arr3 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print()
print("arr3:")
print(arr3)
print()
print()
print(" Pandas Series can be added.  If types don't match perfectly, Panda will try to coax the types.")
print()
print("arr2 + arr3:")
print(arr2 + arr3)
print()
print(" Note: Pandas has promoted the integers to floats to prevent unintentional loss of precision.")
print()
print()
print()
print(" =============================================================================================")
print()
print("                                             Pandas DataFrames: Part 1:")
print()
from numpy.random import randn
np.random.seed(101)
print()
print(" df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])")
print(" First Parameter is Values, Second is Row labels, Third is Column labels.")
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print()
print("df:")
print(df)
print()
print(" df['W']:")
print(df['W'])
print()
print(" df.W  (This is not recommended as it can cause inconsistent errors.)")
print(df.W)
print()
print(" df[['W', 'Z']]:")
print(df[['W', 'Z']])
print()
print(" df['New'] = df['Y'] + df['Z']:")
df['New'] = df['Y'] + df['Z']
print()
print(" print(df):")
print(df)
print()
print()
print(" df.drop('New', axis=1, inplace=True)     #If the axis parameter is omitted it will default to axis=0 which is rows.")
df.drop('New', axis=1, inplace=True)
print()
print("print(df):")
print(df)
print()
print(" The 'inplace=True' argument is needed for a permanent drop.")
print(" df.drop('E') will remove row 'E'. 'axis=0' is the default value.")
print()
print(" Pandas dataframes are dressed up Numpy arrays:")
print(" df.shape =", df.shape)
print()
print(" Note that the rows in df.shape are argument 0, and columns are 1 which is how the axis are named.")
print()
print()
print(" DataFrame row are retrieved differently than columns.")
print()
print(" Method 1: Label")
print(" print(df.loc['D']):")
print(df.loc['D'])
print(" print(df.loc['']):")
print()
print(" Method 2: Position")
print(" print(df.iloc[3]): ")
print(df.loc['D'])
print()
print()
print(" df.loc['B', 'Y'] =", df.loc['B', 'Y'])
print()
print(" df.loc[['A', 'B'], ['W', 'Y']]:")
print(df.loc[['A', 'B'], ['W', 'Y']])

print(" =============================================================================================")
print()
print(" Pandas DataFrames: Part 2:")
print()
print()
print(" Resuming with the DataFrame from the previous lecture...")
print()
print("df:")
print(df)
print()
print(" Boolean operations can also be performed on and in DataFrames.")
print()
print(" print(df > 0)")
print(df > 0)
print(" Saving and viewing the results in another DataFrame produces boolean results.")
print()
print(" booldf = df > 0")
booldf = df > 0
print(" booldf:")
print(booldf)
print()
print(" Applying the boolean results to the original DataFrame produces results that require interpretation.")
print() 
print(" print(df[booldf])")
print()
print(" df[booldf]:")
print(df[booldf])
print()
print(" 'NaN' stands for not a number which means that when a boolean False is applied to a number")
print((" the results are not numeric."))
print()
print(" The above process can be abbreviated as simply 'df[df>0]'.")
print()
print(" df[df > 0]:")
print(df[df > 0])
print()
print()
print(' A variation of this can be applied to remove rows from the DataFrame.')
print()
print(" Review the original DataFrame...")
print()
print(" df:")
print(df)
print()
print(" Applying the same boolean operation to column W produces the following...")
print(" df['W'] > 0:")
print(df['W'] > 0)
print()
print(" When the boolean results of that operation are applied to the entire array,")
print(" it eliminates any rows from column W that produced a False value.")
print()
print(" Note: The following example combines both parts of the operation, selecting the boolean")
print(" from the chosen row and then applying that to the entire DataFrame")
print()
print(" df[df['W'] > 0]:")
print(df[df['W'] > 0])
print()
print(" Instead of applying the boolean column to the entire DataFrame, it can be applied only to")
print(" selected columns as in: df[df['W'] > 0]['Y', 'X']].  Also, notice the outputs column order.")
print()
print(" df[df['W'] > 0][['Y', 'X']]:")
print(df[df['W'] > 0][['Y', 'X']])
print()
print()
print(" If you find it easier, the previous statement can be broken in steps.")
print("  Step 1:  booleanSeries = df['W'] > 0")
print("  Step 2:  result = df[booleanSeries]")
print("  Step 3:  selectedCols = ['Y', 'X']")
print("  Step 4:  final = result[selectCols]")
print()
print(" Execute Step1...")
booleanSeries = df['W'] > 0
print(" booleanSeries:")
print(booleanSeries)
print()
print(" Execute Step2...")
result = df[booleanSeries]
print(" result:")
print(result)
print()
print(" Execute Step3...")
selectedCols = ['Y', 'X']
print(" selectedCols:")
print(selectedCols)
print()
print(" Execute Step4...")
final = result[selectedCols]
print(" final:")
print(final)
print()
print()
print(" It is possible to apply multiple conditions to these types of operations.")
print(" The and operator is the ampersand '&', the or operator is the pipe '|'")
print()
print(" df[(df['W'] > 0) & (df['Y'] > 1)]:")
print()
print(df[(df['W'] > 0) & (df['Y'] > 1)])
print()
print()
print(" The original DataFrame, df:")
print(df)
print()
print(" To change the DataFrame indexes:  'df.reset_index()'")
df2 = df.reset_index()
print()
print(" df:")
print(df2)
print()
print(" Note that the original indexes become a column.")
print(" To make the reset permanent use :  'df.reset_index(inplace=True)'")
print()
print(" Create new indexs:  newIndexes = 'CA NY WY OR CO'.split()")
newIndexes = 'CA NY WY OR CO'.split()
print()
print("NewIndexes =", newIndexes)
print("To apply the new indexes, first add them as a column:  df['State'] = nexIndexes")
df['State'] = newIndexes
print()
print(" df:")
print(df)
print()
print(" To permanently apply the new column as the DataFrame index use:  df.set_index('State'), inplace=True")
df.set_index('State', inplace=True)
print()
print(" df:")
print(df)
print()
print(" Again, note that the old indexes were NOT retained as a column because of the 'inplace=True' parameter.")
print(" To change the indexes back,the process must be repeated using the original indexes.")
print()
print(" =============================================================================================")
print()
print(" Pandas DataFrames: Part 3:")
print()
print()
print("outside = ['G1, G1', 'G1', 'G2', 'G2', 'G2']")
print("inside = [1, 2, 3, 1, 2, 3]")
print("hier_index = list(zip(outside, inside))")
print("hier_index = pd.MultiIndex.from_tuples(hier_index)")
print()
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
print(" a) hier_index:")
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print()
print(" b) hier_index:")
print(hier_index)
print()
print(" outside:")
print(outside)
print()
print(" inside:")
print(inside)
print()
print(" final) hier_index:")
print(hier_index)
print()
print()
print(" df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])")
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print()
print(" df:")
print(df)
print()
print()
print(" df.loc['G1']:")
print(df.loc['G1'])
print()
print(" df.loc['G1'],loc[1]:")
print(df.loc['G1'].loc[1])
print()
print(" df.index.names:", df.index.names)
print()
print(" df.index.names = ['Groups', 'Num']")
df.index.names = ['Groups', 'Num']
print()
print(" df:")
print(df)
print()
print(" To extract column B from row 2 of Group 2:  'df.loc['G2'].loc[2].loc['B']'")
print(" df.loc['G2'].loc[2].loc['B'] =", df.loc['G2'].loc[2].loc['B'])
print()
print()
print(" The Pandas abbreviation for cross-section is 'xs'.")
print("'df.xs('G1')' is a synonym for 'df.loc['G1]")
print(" The advantage to 'xs' is for extracting multiple inner groups, such as both row 1s.")
print(" The syntax is 'DataFrame.xs(location name, level=level name).  For example, to extract all values")
print(" from row 1 in both groups:  df.xs(1, 'Num').")
print()
print("df.xs(1, level='Num'):")
print(df.xs(1, level='Num'))
print()
print(" =============================================================================================")
print()
print(" Pandas Missing Data: ")
print()
print() 
print(" dict = { 'A': [1, 2, np,nan], 'B': 5, np.nan, np.nan, 'C': 1, 2, 3}")
dict = { 'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
print()
print(" dict:")
print(dict)
print()
print(" df = pd.DataFrame(dict)")
df = pd.DataFrame(dict)
print()
print(" df:")
print(df)
print()
print(" One of the tools for data cleansing is the dropna() function,  'df.dropna()' will remove")
print(" any rows with a NaN in it,")
print()
print("df.dropna():")
print(df.dropna())
print()
print(" Like the drop() function, the effect of dropna() is temporary unless 'inplace=true' is")
print(" specified.")
print()
print(" Also, ike the drop() function, dropna() has a axis parameter that can be specified.")
print(" 0 (row axis) is the default.  To specify fropping columns with any 'NaN's, speciify dropna(axis=0)")
print()
print("df.dropna(axis=1):")
print(df.dropna(axis=1))
print()
print()
print(" Another useful parameter is thresh (for threshold) which specifies how many non-NAN values")
print(" a row must have to not be dropped.  In the original DataFrame, we see that row 1 has two NAN values")
print(" so we'll use 2 as a threshold value: df.dropna(thresh=2)")
print()
print(" df.dropna(thresh=1):")
print(df.dropna(thresh=2))
print()
print(" Note that row 1 was included because it meets the threshold.")
print()
print()
print(" Another function is the fillna() function.  For fillna() to have any effect at least ones")
print(" parameter must be used, which will probably be the 'value' argument which specifies what value")
print(" will be used to replace any NaNs.")
print()
print(" df.fillna(value='Fill Value'):")
print(df.fillna(value='Fill Value'))
print()
print(" Like other operations, dropna() and fillna() can slice our columns.  Also, mathmatical and")
print(" statistical functions can be chaine onto the functions")
print(" df[A'].fillna(value=df['A]).mean())):")
print(df['A'].fillna(value=df['A'].mean()))
print()
print()
print(" =============================================================================================")
print()
print(" Pandas Groupby: ")
print()
print() 
print(" Groupby allows the user to group together rows bases of a column and preform aggregate")
print(" functions on them.")

print(" data = {'Company':['GOOG', 'GOOG', 'MSFT', 'FB', 'FB'],")
print("        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],")
print("        'Sales':[200, 120, 340, 124, 243,350]}")
print()

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person':  ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':   [400, 300, 400340, 124, 243, 350]}

print(" df = pd.DataFrame(data):")
print()
df = pd.DataFrame(data)
print("df:")
print(df)
print()
print("byCompany = df.groupby('Company')")
byCompany = df.groupby('Company')
print()
print("byCompany:")
print()
print(byCompany.mean())
print("byComp = df.groupby('Company')")
byComp = df.groupby('Company')
print()
print("byComp.sum():")
print(byComp.sum())
print()
print("byComp.mean():")
print(byComp.mean())
print()
print("byComp.std():")
print(byComp.std())
print()
print("byComp.sum().loc['FB]:")
print(byComp.sum().loc['FB'])
print()
print("df.groupby('Company').sum().loc['GOOG']:")
print(df.groupby('Company').sum().loc['GOOG'])
print()
print("df.groupby('Company').count():")
print(df.groupby('Company').count())
print()
print()
print(" 'describe()' is a very useful function!")
print()
print("df.groupby('Company').describe():")
print(df.groupby('Company').describe())
print()
print()
print(" transpose()' changes the direction of the layout.")
print()
print("df.groupby('Company').describe().transpose()):")
print(df.groupby('Company').describe().transpose())
print()
print()
print(" =============================================================================================")
print()
print(" Pandas Merging, Joining, and Concatenating: ")
print()
print("df1:")
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
print()
print(df1)
print()
print()
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5' 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
print()
print("df2:")
print(df2)
print()
print()
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])
print("df3:")
print(df3)
print()
print()
print(" concat() is the function for concatination of multiple DataFrames")
print(" concat() has an axis argument based on 0 for columns and 1 for rows.  The default is 0.")
print()
print("pd.concat([df1, df2, df3]):")
print(pd.concat([df1, df2, df3]))
print()
print("pd.concat([df1, df2, df3], axis = 1):")
print(pd.concat([df1, df2, df3], axis =1))
print()
print("Note: The NaNs in the last example because Pandas had to preserve the indexes.")
print()
print()
print("The merge() function merges DataFrames much as in SQL.  For an example let's create two new DataFrames.")
print
left = pd.DataFrame({ 'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

print('left:')
print(left)
print()
print('right:')
print(right)
print()
print("pd.merge(left, right, how='inner', on='key'):")
print(pd.merge(left, right, how='inner', on='key'))
print()
print("A more complicated example, requires different DataFrames:")
print()
left = pd.DataFrame({ 'key1': ['K0', 'K0', 'K1', 'K1'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K1', 'K2'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})

print("left")
print(left)
print()
print("right:")
print(right)
print()
print("pd.merge(left, right, on=['key1', 'key2'])")
print(pd.merge(left, right, on=['key1', 'key2']))
print()
print("pd.merge(left, right, how='outer', on=['key1', 'key2']):")
print( pd.merge(left, right, how='outer', on=['key1', 'key2']))
print()
print("print( pd.merge(left, right, how='right', on=['key1', 'key2'])):")
print( pd.merge(left, right, how='right', on=['key1', 'key2']))
print()
print()
print(" The join() function combines the columns of two potentially differently indexed")
print(" DataFrames into a single Dataframe.")

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['K0', 'K2', 'K3'])

print()
print("left:")
print(left)
print()
print("right:")
print(right)
print()
print("left.join(right):")
print(left.join(right))
print()
print("left.join(right, how='outer'):")
print(left.join(right, how='outer'))

print()
print()
print(" =============================================================================================")
print()
print(" Pandas Operations: ")
print()
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
print()
print("df.head():")
print(df.head())
print()
print()
print("df['col2'].unique():")
print(df['col2'].unique())
print()
print("len(df['col2'].unique()):")
print(len(df['col2'].unique()))
print()
print("df['col2'].nunique():")
print(df['col2'].nunique())
print()
print("df['col2'].value_counts():")
print(df['col2'].value_counts())
print()
print("df[df['col1']>2]:")
print(df[df['col1']>2])
print()
print("df[(df['col1'] > 2) & (df['col2'] == 444)]:")
print(df[(df['col1'] > 2) & (df['col2'] == 444)])
print()
print("def times2(x):")
print("     return x * 2")
print()

def times2(x):
    return x * 2

print(" The apply function is one of the most powerful in Pandas.")
print()
print("df['col1'].apply(times2):")
print(df['col1'].apply(times2))
print()
print("df['col3']. apply(len):")
print(df['col3'].apply(len))
print()
print("df['col2']. apply(lanbda x: x * 2)")
print(df['col2']. apply(lambda x: x * 2))
print()
print(("df.drop('col1', axis=1)"))
print(df.drop('col1', axis=1))
print()
print(" To make the drop permanent, use the 'inplace=True' parameter.")
print()
print("df:")
print(df)
print()
print()
print("df.columns:")
print(df.columns)
print()
print("df.index:")
print(df.index)
print()
print("df.sort_values('col2'):")
print(df.sort_values('col2'))
print()
print(" Note: Indexes remain attached to their original rows.")
print()
print()
print("df.isnull():")
print(df.isnull())
print()

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}
df = pd.DataFrame(data)
print("df:")
print(df)
print()
print()
print(" And, of course, Pandas must have a pivot table.")
print()
print("")
print(df.pivot_table(values='D',index=['A','B'], columns=['C']))