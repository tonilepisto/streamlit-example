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

# Add a title
st.title('Data to dataframe app')

# Upload csv
file = st.file_uploader('Upload a CSV file')

# Process file
def process_file(file):
    #st.write(file)
    #df = pd.read_csv(file)
    #file.to_csv ('fileX.csv', index = False, header=True)
    a_1 = pd.read_csv(file,delimiter=';',decimal=',')
    a_1['seconds'] = pd.to_datetime(a_1['seconds'],unit='s')
    a_1.rename(columns={a_1.columns[0]:'Reserve_0'}, inplace=True)
    a_1.rename(columns={a_1.columns[1]:'Reserve_1'}, inplace=True)
    a_1.rename(columns={a_1.columns[2]:'Reserve_2'}, inplace=True)
    a_1.rename(columns={a_1.columns[3]:'Reserve_3'}, inplace=True)
    a_1.rename(columns={a_1.columns[4]:'Reserve_4'}, inplace=True)
    a_1.rename(columns={a_1.columns[5]:'105: MBBR tank 1 blower line pressure PIT701 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[6]:'105: MBBR tank 2 blower line pressure PIT702 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[7]:'105: MBBR tank 1 DO sensor XT001 mg/l'}, inplace=True)
    a_1.rename(columns={a_1.columns[8]:'105: MBBR tank 2 DO sensor XT002 mg/g'}, inplace=True)
    a_1.rename(columns={a_1.columns[9]:'MBBR tank 2 pH sensor XT101 pH'}, inplace=True)
    a_1.rename(columns={a_1.columns[10]:'105: MBBR tank 1 temperature degC'}, inplace=True)
    a_1.rename(columns={a_1.columns[11]:'105: MBBR tank 2 temperature degC'}, inplace=True)
    a_1.rename(columns={a_1.columns[12]:'106: MBBR discharge line TSS sensor TSS001 mg/l'}, inplace=True)
    a_1.rename(columns={a_1.columns[13]:'107: Polymer conentration unit A mg/l'}, inplace=True)
    a_1.rename(columns={a_1.columns[14]:'107: Polymer conentration unit B mg/l'}, inplace=True)
    a_1.rename(columns={a_1.columns[15]:'Reserve_15'})
    a_1.rename(columns={a_1.columns[16]:'108: DAF1 recycling line pressure PT001 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[17]:'108: DAF1 sludge discharge line pressure PT005 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[18]:'Reserve_18'}, inplace=True)
    a_1.rename(columns={a_1.columns[19]:'108: DAF2 recycling line pressure PT002 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[20]:'108: DAF2 sludge discharge line pressure PT006 bar'}, inplace=True)
    a_1.rename(columns={a_1.columns[21]:'Reserve_21'}, inplace=True)
    a_1.rename(columns={a_1.columns[22]:'Reserve_22'}, inplace=True)
    a_1.rename(columns={a_1.columns[23]:'110: Effluent line TSS XT003'})
    a_1.rename(columns={a_1.columns[24]:'110: Effluent line pH sensor XT004'}, inplace=True)
    a_1.rename(columns={a_1.columns[25]:'105: MBBR Blower KF007 PT100 temp'}, inplace=True)
    a_1.rename(columns={a_1.columns[26]:'105: MBBR Blower KF009 PT100 temp'}, inplace=True)
    a_1.rename(columns={a_1.columns[27]:'105: MBBR Blower KF008 PT100 temp'}, inplace=True)
    a_1.rename(columns={a_1.columns[28]:'105: MBBR Blower KF006 PT100 temp'}, inplace=True)
    a_1.rename(columns={a_1.columns[29]:'105: MBBR Blower KF009 Speed Hz'}, inplace=True)
    a_1.rename(columns={a_1.columns[30]:'105: MBBR Blower KF009 Speed A'}, inplace=True)
    a_1.rename(columns={a_1.columns[31]:'105: MBBR Blower KF008 Speed Hz'}, inplace=True)
    a_1.rename(columns={a_1.columns[32]:'105: MBBR Blower KF008 Speed A'}, inplace=True)
    a_1.rename(columns={a_1.columns[33]:'105: MBBR Blower KF007 Speed Hz'}, inplace=True)
    a_1.rename(columns={a_1.columns[34]:'105: MBBR Blower KF007 Speed A'}, inplace=True)
    a_1.rename(columns={a_1.columns[35]:'105: MBBR Blower KF006 Speed Hz'}, inplace=True)
    a_1.rename(columns={a_1.columns[36]:'105: MBBR Blower KF006 Speed A'}, inplace=True)
    a_1.rename(columns={a_1.columns[37]:'Reserve_37'}, inplace=True)
    a_1.rename(columns={a_1.columns[38]:'Reserve_38'}, inplace=True)
    a_1.rename(columns={a_1.columns[39]:'Reserve_39'}, inplace=True)
    a_1.rename(columns={a_1.columns[40]:'Reserve_40'}, inplace=True)
    a_1.rename(columns={a_1.columns[41]:'strTimeDate'}, inplace=True)
    a_1.rename(columns={a_1.columns[42]:'Date'}, inplace=True)
    a_1.rename(columns={a_1.columns[43]:'Reserve_43'}, inplace=True)
    a_1 = a_1[a_1.columns.drop(list(a_1.filter(regex='Reserve')))]
    dfc = a_1.columns
    dfc2 = pd.DataFrame(a_1.columns)
    dfc2.rename(columns={dfc2.columns[0]:'names'}, inplace=True)
    if columnDisplay:
        st.write('Following columns imported:')
        st.write(dfc)

    #st.write('Following columns imported:')
    #st.write(dfc)
    a_1.to_csv('export.csv',index=False,header=True) #Removed exports !!!
    a_1.to_pickle('export.pkl')
    data = pd.read_pickle('export.pkl')
    data = data.set_index('Date')
    dataWriteDone = True

if st.checkbox('Show Columns'):
    columnDisplay = True
else:
    columnDisplay = False


if st.button('Read file to df'):
    process_file(file)




#https://docs.streamlit.io/library/api-reference/widgets

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

# Check if we have dataframe:
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

def draw_chart(option):
    data = pd.read_pickle('export.pkl') # created before
    data = data.set_index('Date') #created before
    #dfc = data.columns
    #st.write(dfc)
    #source = data[['110: Effluent line TSS XT003','110: Effluent line pH sensor XT004']]
    source = data[option]
    st.line_chart(source) #, width = 2000, height = 400)


option = st.selectbox(
    'Which data you want to use ?',
    dfc2["names"])
    #"data['columns'])
'You selected: ', option

if st.button('Draw chart'):
        draw_chart(option)
    
df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

#my_table = st.table(df1) 

df2 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))


#dftest = pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#    })

#option = st.selectbox(
#    'Which number do you like best?',
#     dftest['first column'])

#'You selected: ', option


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

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

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
