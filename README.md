# Cybersecurity Risk Detector

## Overview
This project was developed as part of a machine learning assignment to build a **Cybersecurity Risk Detector**. The aim was to classify and detect potential cybersecurity threats using custom-generated datasets and machine learning algorithms. The project culminates in a local web application for real-time risk prediction.

## Project Requirements and Implementation
### Problem Selection
The project tackles a classification problem to determine the presence or absence of cybersecurity risks. The dataset was custom-generated using Python and saved as `veri.csv`.

### Implementation Steps
1. **Dataset Creation:**
   - Generated synthetic data (`veri.csv`) using Python and stored the code in `veri.ipynb`.
2. **Model Training:**
   - Trained the dataset using 10 different machine learning algorithms.
   - Selected the best-performing algorithm based on Accuracy.
   - Saved the best model as `eniyi.joblib`.
3. **Web Application Development:**
   - Designed a local web application using Streamlit.
   - Integrated the trained model (`eniyi.joblib`) for real-time predictions.
4. **Project Demonstration:**
   - A demonstration video link showcasing the working application is provided in `link.text`.

## Features
- Custom dataset generation.
- Evaluation of multiple ML algorithms.
- Streamlit-based web application for risk detection.
- Best model saved for reuse.

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - Scikit-learn (ML algorithms)
  - Pandas, NumPy (data processing)
  - Matplotlib (visualization)
  - Streamlit (web application)
- **Model Serialization:** joblib
- **Version Control:** Git

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dirshaye/Cybersecurity_Risk_Detector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dirshaye-cyber_security_risk_detector
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure the dataset (`veri.csv`) is in the root directory.
2. To train models and select the best one:
   ```bash
   python app.py
   ```
3. Launch the web application:
   ```bash
   streamlit run app.py
   ```
4. Access the application in your browser and test predictions.

## Project Structure
```
└── dirshaye-cyber_security_risk_detector/
    ├── algoritma.ipynb     # Notebook for evaluating algorithms
    ├── app.py              # Streamlit application script
    ├── eniyi.joblib        # Best-performing ML model
    ├── link.text           # Video demonstration link
    ├── veri.csv            # Generated dataset
    └── veri.ipynb          # Notebook for dataset generation
```

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or feedback, feel free to reach out:
- GitHub: [dirshaye](https://github.com/dirshaye)
