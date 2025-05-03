# IAgroscan - AI-Powered Plant Disease Detection

IAgroscan is an advanced machine learning application designed to detect and identify plant diseases in agricultural crops. Using computer vision and AI, it helps farmers and agricultural specialists quickly diagnose crop health issues.

## 🌱 Features

- **Single Image Detection**: Analyze individual plant images for disease identification
- **Batch Detection**: Process multiple images at once for large-scale assessment
- **Detailed Reports**: Generate comprehensive PDF reports with detection statistics
- **AI-Powered Recommendations**: Receive treatment and prevention advice for detected diseases
- **Data Visualization**: View detection statistics through intuitive charts and graphs
- **Detection History**: Access past detection records for tracking disease patterns

## 🔍 Supported Crops & Diseases

IAgroscan can detect various diseases across multiple crops:

- **Sugarcane**: Yellow Spot (Mycovellosiella koepkei), Red Rot
- **Corn**: Gray Leaf Spot, Rust, Leaf Blight
- **Banana**: Cordana, Pestalotiopsis, Sigatoka

## 💻 Technical Overview

IAgroscan is built with:
- **YOLO (You Only Look Once)**: For rapid, accurate object detection
- **CustomTkinter**: Modern UI framework for desktop application
- **OpenAI Integration**: For generating detailed disease management recommendations
- **Matplotlib**: For statistical visualization of detection results
- **PyMySQL**: For database management of detection records

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Required packages:
  ```
  customtkinter
  pymysql
  pillow
  ultralytics
  reportlab
  matplotlib
  openai
  ```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/MateoVR13/IAgroscan.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your database connection in `connection.py`

4. Add your OpenAI API key in the appropriate section of the code

5. Run the application:
   ```
   python mainWindow.py
   ```

## 📊 How It Works

1. **Select an image** or folder of images containing plant specimens
2. **AI model processes** the images to detect diseases
3. **Review results** displayed directly in the application
4. **Generate reports** with detection statistics and treatment recommendations
5. **Track disease patterns** over time with the built-in database

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- The YOLO model was trained on a custom dataset of agricultural plant diseases
- Special thanks to agricultural specialists who provided expertise for the training data
