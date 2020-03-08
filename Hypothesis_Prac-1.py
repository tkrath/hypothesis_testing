import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
import statsmodels.api as sm
clear()

##Reading data from the path####
## for excel use read_excel
cutlets = pd.read_csv("D:\\Study\\Data Analytics & Data Science\\Data Science\\360DigiTMG\\Data Sets\\Cutlets.csv")
cutlets.columns = "UnitA", "UnitB" ### For changing the column name to a defined attribute####
cutlet = cutlets.iloc[0:35, 0:2] ####Removing the NaN values and assigning the rows and columns which are required###

#######Normality Test######

##from the above tests on individual sample populations its confirmed that they have a normal distribution as the pvalue is >0.05

#######Variance Test#########
#####Levene's Test#####
scipy.stats.levene(cutlet.UnitA, cutlet.UnitB)
###since the pvalue is 0.417 which is >0.05 we fail to reject null H0 which is both the populations have equal variances

#####2 sample T Test #####
scipy.stats.ttest_ind(cutlet.UnitA, cutlet.UnitB)
#since the p values is >0.05 we fail to reject H0. Hence it can be concluded that both the product diameter have a significance difference



