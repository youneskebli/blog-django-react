# Search Atlas Toy Project: Blog Application

Welcome to the **Search Atlas Toy Project**! This project serves as a demonstration of your Django and Python expertise, and optionally your frontend React and containerization skills. Below are the details of the project, setup instructions, features, and testing requirements.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)

---

## Project Overview

This is a **Blog Application** designed to allow writers and editors to manage articles effectively. The application implements core Django features such as authentication, class-based views, and model relationships, while adhering to Django and Python best practices. Editors can approve or reject articles, and writers can create and edit their articles.

---

## Features

### Backend (Django)
- **Dashboard**: Displays a summary of writers, showing the total number of articles they've written and how many were written in the last 30 days.
- **Article Creation**: Writers can create new articles.
- **Writer Article Detail**: Writers can edit the title and content of articles they've written. The status of the article (e.g., Pending, Approved, Rejected) is read-only.
- **Article Approval**: Editors can view and approve or reject articles via a simple interface.
- **Edited Articles**: Editors can see all articles they've approved or rejected.

### Models

#### `Article`
- `created_at` (datetime): Timestamp for when the article was created.
- `title` (string): Title of the article.
- `content` (text): Body content of the article.
- `status` (string): Status of the article, can be "Pending", "Approved", or "Rejected".
- `written_by` (ForeignKey to Writer): The writer of the article.
- `edited_by` (ForeignKey to Writer): The editor who approved or rejected the article.

#### `Writer`
- `is_editor` (boolean): Indicates if the writer is also an editor.
- `name` (string): Name of the writer, connected to the Django User model.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/blog-application
cd blog-application