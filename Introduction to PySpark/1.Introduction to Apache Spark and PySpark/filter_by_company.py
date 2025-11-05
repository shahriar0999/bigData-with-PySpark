# Average salary for entry level in Canada
CA_jobs = ca_salaries_df.filter(ca_salaries_df["company_location"] == "CA").filter(ca_salaries_df['experience_level']
 == "EN").groupBy().avg("salary_in_usd")

# Show the result
CA_jobs.show()