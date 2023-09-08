import os

volumes_path = r'Z:\iacss\IACSS_IJCSS\IJCSS\Volumes\Vol222023Ed2'
word_path = os.path.join(volumes_path, '3-Uploads', '1-Word')

word_file_path = os.path.join(word_path, '10.2478ijcss-2023-0007.docx')

doi, file_extension = os.path.splitext(word_file_path)
# get volume and issue from folder name (must be in the format 'Vol222023Ed1')
volume = volumes_path.split(os.sep)[-1].split('Vol')[1][0:2]
issue = volumes_path.split(os.sep)[-1].split('Ed')[1][0:1]

# create final submission folder (will be used to zip in the end)
submit_folder = os.path.join(volumes_path, '3-Uploads', '10516-Volume{}-Issue{}'.format(volume, issue))

# Update the output_document_path with the desired format
output_document_path = os.path.join(submit_folder, 'Content Specification_{}.docx'.format(doi))

print(submit_folder)
print(output_document_path)
