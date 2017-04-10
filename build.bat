del /F /Q s3site
mkdir s3site
robocopy /S static-html s3site
robocopy /S static s3site
pelican -t theme -s settings.py -o s3site content
cd s3site/pages
copy /Y *.* ..
del /F /Q *.*
cd ../..