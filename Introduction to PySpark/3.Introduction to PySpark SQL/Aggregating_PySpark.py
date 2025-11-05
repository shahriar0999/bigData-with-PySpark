# Find the minimum salaries for small companies
salaries_df.filter(salaries_df.company_size == "S").groupBy().min('salary_in_usd').show()

# Find the maximum salaries for large companies
salaries_df.filter(salaries_df.company_size == "L").groupBy().max("salary_in_usd").show()