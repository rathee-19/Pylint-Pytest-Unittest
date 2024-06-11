import datetime

# Get year input from the user

def date_month (year):
  t  = year
  date_check = t % 10*10
  t = t//10
  date_check = date_check + t%10 
  t = t//10
  month_check = t % 10*10
  t = t//10
  month_check = month_check + t%10 
  
  try:
    object = datetime.date(year, month_check, date_check)
    print(object.strftime("%d %m %Y"))
    return object.strftime("%d %m %Y")
  except:
    print("Invalid")
    return "invalid"   
  
def main():

    year = int(input("Enter year: "))   
    date_month(year)

if __name__ == "__main__":
   main()