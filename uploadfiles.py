import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join( root, filename)
                relative_path = os.path.relpath( local_path, file_from)
                dropbox_path = os.path.join( file_to, relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))
def main():
    access_token = 'sl.BBLwG71ZF34oua-6KSwqUHMmA4wL4VKT99Fw3KUtzZbrxEOVSKs1aYQgBG1mzmj6YCGhg5BupPC7wk7rR6va9qs_TNg5VKUrNNVTFBwcAK8NXg7zclHWgZAKFLGNxPh6gsS2LX4'
    transferData = TransferData(access_token)

    file_from = input("Enter file name : ")
    file_to = input("Enter file path : ")

    transferData.uploadFiles(file_from, file_to)
    print("File has been uploaded.")


main()