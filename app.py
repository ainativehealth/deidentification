import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_model():
    return pipeline("token-classification", model="StanfordAIMI/stanford-deidentifier-base")

def deidentify_text(text, pipe):
    # Use the pipeline to get classifications
    classifications = pipe(text)

    # Sort classifications in reverse order to avoid index shifting
    sorted_classifications = sorted(classifications, key=lambda x: x['start'], reverse=True)

    # Convert text to list of characters for easier manipulation
    text_chars = list(text)
    
    # Replace identified entities with placeholders
    for item in sorted_classifications:
        start = item['start']
        end = item['end']
        entity = item['entity']
        text_chars[start:end] = f"[{entity}]"
    
    # Join the characters back into a string
    redacted_text = ''.join(text_chars)

    return redacted_text

def main():
    st.title("Patient Data De-identification Tool")

    # Load model (cached to avoid reloading)
    model = load_model()

    # Text input for patient data
    patient_data = st.text_area("Enter patient data:", height=150)

    if st.button("De-identify"):
        if patient_data:
            with st.spinner("De-identifying..."):
                de_identified_data = deidentify_text(patient_data, model)
            st.text_area("De-identified data:", value=de_identified_data, height=150)
        else:
            st.warning("Please enter some patient data.")

    st.caption("Note: All processing is done locally. No data is stored or transmitted.")

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 10px;">
            <p>Developed by AINative Health</p>
            <a href="mailto:keith@ainativehealth.com" target="_blank" style="margin: 0 10px;">Email</a>
            <a href="https://github.com/ainativehealth" target="_blank" style="margin: 0 10px;">GitHub</a>
            <a href="https://www.linkedin.com/company/ainativehealth" target="_blank" style="margin: 0 10px;">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()