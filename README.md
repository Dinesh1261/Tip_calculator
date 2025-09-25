# 💰 Tip Calculator

A simple, user-friendly **Tip Calculator** built in Python that helps you split bills fairly among friends, including tips!

## 📌 Features

- Accepts total bill amount (with input validation)
- Lets you choose a tip percentage (e.g., 10%, 12%, 15% — or any value between 0–100%)
- Splits the total (bill + tip) evenly among any number of people
- Handles invalid inputs gracefully (non-numbers, zero/negative people, etc.)
- Outputs each person's share formatted to **2 decimal places** (e.g., `$24.50`)

## 🚀 How to Use

1. **Clone or download** this repository.
2. Open your terminal and navigate to the project folder.
3. Run the script using Python:

```bash
python tip_calculator.py
```

4. Follow the prompts:
   - Enter the total bill (e.g., `50.75`)
   - Enter tip percentage (e.g., `15`)
   - Enter number of people (e.g., `4`)

5. See the result:
   ```
   Each person should pay: $14.29
   ```

## 🛡️ Input Validation

The script includes robust error handling:
- Non-numeric bill → error message
- Tip percentage outside 0–100% → rejected
- Zero or negative number of people → rejected
- Non-integer inputs for tip or people → caught and explained

## 📝 Example

```
Welcome to the Tip Calculator!
What was the total bill? $80
How much tip would you like to give? (e.g., 10, 12, or 15) 15
How many people to split the bill? 3
Each person should pay: $30.67
```

## 🧑‍💻 Requirements

- Python 3.x

No external dependencies — runs with standard Python libraries only!

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

✨ **Perfect for restaurants, cafes, or splitting dinner bills with friends!** ✨
