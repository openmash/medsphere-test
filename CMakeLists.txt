cmake_minimum_required(VERSION 2.8.0)

set(CMAKE_MAKE_PROGRAM "/" CACHE INTERNAL "This does not build")
set(CMAKE_INSTALL_PREFIX "/" CACHE INTERNAL "This does not install")
project(VISTA NONE)
enable_testing()


find_program(SIKULI_EXECUTABLE Sikuli-script.cmd DOC "Path to the Sikuli-script.cmd file" HINTS "c:/Program Files (x86)/Sikuli X/")

#Open client with sikuli script and log in
add_test(FT_open_and_login "@SIKULI_EXECUTABLE@" -r open_and_login.sikuli)
set_tests_properties(FT_open_and_login PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #2
add_test(FT_create_section_schedule "@SIKULI_EXECUTABLE@" -r create_section_schedule.sikuli )
set_tests_properties(FT_create_section_schedule PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #3
add_test(FT_find_patient "@SIKULI_EXECUTABLE@" -r find_patient.sikuli)
set_tests_properties(FT_find_patient PROPERTIES FAIL_REGULAR_EXPRESSION "error")



add_test(FT_close "@SIKULI_EXECUTABLE@" -r close.sikuli )
set_tests_properties(FT_close PROPERTIES FAIL_REGULAR_EXPRESSION "error")
