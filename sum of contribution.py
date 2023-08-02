def calculate_total_contributions(contributions_list):
    total_contributions = 0

    for entry in contributions_list:
        amount_str = entry.split()[-1]
        amount = int(amount_str[:-1]) if amount_str.endswith('✅') else int(amount_str)
        total_contributions += amount

    return total_contributions
contributions_list = [
    #the list
    "1. Reuben Busienei 5550✅",
    "2. Clementine koech 4700✅",
    "3. marshal kiprop 4430✅",
    "4. Silas Kitur 2030✅",
    "5. Meshack kipkemboi 5230✅",
    "6. Duncan kipchirchir 4000✅",
    "7. Kiprop &KIPKURUI 3230✅",
    "8. julia chepngetich 3030",
    "9. Ruth kiplagat 5410✅",
    "10. Derrick korir 3020✅",
    "11. Robert kiptoo 2930✅",
    "12. David keino 12100",
    "13. Isaac Kitur 1900✅",
    "14. Tuwei Hosea 1700✅",
    "15. Silas sugut 3000✅",
    "16. Nelly kirop 2000✅",
    "17. Ismael kiptanui 1000✅",
    "18. Justus samoei 2900✅",
    "19. Amos kemboi 2000✅",
    "20. Jennifer jepkirui 500✅",
    "21. Nancy samoei 500✅",
    "22. Tecla cheruyiot 500✅",
]

# Total calculation
total_contribution_amount = calculate_total_contributions(contributions_list)
#Results
print("Total Contribution Amount:", total_contribution_amount)
