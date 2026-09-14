import subprocess

print('@@MANTENIMIENTO DEL PC@@')

while True:
    print('1. Reparar Windows')
    print('2. Limpiar Red')
    print('3. Buscar actualizaciones')
    print('4. Buscar Virus')
    print('5. Quitar archivos temporales')
    print('6. Salir')

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
        print('Buscando actualizaciones de Windows...')
        subprocess.run([
            'powershell',
            '-Command',
            'Install-Module PSWindowsUpdate -Force -Scope CurrentUser; Get-WindowsUpdate; Install-WindowsUpdate -AcceptAll -AutoReboot'
        ])

    elif opcion == '4':
        print('Iniciando análisis rápido...')
        subprocess.run([
            'powershell',
            '-Command',
            'Start-MpScan -ScanType QuickScan'
        ])

    elif opcion == '5':
        print('Eliminando archivos temporales...')
        subprocess.run('del /q /f /s %temp%\\*', shell=True)
        subprocess.run('del /q /f /s C:\\Windows\\Temp\\*', shell=True)

    elif opcion == '6':
        print('Saliendo del programa...')
        break

    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 6.')