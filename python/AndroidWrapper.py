from ppadb.client import Client as AdbClient
import time

class AndroidAutomation:
    def __init__(self, device_serial=None):
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.device = None
        self.device_serial = device_serial

    def connect_device(self):
        devices = self.client.devices()
        if not devices:
            raise Exception("No devices connected.")
        
        if self.device_serial:
            for device in devices:
                if device.serial == self.device_serial:
                    self.device = device
                    break
            else:
                raise Exception(f"Device with serial {self.device_serial} not found.")
        else:
            # Assume the first connected device if no serial is specified
            self.device = devices[0]

    def execute_script(self, script):
        if not self.device:
            raise Exception("Device not connected. Call connect_device() first.")

        # Example: Mapeamento dos IDs e XPath
        element_ids = {
            "search_bar": "com.example.app:id/searchBar",
            "search_button": "com.example.app:id/searchButton",
            # Adicione outros IDs conforme necessário
        }

        # Seu script de automação aqui
        self.device.shell(f"input tap {element_ids['search_bar']}")  # Exemplo de toque no campo de pesquisa
        time.sleep(2)  # Aguardar para garantir que a ação anterior seja concluída
        self.device.shell(f"input text 'Produto desejado'")  # Exemplo de entrada de texto
        self.device.shell(f"input tap {element_ids['search_button']}")  # Exemplo de toque no botão de pesquisa

    def close_connection(self):
        if self.device:
            self.device.close()
            self.device = None