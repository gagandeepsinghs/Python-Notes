const questionsData = [
    // ---------------- VARIABLES ----------------
    {
        id: 1,
        topic: "1. VARIABLES",
        title: "Create Basic Variables",
        description: "Create variables named name, age, and city and store your name, age, and city in them. Print all three values.",
        template: "# Write your code here\n",
        solution: 'name = "Gagan"\nage = 25\ncity = "Delhi"\n\nprint(name)\nprint(age)\nprint(city)'
    },
    {
        id: 2,
        topic: "1. VARIABLES",
        title: "Print Values",
        description: "Create two variables a = 10 and b = 20. Print their values.",
        template: "# Write your code here\n",
        solution: 'a = 10\nb = 20\nprint(a)\nprint(b)'
    },
    {
        id: 3,
        topic: "1. VARIABLES",
        title: "Calculate Total Price",
        description: "Create variables price = 500 and quantity = 3. Calculate and print the total price.",
        template: "# Write your code here\n",
        solution: 'price = 500\nquantity = 3\ntotal_price = price * quantity\nprint(total_price)'
    },
    {
        id: 4,
        topic: "1. VARIABLES",
        title: "Student Marks",
        description: "Create variables student_name and marks. Store a student's name and marks and print both values.",
        template: "# Write your code here\n",
        solution: 'student_name = "Rahul"\nmarks = 95\nprint(student_name)\nprint(marks)'
    },
    {
        id: 5,
        topic: "1. VARIABLES",
        title: "Swap Variables",
        description: "Create two variables a = 10 and b = 20. Swap their values and print the result.",
        template: "# Write your code here\n",
        solution: 'a = 10\nb = 20\n\na, b = b, a\n\nprint("a =", a)\nprint("b =", b)'
    },

    // ---------------- USER INPUT ----------------
    {
        id: 6,
        topic: "2. USER INPUT",
        title: "Name Input",
        description: "Take the user's name as input and print it.",
        template: "# Note: Using input() will open a popup prompt.\n",
        solution: 'name = input("Enter your name: ")\nprint("Your name is:", name)'
    },
    {
        id: 7,
        topic: "2. USER INPUT",
        title: "Age Input",
        description: "Take the user's age as input and print it.",
        template: "# Note: Using input() will open a popup prompt.\n",
        solution: 'age = input("Enter your age: ")\nprint("Your age is:", age)'
    },
    {
        id: 8,
        topic: "2. USER INPUT",
        title: "Sum of Two Numbers",
        description: "Take two numbers from the user and print their sum. (Remember to convert input to integer!)",
        template: "# Write your code here\n",
        solution: 'num1 = int(input("Enter first number: "))\nnum2 = int(input("Enter second number: "))\nprint("Sum is:", num1 + num2)'
    },
    {
        id: 9,
        topic: "2. USER INPUT",
        title: "Name and City Input",
        description: "Take the user's name and city as input and print both values.",
        template: "# Write your code here\n",
        solution: 'name = input("Enter name: ")\ncity = input("Enter city: ")\nprint("Name:", name)\nprint("City:", city)'
    },
    {
        id: 10,
        topic: "2. USER INPUT",
        title: "Calculate Total Bill",
        description: "Take the product price and quantity from the user and calculate the total bill.",
        template: "# Write your code here\n",
        solution: 'price = float(input("Enter price: "))\nquantity = int(input("Enter quantity: "))\ntotal_bill = price * quantity\nprint("Total Bill:", total_bill)'
    },

    // ---------------- F-STRING ----------------
    {
        id: 11,
        topic: "3. F-STRING",
        title: "Sentence using F-string",
        description: "Create name and age variables and print a sentence using an f-string.",
        template: "# Write your code here\n",
        solution: 'name = "Amit"\nage = 22\nprint(f"My name is {name} and I am {age} years old.")'
    },
    {
        id: 12,
        topic: "3. F-STRING",
        title: "College Info",
        description: "Create name, course, and college variables and display them in one sentence using an f-string.",
        template: "# Write your code here\n",
        solution: 'name = "Priya"\ncourse = "B.Tech"\ncollege = "IIT Delhi"\nprint(f"{name} is studying {course} at {college}.")'
    },
    {
        id: 13,
        topic: "3. F-STRING",
        title: "Product Details",
        description: 'Create product = "Laptop" and price = 50000. Display both using an f-string.',
        template: 'product = "Laptop"\nprice = 50000\n# Write your code here\n',
        solution: 'product = "Laptop"\nprice = 50000\nprint(f"The price of {product} is ₹{price}.")'
    },
    {
        id: 14,
        topic: "3. F-STRING",
        title: "Input with F-string",
        description: "Take the user's name and age as input and display them using an f-string.",
        template: "# Write your code here\n",
        solution: 'name = input("Enter name: ")\nage = input("Enter age: ")\nprint(f"User {name} is {age} years old.")'
    },
    {
        id: 15,
        topic: "3. F-STRING",
        title: "Student Marks F-string",
        description: "Create name, marks, and grade variables and display all three using one f-string.",
        template: "# Write your code here\n",
        solution: 'name = "Ravi"\nmarks = 85\ngrade = "A"\nprint(f"Student {name} scored {marks} marks and got grade {grade}.")'
    }
];
