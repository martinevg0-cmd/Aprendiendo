import subprocess
import os

def encontrar_malwarebytes():
    rutas = [
        r'C:\Program Files\Malwarebytes\Malwarebytes.exe',
        r'C:\Program Files (x86)\Malwarebytes\Malwarebytes.exe',
    ]
    for ruta in rutas:  
        if os.path.exists(ruta):  
            return ruta
    return None

print("⚠️  IMPORTANTE: Ejecuta este script como ADMINISTRADOR")
print("Click derecho en la ventana de CMD → Ejecutar como administrador\n")
print('@@MANTENIMIENTO DEL PC@@\n')

while True:
    print('1. Reparar Windows')
    print('2. Limpiar Red')
    print('3. Buscar actualizaciones')
    print('4. Buscar Virus')
    print('5. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        print('Reparando Windows...')
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/CheckHealth'])
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/ScanHealth'])
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/RestoreHealth'])
        subprocess.run(['sfc', '/scannow'])
    
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
        ruta = encontrar_malwarebytes()
        if ruta:
            subprocess.Popen(ruta)  
        else:
            print('❌ Malwarebytes no encontrado. Por favor, instálalo.')
    
    elif opcion == '5':
        print('Saliendo del programa...')
        break
    
    else:
        print('❌ Opción no válida. Selecciona 1-5.')
