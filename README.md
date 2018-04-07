## Basic Questionnaire for oTree

This is a basic questionnaire that can be executed after or before other applications in oTree.
It includes four pages which are located under templates:

- Introduction.html
- Survey1.html
- Survey2.html
- Demographics.html

The questionnaire always starts with Introduction.html, and always ends with a Demographics.html.
Between these two pages, the application randomizes other pages included under templates as "Survey*.html" and incorporated in models.py and pages.py.
The order of items and questions on every page are also randomized.

The questionnaire was created on oTree version 2.0.29, and can be tested [here](https://otree-questionnaire.herokuapp.com "here").