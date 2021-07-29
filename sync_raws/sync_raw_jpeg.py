import os
import stat
import sys

"""
NOTE- We are considering that you have selected the JPGs and 
want to delete their corresponding ARWs.
This script reads the files of the folder passed as an argument 
and then removes the Raw images (.ARW) which do not have JPGs with the same name.

Ex- 
    If a folder contains 
    [ 'YAS01448.JPG', 'YAS01449.JPG', 'YAS01448.ARW', 'YAS01449.ARW','YAS01571.ARW' ], 
    then this script will delete 'YAS01571.ARW' as it does not have any corresponding 
    JPG (No "YAS01571.JPG" is present) 

Command -
    python sync_raw_jpeg.py "path\to\folder"
"""


def main(folder):
    try:
        folder = folder.replace("\\", "/")
        print("Folder name selected is - ", folder)
        jpeg_files = [f_name.replace('.JPG', '') for f_name in os.listdir(
            folder) if '.JPG' in f_name]
        raw_files = [f_name.replace('.ARW', '')
                     for f_name in os.listdir(folder) if '.ARW' in f_name]
        # delete raw if jpeg is not present
        print("JPGs in folder - ", jpeg_files)
        print("RAWs in folder - ", raw_files)
        to_be_deleted = list(set(raw_files)-set(jpeg_files))
        print("These RAWs will be deleted - ", to_be_deleted)
        raw_extension = ".ARW"
        # DELETE
        delete_count = 0
        for file in to_be_deleted:
            path = folder + "/" + file + raw_extension
            # Remove the file
            # This is to change persmissions to delete
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
            delete_count += 1
        print(str(delete_count) + " Raws deleted")
        print("Deleted the duplicate RAWs which do not have JPGs")
        return True
    except Exception as e:
        print(f"Error caused due to {e}")
        return False


if __name__ == "__main__":
    result = main(sys.argv[1])
    if result:
        print("Sync is completed.")
    else:
        print("Sync failed !!!")
