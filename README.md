# Flight Search Application

This repository contains a simple Python application for searching flights, along with a BDD test suite using Behave and Allure reporting.

## Application

The `app.py` file contains a `FlightSearch` class that simulates searching through a predefined list of flights based on origin, destination, and maximum price. It also allows checking flight availability and retrieving flight details by ID.

## BDD Tests (Behave)

The BDD tests are located in the `features/` directory:

*   `flight_search.feature`: Contains scenarios written in Gherkin syntax describing how the flight search functionality should behave.
*   `features/steps/flight_search_steps.py`: Contains the Python code (step definitions) that implements the steps defined in the feature file.

### Tags

Scenarios are tagged for selective execution:

*   `@sanity`: Critical, fast-running checks.
*   `@critical`: Tests covering the most important functionality.
*   `@edgecase`: Tests for boundary conditions.
*   `@negative`: Tests for invalid inputs or expected failures.

## Running Tests Locally

1.  **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Behave tests:**
    ```bash
    behave features/
    ```

4.  **Run specific tags:**
    ```bash
    behave --tags=@sanity features/
    behave --tags="@critical and not @sanity" features/
    ```

## Allure Reporting

This project is configured to generate Allure reports.

1.  **Run tests with the Allure formatter:**
    ```bash
    behave -f allure_behave.formatter:AllureFormatter -o allure-results features/
    ```
    This command generates JSON results in the `allure-results/` directory.

2.  **Generate and view the HTML report:**
    You need to have Allure command-line tool installed. See [Allure Framework documentation](https://docs.qameta.io/allure/#_installing_a_commandline) for installation instructions.
    ```bash
    allure serve allure-results/
    ```
    This command will generate the report and open it in your default web browser.

## GitHub Actions

A GitHub Actions workflow is defined in `.github/workflows/run-tests.yml`. This workflow automatically:

*   Checks out the code.
*   Sets up Python.
*   Installs dependencies.
*   Runs the Behave tests using the Allure formatter on every push and pull request to the `main` or `master` branch.
*   Uploads the `allure-results/` directory as a build artifact named `allure-results-flight-search`.

You can download the artifact from the Actions tab in the GitHub repository to generate the report locally using the `allure serve` command mentioned above.

