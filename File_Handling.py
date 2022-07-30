##write
import os

# f=open("Sample.txt","w")
# f.write("We are learning python")
# f.close()

# print(os.getcwd())
# f=open("Sample1.txt","w")
# f.write("This is the second text file")
# f.close()
#
# f=open("Sample1.txt","w")
# f.write("This is the second text file\new data ")
# f.close()


# data = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence.
# Machine learning algorithms build a model based on sample data, known as training data, in order
# to make predictions or decisions without being explicitly programmed to do so."""
# file = open("Machine_Learning_Intro.txt","w")
# file.write(data)
# file.close()

# data2 = """Machine learning algorithms are used in a wide variety of applications, such as in
# medicine, email filtering, speech recognition, and computer vision, where it is difficult or
# unfeasible to develop conventional algorithms to perform the needed tasks."""
# file = open("Machine_Learning.txt","w")
# file.write(data2)
# file.close()
#
# data2 = """\n\n\nMachine learning algorithms are used in a wide variety of applications, such as in
# medicine, email filtering, speech recognition, and computer vision, where it is difficult or
# unfeasible to develop conventional algorithms to perform the needed tasks."""
# file=open("Machine_Learning.txt","a")
# file.write(data2)
# file.close()


# r_f=open("Sample.txt","r")
# print(r_f.read())
# r_f.close()

# text = """Line 0 :- This is first line
# Line 1 :- This is second line
# Line 2 :- This is third line
# Line 3 :- This is forth line
# Line 4 :- This is fifth line
# Line 5 :- This is sixth line"""
#
# with open ("sample_with.txt","w") as file:
#     file.write(text)
#
# with open ("sample_with.txt","r") as file:
#     print(file.read())


# f=open("Sample_000.txt","w")
# f.write("Data science")
# f.close()
#
# old_file="Sample.txt"
# new_file="sample.txt"
# os.rename(old_file,new_file)
# os.rename("sample.txt","SAMPLE.txt")
#
# f=open("SAMPLE.txt","r")
# print(f.read())
# f.close()

# os.rename(r"C:\Users\Admin\PycharmProjects\pythonProject4\Sample_000.txt","Sample_002.txt")

##remove
# os.remove("SAMPLE.txt")
#os.remove(r"C:\Users\Admin\PycharmProjects\pythonProject4\SAMPLE.txt")


###os.path.exists
# print(os.path.exists("Sample_002.txt"))
#
# print(os.path.exists("Sample_003.txt"))

# if os.path.exists("xyz.txt"):
#     os.remove("xyz.txt")
# else:
#     print("File not present")

##create Directory(mkdir)

#os.mkdir("python & data science")
#os.mkdir("Data")
print(os.getcwd())

path=r"C:\Users\Admin\PycharmProjects\pythonProject4"
# new_folder_path = path + "\Datalake\databricks"
# os.makedirs(new_folder_path)

# new_path = path + "\AWS\Cred\S3_Cred"
# os.makedirs(new_path)

##foldar_path="Data"
print(os.path.exists("Data"))
os.rmdir("Data")



