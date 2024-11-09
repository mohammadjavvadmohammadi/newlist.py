color_list = ( "red" , "blue" , "green" , 12 , 7 )
for item in color_list:
    if isinstance(item, str):
        print(f" {item} is mu color")
    elif isinstance(item, int):
        print("Error")
        
               