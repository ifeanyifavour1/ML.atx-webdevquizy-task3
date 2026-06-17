# Git and Version Control Basics
doc_id: doc_17
topic: Git
difficulty: beginner

## What is Git?
Git is a version control system that tracks changes in your code. It lets you save snapshots of your project, go back to earlier versions, and collaborate with others.

## Basic Git Commands
- git init — start a new git repository
- git status — see what files have changed
- git add . — stage all changes
- git commit -m "message" — save a snapshot
- git log — see commit history

## Branching
- git branch — list all branches
- git branch feature-nav — create a new branch
- git checkout feature-nav — switch to that branch
- git merge feature-nav — merge branch into main

## Remote Repository (GitHub)
- git remote add origin URL — connect to GitHub
- git push origin main — upload to GitHub
- git pull origin main — download latest changes
- git clone URL — copy a repository

## Good Commit Messages
Bad: "fixed stuff"
Good: "fix: navbar link not working on mobile"
Always describe WHAT changed and WHY.