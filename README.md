# 🚀 Real-Time Process Monitoring Dashboard

## 📌 Overview
The **Real-Time Process Monitoring Dashboard** is a sleek and intuitive PyQt6-based GUI application designed to monitor system resource usage and manage running processes in real time. It provides dynamic visualizations for CPU, memory, and disk usage, along with an interactive process manager to search, view, and terminate processes effortlessly.

## 🎯 Features
✅ **Real-time System Monitoring**: Tracks CPU, memory, and disk usage with dynamic visual graphs.  
✅ **Process Management**: Displays active processes, sorted by CPU usage, with an instant search option.  
✅ **Process Termination**: Select and terminate processes directly from the interface.  
✅ **User-friendly Interface**: A modern dark-themed UI designed using PyQt6 with interactive elements.  

## 🛠️ Technologies Used
🔹 **Python 3**  
🔹 **PyQt6** – GUI Development  
🔹 **PyQtGraph** – Graphical plotting  
🔹 **Psutil** – System resource monitoring  

## ⚙️ Installation
### 📌 Prerequisites
Ensure you have Python installed. Download it from [python.org](https://www.python.org/).

### 📥 Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/realtime-process-monitor.git
   cd realtime-process-monitor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## 📂 Project Structure
```
realtime-process-monitor/
│-- main.py             # Entry point for the application
│-- system_info.py      # Handles system monitoring and process management
│-- ui.py               # Defines the GUI layout and interactions
│-- requirements.txt    # List of dependencies
│-- README.md           # Project documentation
```

## 📊 Usage
🎯 **Monitor System Usage**: Launch the application to view real-time CPU, memory, and disk statistics.  
🎯 **Manage Processes**:
- Use the search bar to filter processes.
- Click on a process to select it.
- Press the **Kill Process** button to terminate it.  

## 🤝 Contributing
Contributions are welcome! If you find a bug or have an enhancement idea:
1. **Fork** the repository.
2. **Create a new branch** (`feature-new-feature` or `bugfix-description`).
3. **Commit your changes**.
4. **Open a pull request**.

## 📜 License
This project is licensed under the **Apache License**. See the `LICENSE` file for details.

🚀 Happy Monitoring! 🎯

