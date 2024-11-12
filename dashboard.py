import pandas as pd
import streamlit as st
from pinotdb import connect
import plotly.express as px
from datetime import datetime
import time

# Set up the page layout
st.set_page_config(layout="wide")
st.header("Real-Time Data Streaming and Analytics Dashboard")

# Connect to Apache Pinot
conn = connect(host='ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com', port=8099, path='/query/sql', scheme='http')

# Display the last update time
now = datetime.now()
dt_string = now.strftime("%d %B %Y %H:%M:%S")
st.write(f"Last update: {dt_string}")

# Set up auto-refresh options
if "sleep_time" not in st.session_state:
    st.session_state.sleep_time = 2
if "auto_refresh" not in st.session_state:
    st.session_state.auto_refresh = True

auto_refresh = st.checkbox('Auto Refresh?', st.session_state.auto_refresh)
st.session_state.auto_refresh = auto_refresh

if auto_refresh:
    refresh_rate = st.number_input('Refresh rate in seconds', value=st.session_state.sleep_time, min_value=1)
    st.session_state.sleep_time = refresh_rate
else:
    refresh_rate = st.session_state.sleep_time

# Set up database cursor
curs = conn.cursor()

# Query for distinct regions and genders
curs.execute("SELECT DISTINCT REGIONNAME FROM Region_Page_Summary")
regions = [row[0] for row in curs]
selected_regions = st.multiselect("Select Regions:", regions, default=regions)

curs.execute("SELECT DISTINCT GENDER FROM Session_Window_Analysis")
genders = [row[0] for row in curs]
selected_genders = st.multiselect("Select Genders:", genders, default=genders)

# Apply filters to the queries
region_filter = "'" + "', '".join(selected_regions) + "'"
gender_filter = "'" + "', '".join(selected_genders) + "'"

# Column layout for panel 1 and panel 2
col1, col2 = st.columns(2)

# Query 1: Page Visits by Region
query1 = f"""
SELECT REGIONNAME, SUM(TOTALPAGEVISITS) as PageVisits
FROM Region_Page_Summary
WHERE REGIONNAME IN ({region_filter})
GROUP BY REGIONNAME
ORDER BY PageVisits DESC
LIMIT 10
"""
curs.execute(query1)
df_summary1 = pd.DataFrame(curs, columns=[item[0] for item in curs.description])

# Panel 1: Page Visits by Region (Bar Chart)
with col1:
    fig1 = px.bar(df_summary1, x="PageVisits", y="REGIONNAME", title="Page Visits by Region", orientation='h', color='REGIONNAME', text_auto=True)
    fig1.update_traces(textposition='outside')
    fig1.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        xaxis_title="Total Visits",             
        yaxis_title=None
    )
    st.plotly_chart(fig1)

# Query 2: Average View Time by Region
query2 = f"""
SELECT REGIONNAME, AVG(AVERAGEVIEWTIME) as AvgViewTime
FROM Region_Page_Summary
WHERE REGIONNAME IN ({region_filter})
GROUP BY REGIONNAME
ORDER BY AvgViewTime DESC
LIMIT 10
"""
curs.execute(query2)
df_summary2 = pd.DataFrame(curs, columns=[item[0] for item in curs.description])

# Panel 2: Average View Time by Region (Bar Chart)
with col2:
    fig2 = px.bar(df_summary2, x="AvgViewTime", y="REGIONNAME", title="Average View Time by Region (Seconds)", orientation='h', color='REGIONNAME', text_auto=True)
    fig2.update_traces(textposition='outside')
    fig2.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        xaxis_title="Average View Time (s)",             
        yaxis_title=None
    )
    st.plotly_chart(fig2)

# Second row with two more columns (Panel 3 and Panel 4)
col3, col4 = st.columns(2)

# Query 3: Session Length Analysis by Gender
query3 = f"""
SELECT GENDER, AVG(SESSIONLENGTHSECONDS) as AvgSessionLength
FROM Session_Window_Analysis
WHERE GENDER IN ({gender_filter})
GROUP BY GENDER
ORDER BY AvgSessionLength DESC
"""
curs.execute(query3)
df_summary3 = pd.DataFrame(curs, columns=[item[0] for item in curs.description])

# Panel 3: Average Session Length by Gender
with col3:
    fig3 = px.bar(df_summary3, x="GENDER", y="AvgSessionLength", title="Average Session Length by Gender (Seconds)", color='GENDER', text_auto=True)
    fig3.update_traces(textposition='outside')
    fig3.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        xaxis_title=None,             
        yaxis_title="Average Session Length (s)"
    )
    st.plotly_chart(fig3)

# Query 4: Total Page Visits Over Time (Last 5 Minutes)
query4 = f"""
SELECT STARTWINDOW, SUM(VIEWCOUNT) as TotalViews
FROM PageViews_Tumbling
WHERE REGIONNAME IN ({region_filter})
GROUP BY STARTWINDOW
ORDER BY STARTWINDOW DESC
LIMIT 5
"""
curs.execute(query4)
df_summary4 = pd.DataFrame(curs, columns=[item[0] for item in curs.description])
df_summary4['STARTWINDOW'] = pd.to_datetime(df_summary4['STARTWINDOW'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Bangkok')

# Panel 4: Total Page Visits Over Time
with col4:
    fig4 = px.line(df_summary4, x="STARTWINDOW", y="TotalViews", title="Total Page Visits Over Time (Last 5 Minutes)", markers=True)
    fig4.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        xaxis_title="Time",             
        yaxis_title="Total Page Visits"
    )
    st.plotly_chart(fig4)

# Refresh logic
if auto_refresh:
    time.sleep(refresh_rate)
    st.rerun()
