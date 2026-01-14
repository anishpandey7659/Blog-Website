# 📝 MyBlog - Django Blog Platform
## A modern, feature-rich blogging platform built with Django and styled with Tailwind CSS. Create, share, and discover amazing content with an intuitive and beautiful interface.

![django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=for-the-badge&logo=tailwind-css)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 🎥 Demo
📺 **See it in action!** Watch the full demo video on LinkedIn:
[![Demo Video](https://img.shields.io/badge/LinkedIn-Demo%20Video-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/posts/anish-pandey-9235a32a6_exploring-django-backend-i-just-dove-ugcPost-7416871600941228033-z0Bv)

> 🎬 Click the badge above to watch a complete walkthrough of the Document QA RAG system, including PDF upload, question-answering, and the RAG pipeline in action!

---

✨ Features

# 🔐 User Authentication

* User registration and login
* Secure authentication system
* Profile management
* Personalized user dashboards

# 📰 Blog Management
1. Create Posts - Rich text editor with image upload support
2. Edit & Delete - Full control over your content
3. Categories - Organize posts by topics
4. Search Functionality - Find posts by title or category
5. Responsive Design - Beautiful UI on all devices

# 👤 User Profiles
* Personalized profile pages
* View all posts by a user
* User statistics (post count, comments, join date)
* Avatar integration
* Edit and delete own posts from profile

## 💬 Interactive Features
* Comment system on blog posts
* Real-time search with filters
* Explore page to discover new content
* Elegant post cards with hover effects

## 🎨 Modern UI/UX
* Clean and intuitive interface
* Smooth animations and transitions
* Mobile-responsive design
* Dark mode ready
* Professional gradient themes

# 🚀 Quick Start

## Prerequisites
* Python 3.10 or higher
* pip (Python package manager)
* Virtual environment (recommended)
*  Installation
* Clone the repository

   ```bash
  git clone https://github.com/yourusername/myblog.git
  cd myblog
1. Create and activate virtual environment
    ```
    
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

2. Install dependencies
    ```
      
      pip install -r requirements.txt
3. Set up the database
    ```

    python manage.py makemigrations
    python manage.py migrate
4. Create a superuser
    ```

    python manage.py createsuperuser

5. Run the development server
    ```

    python manage.py runserver
6. Visit the application
* Main site: http://127.0.0.1:8000/
* Admin panel: http://127.0.0.1:8000/admin/

# 📁 Project Structure
```
myblog/
├── app1/                      # Main application
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   └── app1/
│   │       ├── base.html      # Base template
│   │       ├── index.html     # Home page
│   │       ├── more.html      # Explore page
│   │       ├── profile.html   # User profile
│   │       └── ...
│   ├── static/                # Static files (CSS, JS, images)
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   └── forms.py               # Forms
├── media/                     # User uploaded files
├── myblog/                    # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

# 🛠️ Tech Stack
- Backend: Django 5.0
- Frontend: HTML5, TailwindCSS
- Database: SQLite (development) / PostgreSQL (production ready)
- Authentication: Django Auth
- File Upload: Django FileField with Pillow

# 📸 Screenshots
* Home Page
* Beautiful landing page with latest blog posts

# Explore Page
* Discover new content with advanced search and filters

# User Profile
* Personalized dashboard with user statistics and post management

# Blog Post Detail
* Clean reading experience with comments section

# 🔧 Configuration
* Environment Variables
* Create a .env file in the project root:

# Static Files
- For production, collect static files:
  ```
    python manage.py collectstatic
# 📝 Usage
1. Creating a Blog Post
2. Log in to your account
3. Click "New Post" in the navigation bar
4. Fill in the title, content, category (optional), and upload an image
5. Click "Create Post"
## Searching for Posts
1. Go to the Home or Explore page
2. Use the search bar at the top
3. Enter keywords from the post title or category
4. Results will filter automatically
## Managing Your Profile
1. Click on your username in the navigation bar
2. View your profile with all your posts
3. Edit or delete posts directly from your profile
4. See your statistics and activity

# 🤝 Contributing
* Contributions are welcome! Please feel free to submit a Pull Request.

# Fork the repository
1. Create your feature branch (git checkout -b feature/AmazingFeature)
2. Commit your changes (git commit -m 'Add some AmazingFeature')
3. Push to the branch (git push origin feature/AmazingFeature)
4. Open a Pull Request

# 📄 License
* This project is licensed under the MIT License - see the LICENSE file for details.

# 👨‍💻 Author
## Anish Pandey

## GitHub: @anishpandey
## Email: anishpandey1232@gmail.com

#🙏 Acknowledgments
* Django Documentation
* Tailwind CSS
* UI Avatars API for profile pictures
* The amazing Django community
##⭐ If you found this project helpful, please give it a star!

## Made with ❤️ using Django and TailwindCSS


