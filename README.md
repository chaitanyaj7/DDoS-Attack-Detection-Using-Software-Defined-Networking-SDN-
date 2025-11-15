🛡️ Distributed Denial of Service (DDoS) Attack Detection Using Machine Learning in SDN

Duration: Oct 2025 – Nov 2025
Objective: Detect and mitigate DDoS attacks in Software Defined Networking (SDN) environments using Machine Learning.

This project focuses on enhancing network security by identifying abnormal traffic patterns and responding to DDoS attacks in real time. Using ML models such as Support Vector Machines (SVM) and Decision Trees, the system classifies network traffic into attack or normal categories to improve early detection and mitigation.

🚀 Project Overview

DDoS attacks aim to disrupt network services by overwhelming the network with excessive traffic.
In SDN, centralized controllers help monitor and manage traffic efficiently—making SDN ideal for ML‑based DDoS detection.

This project integrates:

Traffic collection from SDN controller

Feature extraction from network metrics

Machine learning classification

Real-time attack detection & mitigation

🧰 Technologies Used

Machine Learning

Support Vector Machines (SVM)

Decision Trees

Software Defined Networking (SDN)

OpenFlow (controller–switch communication)

Python

🎯 Key Achievements

Implemented SVM to establish an optimal decision boundary between attack and non‑attack traffic.

Built Decision Tree models to analyze network features and improve classification accuracy.

Enhanced overall DDoS detection accuracy and response time in SDN.
⚙️ How the System Works
1️⃣ Data Collection

Network flow statistics collected from SDN controller

Extracted attributes like packet count, flow duration, source/destination IP, etc.

2️⃣ Preprocessing

Removed missing values

Normalized feature values

Encoded labels (attack / normal)

3️⃣ Model Training

Trained two ML models:

SVM: to find the best hyperplane separating attack vs. normal instances

Decision Tree: to model decisions based on flow-level features

4️⃣ Real-Time Detection

Incoming traffic is classified using trained models

Attackers are automatically blocked using flow rules

📊 Results

✔ Improved accuracy in identifying DDoS attacks
✔ Faster detection time due to SDN’s centralized visibility
✔ ML models successfully differentiated attack vs. normal traffic
✔ Decision Tree helped interpret important network features contributing to attacks

(Add actual accuracy values once your training results are final.)

📌 Future Enhancements

Integrate Deep Learning models (LSTM/CNN)

Experiment with additional SDN controllers (ONOS, OpenDaylight)

Implement multi-class attack detection

Deploy on real hardware switches

🧑‍💻 Author

Chaitanya Jamdar
Machine Learning & SDN Researcher
