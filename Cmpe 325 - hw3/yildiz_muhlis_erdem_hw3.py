from functools import reduce 

def calculate(total_insulin, my_new_list): 
  
  unit_insulin_lower = 1800 / total_insulin
  # I used the formulas given in the question to find out how much unicillin the patient needs.
  insulin_needed = []
  for value in my_new_list:
    insulin_needed.append(value  / unit_insulin_lower)

  return insulin_needed


patients_bg_dic = {} # This dictionary keeps patients name as a key and patient's 12-hour blood glucose values as values.
patients_insulin_dic={} # This dictionary keeps patients name as a key and it also keeps insulin needed and over_120_glucose_val_list as tuple as a value.


for i in range(5):

  # Get 5 patients name and patient's 12-hour blood glucose values
  name = input("Enter patient name: ")


  # Here's the reason why I'm using the map() and split() functions: Python normally takes all input as strings.
  # Here, I separated all the numbers I wrote with spaces with split() and converted these values to int values with map(). Finally, I put these numbers in the list.
  glucose_val_list = list(map(int, input("Enter patient's 12-hour blood glucose values: ").split())) 
  

  # Store name and glucose values in dictionary
  patients_bg_dic[name] = glucose_val_list


  # Using lambda and filter, I selected the values greater than 120 in the existing list and put them in my new list.
  over_120_glucose_val_list = list(filter(lambda x: x > 120, glucose_val_list))
  print( "Glucose values over 120 mg/dL: " ,over_120_glucose_val_list  )
  

  num_insulin = int(input("How many times did you take insulin in 12 hours? : "))
  insulin_doses = list(map(int, input("Enter insulin doses: ").split()))


  # Calculate the total amount of insulin taken using reduce() function
  total_insulin = reduce(lambda x, y: x + y, insulin_doses)

  my_new_list = []  # Create a new list to keep after subtracting 120 from the values
  
  # Subtracting 120 from the values
  for i in range(len(over_120_glucose_val_list)):  
    my_new_list.append(over_120_glucose_val_list[i] - 120)  

  # Calculate how much insulin is needed for each value in over_120_glucose_val_list
  insulin_needed = calculate(total_insulin, my_new_list)
  

  my_tuple=(insulin_needed,over_120_glucose_val_list)
  patients_insulin_dic[name] = (my_tuple)


# Print patient blood glucose data
print("12-hour blood glucose values of patients in service:")
print(patients_bg_dic)


# Print how many units of insulin per patient are needed to normalize blood sugar over 120 mg/dl
for name, data in patients_insulin_dic.items():
  print(name," should take ")
  for i, x in enumerate(patients_insulin_dic[name][1]):
   print("{:.2f}".format(patients_insulin_dic[name][0][i])," unit insulin for ",x," mg/dL") 
   