# Average salaries at large us companies
large_companies=salaries_df.filter(salaries_df.company_size == "L").filter(salaries_df.company_location == "US").groupBy().avg('salary_in_usd').show()

#set a large companies variable for other analytics
large_companies=salaries_df.filter(salaries_df.company_size == "L").filter(salaries_df.company_location == "US")

# Total salaries in usd
large_companies.groupBy().sum("salary_in_usd").show()