#  
        
def sum (*numbers):
    answer = 0 
    for num in numbers: 
        answer += num
    return answer

def multiply(*values):
    answer = 1
    for num in  values:
        answer*=num
        
    return answer

def student_artributes(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")
    
def my_country(country="Kenya"):
    print(f"Hello from {country}")    
    
        