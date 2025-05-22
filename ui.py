import streamlit as st
import requests
from prototypes.prompts import prompts

st.set_page_config(page_title="Meeting Minutes & More")
st.title("📋 AI Insights Project 🤖")

meeting_type = st.selectbox("Select type of meeting", list(prompts.keys()))
uploaded = st.file_uploader("Upload a transcript (.txt)", type=["txt"])
if uploaded:
    transcript = uploaded.read().decode("utf-8")
    st.subheader("Preview of Transcript")
    st.text_area("transcript preview", transcript, height=200)
    
    if st.button("Generate Summary & Actions"):
        with st.spinner("Calling the LLM…"):
            # generate summary and action items
            files = {"file": ("transcript.txt", transcript)}
            data  = {"meeting_type": meeting_type}
            resp  = requests.post(
                "http://localhost:8000/process_transcript/", 
                files=files,
                data=data
            )
        #display
        if resp.status_code == 200:
            result = resp.json()

            st.subheader("📝 Summary")
            for line in result["summary"].splitlines():
                st.markdown(f"- {line.strip().lstrip('-')}")

            st.subheader("✅ Action Items")
            items = result["action_items"]
            if isinstance(items, list):
                for item in items:
                    task = item.get("task", "[no task]")
                    owner = item.get("owner", "[no owner]")
                    due_date = item.get("due_date", "[no date]")
                    st.write(f"- **{task}** — _{owner}_ (due: {due_date})")
            else:
                st.error("Could not parse action items.")
        else:
            st.error(f"Error {resp.status_code}: {resp.text}")