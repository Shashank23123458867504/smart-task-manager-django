# Smart Task Manager

A simple yet functional **Task Management Web Application** built using **Django**.  
This project allows users to register, log in, manage their profile, create categories, and perform full CRUD operations on tasks.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login
- User Logout
- Protected routes using `@login_required`

### 👤 User Profile
- Bio
- Timezone
- Profile Image upload

### 🗂 Category Management
- Users can create their own categories
- Categories are reusable across multiple tasks
- Categories are user-specific

### ✅ Task Management (CRUD)
- Create tasks
- View task list
- Update tasks
- Soft delete tasks (`is_deleted=True`)
- Optional due date with date-time picker
- Task priority and status support

### 🔒 Security / Access Control
- Users can only access their own tasks and categories
- Category dropdown is filtered per logged-in user

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite3
- **Language:** Python

---

## 📂 Project Structure

```bash
SmartTaskManager/
│
├── app/
├── SmartTaskManager/
├── templates/
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   ├── tasks/
│   │   ├── task_form.html
│   │   ├── task_list.html
│   │   └── category_form.html
│   └── home.html
│
├── manage.py
├── .gitignore
└── README.md
