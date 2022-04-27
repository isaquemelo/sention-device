# sention-device
- Modulo de armazenamento fixo: 
 	- Armazenamento KVS - ok
 	- Ferramenta de limpeza total para limpar dados salvos - ok
 	
- Modulo de configuração inicial (ok):
	- Chama modulo de rede para criação/desativação da rede
	- Chama modulo de servidor para fornecer interface para o usuario
	- Define conexão com wifi do usuario (SSID, password) utilizando dados fornecidos pelo o servidor
	- Necessidades finais: 
		- Ter armazenado no KVS:
			- deviceId
			- SSID, password
			- user, password
		- Retornar todos os dados armazenados
		
- Modulo de autenticação:
	- Efetua requisição de auth utilizando dados do usuario e armazena o token para uso (ok)
	- Necessidades finais:
		- Receber user e password como parametros
		- Ter amazenado um token valido no KVS
		- Retornar token de autenticacao do usuario
- Modulo de rede:
	- Se conectar ao wifi com dados passados por parametro (ok)
	- Ligar rede wifi (ok)
	- Desligar rede wifi (ok)
	- Testar conexão com internet (ok)

- Modulo servidor:
	- Criar servidor web (ok)
	- Desativar servidor web
	- Fornecer API de configuração inicial (ok)
- Modulo gerente:
	- Chama modulo de configuração se necessário
	- Chama module de rede para se conectar ao wifi
	- Chama modulo de autenticação
	- Chama modulo de carregamento
	- Chama modulo de processamento
	
- Modulo de carregamento (ok):
	- Requisita configuração do usuario:
		- Se estiverem vazias continua em loop solicitando as configurações
	- Configura pinos e importações necessarias dado as configurações do usuario

- Modulo de processamento (ok):
	- Lê dados dos sensores
	- Passa dados dos sensores para o modulo de atuação
	- Passa dados dos sensores para o modulo de contato
	
- Modulo de atuação (ok):
	- Recebe dados de sensores e verifica se algum atuador deve ser acionado
	
- Modulo de contato:
	- Envia dados dos sensores recebidos para o servidor
	