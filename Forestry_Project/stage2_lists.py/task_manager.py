# =================================================================
# 🤖 MINI PROJECT: SMART TASK MANAGER
# =================================================================

# Shuruat me list ekdum khali hai
tasks = []

print("--- 🛠️ AI TASK MANAGER STARTED ---")

# 1. Using .append() -> Tasks add karna
tasks.append("Complete Python Stage 2 Revision")
tasks.append("Push Forestry project to GitHub")
tasks.append("Review Team Devdoots next meeting agenda")

# 2. Using len() -> Total tasks check karna
print(f"\n📊 Total Tasks Pending: {len(tasks)}")

# 3. Using Indexing -> Sabse pehla task dekhna (Top Priority)
print(f"🎯 Top Priority Task  : {tasks[0]}")

# 4. Using .insert() -> Emergency task ko ekdum top (0 index) par daalna
tasks.insert(0, "Urgent: Fix VS Code Terminal Error")
print(f"\n⚠️ Urgent Task Added! New Top Priority: {tasks[0]}")

print("\n--- Current To-Do List ---")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# 5. Using .remove() -> Jab ek kaam poora ho jaye toh use delete karna
print("\n✅ Doing task: 'Urgent: Fix VS Code Terminal Error'...")
tasks.remove("Urgent: Fix VS Code Terminal Error")

print(f"\n📊 Remaining Tasks Count: {len(tasks)}")