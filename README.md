## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Meghana-Poojary/ChatWithSQL.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the SQLite database

Run the following command to generate `student.db`:

```bash
python sqlite.py
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

### 5. Add your Groq API key

Enter your Groq API key in the Streamlit sidebar to start querying the database.
