
import PySimpleGUI as sg
from visao import criar_janela_novo_evento, criar_janela_cadastro_kit, exibir_popup_erro, exibir_popup_sucesso
from evento import Evento
from kit_de_corrida import KitDeCorrida
from database import Database


def executar_criar_evento():
    # SIMULAÇÃO: No sistema completo, esta informação viria da tela de login.
    # Para este teste, vamos fixar o CPF de um organizador.
    # Certifique-se de que um organizador com este CPF existe em 'organizadores.json'
    CPF_ORGANIZADOR_LOGADO = "111.222.333-44" 

    db = Database()
    
    organizador_encontrado = any(org.cpf == CPF_ORGANIZADOR_LOGADO for org in db.carregar_organizadores())
    if not organizador_encontrado:
        from organizador import Organizador
        org_teste = Organizador("Organizador Teste", CPF_ORGANIZADOR_LOGADO, "teste@email.com")
        org_teste.senha_hash = "senha_teste" 
        db.salvar_organizador(org_teste)
        print(f"Organizador de teste com CPF {CPF_ORGANIZADOR_LOGADO} criado.")


    janela_principal = criar_janela_novo_evento()
    kits_do_evento_obj = [] 
    while True:
        window, event, values = sg.read_all_windows()

        if window == janela_principal and event in (sg.WIN_CLOSED, '-CANCELAR-'):
            break

        if event == '-CADASTRAR_KITS-':
            janela_kits = criar_janela_cadastro_kit(kits_do_evento_obj)
            
            while True:
                event_kit, values_kit = janela_kits.read()
                if event_kit in (sg.WIN_CLOSED, '-SALVAR_KITS-'):
                    break
                
                if event_kit == '-ADICIONAR_KIT-':
                    nome = values_kit['-NOME_KIT-']
                    descricao = values_kit['-DESCRICAO-']
                    valor_str = values_kit['-VALOR-']
                    
                    if nome and descricao and valor_str:
                        try:
                            valor = float(valor_str.replace(',', '.'))
                            novo_kit = KitDeCorrida(nome, descricao, valor)
                            kits_do_evento_obj.append(novo_kit)
                            janela_kits['-LISTA_KITS-'].update(values=kits_do_evento_obj)
                            
                            janela_kits['-NOME_KIT-'].update('')
                            janela_kits['-DESCRICAO-'].update('')
                            janela_kits['-VALOR-'].update('')
                        except ValueError:
                            exibir_popup_erro('O valor do kit deve ser um número válido.')
                    else:
                        exibir_popup_erro('Todos os campos do kit são obrigatórios.')
                
                if event_kit == '-REMOVER_KIT-':
                    selecionados = values_kit['-LISTA_KITS-']
                    if selecionados:
                        kit_para_remover = selecionados[0]
                        kits_do_evento_obj.remove(kit_para_remover)
                        janela_kits['-LISTA_KITS-'].update(values=kits_do_evento_obj)

            janela_kits.close()
            janela_principal['-STATUS_KITS-'].update(f'{len(kits_do_evento_obj)} kit(s) cadastrado(s).', text_color='lime')

        if event == '-SALVAR_EVENTO-':
            campos_obrigatorios = ['-NOME_EVENTO-', '-DATA_EVENTO-', '-DISTANCIA-', '-LOCAL-', '-HORAS-', '-MINUTOS-', '-DATA_CANCEL-']
            if any(not values[campo] for campo in campos_obrigatorios) or not kits_do_evento_obj:
                exibir_popup_erro('Por favor, preencha todos os campos e cadastre pelo menos um kit.')
                continue

            tempo_corte = f"{values['-HORAS-']}:{values['-MINUTOS-']}"
            distancia_str = values['-DISTANCIA-']
            
            evento = Evento(
                nome=values['-NOME_EVENTO-'],
                data=values['-DATA_EVENTO-'],
                distancia=int(distancia_str),
                local_largada=values['-LOCAL-'],
                tempo_corte=tempo_corte,
                data_limite_cred=values['-DATA_CANCEL-'],
                organizador_cpf=CPF_ORGANIZADOR_LOGADO
            )
            evento.kits = kits_do_evento_obj 
            db.salvar_evento(evento)
            
            exibir_popup_sucesso('Sucesso!', 'Evento criado e salvo no banco de dados.')
            break

    janela_principal.close()


if __name__ == '__main__':
    executar_criar_evento()