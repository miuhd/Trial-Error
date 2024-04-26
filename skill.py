class SkillManagementSystem:
def __init__(self):
self.employee_skills = {}
 
def update_skills(self, emp_id, skill_category, proficiency, years_experience):
if emp_id not in self.employee_skills:
self.employee_skills[emp_id] = {}
self.employee_skills[emp_id][skill_category] = {
'proficiency': proficiency,
'years_experience': years_experience
}
print(f"Skills updated for Employee ID {emp_id}.")
 
def view_skills(self, emp_id):
if emp_id in self.employee_skills:
print(f"Skills for Employee ID {emp_id}:")
for category, data in self.employee_skills[emp_id].items():
print(f"{category}: Proficiency - {data['proficiency']}, Years of Experience - {data['years_experience']}")
else:
print("Employee ID not found.")
 
def add_skill(self, emp_id, skill_category, proficiency, years_experience):
if emp_id not in self.employee_skills:
self.employee_skills[emp_id] = {}
self.employee_skills[emp_id][skill_category] = {
'proficiency': proficiency,
'years_experience': years_experience
}
print(f"New skill added for Employee ID {emp_id}.")
 
def generate_report(self, emp_id):
if emp_id in self.employee_skills:
print(f"Generating report for Employee ID {emp_id}...")
# Add code to generate and display the report
else:
print("Employee ID not found.")
 
def verbal_update(self, emp_id, update_text):
if emp_id in self.employee_skills:
print(f"Verbal update recorded for Employee ID {emp_id}: {update_text}")
# Add code to process the verbal update
else:
print("Employee ID not found.")
 
# Initialize the Skill Management System
sms = SkillManagementSystem()
 
# CLI Menu
while True:
print("\nSkill Management System CLI:")
print("1. Update Employee Skills")
print("2. View Employee Skills")
print("3. Add New Skill")
print("4. Generate Skill Report")
print("5. Verbal Skill Update")
print("6. Exit")
 
choice = input("Enter your choice: ")
 
if choice == '1':
emp_id = input("Enter employee ID: ")
category = input("Select the skill category to update: ")
proficiency = input("Enter proficiency level: ")
years_exp = input("Enter years of experience: ")
sms.update_skills(emp_id, category, proficiency, years_exp)
 
elif choice == '2':
emp_id = input("Enter employee ID: ")
sms.view_skills(emp_id)
 
elif choice == '3':
emp_id = input("Enter employee ID: ")
category = input("Enter the new skill category: ")
proficiency = input("Enter proficiency level: ")
years_exp = input("Enter years of experience: ")
sms.add_skill(emp_id, category, proficiency, years_exp)
 
elif choice == '4':
emp_id = input("Enter employee ID: ")
sms.generate_report(emp_id)
 
elif choice == '5':
emp_id = input("Enter employee ID: ")
update_text = input("Record a brief overview of technical activities: ")
sms.verbal_update(emp_id, update_text)
 
elif choice == '6':
print("Exiting the Skill Management System CLI.")
break
 
else:
print("Invalid choice. Please enter a valid option.")
