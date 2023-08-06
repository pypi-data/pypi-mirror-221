from tiivad import *

validate_files(['''submission.py'''])
execute_test(file_name='''submission.py''', standard_input_data=['''Kasutajasisend'''],
             input_files=[('''sisendfail.txt''', '''Sisendfaili sisu.\nRida2\nRida3\nRida4''')], generic_checks=[
        {'check_type': '''ANY_OF_THESE''', 'nothing_else': None, 'expected_value': ['''down''', '''up'''],
         'consider_elements_order': False, 'before_message': '''Kontrollib, kas väljund sisaldab võtmesõna.''',
         'passed_message': '''Programmi väljund sisaldab antud võtmesõna.''',
         'failed_message': '''Programmi väljund ei sisalda antud võtmesõna.''', 'is_numeric': False}],
             output_file_checks=[
                 {'file_name': '''valjundfail.txt''', 'check_type': '''ALL_OF_THESE''', 'nothing_else': None,
                  'expected_value': ['''Väljundfaili eeldatav sisu''', '''Rida2''', '''Rida3''', '''Rida4'''],
                  'consider_elements_order': False,
                  'before_message': '''Kontrollib, kas väljundfail sisaldab võtmesõna.''',
                  'passed_message': '''Programmi väljundfail sisaldab antud võtmesõna.''',
                  'failed_message': '''Programmi väljundfail ei sisalda antud võtmesõna.'''}],
             exception_check={'expected_value': True,
                              'before_message': '''Kontrollib, et programm ei viskaks erindit.''',
                              'passed_message': '''Programm ei visanud erindit.''',
                              'failed_message': '''Programm viskas erindi.'''}, type='''program_execution_test''',
             points_weight=1.0, id=1, name='''Programmi käivituse test.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''turtle'''],
     'before_message': '''Kontrollib, kas programm impordib mooduli.''',
     'passed_message': '''Programm importis mooduli.''', 'failed_message': '''Programm ei importinud moodulit.''',
     'is_numeric': False}], type='''program_imports_module_test''', points_weight=10.0, id=2,
             name='''Programm impordib mooduli''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[
    {'check_type': '''ANY_OF_THESE''', 'nothing_else': None, 'expected_value': ['''close'''],
     'before_message': '''Kontrollib, kas programm kutsub välja turtle funktsiooni.''',
     'passed_message': '''Programm kutsus välja vähemalt ühe turtle funktsiooni.''',
     'failed_message': '''Programm ei kutsnud välja ühtegi turtle funktsiooni.''', 'is_numeric': False}],
             type='''program_calls_function_test''', points_weight=1.0, id=3,
             name='''Programm kutsub välja turtle funktsiooni.''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', contains_check=False,
             before_message='''Kontrollib, kas programmis esineb tsükkel.''',
             passed_message='''Programmis esines tsükkel.''', failed_message='''Programmis ei esine ühtegi tsüklit.''',
             type='''program_contains_loop_test''', points_weight=1.0, id=4, name='''Programmis esineb tsükkel.''',
             inputs=None, passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', contains_check=True,
             before_message='''Kontrollib, kas programmis esineb try/except plokk.''',
             passed_message='''Programmis ei esine try/except plokki.''',
             failed_message='''Programmis esines try/except plokk.''', type='''program_contains_try_except_test''',
             points_weight=1.0, id=5, name='''Programmis ei tohi olla try/except plokki.''', inputs=None,
             passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', contains_check=False,
             before_message='''Kontrollib, kas programm kutsub välja 'print' käsu.''',
             passed_message='''Programm kutsus välja 'print' käsu.''',
             failed_message='''Programm ei kutsunud välja 'print' käsku.''', type='''program_calls_print_test''',
             points_weight=1.0, id=6, name='''Programm peab välja kutsuma 'print' käsu.''', inputs=None,
             passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[{'check_type': '''ANY_OF_THESE''', 'nothing_else': None,
                                                             'expected_value': ['''down''', '''up''',
                                                                                '''seosta_lapsed_ja_vanemad'''],
                                                             'before_message': '''Kontrollib, kas programm defineerib vähemalt ühe antud funktsioonidest.''',
                                                             'passed_message': '''Programm defineeris vähemalt ühe antud funktsioonidest.''',
                                                             'failed_message': '''Programm ei defineerinud välja ühtegi antud funktsioonidest.''',
                                                             'is_numeric': False}],
             type='''program_defines_function_test''', points_weight=1.0, id=7,
             name='''Programm defineerib vähemalt ühe antud funktsioonidest.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[{'check_type': '''ANY_OF_THESE''', 'nothing_else': None,
                                                             'expected_value': ['''seosta_lapsed_ja_vanemad''',
                                                                                '''yes''', '''no'''],
                                                             'consider_elements_order': False,
                                                             'before_message': '''Kontrollib, kas programm sisaldab võtmesõna.''',
                                                             'passed_message': '''Programm sisaldab võtmesõna.''',
                                                             'failed_message': '''Programm ei sisalda võtmesõna.''',
                                                             'is_numeric': False}],
             type='''program_contains_keyword_test''', points_weight=1.0, id=8, name='''Programm sisaldab võtmesõna.''',
             inputs=None, passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=False,
             before_message='''Kontrollib, kas funktsioonis esineb tsükkel.''',
             passed_message='''Funktsioonis esines tsükkel.''',
             failed_message='''Funktsioonis ei esine ühtegi tsüklit.''', type='''function_contains_loop_test''',
             points_weight=1.0, id=9, name='''Funktsioonis esineb tsükkel.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', generic_checks=[
    {'check_type': '''ANY_OF_THESE''', 'nothing_else': None, 'expected_value': ['''ff.close()''', '''no'''],
     'consider_elements_order': False, 'before_message': '''Kontrollib, kas funktsioon sisaldab võtmesõna.''',
     'passed_message': '''Funktsioon sisaldab võtmesõna.''', 'failed_message': '''Funktsioon ei sisalda võtmesõna.''',
     'is_numeric': False}], type='''function_contains_keyword_test''', points_weight=1.0, id=10,
             name='''Funktsioon sisaldab võtmesõna.''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=False,
             before_message='''Kontrollib, kas funktsioonis esineb return.''',
             passed_message='''Funktsioonis esines return.''',
             failed_message='''Funktsioonis ei esine ühtegi return'i.''', type='''function_contains_return_test''',
             points_weight=1.0, id=11, name='''Funktsioonis esineb return.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', generic_checks=[
    {'check_type': '''ANY_OF_THESE''', 'nothing_else': None,
     'expected_value': ['''down''', '''up''', '''forward''', '''left''', '''right''', '''fd''', '''rt''', '''lt''',
                        '''bk''', '''goto'''],
     'before_message': '''Kontrollib, kas funktsioon kutsub välja turtle funktsiooni.''',
     'passed_message': '''Funktsioon kutsus välja vähemalt ühe turtle funktsiooni.''',
     'failed_message': '''Funktsioon ei kutsnud välja ühtegi turtle funktsiooni.''', 'is_numeric': False}],
             type='''function_calls_function_test''', points_weight=1.0, id=12,
             name='''Funktsioon kutsub välja turtle funktsiooni.''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=False,
             before_message='''Kontrollib, kas funktsioon kutsub välja print käsu.''',
             passed_message='''Funktsioon kutsub välja print käsu.''',
             failed_message='''Funktsioon ei kutsu välja print käsku.''', type='''function_calls_print_test''',
             points_weight=1.0, id=13, name='''Funktsioon kutsub välja print käsu.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=False,
             before_message='''Kontrollib, kas funktsioon on rekursiivne.''',
             passed_message='''Funktsioonis on rekursiivne.''', failed_message='''Funktsioonis ei ole rekursiivne.''',
             type='''function_is_recursive_test''', points_weight=1.0, id=14, name='''Funktsioonis on rekursiivne.''',
             inputs=None, passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', generic_checks=[
    {'check_type': '''ANY_OF_THESE''', 'nothing_else': None,
     'expected_value': ['''down''', '''up''', '''seosta_lapsed_ja_vanemad2'''],
     'before_message': '''Kontrollib, kas funktsioon defineerib vähemalt ühe antud funktsioonidest.''',
     'passed_message': '''Funktsioon defineeris vähemalt ühe antud funktsioonidest.''',
     'failed_message': '''Funktsioon ei defineerinud ühtegi antud funktsioonidest.''', 'is_numeric': False}],
             type='''function_defines_function_test''', points_weight=1.0, id=15,
             name='''Funktsioon defineerib vähemalt ühe antud funktsioonidest.''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''turtle'''],
     'before_message': '''Kontrollib, kas funktsioon impordib mooduli.''',
     'passed_message': '''Funktsioon importis mooduli.''', 'failed_message': '''Funktsioon ei importinud moodulit.''',
     'is_numeric': False}], type='''function_imports_module_test''', points_weight=1.0, id=16,
             name='''Funktsioon importib mooduli turtle.''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=True,
             before_message='''Kontrollib, kas funktsioonis esineb try/except plokk.''',
             passed_message='''Funktsioonis ei esine try/except plokki.''',
             failed_message='''Funktsioonis esines try/except plokk.''', type='''function_contains_try_except_test''',
             points_weight=1.0, id=17, name='''Funktsioonis ei tohi olla try/except plokki.''', inputs=None,
             passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', contains_check=False,
             before_message='''Kontrollib, kas funktsioon kasutab ainult lokaalseid muutujaid.''',
             passed_message='''Funktsioon kasutab ainult lokaalseid muutujaid.''',
             failed_message='''Funktsioon ei kasuta ainult lokaalseid muutujaid.''', type='''function_is_pure_test''',
             points_weight=1.0, id=18, name='''Funktsioon kasutab ainult lokaalseid muutujaid.''', inputs=None,
             passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''seosta_lapsed_ja_vanemad''', function_type='''FUNCTION''',
             create_object=None, arguments=["lapsed.txt", "nimed.txt"], standard_input_data=['''Kasutajasisend'''],
             input_files=[('''sisendfail.txt''', '''Sisendfaili sisu.''')], return_value=3, generic_checks=[
        {'check_type': '''ANY_OF_THESE''', 'nothing_else': None, 'expected_value': ['''down''', '''up'''],
         'consider_elements_order': False,
         'before_message': '''Kontrollib, kas funktsiooni väljund sisaldab võtmesõna.''',
         'passed_message': '''Funktsiooni väljund sisaldab antud võtmesõna.''',
         'failed_message': '''Funktsiooni väljund ei sisalda antud võtmesõna.''', 'is_numeric': False}],
             output_file_checks=[
                 {'file_name': '''valjundfail.txt''', 'check_type': '''ALL_OF_THESE''', 'nothing_else': None,
                  'expected_value': ['''Väljundfaili eeldatav sisu'''], 'consider_elements_order': True,
                  'before_message': '''Kontrollib, kas funktsiooni väljundfail sisaldab võtmesõna.''',
                  'passed_message': '''Funktsiooni väljundfail sisaldab antud võtmesõna.''',
                  'failed_message': '''Funktsiooni väljundfail ei sisalda antud võtmesõna.'''}],
             type='''function_execution_test''', points_weight=1.0, id=19,
             name='''Funktsiooni käivituse test (tavaline).''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''võta_hind''', function_type='''METHOD''',
             create_object='''return Raamat("Harry Potter", 10.7)''', arguments=[], standard_input_data=[],
             input_files=[], return_value=10.7, generic_checks=[], output_file_checks=[],
             type='''function_execution_test''', points_weight=1.0, id=222,
             name='''Funktsiooni käivituse test (isendimeetod).''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''loe''', function_type='''METHOD''',
             create_object='''return Lugemik''', arguments=[], standard_input_data=[], input_files=[],
             return_value=True, generic_checks=[], output_file_checks=[], type='''function_execution_test''',
             points_weight=1.0, id=223, name='''Funktsiooni käivituse test (klassimeetod).''', inputs=None,
             passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', function_name='''loe''', function_type='''METHOD''',
             create_object='''return Lugemik''', arguments=[], standard_input_data=[], input_files=[],
             return_value=True, generic_checks=[
        {'check_type': '''ANY_OF_THESE''', 'nothing_else': None, 'expected_value': [2.3],
         'consider_elements_order': False,
         'before_message': '''Kontrollib, kas funktsiooni väljund sisaldab võtmesõna.''',
         'passed_message': '''Funktsiooni väljund sisaldab antud võtmesõna.''',
         'failed_message': '''Funktsiooni väljund ei sisalda antud võtmesõna.''', 'is_numeric': True}],
             output_file_checks=[], type='''function_execution_test''', points_weight=1.0, id=224,
             name='''Funktsiooni käivituse test (klassimeetod).''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Raamat''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''math''', '''pi'''],
     'before_message': '''Kontrollib, kas klass impordib mooduli.''', 'passed_message': '''Klass importis mooduli.''',
     'failed_message': '''Klass ei importinud moodulit.''', 'is_numeric': False}], type='''class_imports_module_test''',
             points_weight=10.0, id=20, name='''Klass impordib mooduli''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Raamat''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''võta_hind''', '''suurenda_hinda'''],
     'before_message': '''Kontrollib, kas klass defineerib funktsiooni.''',
     'passed_message': '''Klass defineerib funktsiooni.''', 'failed_message': '''Klass ei defineerib funktsiooni.''',
     'is_numeric': False}], type='''class_defines_function_test''', points_weight=10.0, id=21,
             name='''Klass defineerib funktsiooni''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Jutustus''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''Raamat'''],
     'before_message': '''Kontrollib, kas klass kutsub välja teise klassi.''',
     'passed_message': '''Klass kutsub välja teise klassi.''',
     'failed_message': '''Klass ei kutsu välja teist klassi.''', 'is_numeric': False}],
             type='''class_calls_class_test''', points_weight=10.0, id=22, name='''Klass kutsub välja teise klassi''',
             inputs=None, passed_next=None, failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Jutustus''', class_function_name='''add_book''',
             generic_checks=[{'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''print'''],
                              'before_message': '''Kontrollib, kas klassi funktsioon kutsub välja funktsiooni.''',
                              'passed_message': '''Klassi funktsioon kutsub välja funktsiooni.''',
                              'failed_message': '''Klassi funktsioon ei kutsu välja funktsiooni.''',
                              'is_numeric': False}], type='''class_function_calls_function_test''', points_weight=10.0,
             id=23, name='''Klassi funktsioon kutsub välja funktsiooni''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''Raamat'''],
     'before_message': '''Kontrollib, kas programm defineerib klassi.''',
     'passed_message': '''Programm defineerib klassi.''', 'failed_message': '''Programm ei defineeri klassi.''',
     'is_numeric': False}], type='''program_defines_class_test''', points_weight=10.0, id=24,
             name='''Programm defineerib klassi''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Jutustus''', superclass_name='''Raamat''',
             before_message='''Kontrollib, kas programm defineerib alamklassi.''',
             passed_message='''Programm defineerib alamklassi.''',
             failed_message='''Programm ei defineeri alamklassi.''', type='''program_defines_subclass_test''',
             points_weight=10.0, id=25, name='''Programm defineerib alamklassi''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''Raamat'''],
     'before_message': '''Kontrollib, kas programm kutsub välja klassi.''',
     'passed_message': '''Programm kutsub välja klassi.''', 'failed_message': '''Programm ei kutsu välja klassi.''',
     'is_numeric': False}], type='''program_calls_class_test''', points_weight=1.0, id=26,
             name='''Programm kutsub välja klassi''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', generic_checks=[
    {'check_type': '''ALL_OF_THESE''', 'nothing_else': None, 'expected_value': ['''print_info'''],
     'before_message': '''Kontrollib, kas programm kutsub välja klassi funktsiooni.''',
     'passed_message': '''Programm kutsub välja klassi funktsiooni.''',
     'failed_message': '''Programm ei kutsu välja klassi funktsiooni.''', 'is_numeric': False}],
             type='''program_calls_class_function_test''', points_weight=1.0, id=27,
             name='''Programm kutsub välja klassi funktsiooni''', inputs=None, passed_next=None, failed_next=None,
             visible_to_user=None)
execute_test(file_name='''submission.py''', class_name='''Raamat''',
             create_object='''return Raamat("Truth and Justice", "A. H. Tammsaare", 453)''',
             fields_final=[('''title''', "Truth and Justice"), ('''author''', "A. H. Tammsaare"), ('''pages''', 453)],
             before_message='''Kontrollib, kas klassi isend väärtustab õiged väljad.''',
             passed_message='''Klassi isend väärtustas õiged väljad.''',
             failed_message='''Klassi isend ei väärtustanud õigeid välju.''', type='''class_instance_test''',
             points_weight=1.0, id=1323, name='''Klassi isendi loomise test''', inputs=None, passed_next=None,
             failed_next=None, visible_to_user=None)
print(Results(None))
