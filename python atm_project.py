 # ==========================================
#         PROJECT: FASHION BANK ATM
# ==========================================
# Author: Harsh Rajbhar
# Description: A professional CLI-based ATM simulation system.

# Initial Balance Setup
balance = 500000.00  # Professional tip: Use lowercase variables & floats for currency

print("====================================")
print("    WELCOME TO THE FASHION BANK!    ")
print("====================================")

while True:
    print("\n----- ATM MAIN MENU -----")
    print("1. CHECK BALANCE")
    print("2. DEPOSIT MONEY")
    print("3. WITHDRAW MONEY")
    print("4. EXIT")
    print("-------------------------")

    # Exception safety handle karne ke liye try-except block lagaya hai
    try:
        choice = int(input("Enter your option (1-4): "))
    except ValueError:
        print("\n[ERROR] Invalid input! Please enter a number between 1 and 4.")
        continue

    # OPTION 1: Check Balance 
    if choice == 1:
        print("\n--- BALANCE DETAILS ---")
        print(f"Available Balance: ${balance:,.2f}")
    
    # OPTION 2: Deposit Money
    elif choice == 2:
        print("\n--- DEPOSIT SECTION ---")
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                balance += amount  # Short form of balance = balance + amount
                print(f"Transaction Successful! Deposited: ${amount:,.2f}")
                print(f"Total Available Balance: ${balance:,.2f}")
            else:
                print("[WARNING] Deposit amount must be greater than zero.")
        except ValueError:
            print("[ERROR] Invalid amount entered.")

    # OPTION 3: Withdraw Money
    elif choice == 3:
        print("\n--- WITHDRAWAL SECTION ---")
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount <= 0:
                print("[WARNING] Withdrawal amount must be greater than zero.")
            elif amount > balance:
                
                print("\n[TRANSACTION DENIED] Transaction Inoperable! Insufficient balance.")
                print(f"Your current balance is: ${balance:,.2f}")
            else:
                balance -= amount
                print(f"Transaction Successful! Cash Dispensed: ${amount:,.2f}")
                print(f"Remaining Balance: ${balance:,.2f}")
        except ValueError:
            print("[ERROR] Invalid amount entered.")

    # OPTION 4: Exit System
    elif choice == 4:
        print("\n====================================")
        print("  Thank you for using Fashion Bank!  ")
        print("     Your card has been ejected.     ")
        print("====================================")
        break  # Softly exits the loop

    else:
        print("\n[WARNING] Invalid choice! Please select an option from 1 to 4.")