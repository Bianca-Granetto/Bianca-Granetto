#!/usr/bin/python
arquivo = open('cursos.txt', 'a')
arquivo.write('Conheça nossos cursos!!!\n')
arquivo.write('1-Python\n')
print(arquivo,"Conteúdo do Arquivo")
arquivo.close()
arquivo = open('cursos.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()
