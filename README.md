# Golden Raspberry Awards API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-2.3.3-green)
![License](https://img.shields.io/badge/license-MIT-orange)

A professional RESTful API service built with Flask that provides comprehensive information about the Golden Raspberry Awards, specifically the "Worst Picture" category. The API enables easy access to historical award data, including winners, statistics, and producer analytics.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Technical Details](#technical-details)

---

## 🎯 Overview

The Golden Raspberry Awards API is a RESTful service that processes and displays information related to the Golden Raspberry Awards "Worst Picture" category. Built following Richardson Maturity Model Level 2, it provides a clean, resource-oriented interface for querying award data.

## ✨ Features

- **Movie Search by Year**: Query all movies nominated in a specific year
- **Winner Listing**: Retrieve all award-winning movies
- **Multiple Winners Analysis**: Identify years with multiple winners
- **Producer Interval Analysis**: Find producers with the longest and shortest intervals between consecutive wins
- **In-Memory Database**: Fast SQLite database loaded from CSV for optimal performance
- **Comprehensive Testing**: Full test coverage with pytest
- **RESTful Design**: Clean, intuitive API endpoints following REST principles

## 📋 Requirements

- **Python**: Version 3.8 or higher (tested with 3.12)
- **pip**: Python package manager
- **Dependencies**:
  - Flask 2.3.3
  - pandas 1.5.3
  - pytest (for testing)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/httpEduardo/Backend.git
cd Backend
```

### 2. Create a Virtual Environment

Create an isolated Python environment for the project:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

The API uses an in-memory SQLite database initialized from the `Movielist.csv` file. 

**Important**: Ensure the `Movielist.csv` file is present in the project root directory. The CSV should contain the following columns:
- `year`: Year of the award
- `title`: Movie title
- `studios`: Production studio(s)
- `producers`: Producer name(s)
- `winner`: "yes" for winners, empty for nominees

## 🏃 Running the API

Start the development server:

```bash
python run.py
```

The API will be available at:
```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 1. Get Movies by Year

Retrieve all movies from a specific year.

**Endpoint:** `GET /api/movies/<year>`

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/movies/1980
```

**Example Response:**
```json
[
  {
    "id": 1,
    "year": 1980,
    "title": "Can't Stop the Music",
    "studios": "Associated Film Distribution",
    "producers": "Allan Carr",
    "winner": true
  },
  {
    "id": 2,
    "year": 1980,
    "title": "Cruising",
    "studios": "Lorimar Productions, United Artists",
    "producers": "Jerry Weintraub",
    "winner": false
  }
]
```

---

### 2. List Winner Movies

Retrieve all movies that won the award.

**Endpoint:** `GET /api/movies/winners`

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/movies/winners
```

**Example Response:**
```json
[
  {
    "id": 1,
    "year": 1980,
    "title": "Can't Stop the Music",
    "studios": "Associated Film Distribution",
    "producers": "Allan Carr",
    "winner": true
  },
  {
    "id": 5,
    "year": 1981,
    "title": "Mommie Dearest",
    "studios": "Paramount Pictures",
    "producers": "Frank Yablans",
    "winner": true
  }
]
```

---

### 3. Years with Multiple Winners

Retrieve years that had more than one winner.

**Endpoint:** `GET /api/movies/multiple-winners`

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/movies/multiple-winners
```

**Example Response:**
```json
[
  {
    "year": 1986,
    "win_count": 2
  },
  {
    "year": 1990,
    "win_count": 2
  }
]
```

---

### 4. Producer Award Intervals

Retrieve the producer with the longest and shortest interval between consecutive awards.

**Endpoint:** `GET /api/movies/intervals`

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/movies/intervals
```

**Example Response:**
```json
{
  "maximum": {
    "producer": "Matthew Vaughn",
    "interval": 13,
    "first_year": 2002,
    "last_year": 2015
  },
  "minimum": {
    "producer": "Joel Silver",
    "interval": 1,
    "first_year": 1990,
    "last_year": 1991
  }
}
```

---

## 🧪 Testing

The API includes comprehensive integration tests using pytest.

### Running Tests

Ensure your virtual environment is active, then run:

```bash
pytest
```

### Expected Output

```
============================= test session starts ==============================
collected 5 items

tests/test_app.py .....                                               [100%]

============================== 5 passed in 0.45s ===============================
```

### Test Coverage

The test suite covers:
- Movie retrieval by year
- Winner movie listing
- Multiple winners per year
- Producer interval calculations
- Error handling for invalid routes

---

## ⚠️ Error Handling

The API provides clear error messages for various scenarios:

### 404 - Not Found

**Scenario 1: Invalid Route**

```bash
curl -X GET http://127.0.0.1:5000/api/invalid-route
```

**Response:**
```json
{
  "error": "Route not found"
}
```

**Scenario 2: No Data Found**

```bash
curl -X GET http://127.0.0.1:5000/api/movies/1900
```

**Response:**
```json
{
  "error": "No movies found for the specified year."
}
```

---

## 🔧 Technical Details

### Architecture

- **Framework**: Flask 2.3.3
- **Database**: SQLite (in-memory)
- **Data Processing**: pandas 1.5.3
- **Maturity Model**: Richardson Maturity Model Level 2
  - Uses proper HTTP methods
  - Resource-based URLs
  - Structured JSON responses

### Project Structure

```
.
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── app.py               # Application logic and endpoints
│   └── routes.py            # Route registration
├── tests/
│   └── test_app.py          # Integration tests
├── config.py                # Configuration settings
├── database.py              # Database initialization
├── run.py                   # Application entry point
├── Movielist.csv            # Award data source
└── requirements.txt         # Python dependencies
```

### Database Schema

```sql
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    title TEXT,
    studios TEXT,
    producers TEXT,
    winner BOOLEAN
)
```

---

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.