import streamlit as st

from doc_generator import create_curriculum_doc
from prompt_builder import build_prompt
from gemini_api import generate_curriculum
from validator import validate_curriculum

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Curriculum Map Generator",
    page_icon="📚",
    layout="wide"
)

# --------------------------------
# SESSION STATE
# --------------------------------

if "topics" not in st.session_state:
    st.session_state.topics = []

# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.title("📚 Curriculum Map")

    st.markdown("""
Generate a complete Curriculum Map using Gemini AI.

### Workflow

1. Enter Standards
2. Add Topics
3. Add Competencies
4. Generate Curriculum Map
5. Download DOCX
""")

    st.divider()

    st.metric("Topics", len(st.session_state.topics))

# --------------------------------
# TITLE
# --------------------------------

st.title("📚 Curriculum Map Generator")

st.caption(
    "Generate professionally aligned curriculum maps."
)

st.divider()

# --------------------------------
# STANDARDS
# --------------------------------

st.subheader("Curriculum Standards")

content_standard = st.text_area(
    "Content Standard",
    height=120
)

performance_standard = st.text_area(
    "Performance Standard",
    height=120
)

st.divider()

# --------------------------------
# ADD TOPIC
# --------------------------------

col1, col2 = st.columns([1, 4])

with col1:

    if st.button("➕ Add Topic"):

        st.session_state.topics.append(
            {
                "topic": "",
                "acquisition": [""],
                "meaning": [""],
                "transfer": [""]
            }
        )

        st.rerun()

# --------------------------------
# TOPICS
# --------------------------------

for i, topic in enumerate(st.session_state.topics):

    with st.expander(f"📘 Topic {i+1}", expanded=True):

        topic["topic"] = st.text_input(
            "Topic Name",
            value=topic["topic"],
            key=f"topic_{i}"
        )

        # ----------------------------
        # Acquisition
        # ----------------------------

        st.markdown("### Acquisition Competencies")

        for j in range(len(topic["acquisition"])):

            topic["acquisition"][j] = st.text_area(
                f"Acquisition {j+1}",
                value=topic["acquisition"][j],
                key=f"acq_{i}_{j}"
            )

        if st.button(
            "Add Acquisition",
            key=f"acq_btn_{i}"
        ):
            topic["acquisition"].append("")
            st.rerun()

        # ----------------------------
        # Make Meaning
        # ----------------------------

        st.markdown("### Make Meaning Competencies")

        for j in range(len(topic["meaning"])):

            topic["meaning"][j] = st.text_area(
                f"Make Meaning {j+1}",
                value=topic["meaning"][j],
                key=f"mm_{i}_{j}"
            )

        if st.button(
            "Add Make Meaning",
            key=f"mm_btn_{i}"
        ):
            topic["meaning"].append("")
            st.rerun()

        # ----------------------------
        # Transfer
        # ----------------------------

        st.markdown("### Transfer Competencies")

        for j in range(len(topic["transfer"])):

            topic["transfer"][j] = st.text_area(
                f"Transfer {j+1}",
                value=topic["transfer"][j],
                key=f"tr_{i}_{j}"
            )

        if st.button(
            "Add Transfer",
            key=f"tr_btn_{i}"
        ):
            topic["transfer"].append("")
            st.rerun()

        st.divider()

        if st.button(
            "🗑 Remove Topic",
            key=f"remove_{i}"
        ):
            st.session_state.topics.pop(i)
            st.rerun()

# --------------------------------
# GENERATE
# --------------------------------

st.divider()

if st.button(
    "🚀 Generate Curriculum Map",
    type="primary",
    use_container_width=True
):

    # Validation
    if len(st.session_state.topics) == 0:

        st.error("Please add at least one Topic.")

    elif content_standard.strip() == "":

        st.error("Please enter the Content Standard.")

    elif performance_standard.strip() == "":

        st.error("Please enter the Performance Standard.")

    else:

        # ----------------------------
        # Build Input Data
        # ----------------------------

        data = {
            "content_standard": content_standard,
            "performance_standard": performance_standard,
            "topics": st.session_state.topics
        }

        # ----------------------------
        # Build Prompt
        # ----------------------------

        prompt = build_prompt(data)

        with st.expander("Prompt Preview"):

            st.code(prompt)

        # ----------------------------
        # Generate Response
        # ----------------------------

        with st.spinner("Generating Curriculum Map..."):

            response = generate_curriculum(prompt)

        

        # ----------------------------
        # Validate Response
        # ----------------------------


        if response.get("success") is False:
            st.error(response["error"])
            st.stop()

        valid, message = validate_curriculum(response)

        if valid:

            curriculum = response

            st.success("✅ Curriculum generated successfully!")

            doc = create_curriculum_doc(curriculum)

            st.download_button(
                "📥 Download Curriculum Map",
                data=doc,
                file_name="Curriculum_Map.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        else:
            st.error(message)

            st.subheader("Raw Gemini Response")
            st.write(response) 