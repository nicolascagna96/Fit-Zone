# FitZone - Your Fitness Shop!

![picture alt](/static/image/fit-zone-home.PNG "fit-zone-homepage")

## Introduction

FitZone is a fictional e-commerce of fitness supplements and gym gear based in Cork, Ireland. The website is hosted on Heroku at https://fit-zone.herokuapp.com/.

This website is for educational purposes only and the credit card payment functionality is not set up to accept real payments. If testing the credit card payment, you can use the test card details below. For more information see the [Stripe Testing Payment](https://stripe.com/docs/testing "Stripe testing") page.

- 4242424242424242 (Visa) 
- Expiration date = Any future date (Example: 12/24)
 - CVN = any 3 digits (Example: 132) 
- Postcode = any 5 digits (Example: 12345)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux)
- [Architecture](#architecture)
- [Design](#agile-development)
- [Design](#design) 
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [ Deployment](#deployment)
- [Credits](#credits)

## User Stories

You can check the kanban board [here](https://github.com/users/nicolascagna96/projects/4/views/1 "kanban board") 

### Admin

- As an Admin I want to be able to add, edit and delete products from the Django admin panel and from the frontend.

- As an Admin I would like to be able to access Django Admin panel to check orders, comment, contact messages and workout plan requests.

- As an admin I would like to have a panel in the Django Admin to create, edit and delete blog posts.

### User

- As a User I can create an account so that I can save my details when I do the checkout.

- As a User I can log in and log out from my account.

- As a User I want to be able to update details on my account.

- As a User I want to be able to select the product to buy.

- As a User I can signup for the newsletter

- As an User I can re-set my password.

- As a User I can edit and delete products from my basket before my purchase.

- As a User I can view all likes and comments on the blog posts.

- As a User I can leave likes and comments under every blog posts.

- As a User I want a checkout functionality so that I can checkout securely.

- As a User I want a navigation bar so that I can navigate the entire website.

- As a User I have the link to the privacy policy so that I know my rights.

- As a User I want a contact page so that I can send the message to the Site Admin.

### Overall Goals

- Create an e-commerce cloud-hosted Full-Stack web application to sell fitness related products online.

- Allow the superuser access to full CRUD (create, read, update and deleted) functionality on blog posts and products.

- To provide users with a targeted product selection and smooth customer experience when shopping at FitZone.

### Strategy
FitZone is focused on selling B2C (Business to Customer) products to end users. Recently many consumers have turned to online shopping. FitZone aims to benefit consumers by offering large discounts on fitness related products, such as food supplements, gym gear and tailored workout plans.

### Site User / Target Audience / Demographic
- Target market is aimed at anyone in the 18-50 years old
- People that wants to start an healthy lifestyle again.
- People who are interested in fitness aricles.

### Site Goals
- Site's main purpose is clear
- User authentication
- CRUD functionality for superuser
- Simple navigation that allows the user to easily find information.

# Architecture

## Database Schema

# Design

## Wireframes

## Navigation

# Features

## Existing Features

## Home Page
In the homepage we can see the navigation bar, authentication options and the bag. The user can also sign up to the mailing list. There is also a link to "shop now" who brings to all products present in the website.

![picture alt](/static/image/fit-zone-home.PNG "fit-zone-homepage")

## Navigation Bar:
In the nav bar we can find the login and logout links, the search bar, the logo, the shopping bag, product filters, contact form, request a tailored workout plan form and the free delivery banner.

![picture alt](/static/image/navbar.PNG "fit-zone")

## All Products view
In the all products view we can see the entire list of products, products details such as price, rating and image.

![picture alt](/static/image/product.PNG "fit-zone")

## Product detail view
In the product detail view we can see:
- Product Name
- Image
- Price
- Description
- Rating
- Category
- Add to the basket functionality
- Edit and delete buttons (if you're logged in as superuser)

![picture alt](/static/image/product-details.PNG "fit-zone")

## Filter Functionality
![picture alt](/static/image/filter-functionality.PNG "fit-zone")

## My account 
From here the user can saving their shopping details, login/logout and the superuser(s) can add products.

![picture alt](/static/image/filter-functionality.PNG "fit-zone")


## Add Products
The superuser(s) can add new products directly from the frontend, instead of doing it from the Django Administration panel.

![picture alt](/static/image/add-product.PNG "fit-zone")

## Edit Products
The superuser(s) can edit new products directly from the frontend, instead of doing it from the Django Administration panel.

![picture alt](/static/image/edit-product.PNG "fit-zone")

## Delete Products
The superuser(s) can delete new products directly from the frontend, instead of doing it from the Django Administration panel.

![picture alt](/static/image/delete-product.PNG "fit-zone")

## Shopping Bag 
In the shopping bags includes:
- List of Products 
- The subtotals
- Users can edit and delete items
- Secure Checkout Buttons
- Message that reminds the customers how much they need to spend to get free delivery.
- Keep Shopping option that brings Users to the All Products page.

![picture alt](/static/image/shopping-bag.PNG "fit-zone")
![picture alt](/static/image/shopping-bag2.PNG "fit-zone")

## Checkout
The chekout page includes:
- Form to fill with delivery details and payment details.
- Summary of the bag
- Option to adjust the bag
- Complete Order button

![picture alt](/static/image/checkout.PNG "fit-zone")

## Checkout Confirmation
An order was successfully placed. The user/customer will receive a confirmation email. 

![picture alt](/static/image/checkout-confirmation.PNG "fit-zone")

## Register

![picture alt](/static/image/signup.PNG "fit-zone")

## Log In

![picture alt](/static/image/login.PNG "fit-zone")

## log Out

![picture alt](/static/image/log-out.PNG "fit-zone")

## Blog

![picture alt](/static/image/blog.PNG "fit-zone")

## Blog comments and likes
The users can leave likes and comments to each block post.

![picture alt](/static/image/blog-like-comments.PNG "fit-zone")

## Contact Form

Users can contact us to receive assistance for their orders, or if they have questions regarding our business.

![picture alt](/static/image/contact-form.PNG "fit-zone")

## Workout Plan

The Users can request tailored workout plans and our Personal Trainers will contact them back to request more information.

![picture alt](/static/image/workout-plan.PNG "fit-zone")

## Newletter and footer 
Users can subscribe to the FitZone newsletter and they can find the Facebook page of the e-commerce.

![picture alt](/static/image/newsletter.PNG "fit-zone")

## 404 Page
A 404 page was created to handle user navigational errors and give user a quick ink to direct them back to shopping.

![picture alt](/static/image/404.PNG "fit-zone")

## Features to Implements.
- Social logins
- About us page
- Customer Reviews functionality

# Marketing Strategies & SEO

## SEO - Search Engine Optimization

The optimization of web pages and content was carried out through the use of Google keyword research, aiming to enhance the ranking in search engines. Utilizing both short-tail and long-tail keywords, as well as exploring "People also ask" and "Related searches" sections, helped in identifying relevant keywords.

![picture alt](/static/image/keywords.PNG "fit-zone")

## Content Marketing

I created a blog to generate and distribute content to attract potential customers and retain existing ones. The objective of the blog post is to establish trust and foster loyalty among the audience. The blog has also an educational purpose for our customers

## Social Media
A Facebook business page was created with the goal of growing our audience organically by constructing a community and promoting loyalty among our target market. Facebook one of the most used social media app and is free. The business can connect directly with customers through the Facebook platform, reaching a broader global audience.

![picture alt](/static/image/facebook.PNG "fit-zone")

![picture alt](/static/image/facebook-post.PNG "fit-zone")

## Mail Chimp - Email Marketing

I have added a newsletter sign up form using Mail Chimp, so that shoppers can sign up to receive information regarding the FitZone.

![picture alt](/static/image/newsletter.PNG "fit-zone")

## XML Sitemap

I've created a sitempa for FitZone using [XML-Sitemaps.com](https://www.xml-sitemaps.com/ "XML Sitemaps"). An XML sitemap is a file that lists all the pages on a website and provides information about each page to search engines. The purpose of an XML sitemap is to help search engines understand the structure and organization of a website, and to allow them to more easily crawl and index the site's content. Overall, XML sitemaps are an important tool for website owners who want to improve their visibility in search engines and drive more traffic to their site.

I've created also a robots.txt file. The robots.txt file is a standard used by websites to communicate with web robots (often referred to as "bots"), such as search engine crawlers, about which pages or sections of the site should not be processed or accessed. The file is placed in the root directory of a website and typically consists of a series of rules that specify which pages or files should be blocked and which should be allowed.

# Technologies Used

## Languages Used
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML "HTML") 
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS3") 
- [JavaScript](https://www.javascript.com/ "JavaScript") 
- [Python](https://www.python.org/ "Python") 

## Frameworks, Libraries & Programs Used
- [AWS - S3](https://aws.amazon.com/s3/ "AWS") - To host static files.
- [Heroku](https://id.heroku.com/login "Heroku") - To host the website.
- [Gitpod](https://gitpod.io/workspaces "Gitpod") - IDE.
- [Github](https://github.com "Github") - Repository.
- [Bootstrap4](https://getbootstrap.com/docs/4.6/getting-started/introduction/ "Bootstrap") - Used to build the UI.
- [Django](https://www.djangoproject.com/ "Django") - Python-based web framework.
- [Font Awesome](https://fontawesome.com/ "Font Awesome") - Free Icons.
- [Google Font](https://fonts.google.com/about "Google Fonts") - for typography.
- [Pexels](https://www.pexels.com/ "Pexels") - for images.
- [Am I Responsive](https://ui.dev/amiresponsive "Am I Responsive") - to check if the website is responsive.
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html "Django") - for user authentication.
- [Crispy Forms](https://www.djangoproject.com/ "Crispy Forms") - Python-based web framework.
- [Stripe](https://stripe.com/en-ie "Stripe") - For testing the payments.
- [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL") - Database.
- [Mail Chimp](https://mailchimp.com/?currency=EUR "Mail chimp") - Signup form and newsletter.
- [Privacy Policy Generator](https://www.termsandconditionsgenerator.com/ "Mail chimp") - To generate the privacy policy for the website.


# Testing

## Validation Testing

## HTML

## Python Validator - Flake8
The website pep8online.com is currently down so flake8 was used. This can be done by typing "python3 -m flake8" command in the terminal. Migration and settings errors remain as advised by code institute. Click here to see the result:
## CSS Validator

![picture alt](/static/image/css.PNG "fit-zone")

## JS Validator
Javascript was run through the JSHint validator.
