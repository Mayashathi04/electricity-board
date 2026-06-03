# ⚡ Electricity Board Connection Hub

A sleek, full-stack utility management console designed to streamline the tracking, provisioning, and regulation of power distribution lines. Built with a modern glassmorphic dark-theme user interface, this dashboard allows grid administrators to allocate power lines across different customer sectors, monitor peak kilowatt loads, and dynamically toggle active grid supply lines.

🌐 **Live Deployment Link:** [Click Here to View the Live App](https://electricity-board-ge2p.onrender.com)

---

## ✨ Features
* **Modern UI/UX:** Stunning dark-mode dashboard styled with Glassmorphism properties (backdrop-blur filters, subtle semi-transparent borders).
* **Grid Capacity Tracking:** Easily register consumer details, categorize connection tiers, and allocate precise capacity loads in kilowatts (kW).
* **Real-time State Management:** Toggle live grid distribution lines instantly between `ACTIVE` and `SUSPENDED` line states with automatic visual feedback.
* **Persistent Storage:** Fully integrated with an underlying SQL database to ensure your records persist through refreshes.
* **Responsive Architecture:** Built utilizing flexible layout systems (CSS Grid and Flexbox) to seamlessly adapt to different screen dimensions.

---

## 🛠️ Technology Stack Breakdown

* **Frontend View Layer:** HTML5, CSS3 (Modern Flexbox/Grid layouts), JavaScript (ES6+ Fetch API)
* **Backend Application Server:** Python 3, Flask Micro-framework
* **Database Management Engine:** SQLite3 Relational Engine
* **Production Deployment:** Gunicorn Web Server hosted on Render Cloud Infrastructure

---

## 🚀 How to Run Locally

If you wish to clone this repository and run the application in a local development workspace, execute the following commands in your terminal:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mayashathi04/electricity-board.git](https://github.com/Mayashathi04/electricity-board.git)
   cd electricity-board