# HyreNet Platform - Automation Testing (GUVI BugAthon)

This project is a dedicated Automation Testing framework built to identify bugs and validate functionalities on the HyreNet platform as part of the GUVI & HCL Career Carnival.

## 🚀 Project Overview
- *Goal:* To automate the login process and validate the Template/Report dashboard.
- *Tools Used:* Python, Selenium WebDriver, Pytest, and Pytest-HTML for reporting.
- *Bug Discovery:* Successfully identified UI alignment issues in CSV reports and performance-related timeout bugs during automation.

## 📁 Project Structure
- tests/: Contains the test scripts (Login and Dashboard validation).
- pages/: Implements the Page Object Model (POM) for better code maintainability.
- reports/: Stores the execution evidence.
- HyreNet_BugAthon_Report_Thendralarasu.xlsx: Detailed manual and automation test case report.
- final_report.html: Interactive automation execution report.

## 🐞 Bugs Found
1. *CSV Alignment Issue:* Downloaded leaderboard data columns are misaligned.
2. *Performance Timeout:* Sign-In button interaction takes longer than expected, causing automation timeouts.

## 🛠️ How to Run
1. Install dependencies: pip install -r requirements.txt
2. Run tests: python -m pytest tests/test_login.py --html=final_report.html
