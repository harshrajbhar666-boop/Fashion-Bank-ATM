try:
    # 1. Input file se data read karna
    with open("input.txt", "r") as input_file:
        data = input_file.read()
    
    # 2. Data ko process karna (Uppercase mein badalna)
    processed_data = data.upper() 

    # 3. Sahi variable alias use karke processed data ko write karna
    with open("output.txt", "w") as output_file:
        output_file.write(processed_data)
       
    print("File processing completed successfully!")

except FileNotFoundError:
    print("Error: 'input.txt' file are not found. Create a file.")
except Exception as e:
    print(f"Different error occurred: {e}")
