import PySimpleGUI as sg

def criar_janela_cadastro_kit(kits_atuais):
    sg.theme('DarkBlue14')

    layout_coluna_esquerda = [
        [sg.Text('Adicionar Novo Kit', font=('Helvetica', 16))],
        [sg.Text('Nome do Kit*', size=(12, 1)), sg.Input(key='-NOME_KIT-')],
        [sg.Text('Descrição*', size=(12, 1)), sg.Multiline(key='-DESCRICAO-', size=(35, 4))],
        [sg.Text('Valor (R$)*', size=(12, 1)), sg.Input(key='-VALOR-', size=(15,1))],
        [sg.Button('Adicionar Kit', key='-ADICIONAR_KIT-')]
    ]

    layout_coluna_direita = [
        [sg.Text('Kits do Evento', font=('Helvetica', 16))],
        [sg.Listbox(values=kits_atuais, key='-LISTA_KITS-', size=(40, 8))],
        [sg.Button('Remover Selecionado', key='-REMOVER_KIT-')]
    ]

    layout = [
        [sg.Column(layout_coluna_esquerda), sg.VSeperator(), sg.Column(layout_coluna_direita)],
        [sg.HorizontalSeparator()],
        [sg.Button('Salvar e Voltar', key='-SALVAR_KITS-')]
    ]
    
    return sg.Window('PaceHub - Cadastro de Kits do Evento', layout, finalize=True, modal=True)


def criar_janela_novo_evento():
    sg.theme('DarkBlue14')

    layout = [
        [sg.Text('Criar Novo Evento', font=('Helvetica', 20))],
        [sg.Text('Nome do Evento*', size=(25,1)), sg.Input(key='-NOME_EVENTO-')],
        [sg.Text('Data do Evento*', size=(25,1)), sg.Input(key='-DATA_EVENTO-', size=(12,1), readonly=True), sg.Button('Selecionar', key='-BOTAO_CALENDARIO_EVENTO-')],
        [sg.Text('Distância (km)*', size=(25,1)), sg.Combo(['5', '10', '21', '42'], key='-DISTANCIA-', readonly=True)],
        [sg.Text('Kits do Evento*', size=(25,1)), sg.Button('Cadastrar Kits', key='-CADASTRAR_KITS-'), sg.Text('', key='-STATUS_KITS-')],
        [sg.Text('Local de Largada*', size=(25,1)), sg.Input(key='-LOCAL-')],
        [sg.Text('Tempo de Corte*', size=(25,1)),
         sg.Input(key='-HORAS-', size=(4,1), default_text='6'), sg.Text('horas e'),
         sg.Input(key='-MINUTOS-', size=(4,1), default_text='0'), sg.Text('minutos')],
        [sg.Text('Data Limite para Cancelamento*', size=(25,1)), sg.Input(key='-DATA_CANCEL-', size=(12,1), readonly=True), sg.Button('Selecionar', key='-BOTAO_CALENDARIO_CANCEL-')],
        [sg.Text('* Campos obrigatórios', text_color='red')],
        [sg.Button('Salvar Evento', key='-SALVAR_EVENTO-'), sg.Button('Cancelar', key='-CANCELAR-')]
    ]

    return sg.Window('PaceHub - Novo Evento', layout, finalize=True, resizable=True)

def exibir_popup_erro(titulo: str, mensagem: str):
    """Exibe uma janela de pop-up de erro com título e mensagem personalizados."""
    sg.popup(titulo, mensagem, title='Erro')

def exibir_popup_sucesso(titulo: str, mensagem: str):
    """Exibe uma janela de pop-up de sucesso padronizada."""
    sg.popup(titulo, mensagem, title="Sucesso")