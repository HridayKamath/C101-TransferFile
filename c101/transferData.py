import dropbox

class TransferData (object):

    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEUXFS6ldb1Z1OahQvX2E1pE0PmnrZqfpHZXZy-CdCJOl6rBB6aud1DFf3JWTMf4_3NVJP4m9DFT0l0PplUcBqUmmnvZSG2ldrDgVdNe5iXF5EQkOWizfwKF28RXDAfsDTWW54r0R8E'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to Dropbox: ')

    transferData.uploadFile(file_from, file_to)
    print('File has been transfered.')

if __name__ == '__main__':
    main()