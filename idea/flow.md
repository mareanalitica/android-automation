### **Fluxo de Mineração de Preços em Supermercados Carrefour - APP Android**

#### **Objetivo:**
O objetivo deste fluxo é automatizar a extração de preços de produtos em um supermercado específico dentro do aplicativo móvel dos Supermercados Carrefour. Vários fluxos serão executados em paralelo para diferentes supermercados, e os dados serão centralizados em um único data lake.

#### **Pré-requisitos:**
1. Dispositivos físicos ou emuladores configurados para automação.
2. Ambiente de execução com suporte para paralelismo.
3. Acesso ao aplicativo móvel do Carrefour.

#### **Passos:**

1. **Autenticação:**
   - **Caso de Teste: Verificar Login**
     - Automatizar o processo de login no aplicativo usando credenciais válidas.

2. **Seleção do Supermercado:**
   - **Caso de Teste: Escolher Supermercado**
     - Navegar até a seção de supermercados.
     - Escolher um supermercado específico para extração de preços.

3. **Pesquisa de Produtos:**
   - **Caso de Teste: Buscar Produtos e Preços**
     - Realizar a busca por produtos específicos.
     - Extrair os preços dos produtos listados.

4. **Coleta de Dados:**
   - **Caso de Teste: Armazenar Dados no Data Lake**
     - Coletar os dados de preços obtidos.
     - Enviar os dados para um data lake centralizado.

5. **Encerramento:**
   - **Caso de Teste: Logout**
     - Realizar o logout da conta no aplicativo.

#### **Execução em Paralelo:**
   - Configurar diferentes hosts para executar este fluxo simultaneamente, cada um focado em um supermercado específico.
   - As instâncias em paralelo devem usar dados de login diferentes e armazenar os resultados no mesmo data lake centralizado.

#### **Considerações:**
- Cada instância do fluxo deve ser independente e não compartilhar estados para garantir a execução em paralelo.
- O data lake deve ser acessível por todas as instâncias para centralizar os dados extraídos.