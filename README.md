# FitZone - Your Fitness Shop!

![picture alt](/static/image/fit-zone-home.PNG "fit-zone-homepage")

## Introduction

FitZone is a fictional e-commerce in fitness supplements and gear based in Cork, Ireland. The website is hosted on Heroku at https://fit-zone.herokuapp.com/.

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

### Home Page
In the homepage we can see the navigation bar, authentication options and the bag. The user can also sign up to the mailing list. There is also a link to "shop now" who brings to all products present in the website.