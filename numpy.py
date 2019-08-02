import numpy as np

wing_widths = [7.02, 6.84, 6.56, 6.44, 0.0, 0.0, 4.92, 6.35, 6.07, 6.68, 6.91, 7.09, 8.90, 0.0,
               9.79, 6.32, 7.24, 7.27, 8.02, 0.0, 7.76, 6.94, 5.80, 7.43, 6.85, 8.44, 5.16, 7.96, 
               0.0, 6.99, 8.56, 5.20, 5.76, 6.87, 6.41, 0.0, 7.36, 5.74, 7.06, 6.44, 8.06, 7.86]
            

print(np.mean(wing_widths)) #Returns the mean of the dataset
print(np.amax(wing_widths))

#How to calculate percentage
class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])
millennials = np.mean(class_year > 2004)
print(millennials)

#percentage = np.mean(dataset COMPARE value)

# two dimensional arrays 
# axis = 1 will return average for average for each array, whereas axis = 0 does it for each index in each array

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

trial_mean = np.mean(allergy_trials, axis=1)
patient_mean = np.mean(allergy_trials, axis=0)

# Sort an array from largest to smallest 

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps)
print(sorted_temps)

# Calculate median 

large_set = np.genfromtxt('household_income.csv', delimiter=',')

large_set_median = np.median(large_set)

#Calculate percentiles

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)

seventieth_percentile = np.percentile(patrons, 70)
