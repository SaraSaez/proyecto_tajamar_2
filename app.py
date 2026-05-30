from gastos import GestorGastos
import ui

if __name__ == "__main__":
    #instanciar el objeto 'gestor'
    mi_gestor = GestorGastos()
    ui.ejecutar_ui(mi_gestor)