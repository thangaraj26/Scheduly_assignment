# Scheduly_assignment

This Repo Contains FLASK API  to extract Information about meeting from sentence.
(i.e) participants, date, time, and agenda




# Documentation

## Step 1:
### Enable venv before running the scripts
For MAC/Linux , terminal
`$ source bin/activate`
For Windows , cmd
`> source/activate.ps1`

### installing the requirements

`pip install -r requirements.txt`

The repo have Third party like [spacy](https://github.com/explosion/spaCy) and [snips-nlu-parser](https://github.com/snipsco/snips-nlu-parsers/tree/master/python)

**Make sure you installed the packages correctly before run the script.**


## Usage - API

RUN `$ python main.py`

Test with Postman or other API Development Platform

URL =  `http://127.0.0.1:5000/api/v1/schedule`

(Pass it in the request body)

Example Input: 
1. Schedule a meeting next week between John, Mary, and Jane to discuss the new product launch. We'll need 1 hour.
2. Schedule a meeting next Wednesday with Alex and Jim to discuss the new marketing campaign. We'll need 2 hours.

Example Output:

 ``` javascript
1.
{
    "status": true,
    "participants": [
        "John",
        "Mary",
        "Jane"
    ],
    "agenda": "new product launch.",
    "date": {
        "kind": "InstantTime",
        "value": "2023-03-13 00:00:00 +05:30",
        "grain": "Week",
        "precision": "Exact"
    },
    "time": {
        "kind": "Duration",
        "years": 0,
        "quarters": 0,
        "months": 0,
        "weeks": 0,
        "days": 0,
        "hours": 1,
        "minutes": 0,
        "seconds": 0,
        "precision": "Exact"
    }
}

2. 

 {
    "status": true,
    "participants": [
        "Alex",
        "Jim"
    ],
    "agenda": "new marketing campaign.",
    "date": {
        "kind": "InstantTime",
        "value": "2023-03-15 00:00:00 +05:30",
        "grain": "Day",
        "precision": "Exact"
    },
    "time": {
        "kind": "Duration",
        "years": 0,
        "quarters": 0,
        "months": 0,
        "weeks": 0,
        "days": 0,
        "hours": 2,
        "minutes": 0,
        "seconds": 0,
        "precision": "Exact"
    }
}
