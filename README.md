# 🚀 JetBrainX

**JetBrainX** is a powerful and lightweight mathematical expression solver built with Flask and SymPy. It evaluates algebraic expressions, supports differentiation and integration, and provides instant results via a simple API.

## 🌐 Live Demo

Access JetBrainX from any of the following links:
- 🔗 [jmx.vercel.app](https://jmx.vercel.app)
- 🔗 [jetmathx.vercel.app](https://jetmathx.vercel.app)
- 🔗 [jet-math-x.vercel.app](https://jet-math-x.vercel.app)

## ✨ Features
- ✅ Supports basic arithmetic operations (+, -, *, /, ^)
- ✅ Symbolic differentiation & integration
- ✅ Trigonometric functions (sin, cos, tan, etc.)
- ✅ Easy-to-use REST API
- ✅ Fast and lightweight

## 🚀 How It Works
JetBrainX processes mathematical expressions through a Flask-based API, evaluates them using SymPy, and returns JSON responses.

### Example Usage
#### Request:
```bash
https://jetmathx.vercel.app/diff(x**2,x)
```
#### Response:
```json
{
  "expression": "diff(x**2,x)",
  "result": "2*x"
}
```

## 🛠 Installation & Setup
Want to run JetBrainX locally? Follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/JetBrainX.git
cd JetBrainX
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

By default, the server will run on `http://127.0.0.1:5000/`.

## 📌 API Usage
You can send GET requests directly in the browser or using tools like **Postman** or **cURL**.

### Example Endpoints
| Endpoint | Description |
|----------|-------------|
| `/2+3*5` | Basic arithmetic |
| `/sin(3.14)` | Trigonometric function |
| `/cos(0)` | Cosine function |
| `/tan(45)` | Tangent function |
| `/diff(x^3, x)` | Differentiation |
| `/integrate(x^2, x)` | Integration |
| `/factor(x^2 - 4)` | Factorization |
| `/expand((x-2)*(x+2))` | Expansion |
| `/simplify((x^2 + 2*x + 1)/(x+1))` | Simplification |
| `/limit(sin(x)/x, x, 0)` | Limit Calculation |

## 🛠 Bug Reports & Improvements
Found a bug or have a feature suggestion? Feel free to open an issue on GitHub!

### 🔥 Known Issues & Improvements Needed
1️⃣ **Cool Responsive Home Page** - A front-end UI is needed to improve user experience. <br>
2️⃣ **Whitespace Handling** - Expressions with encoded spaces (e.g., `%20`) result in errors. Needs a fix for proper parsing.

## 👨‍💻 Technologies Used
- **Flask** - Web framework
- **SymPy** - Symbolic mathematics library
- **Vercel** - Deployment platform

## 💡 Future Enhancements
- ✅ Support for complex numbers
- ✅ Graph plotting feature
- ✅ Web UI for easier interaction

## 🏆 Contributors
- **Vivek Jetani (NoahJet)** – Creator & Developer

## 📜 License
This project is open-source under the **MIT License**.

---
🔥 *JetBrainX - The Smartest Way to Evaluate Math Expressions!*

