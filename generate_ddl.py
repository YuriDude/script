import datetime;

C_FILE_IN = "Arc_struct.csv"
C_FILE_OUT ="generated_ddl.sql"
C_CREATE = "CREATE TABLE "

file_in =  open(C_FILE_IN,"r")
file_lines = file_in.readlines()
file_out = open (C_FILE_OUT,"w")
current_table = str()
tables_built = 0
columns_built = 0

for line in file_lines:
    t_list = line.split(",")

    if len(current_table) == 0:
        # first iteration, new table + first record
        current_table = str( t_list[0] )
        tables_built += 1
        columns_built += 1
        file_out.write(f"{C_CREATE}  {current_table} (\n " )
        file_out.write(f"  {t_list[1]}  {t_list[2]} " )
    else:        
        if current_table == str( t_list[0] )   :
             
            columns_built +=1
            file_out.write(f" ,{t_list[1]}  {t_list[2]} " )
            
        else:
            # new table + first record
            current_table = str( t_list[0] )
            tables_built += 1
            columns_built += 1
            file_out.write(");\n " )                        
            file_out.write(f"{C_CREATE}  {current_table} (\n " )    
            file_out.write(f"  {t_list[1]}  {t_list[2]} " )
            
    
file_out.write(f");" )   
    
file_in.close()
file_out.close()

print (f"Done: {datetime.datetime.now()}")
print (f"Tables Built: {tables_built}")
print (f"Columns Built: {columns_built}")