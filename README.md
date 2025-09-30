cat > README.md << 'EOF'
# B.Sc. Nursing Free Books

![Nursing Books Banner](https://img.shields.io/badge/Educational-Platform-blue) ![React](https://img.shields.io/badge/React-18.2.0-blue) ![Django](https://img.shields.io/badge/Django-4.2.7-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

A comprehensive full-stack educational website that provides free access to nursing textbooks and educational resources. Students can browse, search, preview, and download nursing books organized by academic year and subject, while administrators can manage the entire content library through a secure admin panel.

## 🌟 Features

### 🌍 Public Features (No Login Required)
- **Year-wise Organization**: Browse books by academic year (1st, 2nd, 3rd, 4th Year)
- **Subject Categories**: Organized by subjects (Anatomy, Physiology, Pharmacology, etc.)
- **Book Management**: View detailed book information with thumbnails
- **PDF Preview**: In-browser PDF viewing capability
- **Download Functionality**: Direct PDF download feature
- **Advanced Search**: Global search and filtering by title, author, subject, year
- **Responsive Design**: Mobile-friendly interface for all devices
- **Professional UI**: Clean, modern design optimized for students

### 🔐 Admin Features (Authentication Required)
- **Secure Login**: Django-based admin authentication system
- **Content Management**: Upload, edit, and delete PDF books
- **Metadata Management**: Manage book titles, authors, descriptions, subjects
- **Visibility Control**: Set books as public or private
- **File Management**: Automatic file size calculation and storage
- **Subject Administration**: Add, edit, and remove subject categories
- **User Management**: Manage admin users and permissions
- **Django Admin Integration**: Full access to Django's admin panel

### 🎨 Design Features
- **Modern Interface**: Clean, minimal design with blue and white color scheme
- **Card-based Layout**: Professional book cards with hover effects
- **Typography**: Inter font family for excellent readability
- **Responsive Grid**: Adaptive layouts for different screen sizes
- **Smooth Animations**: Professional transitions and hover states
- **Mobile Optimization**: Touch-friendly interface for mobile devices

## 🛠️ Tech Stack

### Backend
- **Django 4.2.7** - Python web framework
- **Django REST Framework** - API development
- **Django CORS Headers** - Cross-origin resource sharing
- **Django Filters** - Advanced filtering capabilities
- **Pillow** - Image processing for thumbnails
- **SQLite** - Database (development)

### Frontend
- **React 18.2.0** - JavaScript UI framework
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client for API calls
- **React Icons** - Icon components
- **TailwindCSS (CDN)** - Utility-first CSS framework
- **Inter Font** - Modern typography

### Development Tools
- **Python 3.11+** - Backend runtime
- **Node.js & npm** - JavaScript runtime and package manager
- **VS Code** - Recommended code editor
- **Git** - Version control

## 📋 Prerequisites

- **macOS** (or Linux/Windows with minor adjustments)
- **Python 3.11 or higher**
- **Node.js 16 or higher**
- **Git** for version control
- **Internet connection** for package downloads

## 🚀 Quick Start

### 1. Clone Repository
\`\`\`bash
git clone <repository-url>
cd nursing-books-website
\`\`\`

### 2. Backend Setup
\`\`\`bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv nursing_books_env
source nursing_books_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Create initial data
python manage.py shell
# In shell:
from books.models import Year, Subject
Year.objects.create(name="1st Year", order=1)
Year.objects.create(name="2nd Year", order=2)
Year.objects.create(name="3rd Year", order=3)
Year.objects.create(name="4th Year", order=4)
subjects = ["Anatomy", "Physiology", "Pharmacology", "Pathology", "Medical-Surgical Nursing", "Community Health Nursing", "Mental Health Nursing", "Pediatric Nursing", "Obstetric Nursing", "Nursing Research", "Nursing Administration"]
for subject in subjects:
    Subject.objects.create(name=subject)
exit()

# Start backend server
python manage.py runserver
\`\`\`

### 3. Frontend Setup
\`\`\`bash
# Navigate to frontend directory (new terminal)
cd frontend

# Install dependencies
npm install

# Start frontend server
npm start
\`\`\`

### 4. Access Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://127.0.0.1:8000/api
- **Admin Panel**: http://127.0.0.1:8000/admin

## 📚 Usage

### For Students
1. **Browse Books**: Visit homepage to explore available books
2. **Search Content**: Use search bar to find specific books or authors
3. **Filter Results**: Click on year categories or subjects to filter
4. **Preview PDFs**: Click "Preview" to view books in browser
5. **Download Books**: Click "Download" to save PDFs locally

### For Administrators
1. **Login**: Click "Admin Login" and enter credentials
2. **Add Books**: 
   - Go to Django Admin panel
   - Navigate to Books → Add Book
   - Fill in book details and upload PDF
   - Set visibility (Public/Private)
3. **Manage Content**: Edit book information, subjects, and years
4. **Monitor Usage**: Track uploaded books and user activity

## 🌐 API Documentation

### Base URL
\`\`\`
http://127.0.0.1:8000/api
\`\`\`

### Endpoints

#### Authentication
- \`POST /admin/login/\` - Admin login
- \`POST /admin/logout/\` - Admin logout
- \`GET /auth/check/\` - Check authentication status

#### Books
- \`GET /books/\` - List all public books
- \`GET /books/{id}/\` - Get book details
- \`POST /books/\` - Create book (admin only)
- \`PUT /books/{id}/\` - Update book (admin only)
- \`DELETE /books/{id}/\` - Delete book (admin only)
- \`GET /books/{id}/download/\` - Download PDF
- \`GET /books/{id}/preview/\` - Preview PDF

#### Subjects & Years
- \`GET /subjects/\` - List all subjects
- \`GET /years/\` - List all academic years

### Query Parameters
- \`search\` - Search in title, author, description
- \`year\` - Filter by academic year ID
- \`subject\` - Filter by subject ID
- \`ordering\` - Sort by field (upload_date, title, author)

## 📁 Project Structure

\`\`\`
nursing-books-website/
├── README.md
├── backend/
│   ├── nursing_books_env/          # Python virtual environment
│   ├── nursing_books/              # Django project settings
│   │   ├── settings.py             # Main configuration
│   │   ├── urls.py                 # URL routing
│   │   └── wsgi.py                 # WSGI application
│   ├── books/                      # Main Django app
│   │   ├── models.py               # Database models
│   │   ├── serializers.py          # API serializers
│   │   ├── views.py                # API views and logic
│   │   ├── urls.py                 # App URL patterns
│   │   ├── admin.py                # Admin interface config
│   │   └── migrations/             # Database migrations
│   ├── media/                      # User uploaded files
│   │   ├── books/                  # PDF storage
│   │   └── thumbnails/             # Book cover images
│   ├── db.sqlite3                  # SQLite database
│   ├── manage.py                   # Django CLI tool
│   └── requirements.txt            # Python dependencies
└── frontend/
    ├── public/                     # Static assets
    ├── src/
    │   ├── components/             # Reusable React components
    │   │   ├── Layout/Header.jsx   # Navigation header
    │   │   └── BookCard/BookCard.jsx # Book display cards
    │   ├── pages/                  # Page components
    │   │   ├── Home/Home.jsx       # Homepage
    │   │   └── Admin/              # Admin pages
    │   ├── services/api.js         # API communication layer
    │   ├── App.js                  # Main React component
    │   ├── index.js                # React entry point
    │   └── index.css               # Global styles
    ├── package.json                # Node.js dependencies
    └── node_modules/               # Installed packages
\`\`\`

## 🔧 Configuration

### Development Settings
The application comes with development-ready settings. For production:

#### Backend Configuration
\`\`\`python
# settings.py
SECRET_KEY = 'your-production-secret-key'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database (PostgreSQL recommended for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
\`\`\`

#### Frontend Configuration
Update API base URL in \`src/services/api.js\`:
\`\`\`javascript
const API_BASE = 'https://your-backend-domain.com/api';
\`\`\`

## 🚀 Deployment

### Backend (Heroku)
\`\`\`bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
\`\`\`

### Frontend (Vercel)
\`\`\`bash
# Install Vercel CLI
npm i -g vercel

# Build project
npm run build

# Deploy
vercel --prod
\`\`\`

## 🧪 Testing

### Backend Tests
\`\`\`bash
cd backend
source nursing_books_env/bin/activate
python manage.py test
\`\`\`

### Frontend Tests
\`\`\`bash
cd frontend
npm test
\`\`\`

## 🛠️ Troubleshooting

### Common Issues

#### Backend Issues
- **Virtual Environment**: Ensure \`nursing_books_env\` is activated
- **Database Errors**: Run \`python manage.py migrate\`
- **Import Errors**: Check all dependencies are installed
- **Permission Errors**: Verify media folder permissions

#### Frontend Issues
- **Styling Missing**: Clear browser cache (Cmd+Shift+R)
- **API Errors**: Verify backend is running on port 8000
- **Build Errors**: Delete \`node_modules\` and run \`npm install\`
- **CORS Issues**: Check Django CORS settings

#### General Issues
- **Port Conflicts**: Change ports if 3000/8000 are occupied
- **File Upload**: Ensure media directory is writable
- **Login Problems**: Verify admin user has \`is_staff=True\`

### Debug Tips
1. Check browser console (F12) for JavaScript errors
2. Monitor Django server logs in terminal
3. Use Django admin panel to verify data
4. Test API endpoints directly using tools like Postman

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch**: \`git checkout -b feature/amazing-feature\`
3. **Commit changes**: \`git commit -m 'Add amazing feature'\`
4. **Push to branch**: \`git push origin feature/amazing-feature\`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint for JavaScript code
- Write descriptive commit messages
- Add comments for complex logic
- Test features thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
- **Issues**: Create a GitHub issue for bugs or feature requests
- **Documentation**: Check this README and inline code comments
- **Community**: Join discussions in GitHub Discussions

### Reporting Bugs
When reporting bugs, please include:
- Operating system and version
- Python and Node.js versions
- Complete error messages
- Steps to reproduce the issue

## 🎯 Roadmap

### Planned Features
- [ ] User registration and personal bookmarks
- [ ] Book rating and review system
- [ ] Advanced search with multiple filters
- [ ] Mobile application development
- [ ] Analytics dashboard for admins
- [ ] Email notifications for new books
- [ ] Multi-language support
- [ ] Dark theme option
- [ ] Offline reading capabilities
- [ ] Social sharing features

### Version History
- **v1.0.0** - Initial release with core features
- **v1.1.0** - Enhanced search and filtering
- **v1.2.0** - Mobile responsive improvements
- **v2.0.0** - User authentication system (planned)

## 📊 Statistics

- **Languages**: Python, JavaScript, CSS
- **Frameworks**: Django, React
- **Database**: SQLite (dev), PostgreSQL (prod)
- **File Storage**: Local filesystem (dev), AWS S3 (prod recommended)
- **Authentication**: Django built-in
- **API**: RESTful with Django REST Framework

## 🙏 Acknowledgments

- **Django Community** for the excellent web framework
- **React Team** for the powerful UI library
- **TailwindCSS** for the utility-first CSS framework
- **Nursing Education Community** for inspiration and requirements
- **Open Source Contributors** who made this project possible

---

**Built with ❤️ for nursing students worldwide**

*This project aims to democratize access to quality nursing education resources and support the next generation of healthcare professionals.*
EOF