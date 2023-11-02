#! /bin/bash 
var_log_porciento=$(df -h  /dev/sda1 | awk 'NR==2 {print $5}' | tr -d '%')
directorio_log="/var/log/"
directorio_log_OpenR="/var/log/openresty/"

if [ "$var_log_porciento" -ge "90" ];
    then
    rm -rf /var/log/*.gz    # borra los comprimidos

    for file in "$directorio_log"/*; do   # Usar un bucle for para recorrer los archivos en el directorio
        if [ -f "$file" ]; then
        > "$file"  # Redirigir la salida nula al archivo para dejarlo en blanco
        fi
    done  
    for file in "$directorio_log_OpenR"/*; do  
        if [ -f "$file" ]; then
        > "$file"    # Redirigir la salida nula al archivo para dejarlo en blanco
        fi
    done 
    
    journalctl --vacuum-time=1d   #borra registros del sitema
fi

