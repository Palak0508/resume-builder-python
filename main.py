# Improved Resume Builder (Simple + Slightly Professional)

import os

print("========== RESUME BUILDER ==========\n")

# Menu
print("1. Create Resume")
print("2. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("\nEnter your details:\n")

    # Basic Details
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    # Extra fields (NEW)
    objective = input("Career Objective: ")
    education = input("Education: ")
    skills = input("Skills (comma separated): ")
    projects = input("Projects: ")
    hobbies = input("Hobbies: ")

    # Validation
    if name == "" or email == "" or phone == "":
        print("\n❌ Error: Name, Email, and Phone are required!")
    else:
        print("\nCreating your resume...\n")

        # Resume Format (Improved)
        resume = "\n========== RESUME ==========\n\n"
        resume += "Name      : " + name + "\n"
        resume += "Email     : " + email + "\n"
        resume += "Phone     : " + phone + "\n"

        resume += "\n--- OBJECTIVE ---\n"
        resume += objective + "\n"

        resume += "\n--- EDUCATION ---\n"
        resume += education + "\n"

        resume += "\n--- SKILLS ---\n"
        resume += skills + "\n"

        resume += "\n--- PROJECTS ---\n"
        resume += projects + "\n"

        resume += "\n--- HOBBIES ---\n"
        resume += hobbies + "\n"

        resume += "\n============================\n"

        # Save file
        file = open("resume.txt", "w")
        file.write(resume)
        file.close()

        print("✅ Resume created successfully!")

        # Show file location
        print("📁 Saved at:", os.getcwd())

        # Extra logic (small professional touch)
        if "Python" in skills:
            print("💡 Good job! Python is a valuable skill.")
        else:
            print("💡 Tip: Consider adding programming skills like Python.")

elif choice == "2":
    print("Exiting program...")

else:
    print("❌ Invalid choice. Please run again.")