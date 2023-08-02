def calculate_total_contributions(contributions_list):
    total_contributions = 0

    for entry in contributions_list:
        amount_str = entry.split()[-1]
        amount = int(amount_str[:-1]) if amount_str.endswith('✅') else int(amount_str)
        total_contributions += amount

    return total_contributions
contributions_list = [
    "Reuben Busienei 5550✅",
    "Clementine koech 4700✅",
    "marshal kiprop 4430✅",
    "Silas Kitur 2030✅",
    "Meshack kipkemboi 5230✅",
    "Duncan kipchirchir 4000✅",
    "Kiprop &KIPKURUI 3230✅",
    "julia chepngetich 3030",
    "Ruth kiplagat 5410✅",
    "Derrick korir 3020✅",
    "Robert kiptoo 2930✅",
    "David keino 12100",
    "Isaac Kitur 1900✅",
    "Tuwei Hosea 1700✅",
    "Silas sugut 3000✅",
    "Nelly kirop 2000✅",
    "Ismael kiptanui 1000✅",
    "Justus samoei 2900✅",
    "Amos kemboi 2000✅",
    "Jennifer jepkirui 500✅",
    "Nancy samoei 500✅",
    "Tecla cheruyiot 500✅",
]

# Calculate the total contributions
total_contribution_amount = calculate_total_contributions(contributions_list)

# Display the result
print("Total Contribution Amount:", total_contribution_amount)
