separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['stai', 'traba', 'cuvant_scurt', 'variabila_fixa', 'trecem_peste',
                 'numa_asa', 'fa', 'cuvant_dublu', 'celalalt_adevar', 'cuvant_cu_puncte', 'pentru', 'no_arata-mi',
                 'adevar', 'liniuta', 'cuvant_cu_numere', 'cuvant_cu_numere_lungi', 'da-napoi', 'cuvant_si_mai_scurt', 'cat_ii_de_mare?',
                 'inainte_de_traba', 'merge_si_asa', 'nimic', 'sa_marga']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1
