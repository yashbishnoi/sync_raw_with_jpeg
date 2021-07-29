# sync_raw_with_jpeg

I made this to make the workflow of a photographer easier by making a script.
The usual workflow involves grouping pictures by type and then selecting and deleting from the JPGs as they are easily opened on PC.
But while doing this, RAW copies of those JPGs are left and it is a very boring task to delete them.

These scripts will help you to just perform the selection on JPGs and then just right click in the folder and click on Sync Raw button and it will do the job for you.

Steps to do that-

Install Python and dependencies- 
Run create_context_menu_key.py file in Powershell as an administrator like python create_context_menu_key.py. It will create the button in right click menu (context menu).
The other script does the main fucntionality


-----------------------------------------------------------------------
In case you want to use it manually

NOTE- Considering that you have selected the JPGs and 
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
