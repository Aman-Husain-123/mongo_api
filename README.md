# MongoDB FastAPI CRUD Application

A FastAPI-based REST API application for performing CRUD operations on MongoDB using Motor (async MongoDB driver).

## 🚀 Features

- ✅ **Async MongoDB Operations** using Motor driver
- ✅ **FastAPI** for high-performance REST API
- ✅ **CRUD Operations** - Create, Read, Update, Delete
- ✅ **Environment Variables** for secure configuration
- ✅ **Pydantic Models** for data validation
- ✅ **Error Handling** with proper HTTP status codes

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/euron/insert` | Insert new record |
| GET | `/euron/getdata` | Get all records |
| GET | `/euron/showdata` | Show all records (alias) |
| POST | `/euron/update/{record_id}` | Update specific record |
| DELETE | `/euron/delete/{record_id}` | Delete specific record |

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB Atlas
- **Driver:** Motor (AsyncIOMotorClient)
- **Validation:** Pydantic
- **Environment:** python-dotenv

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aman-Husain-123/mongo_db_data_update_testing.git
cd mongo_db_data_update_testing
```

### 2️⃣ Environment Variables Setup
```bash
# Create .env file in the root directory
# Add your MongoDB connection string
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?appName=YourApp
```

**⚠️ SECURITY NOTE:** Never commit your `.env` file to version control. It contains sensitive database credentials.

### 3️⃣ Create Virtual Environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# Mac/Linux
python -m venv myenv
source myenv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application
```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

## 📊 Data Model

```python
class eurondata(BaseModel):
    name: str
    phone: int
    city: str
    course: str
```

## 🔧 API Usage Examples

### Insert Data
```bash
curl -X POST "http://localhost:8000/euron/insert" \
-H "Content-Type: application/json" \
-d '{
    "name": "John Doe",
    "phone": 1234567890,
    "city": "New York",
    "course": "Python"
}'
```

### Get All Data
```bash
curl -X GET "http://localhost:8000/euron/getdata"
```

### Update Record
```bash
curl -X POST "http://localhost:8000/euron/update/{record_id}" \
-H "Content-Type: application/json" \
-d '{
    "name": "Jane Doe",
    "phone": 9876543210,
    "city": "Los Angeles",
    "course": "JavaScript"
}'
```

### Delete Record
```bash
curl -X DELETE "http://localhost:8000/euron/delete/{record_id}"
```

## 📁 Project Structure

```
mongo_db_data_update_testing/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
├── Example2/           # Additional example
│   ├── main.py
│   ├── .env
│   └── requirements.txt
└── myenv/              # Virtual environment
```

## 🔒 Security Features

- Environment variables for database credentials
- `.env` files excluded from version control
- Input validation using Pydantic models
- Proper error handling and HTTP status codes

## 🌐 MongoDB Atlas Setup

1. Create a MongoDB Atlas account
2. Create a new cluster
3. Create a database user
4. Get your connection string
5. Replace `username`, `password`, and cluster details in your `.env` file

## 📖 API Documentation

Once the server is running, visit:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Aman Husain**
- GitHub: [@Aman-Husain-123](https://github.com/Aman-Husain-123)
- Repository: [mongo_db_data_update_testing](https://github.com/Aman-Husain-123/mongo_db_data_update_testing)

## 🐛 Issues & Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Aman-Husain-123/mongo_db_data_update_testing/issues) on GitHub.

---

⭐ **Star this repository if you find it helpful!**