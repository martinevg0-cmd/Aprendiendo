import subprocess

print('@@MANTENIMIENTO DEL PC@@')
print('Reparar Windows')
print('Limpiar Red')
print('Buscar actualizaciones')
print('Buscar Virus')

while True:
    print('1. Reparar Windows')
    print('2. Limpiar Red')
    print('3. Buscar actualizaciones')
    print('4. Buscar Virus')
    print('5. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        print('Reparando Windows...')
        subprocess.run(['sfc', '/scannow'])
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/CheckHealth'])
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/ScanHealth'])
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/RestoreHealth'])
    elif opcion == '2':
        print('Limpiando Red...')
        subprocess.run(['ipconfig', '/flushdns'])
        subprocess.run(['netsh', 'winsock', 'reset'])
        subprocess.run(['netsh', 'int', 'ip', 'reset'])
    elif opcion == '3':
        print('Buscando actualizaciones...')
        subprocess.run(['UsoClient', 'StartScan'])
        
    elif opcion == '4':
        print('Buscando Virus...')
        subprocess.Popen([r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Malwarebytes.lnk'])
    
        
    elif opcion == '5':
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 5.')
