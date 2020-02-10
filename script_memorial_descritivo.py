import os
import datetime
from datetime import datetime
from datetime import date

class MemorialDescritivo:

    def __init__(self, num_conf_direito, list_conf_direito, list_dist_direito,
                txt_direito, texto_direito, add_dist_direito, n_lote_direito, n_distancia_direito,
                num_conf_esquerdo, list_conf_esquerdo, list_dist_esquerdo, txt_esquerdo, texto_esquerdo,
                add_dist_esquerdo, n_lote_esquerdo, n_distancia_esquerdo, nome_rua, largura_testada, txt_testada,
                texto_testada, num_conf_fundos, list_conf_fundos, list_dist_fundos, txt_fundos,
                texto_fundos, add_dist_fundos, n_lote_fundos, n_distancia_fundos, my_arquivo, conteudo,
                save, modo_gravacao, status_salvamento, caminho_save, file_visual, conteudo_visual, msg_retorno, opcao,
                slct, registro, new_file, novo_registro, numeral, inumeral, texto_intel, num_1, alfa_1, inum_1, ialfa_1,
                alfa, num, inum, ialfa, tl_direito, tl_esquerdo, tl_fundos, tl_testada, txt_caracteriza, caracteriza, area_total,
                perimetro, altura, cateto_m, n_lote, n_quadra
                ):

        self.numeral = numeral
        self.inumeral = inumeral
        self.texto_intel = texto_intel
        self.num_1 = num_1
        self.alfa_1 = alfa_1
        self.inum_1 = inum_1
        self.ialfa_1 = ialfa_1
        self.alfa = alfa
        self.num = num
        self.inum = inum
        self.ialfa = ialfa

        self.file_visual = file_visual
        self.conteudo_visual = conteudo_visual

        self.my_arquivo = my_arquivo
        self.conteudo = conteudo
        self.save = save
        self.modo_gravacao = modo_gravacao
        self.status_salvamento = status_salvamento
        self.caminho_save = caminho_save

        self.nome_rua = nome_rua
        self.largura_testada = largura_testada
        self.txt_testada = txt_testada
        self.texto_testada = texto_testada
        self.tl_testada = tl_testada

        self.num_conf_direito = num_conf_direito #quantidade de confrontantes
        self.list_conf_direito = list_conf_direito #armazena os confrontantes
        self.list_dist_direito = list_dist_direito #armazena as distâncias entre os confrontantes
        self.txt_direito = txt_direito #texto padrão
        self.texto_direito = texto_direito
        self.add_dist_direito = add_dist_direito #recebe a soma das distâncias dos confrontantes
        self.n_lote_direito = n_lote_direito #monta a frase de retorno do memorial
        self.n_distancia_direito = n_distancia_direito
        self.tl_direito = tl_direito

        self.num_conf_esquerdo = num_conf_esquerdo
        self.list_conf_esquerdo = list_conf_esquerdo
        self.list_dist_esquerdo = list_dist_esquerdo
        self.txt_esquerdo = txt_esquerdo
        self.texto_esquerdo = texto_esquerdo
        self.add_dist_esquerdo = add_dist_esquerdo
        self.n_lote_esquerdo = n_lote_esquerdo
        self.n_distancia_esquerdo = n_distancia_esquerdo
        self.tl_esquerdo = tl_esquerdo

        self.num_conf_fundos = num_conf_fundos #quantidade de confrontantes
        self.list_conf_fundos = list_conf_fundos #armazena os confrontantes
        self.list_dist_fundos = list_dist_fundos #armazena as distâncias entre os confrontantes
        self.txt_fundos = txt_fundos #texto padrão
        self.texto_fundos = texto_fundos
        self.add_dist_fundos = add_dist_fundos #recebe a soma das distâncias dos confrontantes
        self.n_lote_fundos = n_lote_fundos #monta a frase de retorno do memorial
        self.n_distancia_fundos = n_distancia_fundos
        self.tl_fundos = tl_fundos

        self.msg_retorno = msg_retorno
        self.opcao = opcao
        self.slct = slct
        self.registro = registro
        self.new_file = new_file
        self.novo_registro = novo_registro

        self.txt_caracteriza = txt_caracteriza
        self.caracteriza = caracteriza
        self.area_total = area_total
        self.perimetro = perimetro
        self.altura = altura
        self.cateto_m = cateto_m
        self.n_lote = n_lote
        self.n_qadra = n_quadra


    def ia_confronta(self, x):
        self.numeral = []
        self.inumeral, i = 0, 0
        while i < len(x):
            c = x[i].isnumeric()
            if c == True:
                self.numeral.append(c)
                self.inumeral += 1
            i = i + 1
        if self.inumeral == len(x):
            return 'o LOTE n.'

        self.num_1 = []
        self.alfa_1 = []
        self.inum_1, self.ialfa_1, e = 0, 0, 0
        while e < len(x):
            t = x[e].isnumeric()
            if t == True:
                self.num_1.append(x[e])
                self.inum_1 += 1
            if t == False:
                self.alfa_1.append(x[e])
                self.ialfa_1 += 1
            e = e + 1
        if (self.ialfa_1 > self.inum_1):
            return 'o confrontante'

        self.alfa, self.num = [], []
        self.inum, self.ialfa, j = 0, 0, 0
        while j < len(x):
            n = x[j].isnumeric()
            if n == True:
                self.num.append(x[j])
                self.inum += 1
            if n == False:
                self.alfa.append(x[j])
                self.ialfa += 1
            j = j + 1
        if ((self.inum - self.ialfa) == 0 or (self.inum - self.ialfa) == 1) and self.ialfa != 0:
            return 'o LOTE n.'

    def salvar_arquivo(self):
        while True:
            try:
                self.save = str(input('Salvar como: '))
                self.caminho_save = ('c:/Temp/'+self.save+'.txt')
                self.status_salvamento = os.path.exists(self.caminho_save)
                if not self.status_salvamento == False or self.status_salvamento == '':
                    raise BaseException
                break
            except BaseException:
                print('O arquivo {} já existe! \n'.format(self.save))


    def converte_decimal(self, x):
        return str(x).replace('.', ',')

    def descreve_testada(self):

        self.nome_rua = str(input('Nome da Rua: '))

        while True:
            try:
                self.largura_testada = float(input('Largura da testada: '))
                if self.largura_testada == '':
                    raise ValueError
                break
            except ValueError:
                print('Valor inválido!')

        self.txt_testada = ['Frente: ', 'Para a {}, medindo {} metros. \n']
        self.texto_testada = self.txt_testada[0]
        self.texto_testada += self.txt_testada[1].format(self.nome_rua.upper(), self.converte_decimal(self.largura_testada))
        self.tl_testada = self.largura_testada

    def descreve_lado_direito(self):

        self.list_conf_direito = []
        self.list_dist_direito = []
        self.add_dist_direito = 0
        self.texto_direito = ''

        while True:
            try:
                self.num_conf_direito = int(input('Quantidade de confrontantes (lado direito): '))
                if self.num_conf_direito == '':
                    raise ValueError
                break
            except ValueError:
                print('Digite um valor válido!')


        if self.num_conf_direito == 1:
            self.txt_direito = ['Lado direito: ', 'Dividindo com {} {}, medindo {} metros{} \n']
        else:
            self.txt_direito = ['Lado direito: ', 'Dividindo com {} {}, medindo {} metros{} ', 'Totalizando {} metros. \n']

        self.texto_direito = self.txt_direito[0]
        d = 1 #Implementa e gera a descrição do lado direito
        while d <= self.num_conf_direito:

            if d < self.num_conf_direito:
                self.pt = ';'
            elif d == self.num_conf_direito:
                self.pt = '.'

            space = ''
            while True:
                try:
                    self.n_lote_direito = str(input('{}º confrontante (lado direito): '.format(d)))
                    if self.n_lote_direito == '':
                        raise BaseException
                    v_space = ''
                    space = len(self.n_lote_direito)
                    i = 0
                    while i < space:
                            v_space += ' '
                            if self.n_lote_direito == v_space:
                                raise BaseException
                            i = i + 1
                    break
                except BaseException:
                    print('Digite um valor válido!')
                except BaseException:
                    print('Digite um valor válido!')

            while True:
                try:
                    self.n_distancia_direito = float(input('Distância: '))
                    if self.n_distancia_direito == '':
                        raise ValueError
                    break
                except ValueError:
                    print('Valor inválido!')

            self.list_conf_direito.append(self.n_lote_direito)
            self.list_dist_direito.append(self.n_distancia_direito)
            self.add_dist_direito += self.n_distancia_direito
            self.texto_direito += self.txt_direito[1].format(self.ia_confronta(self.n_lote_direito), self.n_lote_direito.upper(), self.converte_decimal(self.n_distancia_direito), self.pt)
            self.tl_direito = self.add_dist_direito
            d = d + 1

    def descreve_lado_esquerdo(self):

        self.list_conf_esquerdo = []
        self.list_dist_esquerdo = []
        self.add_dist_esquerdo = 0
        self.texto_esquerdo = ''

        while True:
            try:
                self.num_conf_esquerdo = int(input('Quantidade de confrontantes (lado esquerdo): '))
                if self.num_conf_esquerdo == '':
                    raise ValueError
                break
            except ValueError:
                print('Digite um valor válido!')

        if self.num_conf_esquerdo == 1:
            self.txt_esquerdo = ['Lado esquerdo: ', 'Dividindo com {} {}, medindo {} metros{} \n']
        else:
            self.txt_esquerdo = ['Lado esquerdo: ', 'Dividindo com {} {}, medindo {} metros{} ', 'Totalizando {} metros. \n']

        self.texto_esquerdo = self.txt_esquerdo[0]
        e = 1 #Implementa e gera a descriação do lado esquerdo
        while e <= self.num_conf_esquerdo:

            if e < self.num_conf_esquerdo:
                self.pt_ = ';'
            elif e == self.num_conf_esquerdo:
                self.pt_ = '.'

            space = ''
            while True:
                try:
                    self.n_lote_esquerdo = str(input('{}º confrontante (lado esquerdo): '.format(e)))
                    if self.n_lote_esquerdo == '':
                        raise BaseException
                    v_space = ''
                    space = len(self.n_lote_esquerdo)
                    i = 0
                    while i < space:
                            v_space += ' '
                            if self.n_lote_esquerdo == v_space:
                                raise BaseException
                            i = i + 1
                    break
                except BaseException:
                    print('Digite um valor válido!')
                except BaseException:
                    print('Digite um valor válido!')

            while True:
                try:
                    self.n_distancia_esquerdo = float(input('Distância: '))
                    if self.n_distancia_esquerdo == '':
                        raise ValueError
                    break
                except ValueError:
                    print('Valor inválido!')

            self.list_conf_esquerdo.append(self.n_lote_esquerdo)
            self.list_dist_esquerdo.append(self.n_distancia_esquerdo)
            self.add_dist_esquerdo += self.n_distancia_esquerdo
            self.texto_esquerdo += self.txt_esquerdo[1].format(self.ia_confronta(self.n_lote_esquerdo), self.n_lote_esquerdo.upper(), self.converte_decimal(self.n_distancia_esquerdo), self.pt_)
            self.tl_esquerdo = self.add_dist_esquerdo
            e = e + 1

    def descreve_fundos(self):

        self.list_conf_fundos = []
        self.list_dist_fundos = []
        self.add_dist_fundos = 0
        self.texto_fundos = ''
        self.caracteriza = ''

        while  True:
            try:
                self.num_conf_fundos = int(input('Quantidade de confrontantes (fundos): '))
                if self.num_conf_fundos == '':
                    raise ValueError
                break
            except ValueError:
                print('Digite um valor válido!')

        if self.num_conf_fundos == 1:
            self.txt_fundos = ['Fundos: ', 'Dividindo com {} {}, medindo {} metros{} \n']
            self.txt_caracteriza = ['Sendo o lote {}, da Quadra {}, com área total de {:.3f}m². \n']
        else:
            self.txt_fundos = ['Fundos: ', 'Dividindo com {} {}, medindo {} metros{} ', 'Totalizando {} metros. \n']
            self.txt_caracteriza = ['Sendo o lote {}, da Quadra {}, com área total de {:.3f}m². \n']

        self.texto_fundos = self.txt_fundos[0]
        f = 1 #Implementa e gera a descriação do lado esquerdo
        while f <= self.num_conf_fundos:

            if f < self.num_conf_fundos:
                self.ptf = ';'
            elif f == self.num_conf_fundos:
                self.ptf = '.'

            space = ''
            while True:
                try:
                    self.n_lote_fundos = str(input('{}º confrontante (fundos): '.format(f)))
                    if self.n_lote_fundos == '':
                        raise BaseException
                    v_space = ''
                    space = len(self.n_lote_fundos)
                    i = 0
                    while i < space:
                            v_space += ' '
                            if self.n_lote_fundos == v_space:
                                raise BaseException
                            i = i + 1
                    break
                except BaseException:
                    print('Digite um valor válido!')
                except BaseException:
                    print('Digite um valor válido!')

            while True:
                try:
                    self.n_distancia_fundos = float(input('Distância: '))
                    if self.n_distancia_fundos == '':
                        raise ValueError
                    break
                except ValueError:
                    print('Valor inválido!')

            self.list_conf_fundos.append(self.n_lote_fundos)
            self.list_dist_fundos.append(self.n_distancia_fundos)
            self.add_dist_fundos += self.n_distancia_fundos
            self.texto_fundos += self.txt_fundos[1].format(self.ia_confronta(self.n_lote_fundos), self.n_lote_fundos.upper(), self.converte_decimal(self.n_distancia_fundos), self.ptf)
            self.tl_fundos = self.add_dist_fundos
            f = f + 1
        print('--- Informe --- \n')
        self.n_lote = str(input('Número do lote: '))
        self.n_quadra = str(input(('Número da quadra: ')))
        self.caracteriza = self.txt_caracteriza[0].format(self.n_lote, self.n_quadra, self.calcula_area_total())

    def calcula_area_total(self):

        self.perimetro = self.tl_testada + self.tl_fundos + self.tl_direito + self.tl_esquerdo

        if self.tl_testada == self.tl_fundos and self.tl_direito == self.tl_esquerdo:
            return self.tl_testada * self.tl_direito

        if (self.tl_direito > self.tl_esquerdo) or (self.tl_esquerdo > self.tl_direito):
            return ((self.tl_direito + self.tl_esquerdo) * self.tl_testada) / 2

        if self.tl_testada != self.tl_fundos and self.tl_direito == self.tl_esquerdo:
            if self.tl_testada > self.tl_fundos:
                self.cateto_m = (self.tl_testada - self.tl_fundos) / 2
            if self.tl_fundos > self.tl_testada:
                self.cateto_m = (self.tl_fundos - self.tl_testada) / 2

            self.altura = ((self.tl_direito** 2) - (self.cateto_m** 2)) ** (1/2)
            return ((self.tl_testada  + self.tl_fundos) * self.altura) / 2

        """ //////////////// em desenvolvimento ////////////////
        if (self.tl_testada != self.tl_fundos) and (self.tl_direito != self.tl_esquerdo):
            if self.tl_testada > self.tl_fundos:
                self.cateto_m = (self.tl_testada - self.tl_fundos) / 2
            if self.tl_fundos > self.tl_testada:
                self.cateto_m = (self.tl_fundos - self.tl_testada)

            self.altura = ((self.tl_esquerdo ** 2) - (self.cateto_m ** 2)) ** (1/2)
            return ((self.tl_testada + self.tl_fundos) * self.altura) / 2
        """

    def grava_arquivo(self):

        self.my_arquivo = open('c:/Temp/' + self.save + '.txt', self.modo_gravacao)
        self.conteudo = self.my_arquivo.readlines()
        self.conteudo.append(self.texto_testada)

        if self.num_conf_direito > 1:
            self.conteudo.append(self.texto_direito + self.txt_direito[2].format(self.converte_decimal(self.add_dist_direito)))
        else:
            self.conteudo.append(self.texto_direito)

        if self.num_conf_esquerdo > 1:
            self.conteudo.append(self.texto_esquerdo + self.txt_esquerdo[2].format(self.converte_decimal(self.add_dist_esquerdo)))
        else:
            self.conteudo.append(self.texto_esquerdo)

        if self.num_conf_fundos > 1:
            self.conteudo.append(self.texto_fundos + self.txt_fundos[2].format(self.converte_decimal(self.add_dist_fundos)))
            self.conteudo.append(self.caracteriza)
        else:
            self.conteudo.append(self.texto_fundos)
            self.conteudo.append(self.caracteriza)

        self.my_arquivo.writelines(self.conteudo)
        self.my_arquivo.close()

    def visualiza_arquivo(self):
        print('----- Visualizar texto ----- \n')
        self.file_visual = open('c:/Temp/' +self.save+'.txt', 'r' )
        self.conteudo_visual = self.file_visual.readlines()

        for linha in self.conteudo_visual:
            print(linha)

        self.file_visual.close()

    def alterar_memorial(self):

        self.msg_retorno = str(input('Pressione <Y> para corrigir ou <ENTER> para finalizar \n'))
        if self.msg_retorno == 'y' or self.msg_retorno == 'Y':
            self.opcao = int(input('Alterar: [0] Frente | [1] Lado direito | [2] Lado esquerdo | [3] Fundos: '))

            if self.opcao == 0:
                self.slct = self.descreve_testada()
                n = self.texto_testada
            if self.opcao == 1:
                self.slct = self.descreve_lado_direito()
                n = self.texto_direito
            if self.opcao == 2:
                self.slct = self.descreve_lado_esquerdo()
                n = self.texto_esquerdo
            if self.opcao == 3:
                self.slct = self.descreve_fundos()
                n = self.texto_fundos

            self.my_arquivo = open('c:/Temp/'+self.save+'.txt', 'r')
            self.registro = self.my_arquivo.readlines()

            self.my_arquivo.close()

            self.new_file = open('c:/Temp/'+self.save+'-corrigido'+'.txt','a+')
            self.novo_registro = self.new_file.readlines()

            for i in self.registro:
                c = self.registro.index(i)

                if c == self.opcao:
                    self.novo_registro.append(n)
                if c != self.opcao:
                    self.novo_registro.append(self.registro[c])

            self.new_file.writelines(self.novo_registro)
            self.new_file.close()
        else:
            input(f'O Memorial descritivo < {self.save} > foi gerado com sucesso...')

memorial = MemorialDescritivo(

    num_conf_direito='', list_conf_direito='', list_dist_direito='', txt_direito='',
    texto_direito='', add_dist_direito=0, n_lote_direito='', n_distancia_direito=0,
    num_conf_esquerdo ='', list_conf_esquerdo='', list_dist_esquerdo='', txt_esquerdo='', texto_esquerdo='',
    add_dist_esquerdo=0, n_lote_esquerdo='', n_distancia_esquerdo=0, nome_rua = '', largura_testada = 0, txt_testada = '',
    texto_testada = '', num_conf_fundos='', list_conf_fundos='', list_dist_fundos='', txt_fundos='', texto_fundos='', add_dist_fundos=0,
    n_lote_fundos='', n_distancia_fundos=0, my_arquivo='', conteudo='', save='', modo_gravacao='a+', status_salvamento='',
    caminho_save='', file_visual='', conteudo_visual='', msg_retorno='', opcao='', slct='', registro='', novo_registro='',
    new_file='', numeral='', inumeral=0, texto_intel='', num_1 = '', alfa_1 = '', inum_1 = 0, ialfa_1 = 0,
    alfa = '', num ='', inum= 0, ialfa= 0, tl_testada=0, tl_direito=0, tl_esquerdo=0, tl_fundos=0, txt_caracteriza='', caracteriza='',
    area_total=0, perimetro= 0, altura= 0, cateto_m = 0, n_lote='', n_quadra=''


    )

memorial.salvar_arquivo()
memorial.descreve_testada()
memorial.descreve_lado_direito()
memorial.descreve_lado_esquerdo()
memorial.descreve_fundos()
memorial.grava_arquivo()
memorial.visualiza_arquivo()
memorial.alterar_memorial()
memorial.calcula_area_total()
