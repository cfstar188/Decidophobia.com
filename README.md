<img src="README_images/decidophobia banner.png" alt="decidophobia banner"/>

**Decidophobia**: An eCommerce Site for Indecisive Shoppers 
===
![commits](https://img.shields.io/github/commit-activity/t/cfstar188/Decidophobia.com/main)
![dependencies](https://img.shields.io/github/pipenv/locked/dependency-version/cfstar188/Decidophobia.com/django)
![Languages](https://img.shields.io/github/languages/count/cfstar188/Decidophobia.com)
![size](https://img.shields.io/github/repo-size/cfstar188/Decidophobia.com)

## Table of Contents

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Another eCommerce Site... What's Special?!](#another-ecommerce-site-whats-special)
- [In a Nutshell](#in-a-nutshell)
- [General Architecture](#general-architecture)
- [Technical](#technical)
   * [Technical Summary](#technical-summary)
   * [~ Questionnaire](#-questionnaire)
   * [~ HTTP Client](#-http-client)
   * [~ Comparing Products](#-comparing-products)
   * [~ Order Management](#-order-management)
   * [~ User Accounts](#-user-accounts)
   * [~ Discussion Board](#-discussion-board)
- [Main User Stories](#main-user-stories)
- [Project Management](#project-management)
- [Authors](#authors)

<!-- TOC end -->

<!-- TOC --><a name="another-ecommerce-site-whats-special"></a>
## Another eCommerce Site... What's Special?!
Yes, we agree: there are too many eCommerce sites to begin with. But that's exactly why we *decided* to just add 1 more to the list...

Decidophobia is a student-led project designed to solve a very specific problem: the dilemma of choice. Here's a list you can contemplate about:
* Amazon
* eBay
* Walmart
* Craigslist
* Etsy
* Kijiji (🍁)
* Facebook Marketplace
* Instagram
* BestBuy
* Your dog
* My Neighbor
* ...

Clearly, the number of eCommerce sites don't seem to end. With so many choices to pick from, a lot of us humans are tempted to start comparing them all. Why? Because we want to buy something knowing we got the best deal ever! And that's fine... because I do it too. 

With this context in mind, we present a solution to the flurry of open tabs and the constant back-and-forth in between: one website that can just give me the best deal, every single time. 

<!-- TOC --><a name="in-a-nutshell"></a>
## In a Nutshell
<img src="README_images/home_screen.png" alt="decidophobia banner"/>

Decidophobia is mainly an eCommerce aggregator and a product rating system. We use availabe eCommerce API's to request, aggregate and display produts from different websites. Put in other words, we talk to online shopping sites and ask them for a list of their products. Then, we rank those products based on a variety of common-sense metrics like your individual preferences, price and product reviews. 


<!-- TOC --><a name="general-architecture"></a>
## General Architecture

<img src="README_images/general_architecture.png" alt="decidophobia banner"/>

<p>The architecture diagram represents the software architecture for <strong>Decidophobia.com</strong>, a web application developed using Django and React with SQLite as the database. The architecture is designed to handle requests efficiently, process data, and deliver responses to the client. Below is an overview of the various components and their interactions within the system:</p>

<h3>SQLite Database</h3>
<ul>
  <li><strong>Core Models (core_models.py)</strong>: This file defines the database models, which represent the data structures and their relationships.</li>
  <li>The SQLite database is the primary storage for our application data. It is queried directly by the Django application to fetch or store data.</li>
</ul>

<h3>Django Backend</h3>
<ul>
  <li><strong>URLs (urls.py)</strong>: This module maps URLs to the corresponding views in the application.</li>
  <li><strong>Views (views.py)</strong>: Views handle the business logic of the application. They receive web requests, interact with models to retrieve data, and send responses back to the client.</li>
  <li><strong>Django HTTP Framework</strong>: This is the core framework that handles HTTP requests and responses. It integrates the URLs and Views, processing incoming requests based on the defined URL patterns and generating outgoing responses.</li>
  <li><strong>API Services (ShopSearch.py)</strong>: External API services are integrated here, providing additional data or functionalities that complement the core application features.</li>
  <li><strong>Template (HTML)</strong>: Django templates are used to generate HTML content that is returned to the client as part of web responses.</li>
</ul>

<h3>React Frontend</h3>
<ul>
  <li>The React application serves as the frontend of Decidophobia.com. It handles user interactions, makes API calls to the Django backend, and updates the user interface accordingly.</li>
  <li><strong>RESTful API Calls</strong>: The React frontend communicates with the Django backend through RESTful API calls, requesting data and receiving responses in JSON format.</li>
</ul>

<h3>Client</h3>
<ul>
  <li>This is the user's device (e.g., computer, smartphone), which runs the web browser. It sends requests to and receives responses from the React frontend.</li>
</ul>

<h3>Flow of a Request:</h3>
<ol>
  <li><strong>Client Interaction</strong>: The user interacts with the React application, triggering an HTTP request to the Django backend.</li>
  <li><strong>URL Routing</strong>: Django processes the incoming request, routing it to the appropriate view based on the URL.</li>
  <li><strong>Data Processing</strong>: The view may perform database queries through the model, interact with external API services, and process the necessary data.</li>
  <li><strong>Response Generation</strong>: The view generates a response, which could be a JSON data packet for API calls or an HTML page rendered using templates.</li>
  <li><strong>Client Update</strong>: The React frontend processes the response, updating the UI dynamically based on the received data.</li>
</ol>

<p>This architecture ensures that the application is modular, with clear separation of concerns among the database, backend, and frontend. It leverages the strengths of Django and React to provide a responsive and dynamic user experience.</p>

<!-- TOC --><a name="technical"></a>
## Technical
<!-- TOC --><a name="technical-summary"></a>
### Technical Summary
Decidophobia currently sits as a web-app with a Django backend and a React (Next.js) frontend. It also uses Docker to ensure universal runnability, and Postgres as its DBMS.

<!-- TOC --><a name="-questionnaire"></a>
### ~ Questionnaire
React was used to construct a questionnaire that collected user preferences. This included selections about how imporant product ratings, brand reputation and quick delivery time were to the user. 

<!-- TOC --><a name="-http-client"></a>
### ~ HTTP Client
To request product information, an HTTP client was architected using the decorator pattern. The client requests and retrieves information (JSON) using OAuth 2.0 protocols while minting authentication tokens automatically. 

<!-- TOC --><a name="-comparing-products"></a>
### ~ Comparing Products
The product comparison feature uses the JSON returned by the HTTP client to index each product accordingly. By using React, the search result page is created by placing each indexed product into a series of tables. Then, when a user clicks "Compare", the indices of these products is moved onto an array which maps onto the side-by-side product bar at the bottom of the screen. 

<img src="README_images/product_comparison.png" alt="decidophobia banner"/>

<!-- TOC --><a name="-order-management"></a>
### ~ Order Management
React was used to design the shopping cart and order history pages. React components from the Material UI components library were utilized to create the frontend pages. For the cart functionality (adding/removing/updating items), axios was used to send requests to the backend.

Each shopping cart item and purchase-history entry is stored with foreign keys to the products and users tables. Moreover, a randomly generated, unique, 10-character alphanumeric ID was used to identify each specific order.

<img src="README_images/shopping_cart.png" alt="decidophobia banner"/>

<!-- TOC --><a name="-user-accounts"></a>
### ~ User Accounts
React was used to design the user settings page. It interacts with the Django backend, which uses different serializers to change the various components of a user account, i.e. email and password. User accounts are facilitated using a *CustomUser* model that is a subclass of Django's *AbstractBaseUser*.

<!-- TOC --><a name="-discussion-board"></a>
### ~ Discussion Board
React was used to create the discussion board, while user messages were stored in a Django backend. Axios requests are used to interact with the Django backend, primarily to retrieve and insert messages to display onto the discussion board.

<!-- TOC --><a name="main-user-stories"></a>
## Main User Stories

> “There’s always more to build than we have time or resources to build — always.” [name=Jeff Patton]
<details> 
    <summary><strong>Questionnaire</strong></summary>
    
```gherkin=
Feature: Questionairre
  As an frequent shopper, I want to quickly select
  all my individual preferences like budget, favorite
  sites, and delivery time.
  
  Scenario: User arrives at the home page
    Given I clicked on "SearchFilter",
    Then I can toggle my unique preferences
    And get results that are curated appropriately.
```
</details>

<details>
    <summary><strong>eCommerce HTTP Client </strong></summary>
    
```gherkin=
Feature: eCommerce HTTP Client
  As an indecisive shopper, I want to see results 
  from all the eCommerce sites I request for. 
  
  Scenario: User types item name into the search bar
    Given I selected my preferred shopping sites,
    When I click "search"
    Then I will get a list of curated products.
```
</details>

<details>
    <summary><b>Interactive Comparison</b></summary>
    
```gherkin=
Feature: Interactive Comparison
  As a shopper on a budget, I want to interactively
  compare the main features of different products. 
  
  Scenario: User is directed to the search results
    Given I found a suitable product,
    When I click "Compare"
    Then I can compare products side-by-side.
```
</details>
<details>
<summary><b>Shopping Cart</b></summary>

```gherkin=
Feature: Shopping Cart
  As a casual shopper, I want to put items in my shopping cart
  because I want to manage items before I checkout.

  Scenario: User adds item to cart
    Given I'm a logged-in user
    When I go to the item page
    And I click "Add item to cart"
    Then the quantity of items in my cart should go up
    And my subtotal should increment accordingly.
```
</details>

<details>
    <summary><b>User Accounts</b></summary>
    
```gherkin=
Feature: User Accounts
  As an avid shopper, I want to be able to be able to change my
  user account information. 

  Scenario: I want to update my account information
    Given I am logged in
    When I navigate to the settings page
    And I click on the button to change my password, email, etc.
    Then the database will be updated with the new information
    And the changes will be reflected in the GUI
```
</details>

<details>
    <summary><b>Community Discussion Board</b></summary>
    
```gherkin=
Feature: Discussion Board
  As a shopper with FOMO, I want a place to interact with other 
    shoppers where I can discuss the best deals and sales in 
    the website.

  Scenario: I want to look for the hottest new deals
    Given I am logged in,
    When I navigate to the discussion board
    Then I find discussions about different, linked products.
```
</details>

<!-- TOC --><a name="project-management"></a>
## Project Management
<img src="README_images/jira.png" alt="decidophobia banner"/>

Throughout every sprint, Jira was used to manage our prouduct backlog. Our development was mainly split into 3 sprints, along with initial sprint pre-planning sessions. 

Each sprint culminated with a product demo, where either the main features or the newest additions were presented. After our last sprint, we decided to complete a video presentation discussing what our product is, and what its market would look like. 
This video can be watched <a href="https://youtu.be/VAtVXeAbKok">here.</a>

In terms of our work timeline, as followers of the SCRUM methodology, our iterative work process is roughly graphed below:
```mermaid
gantt
    title SCRUM Work Timeline
    dateFormat YY-MM-DD

    section Sprint 1
    Base Features           :a1, 2024-01-26, 14d
    section Sprint 2
    Integrations            :2024-02-15  , 14d
    section Sprint 3
    Bug Fixes & Polish      :2024-03-10  , 14d
```
<!-- TOC --><a name="authors"></a>
## Authors

**Decidophobia is a public project** lead by a team of 7 individuals. 

The members of this team are (listed alphabetically):
- [Ahmed Mohamed](https://github.com/ahmed33033)
- [Chris Flores](https://github.com/cfstar188)
- [Faisal Masalha](https://github.com/TrueDescription)
- [Gaurav Poona](https://github.com/gaurav3247)
- [Hung-Mao Wu](https://github.com/wuhungmao)
- [Justin Tran](https://github.com/JustAProjectacc)
- [Vincent Tran](https://github.com/MintV-Vincent)



<!-- TOC --><a name="tags-decidophobia-ecommerce-documentation"></a>
###### tags: `Decidophobia` `eCommerce` `Documentation`
