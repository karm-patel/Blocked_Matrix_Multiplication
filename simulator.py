import outgen2048 as o2
import outgen8192 as o8
import execout2048 as e2
import execout8192 as e8
import csv_collector as cc
import summary_generator as sg 

print("Executable file creation is in progress...../")
o2.genOutFile2048()
o8.genOutFile8192()
print("Executable file creation is ended...../")
print("======================================================================")
print("Generation of performance data is in progress for 2048....../")
e2.executeOutFiles2048()
print("Generation of performance data is ended for 2048....../")
print("======================================================================")
print("summary collection is in progress..............")
cc.csvCollector()
print("summary collection is ended..............")
print("======================================================================")
print("summary generation is in progress for 2048.............")
sg.summaryGenerator()
print("summary generation is ended for 2048..............")
print("======================================================================")
print("Generation of performance data is in progress for 8192....../")
e2.executeOutFiles8192()
print("Generation of performance data is ended for 8192....../")
print("======================================================================")
print("summary collection is in progress..............")
cc.csvCollector()
print("summary collection is ended..............")
print("======================================================================")
print("summary generation is in progress for 8192.............")
sg.summaryGenerator()
print("summary generation is ended for 8192..............")

print("simulation ended...................")

