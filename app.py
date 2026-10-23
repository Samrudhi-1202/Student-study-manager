import streamlit as st
import json
from pathlib import Path
TASKS_FILE = Path("tasks.json")
# Load tasks saved from an earlier session
if TASKS_FILE.exists():
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = json.load(file)
else:
    tasks = []
# Save tasks to a file
def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
st.set_page_config(
    page_title="Student Study Manager",
    page_icon="📚",
    layout="wide"
)
st.title("📚 Student Study Manager")
st.write("Plan your work. Track your progress. Reach your goals.")
st.divider()
# Calculate dashboard values
total_tasks = len(tasks)
completed_tasks = sum(1 for item in tasks if item["completed"])
pending_tasks = total_tasks - completed_tasks

if total_tasks > 0:
    progress = completed_tasks / total_tasks
else:
    progress = 0.0

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("📝 Total Tasks", total_tasks)
col2.metric("✅ Completed", completed_tasks)
col3.metric("⏳ Pending", pending_tasks)

# Progress section
st.subheader("📊 Overall Progress")
st.progress(progress, text=f"{progress:.0%} completed")
st.divider()
st.subheader("➕ Add a New Task")

subject = st.text_input(
    "Subject",
    placeholder="e.g. Mathematics"
)

task = st.text_input(
    "Task or Assignment",
    placeholder="e.g. Complete Module 1 notes"
)

deadline = st.date_input("Deadline")
if st.button("Add Task", type="primary"):
    if subject.strip() and task.strip():
        new_task = {
            "subject": subject.strip(),
            "task": task.strip(),
            "deadline": str(deadline),
            "completed": False
        }

        tasks.append(new_task)
        save_tasks()

        st.success(f"Task '{task}' added successfully!")
    else:
        st.warning("Please enter both the subject and task.")

# Display all tasks
st.divider()
st.subheader("📋 Your Tasks")

search_query = st.text_input(
    "🔎 Search Tasks",
    placeholder="Search by subject or task name..."
)

if not tasks:
    st.write("No tasks added yet. Add your first task above!")

else:
    # Filter tasks using the search box
    filtered_tasks = [
        (index, item)
        for index, item in enumerate(tasks)
        if search_query.strip().casefold()
        in (item["subject"] + " " + item["task"]).casefold()
    ]

    if not filtered_tasks:
        st.info("No matching tasks found.")

    else:
        for index, item in filtered_tasks:
            st.write(f"**Subject:** {item['subject']}")
            st.write(f"**Task:** {item['task']}")
            st.write(f"**Deadline:** {item['deadline']}")

            if item["completed"]:
                st.success("Completed")
            else:
                st.info("Pending")

            col1, col2 = st.columns(2)

            with col1:
                if not item["completed"]:
                    if st.button(
                        "✅ Mark Complete",
                        key=f"complete_{index}"
                    ):
                        tasks[index]["completed"] = True
                        save_tasks()
                        st.rerun()

            with col2:
                if st.button(
                    "🗑️ Delete Task",
                    key=f"delete_{index}"
                ):
                    tasks.pop(index)
                    save_tasks()
                    st.rerun()

            st.divider()
