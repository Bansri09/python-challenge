# **Python Challenge - PyBank & PyPoll**

## **Overview**

This challenge includes two Python tasks: **PyBank** and **PyPoll**. Both tasks are designed to help you practice your Python scripting skills by solving real-world problems involving financial analysis and vote-counting automation.

- **PyBank**: Analyze a company’s financial records to compute various financial metrics.
- **PyPoll**: Analyze a set of election data to determine the total votes, the distribution of votes among candidates, and the winner.

---

## **Challenge Structure**

The challenge is organized into two main folders, one for each task:

- **PyBank**: Folder containing the Python script and resources for the financial analysis.
- **PyPoll**: Folder containing the Python script and resources for the election data analysis.

Each folder should have the following structure:
- `main.py`: The Python script that performs the analysis.
- `Resources/`: A folder containing the dataset CSV files used for the analysis.
- `Analysis/`: A folder containing the output text file with the results.

---

## **How to Use**

1. **Clone the Repository:**
   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/python-challenge.git


2. **Navigate to the Appropriate Folder**

    To navigate to the folder of the challenge you want to run (either **PyBank** or **PyPoll**), use the following commands:

    ```bash
    cd python-challenge/PyBank
    ```

    or

    ```bash
    cd python-challenge/PyPoll
    ```

3. **Run the Python Script**

    Make sure Python is installed on your machine. To run the Python script, use the following command:

    ```bash
    python main.py
    ```

3. **View the Results**

    The script will print the analysis to the terminal and generate a text file in the `Analysis/` folder containing the same results.

---

## PyBank - Financial Analysis

In this challenge, you are tasked with analyzing a financial dataset (`budget_data.csv`). The dataset contains two columns: **Date** and **Profit/Losses**.

### Objectives

Your goal is to create a Python script that calculates the following:

- The total number of months included in the dataset.
- The net total amount of "Profit/Losses" over the entire period.
- The changes in "Profit/Losses" over the entire period, along with the average of those changes.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in profits (date and amount) over the entire period.

### Sample Results

```plaintext
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
