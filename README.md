# Internet-Speed-Test-
Internet Speed Test using python
This project is a graphical desktop application for testing internet speed using Python and the Tkinter GUI framework. The app measures download speed, upload speed, ping, and displays additional details such as the user's ISP and IP address.

Features:
--Download Speed: Measures and displays download speed in Mbps.
--Upload Speed: Measures and displays upload speed in Mbps.
--Ping: Displays latency in milliseconds.
--ISP Information: Displays the name of the Internet Service Provider.
--IP Address: Shows the user's current public IP address.
--Graphical Interface: Interactive and visually appealing design with buttons for starting the test and resetting the results.


Requirements
-To run the project, you need to have the following installed:
--Python 3.6+
--Tkinter: Comes pre-installed with Python.
--speedtest-cli: A library for running speed tests.
--Install speedtest-cli via pip: pip install speedtest-cli
How to Run the Project
Clone the Repository or Download the Code: Ensure you have all the required files, including the Python script and image assets.

Install Dependencies: Run the following command to install the required library

--pip install speedtest-cli
Update File Paths: Update the file paths in the script for the images (logo, background, buttons) to match your system's directory structure.

Run the Application: Execute the script: python speed_test.py
Use the App:
--Click the Test button to start the internet speed test.
--Click the Reset button to clear the results and reset the app interface.

Folder Structure
Internet Speed Test/
├── images/
│   ├── logo.png          # Application icon
│   ├── background3.png   # Background image
│   ├── button.png        # Test button image
│   ├── reset.png         # Reset button image
├── speed_test.py         # Main Python script
├── README.md             # Documentation

Application Workflow
Start Test: Clicking the Test button runs a speed test using the speedtest library in a separate thread to avoid freezing the UI.
Display Results: Once the test is complete, results are displayed for download, upload, ping, ISP, and IP address.
Reset Results: Clicking the Reset button clears all displayed results.

Troubleshooting
No Results or Errors: Ensure you have a stable internet connection and the speedtest-cli library is installed.
Images Not Loading: Check the file paths for the image files in the script and make sure they are correct.
Future Enhancements
Save Results: Add functionality to save the results in a text or CSV file.
Advanced Visuals: Use additional libraries like matplotlib or Tkinter Canvas for graphical representation.
Cross-Platform Support: Improve UI scaling for better usability across various screen sizes.

License
This project is free to use and distribute under the MIT License.

Author
Developed by Kumara Ayyappan V
Student at Chennai Institute of Technology, Chennai, Tamil Nadu, India.

Enjoy testing your internet speed! 🚀
