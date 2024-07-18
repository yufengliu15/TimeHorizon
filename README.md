# TimeHorizon
A Python CLI that tracks how much time your putting into a given subject. Provides a simple way to track your time, and to export your data to applications such as Excel to analyze your time spent. 

A CLI may discourage the use of the application, but I just wanted to make a time tracking app quickly and easily. 

# Installation Instructions
Clone the repo, install the libraries needed

# How to use
Refer to the 'help' command for familiarizing with the commands

## Data
Your data is stored locally, in ./journal and ./csv 

Don't worry about the currentday.txt, which will be created after your first timer session. This file is to store the current days timer sessions, allowing you to freely exit the program.

### ./journal 
This is for where you write about what you did that day

### ./csv
This is where the amount of time spent is accumulated in a .csv file

## Workflow
When you want to track a project/subjects time, type `start subject` into the CLI.

Then, when your session is finished, you will see how much time was spent. 

Repeat how many times you wish.

At the end of the day, type in `endday` into the CLI. This will add all the times spent on each subject, and ask you to write down the things you've accomplished throughout the day (which you should post on Twitter!). You are able to write anything you want in this section, but here's my format for inspiration: