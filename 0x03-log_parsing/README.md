# Log Parsing Project

## Overview

This project involves parsing and analyzing log data stored in a MongoDB database. The main script, `12-log_stats.py`, connects to the `logs` database, retrieves statistics from the `nginx` collection, and prints various pieces of information, including the number of logs, method counts, status checks, and the top 10 most present IP addresses.

## Requirements

- Python 3.x
- MongoDB 4.2+
- PyMongo library

## Setup

1. **Install MongoDB**: Follow the instructions to install MongoDB from the official [MongoDB documentation](https://docs.mongodb.com/manual/installation/).
2. **Install PyMongo**: Use pip to install the PyMongo library.

   ```bash
   pip install pymongo

