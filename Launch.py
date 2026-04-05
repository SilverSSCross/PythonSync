# Launch.py
import sys
from pathlib import Path

def setup_environment():
    """Añade src al path de Python"""
    project_root = Path(__file__).parent
    src_path = project_root / 'src'
    
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))

def main():
    """Punto de entrada principal"""
    setup_environment()
    
    # Importar DESPUÉS de configurar el path
    from src import MainCLI
    
    # Ejecutar
    cli = MainCLI()
    cli.run()

if __name__ == "__main__":
    main()