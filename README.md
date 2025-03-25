![Screenshot (10)](https://github.com/user-attachments/assets/0de08dd1-c45c-42d9-b3b0-daa0375b657d)

![Screenshot (11)](https://github.com/user-attachments/assets/0266ce6b-f473-40f6-bc1d-59f09c02eba6)

![Screenshot (12)](https://github.com/user-attachments/assets/c208adb2-d241-466d-ba57-25a05886c5a4)

# 🤖 Seq2Seq Chatbot

A chatbot built using **TensorFlow, Keras, and Streamlit**, with a **Seq2Seq model** for generating responses. The model is dynamically downloaded from **Google Drive** during runtime.

---

## 📌 Features
- **Trained on a Seq2Seq model** for text-based chatbot responses.
- **Uses Google Drive to store the `.h5` model**, avoiding GitHub LFS limitations.
- **Built with Streamlit** for an interactive UI.
- **Maintains chat history** for better conversation flow.

---

## 🚀 Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/AbuZar-Ansarii/First_ChatBot.git
cd First_ChatBot
```

### **2. Create a Virtual Environment (Optional, but Recommended)**
```bash
python -m venv chatbot_env
source chatbot_env/bin/activate  # macOS/Linux
chatbot_env\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 📂 Downloading the Model Automatically
The chatbot **automatically downloads** the model from **Google Drive** if it's not present.

If you prefer manual download:
1. **Upload `seq2seq_chatbot.h5` to Google Drive**.
2. Get the **file ID** from the shareable link.
3. Update the `MODEL_FILE_ID` in `app.py`:
   ```python
   MODEL_FILE_ID = "your_google_drive_file_id"
   ```
4. Run the following command to manually download the model:
   ```bash
   python download_model.py
   ```

---

## 🛠 Running the Chatbot
Start the chatbot application using Streamlit:
```bash
streamlit run app.py
```

This will open a web interface where you can chat with the bot. 🤖💬

---

## 🎯 Deployment on Render
1. Push your repository to GitHub.
2. Deploy on **Render** by linking your GitHub repo.
3. Render will automatically install dependencies and download the model.
4. Your chatbot is now live! 🚀

---

## 📜 License
This project is open-source under the **MIT License**. Feel free to modify and enhance it!

---

### 📝 **Contributing**
If you'd like to contribute, fork the repository and submit a pull request with your improvements.

---

### 📩 **Contact**
For any questions or issues, feel free to reach out:
- GitHub: [AbuZar-Ansarii](https://github.com/AbuZar-Ansarii)

