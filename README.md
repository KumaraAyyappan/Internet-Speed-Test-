# 🌐 Internet Speed Test Application 🚀

Welcome to the Internet Speed Test Application! This project is a graphical desktop application that tests your internet speed using Python and Tkinter. It measures download speed, upload speed, ping, and displays additional details like your ISP and IP address.

## 🎯 Project Objectives
- *Measure Internet Speed:* Test the download speed, upload speed, and ping of your internet connection.
- *Visualize Results:* Display speed test results in a user-friendly interface.
- *Error Handling:* Handle errors such as connectivity issues and display appropriate messages.

## 🚀 Features
- *Download Speed:* Displays the download speed in Mbps.
- *Upload Speed:* Displays the upload speed in Mbps.
- *Ping:* Displays the latency in milliseconds.
- *ISP Information:* Displays the name of the Internet Service Provider (ISP).
- *IP Address:* Displays the user's public IP address.
- *Graphical User Interface (GUI):* Built using Tkinter, the application features buttons for starting the test and resetting the results.

## 🛠 Installation Instructions

1. *Clone the Repository*
   ```bash
   git clone https://github.com/yourusername/internet-speed-test.git
   cd internet-speed-test
2. *Install Required Libraries*
   ```bash
    pip install speedtest-cli
3. *Run the Application*
   ```bash
   python speed_test.py
## 🧠 How It Works
The application uses the speedtest-cli library to measure the internet speed. Upon clicking the Test button, it runs a speed test and fetches the following results:

- Download speed (in Mbps)
- Upload speed (in Mbps)
- Ping (in milliseconds)
- ISP (Internet Service Provider)
- Public IP address

- The results are then displayed in the GUI. The user can reset the results by clicking the Reset button.

## 📊 Dashboard Overview
*Key Features:*

- *Download Speed:* Displayed in the middle of the screen, in Mbps.
- *Upload Speed:* Displayed in a similar manner, indicating the upload speed in Mbps.
- *Ping:* Displays the ping value to give users an idea of their internet connection's responsiveness.
- *ISP and IP Address:* Shows the user's ISP name and public IP address.

## 🚀 Future Enhancements
To make this project more robust, we suggest the following additions:

- *Multiple Server Selection:* Allow users to select a server for testing internet speed based on their region.
- *Speed History:* Maintain a history of speed test results over time.
- *Graphical Visualization:* Implement graphs and charts to visualize the speed test results.
- *Improved Error Handling:* Enhance error handling to cover more edge cases (e.g., network issues).

## 📁 Project Structure
Here's a quick overview of the files in this repository:

- *images/:* Contains the image assets used for the GUI (icons, buttons, backgrounds).
- *speed_test.py:* The main Python script that launches the internet speed test application.
- *README.md:* This documentation file.

## 📚 Dataset/Dependencies
The project relies on the following library:

- *speedtest-cli:* A command-line interface for testing internet bandwidth.

To install the required dependency, run the following command:


-by Kumara Ayyappan V





  
  
  
