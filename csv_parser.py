import csv

domain_col_name = "email ID"
domain_list = []

with open("domains.csv", "r") as f:
  data = csv.DictReader(f)
  for row in data:
      for dom in row[domain_col_name].split(";"):
        split = dom.strip().split("@")
        if len(split) == 2 and split[1] not in domain_list:
          domain_list.append(split[1])
  
  print(domain_list)
    
  with open("subjects.txt", "w") as s:
     for item in domain_list:
        s.write(item.strip())