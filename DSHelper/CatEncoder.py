import numpy as np
import math
def OrdinalCalc(df,col,y,normalize):
    # For each categorical value create a numeric relationship to the dependent variable
    distributions = df.groupby(col).mean()[y]

    # If normalize is true normalize the averages
    if normalize:
        nmax = distributions.max()
        nmin = distributions.min()
        nrange = nmax - nmin

        distributions = (distributions - nmin)/nrange

    # Because these distributions can be the same for categorical values ensure they are unique
    # This will maintain that these values are distinct categories and not continous values

    # Determine how many digits the categories could potentially go to
    max_digits = 10 ** math.floor(np.log10(len(distributions)))
    # Add Identifier to the end of the distribution
    ids = [(i+1)/(1000 * max_digits) for i in range(len(distributions))]
    replacements = round(distributions, 2) + ids
    replacements = round(replacements, 8) #eliminates rounding issues from the ids
    replacements = replacements.to_dict()
    return replacements



def GetOrdinal(df_train,y,df_test=None,cols=[],normalize=False):
    # If no columns specified get all of the non numeric columns
    if not cols:
        cols = df_train.dtypes[df_train.dtypes == object].index

    #Remove the independent variable if it is there
    if y in cols:
        cols = list(cols)
        cols.remove(y)

    categories = dict()
    for col in cols:
        if df_train[col].dtypes == object:
            replacements = OrdinalCalc(df_train,col,y,normalize)
            df_train[col] = df_train[col].map(replacements)
            categories[col] = replacements

    if df_test is not None:
        for col in categories:
            df_test[col] = df_test[col].map(categories[col])


    return categories
  
