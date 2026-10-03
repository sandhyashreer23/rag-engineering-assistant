import streamlit as st

from document_reader import (
    read_pdf,
    read_docx
)

from summarizer import (
    summarize_document
)

from classifier import (
    classify_document
)

from rag_pipeline import (
    create_vector_store,
    ask_question
)

st.set_page_config(
    page_title="RAG Engineering Assistant",
    layout="wide"
)

st.title(
    "🤖 RAG-Based Engineering Assistant"
)

uploaded_file = st.file_uploader(
    "Upload PDF/DOCX",
    type=["pdf", "docx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):
        document_text = read_pdf(
            uploaded_file
        )
    else:
        document_text = read_docx(
            uploaded_file
        )

    st.success(
        "Document loaded successfully"
    )

    if st.button(
        "Process Document"
    ):

        with st.spinner(
            "Building knowledge base..."
        ):

            create_vector_store(
                document_text
            )

            summary = summarize_document(
                document_text
            )

            doc_type = classify_document(
                document_text
            )

        st.subheader(
            "Document Type"
        )

        st.success(doc_type)

        st.subheader(
            "Summary"
        )

        st.markdown(summary)

    st.divider()

    st.subheader(
        "Chat With Document"
    )

    question = st.text_input(
        "Ask Question"
    )

    if st.button(
        "Get Answer"
    ):

        with st.spinner(
            "Searching document..."
        ):

            answer = ask_question(
                question
            )

        st.write(answer)