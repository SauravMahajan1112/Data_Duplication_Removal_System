# 📂 Cloud-Based Improved File Handling and Duplication Removal Using MD5

---

## 🗊 Overview
This project implements a **cloud-based file handling system** that optimizes storage and manages file duplication using **MD5 hashing**. Files are uploaded, verified for duplication, and stored efficiently to reduce redundancy. This solution enhances file management, ensures data uniqueness, and optimizes storage utilization.

---

## 🛠️ Features

- ✔️ **Duplicate Detection**: Uses MD5 hashing to detect and prevent duplicate file storage.
- ✔️ **User Authentication**: Supports secure user login and signup functionality.
- ✔️ **File Management**: Upload, download, and delete files with ease.
- ✔️ **Similarity Analysis**: Compares uploaded files for similarity and provides detailed metrics.
- ✔️ **Visualization**: Displays similarity analysis using pie charts.
- ✔️ **Streamlit Integration**: Provides an interactive UI for file handling and operations.

---

## 📚 Technologies Used

- **Python**: Programming language.
- **SQLite**: Database for storing user and file metadata.
- **Streamlit**: Framework for building the web application interface.
- **Matplotlib**: For visualization of file similarity metrics.
- **Hashlib**: For generating MD5 file hashes.
- **Pandas**: For data management and display.
- **OS Module**: For file system interactions.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8 or higher
- Streamlit library installed
- SQLite installed (comes bundled with Python)

### 📂 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/cloud-md5-file-handling.git
   cd cloud-md5-file-handling
   ```

2. **Set Up the Environment:**
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application:**
   ```bash
   streamlit run main.py
   ```

4. **Access the Application:**
   Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## 👍 Usage

1. Navigate to the **Home Page** to view project information.
2. Sign up for a new account or log in with existing credentials.
3. Upload files and check for duplicates:
   - Files with identical content will not be stored again.
   - Similar files are analyzed and compared.
4. Download or delete stored files as needed.
5. View file similarity metrics and visualizations.

---

## 🗊 Screenshots

### Login Page
![WhatsApp Image 2025-01-13 at 21 52 27_32b422c4](https://github.com/user-attachments/assets/27a53ffe-5574-439e-a13d-1f4ecb53465a)

### File Upload Success
![WhatsApp Image 2025-01-13 at 21 54 33_d5582e95](https://github.com/user-attachments/assets/090c3342-91a3-4981-85d5-823a1d65648c)


### Similarity Analysis

![WhatsApp Image 2025-01-13 at 21 56 41_abb25c2a](https://github.com/user-attachments/assets/47b77306-17b9-4305-b51a-ce60c2ba8324)

---

## 🎮 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---

## 🔖 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the **Streamlit** community for their support and tools.
- Special thanks to contributors who improve this project.

---

## 🔎 References

- [Python Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SQLite Documentation](https://sqlite.org/docs.html)

