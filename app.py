# import os
# import sqlite3
# import streamlit as st
# import datetime

# # First, make sure to close the database connection properly
# def close_db_connection(conn):
#     conn.close()

# # Initialize database connection
# conn = sqlite3.connect("todo.db", check_same_thread=False)
# c = conn.cursor()

# # Create table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                 id INTEGER PRIMARY KEY, 
#                 task TEXT, 
#                 status TEXT, 
#                 task_date DATE)''')        
# conn.commit()

# # Get today's date
# today = datetime.date.today()

# # 🏷 App Title and Current Date
# st.title("📝 To-Do List App")
# st.subheader(f"📆 Today: {today.strftime('%A, %d %B %Y')}")

# # 📅 Generate a Horizontal Calendar for the Current Week
# st.write("### Select a Date to View Tasks:")
# week_dates = [today + datetime.timedelta(days=i) for i in range(7)]

# # Create Horizontal Buttons for Each Date
# selected_date = st.session_state.get("selected_date", today)  # Default to today

# date_cols = st.columns(len(week_dates))  # Create columns for each date
# for i, date in enumerate(week_dates):
#     if date_cols[i].button(date.strftime("%a, %d")):
#         st.session_state["selsected_date"] = date
#         # st.experimental_rerun()

# # Use the latest selected date
# selected_date = st.session_state.get("selected_date", today)

# # 📝 Input new task
# new_task = st.text_input(f"✍️ Add a task for {selected_date.strftime('%A, %d %B')}")
# if st.button("➕ Add Task"):
#     if new_task:
#         c.execute("INSERT INTO tasks (task, status, task_date) VALUES (?, ?, ?)", 
#                   (new_task, "Pending", selected_date.strftime("%Y-%m-%d")))
#         conn.commit()
#         # st.experimental_rerun()

# # 📂 Fetch tasks for the selected date
# c.execute("SELECT * FROM tasks WHERE task_date = ?", (selected_date.strftime("%Y-%m-%d"),))
# tasks = c.fetchall()

# # 🗂 Display tasks
# st.write(f"### 🗂 Tasks for {selected_date.strftime('%A, %d %B')}")
# if tasks:
#     for task in tasks:
#         col1, col2 = st.columns([5, 1])
        
#         # ✅ Checkbox to mark task as completed
#         checked = col1.checkbox(task[1], value=(task[2] == "Completed"), key=f"checkbox_{task[0]}")
        
#         if checked and task[2] == "Pending":
#             c.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task[0],))
#             conn.commit()
#             # st.experimental_rerun()

# else:
#     st.write("✅ No tasks for this day!")

# # Properly close the database connection before the app exits
# close_db_connection(conn)


# import os
# import sqlite3
# import streamlit as st
# import datetime

# # Custom CSS for pastel theme (Sage Green & Baby Pink)
# st.markdown(
#     """
#     <style>
#     body {
#         background-color:rgb(128, 223, 207); /* Soft Baby Pink */
#     }
#     .stApp {
#         background-color:rgb(128, 223, 207);
#     }
#     .stTitle, .stSubheader {
#         color:rgb(86, 128, 245); /* Sage Green */
#     }
#     .stButton>button {
#         background-color: rgb(86, 128, 245); /* Muted Sage Green */
#         color: white;
#         border-radius: 8px;
#         padding: 8px;
#     }
#     .stTextInput>div>div>input {
#         border-radius: 8px;
#         border: 1px solid rgb(86, 128, 245);
#     }
#     .stCheckbox>div>label {
#         color: rgb(86, 128, 245)
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Initialize database connection
# conn = sqlite3.connect("todo.db", check_same_thread=False)
# c = conn.cursor()

# # Create table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                 id INTEGER PRIMARY KEY, 
#                 task TEXT, 
#                 status TEXT, 
#                 task_date DATE)''')        
# conn.commit()

# # Get today's date
# today = datetime.date.today()

# # 🏷 App Title and Current Date
# st.title("📝 To-Do List App")
# st.subheader(f"📆 Today: {today.strftime('%A, %d %B %Y')}")

# # 📅 Generate a Horizontal Calendar for the Current Week
# st.write("### Select a Date to View Tasks:")
# week_dates = [today + datetime.timedelta(days=i) for i in range(7)]

# # Create Horizontal Buttons for Each Date
# selected_date = st.session_state.get("selected_date", today)  # Default to today

# date_cols = st.columns(len(week_dates))  # Create columns for each date
# for i, date in enumerate(week_dates):
#     if date_cols[i].button(date.strftime("%a, %d")):
#         st.session_state["selected_date"] = date
#         st.rerun()

# # Use the latest selected date
# selected_date = st.session_state.get("selected_date", today)

# # 📝 Input new task
# new_task = st.text_input(f"✍️ Add a task for {selected_date.strftime('%A, %d %B')}")
# if st.button("➕ Add Task"):
#     if new_task:
#         c.execute("INSERT INTO tasks (task, status, task_date) VALUES (?, ?, ?)", 
#                   (new_task, "Pending", selected_date.strftime("%Y-%m-%d")))
#         conn.commit()
#         st.rerun()

# # 📂 Fetch tasks for the selected date
# c.execute("SELECT * FROM tasks WHERE task_date = ?", (selected_date.strftime("%Y-%m-%d"),))
# tasks = c.fetchall()

# # 🗂 Display tasks
# st.write(f"### 🗂 Tasks for {selected_date.strftime('%A, %d %B')}")
# if tasks:
#     for task in tasks:
#         col1, col2 = st.columns([5, 1])
        
#         # ✅ Checkbox to mark task as completed
#         checked = col1.checkbox(task[1], value=(task[2] == "Completed"), key=f"checkbox_{task[0]}")
        
#         if checked and task[2] == "Pending":
#             c.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task[0],))
#             conn.commit()
#             st.rerun()
# else:
#     st.write("✅ No tasks for this day!")

# # Properly close the database connection before the app exits
# conn.close()



# import os
# import sqlite3
# import streamlit as st
# import datetime

# # Custom CSS for enhanced pastel theme
# st.markdown(
#     """
#     <style>
#     body {
#         background-color:rgb(158, 236, 223); /* Soft Baby Pink */
#     }
#     .stApp {
#         background-color:rgb(159, 243, 218);
#     }
#     .stTitle, .stSubheader {
#         color:rgb(86, 128, 245);/* Deep Sage Green */
#         font-weight: bold;
#     }
#     .stButton>button {
#         background-color: rgb(86, 128, 245);/* Sage Green */
#         color: white;
#         border-radius: 12px rgb(255, 255, 255) !important;
#         padding: 10px;
#         font-size: 16px;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: rgb(86, 128, 245);
#         color:rgb(158, 236, 223);
#         border-color: rgba(158, 236, 223);
#     }
#     .stTextInput>div>div>input {
#         border-radius: 12px;
#         border: 2px solid rgb(86, 128, 245);
#         padding: 8px;
#     }
#     .stCheckbox>div>label {
#         color:rgb(86, 128, 245);
#         font-size: 16px;
#     }
#     .stColumns div {
#         text-align: center;
#         padding: 5px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Initialize database connection
# conn = sqlite3.connect("todo.db", check_same_thread=False)
# c = conn.cursor()

# # Create table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                 id INTEGER PRIMARY KEY, 
#                 task TEXT, 
#                 status TEXT, 
#                 task_date DATE)''')        
# conn.commit()

# # Get today's date
# today = datetime.date.today()

# # 🏷 App Title and Current Date
# st.title("📝 To-Do List App")
# st.subheader(f"📆 Today: {today.strftime('%A, %d %B %Y')}")

# # 📅 Generate a Horizontal Calendar for the Current Week
# st.write("### Select a Date to View Tasks:")
# week_dates = [today + datetime.timedelta(days=i) for i in range(7)]

# # Create Horizontal Buttons for Each Date
# selected_date = st.session_state.get("selected_date", today)  # Default to today

# date_cols = st.columns(len(week_dates))  # Create columns for each date
# for i, date in enumerate(week_dates):
#     if date_cols[i].button(date.strftime("%a, %d")):
#         st.session_state["selected_date"] = date
#         st.rerun()

# # Use the latest selected date
# selected_date = st.session_state.get("selected_date", today)

# # 📝 Input new task
# new_task = st.text_input(f"✍️ Add a task for {selected_date.strftime('%A, %d %B')}")
# if st.button("➕ Add Task"):
#     if new_task:
#         c.execute("INSERT INTO tasks (task, status, task_date) VALUES (?, ?, ?)", 
#                   (new_task, "Pending", selected_date.strftime("%Y-%m-%d")))
#         conn.commit()
#         st.rerun()

# # 📂 Fetch tasks for the selected date
# c.execute("SELECT * FROM tasks WHERE task_date = ?", (selected_date.strftime("%Y-%m-%d"),))
# tasks = c.fetchall()

# # 🗂 Display tasks
# st.write(f"###  Tasks for {selected_date.strftime('%A, %d %B')}")
# if tasks:
#     for task in tasks:
#         col1, col2 = st.columns([5, 1])
        
#         # ✅ Checkbox to mark task as completed
#         checked = col1.checkbox(task[1], value=(task[2] == "Completed"), key=f"checkbox_{task[0]}")
        
#         if checked and task[2] == "Pending":
#             c.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task[0],))
#             conn.commit()
#             st.rerun()
# else:
#     st.write("✅ No tasks for this day!")

# # Properly close the database connection before the app exits
# conn.close()


import os
import sqlite3
import streamlit as st
import datetime

st.set_page_config(layout="wide")
# Custom CSS for enhanced pastel theme
st.markdown(
    """
    <style>
    body {
        background-color: rgb(158, 236, 223);
    }
    .stApp {
        background-color: rgb(159, 243, 218);
    }
    .stTitle, .stSubheader {
        color: rgb(86, 128, 245);
        font-weight: bold;
    }
    .stButton>button {
        background-color: rgb(86, 128, 245);
        color: white;
        border-radius: 12px !important;
        padding: 10px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: rgb(86, 128, 245);
        color: rgb(158, 236, 223);
        border-color: rgba(158, 236, 223);
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid rgb(86, 128, 245);
        padding: 8px;
    }
    .stCheckbox>div>label {
        color: rgb(86, 128, 245);
        font-size: 16px;
    }
    .stColumns div {
        text-align: center;
        padding: 5px;
    }
  
   
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize database connection
conn = sqlite3.connect("todo.db", check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY, 
                task TEXT, 
                status TEXT, 
                task_date DATE)''')        
conn.commit()

# Get today's date
today = datetime.date.today()

# Layout structure
# col1, col2 = st.columns([1, 2])
col1, spacer_col, col2 = st.columns([1, 0.7, 2])

with col1:
   st.markdown("<div class='calendar-container'>", unsafe_allow_html=True)
      
   st.markdown(
        '<iframe src="https://calendar.google.com/calendar/embed?src=b303667364a7b28e31f602b86b250c8e16a20c8a8670bd681b6566fdaa0d2ac5%40group.calendar.google.com&ctz=Asia%2FKolkata" style="border: 0; width: 500px; height: 500px;" frameborder="0" scrolling="no"></iframe>',
        unsafe_allow_html=True
    )
   st.markdown("</div>", unsafe_allow_html=True)
    
with col2:
    # 🏷 App Title and Current Date
    st.title("📝 To-Do List App")
    selected_date = st.session_state.get("selected_date", today)
    
    st.write("### Select a Date to View Tasks:")
    week_dates = [today + datetime.timedelta(days=i) for i in range(7)]

# Create Horizontal Buttons for Each Date
    selected_date = st.session_state.get("selected_date", today)  # Default to today

    date_cols = st.columns(len(week_dates))  # Create columns for each date
    for i, date in enumerate(week_dates):
     if date_cols[i].button(date.strftime("%a, %d")):
        st.session_state["selected_date"] = date
        # st.experimental_rerun()

# Use the latest selected date
    selected_date = st.session_state.get("selected_date", today)
    new_task = st.text_input(f"✍️ Add a task for {selected_date.strftime('%A, %d %B')}")
    if st.button("➕ Add Task"):
      if new_task:
        c.execute("INSERT INTO tasks (task, status, task_date) VALUES (?, ?, ?)", 
                  (new_task, "Pending", selected_date.strftime("%Y-%m-%d")))
        conn.commit()
        # st.experimental_rerun()

# 📂 Fetch tasks for the selected date
    c.execute("SELECT * FROM tasks WHERE task_date = ?", (selected_date.strftime("%Y-%m-%d"),))
    tasks = c.fetchall()

# 🗂 Display tasks
    st.write(f"### 🗂 Tasks for {selected_date.strftime('%A, %d %B')}")
    if tasks:
      for task in tasks:
        col1, col2 = st.columns([5, 1])
        
        # ✅ Checkbox to mark task as completed
        checked = col1.checkbox(task[1], value=(task[2] == "Completed"), key=f"checkbox_{task[0]}")
        
        if checked and task[2] == "Pending":
            c.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task[0],))
            conn.commit()
            # st.experimental_rerun()

    else:
     st.write("✅ No tasks for this day!")

# Properly close the database connection before the app exits
conn.close()
