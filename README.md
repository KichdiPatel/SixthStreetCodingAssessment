# AlphaVantage Python Library

This Python package provides a simple wrapper around the Alpha Vantage API to fetch and process daily stock data. It supports looking up OHLCV data for a given date, as well as finding the min/max prices over recent days.

Built as part of a coding assessment for Sixth Street.

## Viewing this repo

The alphavantage folder contains the code for the library. The examples folder contains an example of how to use this library. The tests folder contains test that were used for this library.

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/KichdiPatel/SixthStreetCodingAssessment.git
cd SixthStreetCodingAssessment
pip install -e .
```

## Discussion

### What compromises did you make due to time constraints?

Because of the time restraints I wasn't able to fully test out the library, and so I only was abe to test with few tickers. I also didn't get to fully understand the outputsize keyword, since that might be able to be used to better improve time complexity.

### How would you approach versioning of this library?

Since this is the first version I used 0.1.0. Which is using the MAJOR.MINOR.PATCH format. So, if large breaking changes are needed I would update MAJOR, for small, new features I would update MINOR, and PATCH is for bug fixes.

### How would we go about publishing this library?

To publish this library, we could use PyPi

### How would you design this if it was going to be a service rather than a library?

If this were a service, I would expose it as a REST API using FastAPI or Flask. There would need to be authentication via some API key and it would be have the three endpoints: lookup, min, max.

### Please include any other comments about your implementation.

I believe my implementation is a good first version. It uses a object oriented design where the AlphaVantage class takes in the API Key. There are some improvements that could be made, but it is functional and handles most edge cases.

### How much time did you spend on this exercise?

I spent the full two hours

### Please include any general feedback you have about the exercise.

I had a lot of fun with this exercise. It was an interesting problem to implement, especially as a library.
