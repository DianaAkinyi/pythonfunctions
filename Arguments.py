#  def year_of_birth(name,age):
#      year=2023-age
#      print(f"Hello{name},you were born in{year}")
    
def my_country(country="kenya"):
     print(f"Hello you are from{country}")

def hello(*names):
    for name in names:
     print(f"Hello{name}") 

def sum(*nums):
   answer =0
   for num in nums :
      answer +=num
      print (answer)
def multiply_many(**kwargs):
    answer =1
    for num in kwargs.values():
       answer*=kwargs
    print (answer)

def concatenate_args(*countries):
      answer =""
      for country in countries:
         answer +=country
      return answer

def concatenate_kwargs(**countries):
      answer =""
      for country in countries.values():
         answer +=country
      return answer

   