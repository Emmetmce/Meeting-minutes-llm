import streamlit as st
from app import gen_summary, extract_action_items

st.set_page_config(page_title="Meeting Minutes & More")

st.title("📋 interview proj")

uploaded = st.file_uploader("Upload a transcript (.txt)", type=["txt"])
if uploaded:
    transcript = uploaded.read().decode("utf-8")
    st.subheader("Preview of Transcript")
    st.text_area("", transcript, height=200)
    
    if st.button("Generate Summary & Actions"):
        with st.spinner("Calling the LLM…"):
            # generate summary and action items
            summary = gen_summary(transcript)
            actions = extract_action_items(transcript)

        st.subheader("📝 Summary")
        for bullet in summary.splitlines():
            st.markdown(f"- {bullet.strip().lstrip('-')}")

        st.subheader("✅ Action Items")
        if isinstance(actions, list):
            for item in actions:
                task = item.get("task") or "[no task]"
                owner = item.get("owner") or "[no owner]"
                due = item.get("due_date") or "[no date]"
                st.write(f"- **{task}** — _{owner}_ (due: {due})")
        else:
            st.error("Failed to parse action items:")
            st.code(str(actions))