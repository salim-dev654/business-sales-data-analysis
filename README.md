# Business Sales Data Analysis System

## Overview

This project is a command-line based Business Sales Data Analysis System built with Python and MariaDB.  
It simulates sales data management by inserting sample data, performing revenue calculations, and generating sales reports.

---

## Features

- Connects to MariaDB using Python's `mysql-connector-python` via Unix socket (optimized for Termux on Android).  
- Database setup automation: creates database and sales table if they don't exist.  
- Insert sample sales data with product details (name, category, quantity, price, sale date).  
- Analyze total revenue generated.  
- View revenue breakdown by product category.  
- Identify best-selling products by units sold.  
- Interactive command-line menu for ease of use.

---

## Technologies

- Python 3.12  
- MariaDB (MySQL)  
- mysql-connector-python  
- Termux (Android Linux environment)  

---

## Setup Instructions

### Prerequisites

- Termux installed on Android device.  
- Python, MariaDB, and Git installed inside Termux.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/salim-dev654/business-sales-data-analysis.git
   cd business-sales-data-analysis/src
