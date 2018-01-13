
# coding: utf-8

# In[110]:


# reads a file, converts all of its fields to an integer and returns a list
# with this converted values. 
def read_csv(file_name):
    final_list = []
    
    f = open(file_name, 'r')
    data = f.read()
    rows = data.split('\n')
    print(rows[0])
    no_header_rows = rows[1::]
    
    for row in no_header_rows:
        string_fields = row.split(',')
        int_fields = []
        
        for string in string_fields:
            int_fields.append(int(string))
        
        final_list.append(int_fields)
    
    return final_list


# In[111]:


# Returns a dict with the summation of births that occurred in a given 
# period (column)
def calc_counts(data, column):
    births ={}
    
    for line in data:
        key = line[column]
        number_of_births = line[4]
        
        if key in births:
            births[key] += number_of_births
        else:
            births[key] = number_of_births
        
    return births


# In[112]:


# returns the keys for maximum and minimum values of a dict
def get_limits(dict):
    
    max_key = max(dict, key = lambda x: dict.get(x))
    min_key = min(dict, key = lambda x: dict.get(x))
    
    return max_key, min_key


# In[113]:


# returns the variation of the number of births of a specific day of the week
# over the year of our data
def dow_over_years(data, dow):
    yearly_values = {}
    yearly_values_list = []
    variation = []
    
    for line in data:
        if line[3] == dow:
            year = line[0]
            births = line[4]
            
            if year in yearly_values:
                yearly_values[year] += births
            else:
                yearly_values[year] = births

    for value in yearly_values.values():
        yearly_values_list.append(value)
        print(value)
    variation.append(0.0)
    for i in range(0, len( yearly_values_list) - 1):
        variation.append(-100*(yearly_values_list[i] - yearly_values_list[i+1]) / yearly_values_list[i])
        
    return variation
        


# In[114]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[:10])

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

m,n = get_limits(cdc_dow_births)
print(m, n)

variation = dow_over_years(cdc_list, 3)

