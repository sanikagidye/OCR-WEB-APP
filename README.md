# OCR-WEB-APP


## Project Overview

This project is a web-based prototype that allows users to upload an image (in formats like JPEG, PNG) containing text in **Hindi** and **English**. It performs Optical Character Recognition (OCR) on the uploaded image to extract text and provides a keyword search functionality to highlight words within the extracted text. The application is built using **Streamlit** for the web interface and **Pytesseract** for OCR, and is deployed on a live platform for public access.

## Features

- Upload an image containing text in **Hindi** and **English**.
- Extract and display the text using **Tesseract OCR**.
- Perform a keyword search within the extracted text.
- Simple and intuitive **Streamlit** interface.
- Deployed online and accessible via a live URL.

## Technologies Used

- **Streamlit**: For creating the web application interface.
- **Pytesseract**: Python wrapper for Google Tesseract OCR to extract text.
- **OpenCV**: For image processing.
- **Pillow**: For handling image uploads and manipulations.
- **Tesseract OCR**: For text extraction in Hindi and English.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sanikagidye/ocr-web-app.git
cd ocr-web-app
```

### 2. Install Python Dependencies
Create a virtual environment (optional but recommended) and install dependencies from `requirements.txt`.

```bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Install Tesseract-OCR
For local development, you need to have Tesseract-OCR installed on your system. Installation instructions depend on your operating system:

- **Windows**:
  - Download and install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract).
  - Add the path to the Tesseract installation folder (e.g., `C:/Program Files/Tesseract-OCR/`) to your system's `PATH`.

- **Linux** (Ubuntu/Debian):
  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr
  sudo apt-get install tesseract-ocr-hin
  ```


### 4. Run the Application Locally
Once all dependencies and Tesseract are installed, you can run the application using Streamlit:

```bash
streamlit run ocr_app.py
```

Open a browser and navigate to `http://localhost:8501` to view the app.

## Project Structure

```bash
ocr-web-app/
│
├── ocr_app.py              # Main Python script for the OCR web application
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level dependencies (Tesseract)
└── README.md               # Project documentation
```

## Deployment

### Deploy on **Streamlit Cloud**
To deploy the app on Streamlit Cloud, follow these steps:

1. **Push the code to GitHub**:
   Ensure that both `requirements.txt` and `packages.txt` are in the repository.

2. **Log in to Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud).
   - Sign in using your GitHub account.

3. **Deploy the app**:
   - Click on "New App" and select your GitHub repository.
   - Set the branch (usually `main`) and the file path to `ocr_app.py`.
   - Click "Deploy".

4. **Access your deployed app**:
   After deployment, Streamlit will provide a live URL where the app is accessible.

### Deploy on **Hugging Face Spaces**
1. **Create a new space** on Hugging Face by selecting the **Streamlit** framework.
2. **Push your code** to the repository provided by Hugging Face.
3. Hugging Face will automatically deploy your app.

## Usage

### Uploading an Image
1. Visit the web app at the deployed URL.
2. Upload an image containing Hindi and/or English text.
3. Click "Process" to extract text from the image.

### Searching Keywords
1. After text extraction, input a keyword in the search bar.
2. The app will highlight the occurrences of the keyword within the extracted text.

## Troubleshooting

### TesseractNotFoundError
If you encounter a `TesseractNotFoundError`, ensure that:
- **Tesseract-OCR** is installed on your system.
- The path to Tesseract is either added to the `PATH` environment variable or specified correctly in your code.

For deployment, ensure the `packages.txt` file is present, which will handle the installation of Tesseract on cloud platforms like Streamlit Cloud.


## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Streamlit](https://streamlit.io/)

