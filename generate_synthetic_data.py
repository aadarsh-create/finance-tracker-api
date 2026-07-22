import random
import csv

expense_templates = {
    "food": ["{vendor} order", "Lunch at {vendor}", "Dinner at {vendor}","Groceries from {vendor}", "{vendor} meal delivery", "Coffee at {vendor}"   ],
    "transport": ["{vendor} ride", "Bus ticket to {place}", "Fuel at {vendor}","Taxi fare", "Metro card recharge", "{vendor} cab booking"],
    "entertainment": ["{vendor} subscription", "Movie tickets at {vendor}", "Concert ticket","Gaming purchase on {vendor}", "{vendor} streaming renewal"],
    "health": ["Medicine purchase at {vendor}", "Doctor consultation", "{vendor} pharmacy bill","Health checkup", "Insurance premium", "Dental visit" ],
    "education": ["Course fee on {vendor}", "Textbook purchase", "{vendor} certification","Tuition payment", "Online course subscription", "Library fine","Bought textbooks", "Book purchase from {vendor}", "Study material purchase","Stationery for college", "Bought reference books"],
    "other": ["Miscellaneous purchase", "Gift bought at {vendor}", "Stationery from {vendor}","{vendor} purchase", "Cashback reward", "Refund from {vendor}"  ],
}

income_templates = {
    "food": ["Meal allowance credited", "Food reimbursement", "{vendor} meal voucher refund"],
    "transport": ["Travel reimbursement", "Fuel allowance credited", "{vendor} fare refund"],
    "entertainment": ["Ticket resale income", "{vendor} refund", "Prize money from contest"],
    "health": ["Medical reimbursement", "Insurance claim received", "Health insurance payout"],
    "education": ["Scholarship received", "Course stipend credited", "Tuition refund"],
    "other": ["Cashback reward", "Gift received", "Miscellaneous refund"],
}

vendors = ["Swiggy", "Zomato", "Amazon", "Uber", "Ola", "Netflix", "Apollo Pharmacy","Udemy", "Coursera", "BigBasket", "Flipkart", "Spotify", "BookMyShow", "IRCTC"]
places = ["airport", "campus", "station", "city center", "mall"]


rows = []
for category, temps in expense_templates.items():
    for _ in range(80):  # ~80 per category → ~480 total
        t = random.choice(temps)
        note = t.format(vendor=random.choice(vendors), place=random.choice(places))
        rows.append({"description": note, "category": category,"type":"expense"})

for category, temps in income_templates.items():
    for _ in range(30):
        t = random.choice(temps)
        note = t.format(vendor=random.choice(vendors))
        rows.append({"description": note, "category": category,"type":"income"})

random.shuffle(rows)
with open("transactions_labeled.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["description", "category","type"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} synthetic rows")