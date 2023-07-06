<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Neighbors Dog Park" />


  &#xa0;

  <!-- <a href="https://neighborsdogpark.netlify.app">Demo</a> -->
</div>

[![](https://images.squarespace-cdn.com/content/v1/629e6c49c6d4cb5b1d5808af/a578b412-bcea-47f6-a078-ed6f670adc86/A4DC5FE9-4813-4B28-B7F1-06E538E2334F.png?format=1500w)](https://www.neighborsatx.com/)


<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/neighbors-dog-park?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/neighbors-dog-park?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/neighbors-dog-park?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jordanistan/neighbors-dog-park?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jordanistan/neighbors-dog-park?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jordanistan/neighbors-dog-park?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jordanistan/neighbors-dog-park?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Neighbors Dog Park 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-Pre-requisites">Pre-requisites</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-How-to-Run-the-Script">How to Run the Script</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jordanistan" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

# Square Customer Renewal Script

This Python script loads a list of customers, identifies customers who've been registered for one or more years, and exports a CSV file with a list of the 20 oldest customers' details for renewal notification purposes.

![](neighbors-members-renew-list.gif)
## :sparkles: Features

- Connects to the Square API using a provided access token.
- Loads a JSON string containing customer data.
- Determines which customers need renewal based on a threshold (default 1 years).
- Writes customer details to a CSV file (`renewal_list.csv`).

## :white_check_mark: Pre-requisites

- You need Python 3.7+ installed. You can download it from [here](https://www.python.org/downloads/).
- Install the `squareup` package. You can install it using pip:
    ```sh
    pip install squareup
    ```
- Set up the Square Access Token as an environment variable. You can do this in the terminal with:
    ```sh
    export SQUARE_ACCESS_TOKEN='your_square_access_token'
    ```
    Replace `'your_square_access_token'` with your actual Square access token.

## :checkered_flag: How to Run the Script

1. Clone this repository to your local machine.
    ```sh
    git clone https://github.com/your_username/renewal_script.git
    cd renewal_script
    ```
2. If necessary, update the JSON string in the `load_customers` function with your actual data.
3. Run the script with:
    ```sh
    python3 renewal_script.py
    ```
4. Check the `renewal_list.csv` file in the project directory. It contains the data of customers whose accounts need renewal.

## Note

The provided customers data is hardcoded into the script for simplicity. In a production environment, you'd likely load this from a database or an API endpoint. Make sure to update the `load_customers` function accordingly if you wish to use this script in such a scenario. 

This script runs in the Square sandbox environment by default. Update the `environment` parameter in the `Client` object if you wish to run it in a production environment.
## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">El Gato</a>

&#xa0;

<a href="#top">Back to top</a>
