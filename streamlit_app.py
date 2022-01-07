#from collections import namedtuple
#import altair as alt
#import math
#import pandas as pd
#import streamlit as st

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import datetime
from dateutil import tz
import time
from bokeh.plotting import figure

"""
# Welcome to Data app

Check out:
https://github.com/MichaelAllen1966/2109_streamlit_examples
https://medium.com/@avra42/streamlit-python-cool-tricks-to-make-your-web-application-look-better-8abfc3763a5b
https://www.youtube.com/watch?v=G9U4Uixssf0&t=3s

"""

# Try to hide menu (it works)
#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

####### Sidebar #######
#ny_zone = tz.gettz('America/New_York')
#cast_time = st.sidebar.slider('Cast Time:', value=datetime.time(0, 0, 0, tzinfo=ny_zone),
#                              min_value=datetime.time(0, 0, 0, tzinfo=ny_zone),
#                              max_value=datetime.time(22, 0, 0, tzinfo=ny_zone),
#                              step=datetime.timedelta(hours=1),
#                              format='H:mm')
if columnDisplay:
    st.sidebar.write('Note: Column display enabled')
else:
    st.sidebar.write('Note: Column display disabled')

d5 = st.sidebar.date_input("date range with default", [datetime.date(2019, 7, 6), datetime.date(2019, 7, 8)])
#st.write('Date range',d5)

t0 = st.sidebar.time_input('Start time', datetime.time(9, 00))
t1 = st.sidebar.time_input('End Time', datetime.time(12, 00))
#st.write('From', t1, 'to', t2)     

def calcTimes():
    timeStart = datetime. datetime. combine(d5[0], t0)
    timeEnd = datetime. datetime. combine(d5[1], t1)
    st.sidebar.write('Time range selected: From', timeStart, 'to', timeEnd)
    timeDiff = timeEnd - timeStart
    st.sidebar.write('Duration:',timeDiff)

if st.sidebar.button('Show times'):
    calcTimes()

#st.write("Hello world! Here is date time slider")
#dateStart = st.sidebar.date_input('start date', datetime.date(2021,1,1))
#st.write(dateStart)
#dateEnd = st.sidebar.date_input('End date', datetime.date(2021,2,1))
#st.write(dateEnd)

#d3 = st.date_input("range, no dates", [])
#st.write(d3)

#d3 = st.date_input("Range, one date", [datetime.date(2019, 7, 6)])
#st.write(d3)

#d5 = st.date_input("date range with default", [datetime.date(2019, 7, 6), datetime.date(2019, 7, 8)])
#st.write(d5)

# Show a matplotlib chart based on user input
#st.write("Hello world! Here is slider that effects on draw output")
#power = st.slider('Power', min_value=0, max_value=5, value=2)

####### Sidebar #######


# Add a title
st.title('Data to dataframe app')

# Upload csv
file = st.file_uploader('Upload a CSV file')

# Process file
#@st.cache
def process_file(file):
    #st.write(file)
    #df = pd.read_csv(file)
    #file.to_csv ('fileX.csv', index = False, header=True)
    a_1 = pd.read_csv(file,delimiter=';',decimal=',')
    i=0
    for col in a_1.columns:
        if col != 'seconds':
            a_1.rename({a_1.columns[i]: 'Col'+str(i)}, axis=1, inplace=True)
        else:
            a_1['seconds'] = pd.to_datetime(a_1['seconds'],unit='s')
            a_1.rename({a_1.columns[i]: 'Date'}, axis=1, inplace=True)
        i = i +1
    #a_1['seconds'] = pd.to_datetime(a_1['seconds'],unit='s')
    #a_1 = a_1[a_1.columns.drop(list(a_1.filter(regex='Reserve')))]
    dfc = a_1.columns
    #dfc2 = list(a_1)
    dfc2 = list(a_1.columns.values)
    if columnDisplay:
        st.write('Following columns imported:')
        st.write(dfc)
    #st.write('Following columns imported:')
    #st.write(dfc)
    a_1.to_csv('export.csv',index=False,header=True) #Removed exports !!!
    a_1.to_pickle('export.pkl')
    #data = pd.read_pickle('export.pkl')
    #data = data.set_index('Date')
    dataWriteDone = True

if st.checkbox('Show Columns'):
    columnDisplay = True
else:
    columnDisplay = False


if st.button('Read file to df'):
    process_file(file)




#https://docs.streamlit.io/library/api-reference/widgets


dfError = False
#try:
    #st.write(data.head())
# catch when df1 is None
#except AttributeError:
    #data = pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
    #})
    #dfError = True
# catch when it hasn't even been defined
#except NameError:
    #data = pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
    #})
    #dfError = True

@st.cache
def readData():
    data = pd.read_pickle('export.pkl')
    data = data.set_index('Date')
    return data 

@st.cache   
def readColumns(data):
     data = pd.read_pickle('export.pkl')
     columnNames = data.columns
     return columnNames

@st.cache
def draw_chart(data,filtered):
    #data = pd.read_pickle('export.pkl')
    #data = data.set_index('Date')
    #st.write(dfc)
    #source = data[['Col0','Col1']]
    source = data[filtered]
    st.line_chart(source) #, width = 2000, height = 400)

# create some dataframe
#dfFilter = pd.DataFrame({f"f_{i}": list(range(100)) for i in range(10)})
#data = pd.read_pickle('export.pkl')
#data = data.set_index('Date')
#filtered = st.multiselect("Filter columns", options=list(data.columns), default=list(data.columns))
#filtered = st.multiselect("Filter columns", options=list(data.columns), default=None)


if st.button('Draw chart'):
        draw_chart(filtered)

data = readData()
columns = readColumns(data)
filtered = st.multiselect("Filter columns", options=list(data.columns), default=None)
draw_chart(data,filtered)
#selectedColumns = st.multiselect("Filter columns", options=list(result[1]), default=None)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  #bar.progress(i + 1)
  #time.sleep(0.1)


#my_table.add_rows(df2)

#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(chart_data)

#Bokeh example
#x = [1, 2, 3, 4, 5]
#y = [6, 7, 2, 4, 5]

#p = figure(
#     title='simple line example',
#     x_axis_label='x',
#     y_axis_label='y')

#p.line(x, y, legend_label='Trend', line_width=2)

#st.bokeh_chart(p, use_container_width=True)




# initialize list of lists
dataU = [['Le goumet', 10], ['The Alcove', 15], ['Mojo Restaurant', 14], ['Mojo Restaurant', 1]]

# Create the pandas DataFrame
df = pd.DataFrame(dataU, columns=['Name', 'ID'])

values = df['Name'].tolist()
options = df['ID'].tolist()
dic = dict(zip(options, values))

a = st.sidebar.selectbox('Choose a restaurant', options, format_func=lambda x: dic[x])

st.write(a)

#@st.cache
#def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

#csvExport = convert_df(data)

#st.download_button(
#     label="Download data as CSV",
#     data=csvExport,
#     file_name='csvExport.csv',
#     mime='text/csv',
# )