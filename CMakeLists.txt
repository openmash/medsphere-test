cmake_minimum_required(VERSION 2.8.0)

set(CMAKE_MAKE_PROGRAM "/" CACHE INTERNAL "This does not build")
set(CMAKE_INSTALL_PREFIX "/" CACHE INTERNAL "This does not install")
project(VISTA NONE)
enable_testing()
set( CANCEL_APPOINTMENT_DAY tuesday)
set( CHECKIN_APPOINTMENT_DAY monday)
set( CLINIC_SEARCH MEN)
set( PATIENT_SEARCH s)
set( MAKE_APPOINTMENT_DAY monday)
set( CLIN_SCHED_EXE "c:\\ClinicalSchedulerCA\\ClinSchd.exe")
set( ACCESS_CODE boating1)
set( VERIFY_CODE boating1.)
set( RESCHED_APPOINTMENT_DAY monday)
set( RESCHED_NEW_APPOINTMENT_DAY tuesday)
set( VERIFY_APPOINTMENT_DAY monday)
set( WALKIN_APPOINTMENT_DAY wednesday)

file(COPY @CMAKE_CURRENT_SOURCE_DIR@/cancel_appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/checkin-appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/close.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/close_clinic.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/create_section_schedule.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/find_patient.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/make_appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/open_and_login.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/reschedule_appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/select_clinic.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/select_provider.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/verify_appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)
file(COPY @CMAKE_CURRENT_SOURCE_DIR@/walkin_appointment.sikuli DESTINATION @CMAKE_CURRENT_BINARY_DIR@/)

configure_file( @CMAKE_CURRENT_BINARY_DIR@/cancel_appointment.sikuli/cancel_appointment.py @CMAKE_CURRENT_BINARY_DIR@/cancel_appointment.sikuli/cancel_appointment.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/checkin-appointment.sikuli/checkin-appointment.py @CMAKE_CURRENT_BINARY_DIR@/checkin-appointment.sikuli/checkin-appointment.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/close.sikuli/close.py @CMAKE_CURRENT_BINARY_DIR@/close.sikuli/close.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/close_clinic.sikuli/close_clinic.py @CMAKE_CURRENT_BINARY_DIR@/close_clinic.sikuli/close_clinic.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/create_section_schedule.sikuli/create_section_schedule.py @CMAKE_CURRENT_BINARY_DIR@/create_section_schedule.sikuli/create_section_schedule.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/find_patient.sikuli/find_patient.py @CMAKE_CURRENT_BINARY_DIR@/find_patient.sikuli/find_patient.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/make_appointment.sikuli/make_appointment.py @CMAKE_CURRENT_BINARY_DIR@/make_appointment.sikuli/make_appointment.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/open_and_login.sikuli/open_and_login.py @CMAKE_CURRENT_BINARY_DIR@/open_and_login.sikuli/open_and_login.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/reschedule_appointment.sikuli/reschedule_appointment.py @CMAKE_CURRENT_BINARY_DIR@/reschedule_appointment.sikuli/reschedule_appointment.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/select_clinic.sikuli/select_clinic.py @CMAKE_CURRENT_BINARY_DIR@/select_clinic.sikuli/select_clinic.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/select_provider.sikuli/select_provider.py @CMAKE_CURRENT_BINARY_DIR@/select_provider.sikuli/select_provider.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/verify_appointment.sikuli/verify_appointment.py @CMAKE_CURRENT_BINARY_DIR@/verify_appointment.sikuli/verify_appointment.py)
configure_file( @CMAKE_CURRENT_BINARY_DIR@/walkin_appointment.sikuli/walkin_appointment.py @CMAKE_CURRENT_BINARY_DIR@/walkin_appointment.sikuli/walkin_appointment.py)


find_program(SIKULI_EXECUTABLE Sikuli-script.cmd DOC "Path to the Sikuli-script.cmd file" HINTS "c:/Program Files (x86)/Sikuli X/")

#Open client with sikuli script and log in
add_test(FT_open_and_login "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/open_and_login.sikuli)
set_tests_properties(FT_open_and_login PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #2 manage the component
add_test(FT_create_section_schedule "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/create_section_schedule.sikuli )
set_tests_properties(FT_create_section_schedule PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #3 create appointment
add_test(FT_find_patient "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/find_patient.sikuli)
set_tests_properties(FT_find_patient PROPERTIES FAIL_REGULAR_EXPRESSION "error")
add_test(FT_select_clinic "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/select_clinic.sikuli)
set_tests_properties(FT_select_clinic PROPERTIES FAIL_REGULAR_EXPRESSION "error")
add_test(FT_make_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/make_appointment.sikuli)
set_tests_properties(FT_make_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")
add_test(FT_verify_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/verify_appointment.sikuli)
set_tests_properties(FT_verify_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")


#Test for Use Case #4 manage appointment
add_test(FT_checkin_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/checkin-appointment.sikuli)
set_tests_properties(FT_checkin_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #5 walkin appontment
add_test(FT_walkin_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/walkin_appointment.sikuli)
set_tests_properties(FT_walkin_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #7 reschedule appointment
add_test(FT_reschedule_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/reschedule_appointment.sikuli)
set_tests_properties(FT_reschedule_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")

#Test for Use Case #6 cancel appointment
add_test(FT_cancel_appointment "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/cancel_appointment.sikuli)
set_tests_properties(FT_cancel_appointment PROPERTIES FAIL_REGULAR_EXPRESSION "error")



#Close the app
add_test(FT_close "@SIKULI_EXECUTABLE@" -r @CMAKE_CURRENT_BINARY_DIR@/close.sikuli )
set_tests_properties(FT_close PROPERTIES FAIL_REGULAR_EXPRESSION "error")


