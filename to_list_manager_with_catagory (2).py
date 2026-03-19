tasks = []

while True:
    print("\n1. Add Task | 2. View All | 3. Filter by Category | 4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        desc = input("Task description: ")
        deadline = input("Deadline (e.g. Friday): ")
        priority = input("Priority (High/Low): ")
        cat = input("Category (Work/Home/School): ")
        tasks.append({"desc": desc, "deadline": deadline, "pri": priority, "cat": cat})
    elif choice == '2' or choice == '3':
        filt = input("Enter category to filter (or press Enter for all): ")
        for t in tasks:
            if not filt or t['cat'].lower() == filt.lower():
                print(f"[{t['pri']}] {t['desc']} - Due: {t['deadline']} ({t['cat']})")
    elif choice == '4': 
        break
    