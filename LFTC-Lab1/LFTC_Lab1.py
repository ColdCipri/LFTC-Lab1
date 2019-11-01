from my_language_specification import *
from ProgramInternalForm import ProgramInternalForm
from scanner import tokenGenerator, isIdentifier, isConstant
from SymbolTable import SymbolTable

if __name__ == '__main__':
    fileName = input("insert file name: ")

    file = open(fileName,'r')
    for line in file:
        print(line)

    with open(fileName, 'r') as file:
        for line in file:
            print([token for token in tokenGenerator(line,separators)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()

    with open(fileName, 'r') as file:
        lineNo = 0
        print ("\n")
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], separators):
                if token in separators + operators + reservedWords:
                    pif.add(codification[token], -1)
                elif isIdentifier(token):
                    print ('Identif - \t' + token)
                    id = symbolTable.add(token)
                    pif.add(codification['identifier'], id)
                elif isConstant(token):
                    print ('Const - \t' + token)
                    id = symbolTable.add(token)
                    pif.add(codification['constant'], id)
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

    print('\nProgram internal form: \n', pif)

    print('\nSymbol table: \n', symbolTable)

    print('\n\nCodification table: \n')

    for e in codification:
        print(e, " -> ", codification[e])
