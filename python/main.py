from ppadb.client import Client as AdbClient
import time
from AndroidWrapper import AndroidAutomation


if __name__ == "__main__":
    try:
        automation = AndroidAutomation(device_serial="your_device_serial")
        automation.connect_device()

        # Execute seu script de automação aqui
        automation.execute_script()

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Certifique-se de fechar a conexão, mesmo em caso de exceção
        if automation:
            automation.close_connection()
