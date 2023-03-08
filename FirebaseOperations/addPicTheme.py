import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
dream_firebase_key = 'firebase_service_account.json'
cred=credentials.Certificate(dream_firebase_key)
firebase_admin.initialize_app(cred, {
    'storageBucket':'<your storage bucket>'
})
fdb = firebase_admin.firestore.client()




def getDataCol():
    c = fdb.collection("DMArtStyles").limit(5).get() #just get first 5 data
    # c = fdb.collection("DMArtStyles").get() $get all data
    for a in c:
        d =a.to_dict()
        print(d['GET_FIELD']) 
        
 

def readFolderAndUploadFirestore():
    file_path ="/Users/cagatay/Desktop/beforeUploadStorage/"
    dir_list = os.listdir(file_path)
    
    for fileName in dir_list:
        if(fileName!='.DS_Store'):
            splitText=fileName.split('.')
            index =splitText[0]
            print(index)
            addDataFirestore(index)
            #uploadStorage(index)

        
            

def addDataFirestore(index):
    photoUrl = 'YOUR_STORAGE_URL'+index+'.jpg'
    fdb.collection('picWTheme').add({'photoUrl':photoUrl,'index':int(index)})

def uploadStorage(index):
    bucket = storage.bucket()
    blob= bucket.blob('picWTheme/'+index+'.jpg')
    path_to_file= '/Users/cagatay/Desktop/beforeUploadStorage/'+index+'.jpg'
    blob.upload_from_filename(path_to_file)

readFolderAndUploadFirestore()