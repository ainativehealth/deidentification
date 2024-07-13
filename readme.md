# Local Patient Data De-identification Tool

## Overview

This tool is built by AINative Health using the StanfordAIMI/stanford-deidentifier-base model. It's designed to help doctors perform de-identification of patient data locally on their machines. The underlying model is based on the work from the [Stanford_Penn_MIDRC_Deidentifier](https://github.com/MIDRC/Stanford_Penn_MIDRC_Deidentifier) project.

## Features

- Local de-identification: All processing is done on your local machine, ensuring data privacy.
- Offline capability: Once the model is loaded, the tool can be used without an internet connection.
- User-friendly interface: Built with Streamlit for easy interaction.
- Efficient processing: Utilizes caching to improve performance.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/local-patient-data-deidentification.git
   cd local-patient-data-deidentification
   ```


2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate # On Windows, use venv\Scripts\activate
   ```


3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

3. The wait for the model to be downloaded.

5. Enter the patient data you want to de-identify in the text area.

5. Click the "De-identify" button to process the text.

6. The de-identified text will appear in a new text area below.

## Privacy and Security

- All processing is done locally on your machine.
- No data is stored or transmitted over the internet.
- The app is configured to disable telemetry and usage statistics collection.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

## Support and Inquiries

For support or inquiries, please contact Keith at keith@ainativehealth.com.

## Acknowledgments

This project utilizes the StanfordAIMI/stanford-deidentifier-base model, which is based on work from the Stanford_Penn_MIDRC_Deidentifier project. We are grateful for their contributions to the field of medical data de-identification.

## Disclaimer

This tool is intended for research and educational purposes only. While it aims to provide accurate de-identification, it should not be solely relied upon for ensuring patient privacy in clinical or production environments without proper validation.