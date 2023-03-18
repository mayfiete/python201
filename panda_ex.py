


# pandas 

pd = __import__('pandas')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pandas_series = pd.Series(numbers)

print(pandas_series)


# dataframe 

df = pd.DataFrame({'numbers': numbers})

print(df)