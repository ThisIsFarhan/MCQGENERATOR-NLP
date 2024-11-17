# Automated MCQs Generator Using NLP  

This project implements an **Automated MCQs Generator** using **Natural Language Processing (NLP)** techniques. Users can input text, and the system generates multiple-choice questions (MCQs) with options and correct answers. The project features an interactive **Streamlit-based user interface** for ease of use.  

---

## Features  

- **Automatic Question Generation**: Extracts key concepts from the input text to create meaningful multiple-choice questions.  
- **Distractor Options**: Generates plausible distractor options to accompany the correct answer.  
- **Streamlit Interface**: Interactive frontend for users to input text and view questions, options, and answers.  
- **Customizable Question Count**: Allows users to select the number of MCQs to be generated.  

---

## Code Structure  

### Backend: Question Generator  

The core logic for generating MCQs is implemented in the `generator.py` file. It:  
1. **Preprocesses Text**: Removes stop words, punctuation, and lemmatizes tokens using SpaCy.  
2. **Extracts Keywords**: Uses **TF-IDF Vectorizer** to identify the most significant terms in the text.  
3. **Generates Questions**:  
   - Replaces keywords with blanks in relevant sentences.  
   - Creates distractor options using unrelated keywords.  
   - Randomizes the order of options.  

### Frontend: Streamlit Application  

The **Streamlit app** (`app.py`) provides an interface for generating MCQs. Features include:  
- **Text Input**: Users can enter the text they want to generate MCQs from.  
- **Slider**: Adjust the number of MCQs to generate (1–8).  
- **Question Display**: Generated questions, options, and correct answers are displayed interactively.  

---

## Installation  

### Prerequisites  

- Python 3.8+  
- Required Python libraries:  
  - `streamlit`  
  - `spacy`  
  - `numpy`  
  - `scikit-learn`  

### Steps  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ThisIsFarhan/MCQGENERATOR-NLP.git
   cd automated-mcq-generator
