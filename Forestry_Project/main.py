#=================================================
#PROJECT:FORESTRY_ECO & REVENUE SIMULATIOR
#=================================================
# Auther:  Harshrajbhar
# Conceptualized with Team Gemini

tree_database = {
    "Teak": {"oxygen": 20, "price": 15000},
    "Neem": {"oxygen": 50, "price": 5000},
    "Mango": {"oxygen": 35, "price": 8000}
}

# STEP 2: Core Simulation Function
def run_forestry_simulation(tree_type, tree_count, total_years):
    print("\n" + "="*50)
    print(f"🌲 STARTING FORESTRY SIMULATION FOR {tree_type.upper()} 🌲")
    print("="*50)
    
    # Safety Check: Agar ped database me nahi hai
    if tree_type not in tree_database:
        print(f"[ERROR] '{tree_type}' humare database me nahi hai!")
        return

    # Database se selected ped ka data nikalna
    selected_tree = tree_database[tree_type]
    
    # Initial Variables (Shuruati counters)
    total_oxygen_produced = 0
    current_valuation = selected_tree["price"] * tree_count
    initial_valuation = current_valuation  # Final profit check karne ke liye

    # STEP 3: Simulation Loop (Logic Building)
    for year in range(1, total_years + 1):
        # 1. Oxygen Calculation: Har saal naye oxygen ko purane total me jodna
        yearly_oxygen = selected_tree["oxygen"] * tree_count
        total_oxygen_produced = total_oxygen_produced + yearly_oxygen
        
        # 2. Financial Compound Growth: Har saal forest ki value 12% badhna
        current_valuation = current_valuation + (current_valuation * 0.12)
        
        # 3. Year-by-Year Dashboard Display (f-string magic)
        print(f"Year {year:02d} 📅 | Total Oxygen: {total_oxygen_produced:,} kg | Forest Value: ₹{current_valuation:,.2f}")

    # STEP 4: Final Summary Report (Attractive Dashboard)
    total_profit = current_valuation - initial_valuation
    
    print("\n" + "="*50)
    print("📊 FINAL ECO-IMPACT & REVENUE REPORT")
    print("="*50)
    print(f"🚀 Total Simulation Period : {total_years} Years")
    print(f"🌳 Total Trees Planted     : {tree_count} {tree_type} Trees")
    print(f"💨 Total Oxygen Contributed: {total_oxygen_produced:,} kg (Eco Contribution!) 🌍")
    print(f"💰 Final Forest Valuation  : ₹{current_valuation:,.2f}")
    print(f"📈 Net Estimated Profit    : ₹{total_profit:,.2f}")
    print("="*50 + "\n")


# =================================================================
# STEP 5: User Interaction & Execution
# =================================================================
print("Welcome to Forestry Eco-Simulator!")
# `.strip().capitalize()` se agar user 'neem' ya '  neem ' likhega toh wo apne aap 'Neem' ho jayega
user_tree = input("Enter tree type (Teak / Neem / Mango): ").strip().capitalize()
user_count = int(input("How many trees did you plant?: "))
user_years = int(input("Enter simulation period (in years): "))

# Machine ko start karna
run_forestry_simulation(user_tree, user_count, user_years)